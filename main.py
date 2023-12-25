import sys
import pygame
from lib.runtime_values import *
from lib.runtime_values import playerc
from lib import farm
from lib import save
from lib import player
from lib import item

pygame.init()
logger.info("파이게임 초기화.")

ground_images: dict[farm.Tiles, pygame.Surface] = {
    farm.Tiles.DIRT: pygame.image.load("assets/img/ground/dirt.png"),
    farm.Tiles.FARMLAND: pygame.image.load("assets/img/ground/farmland.png"),
    farm.Tiles.WATER_FARMLAND: pygame.image.load("assets/img/ground/water_farmland.png"),
}

pygame.display.set_caption(f"sfg {ver_text} by newkini")
pygame.display.set_icon(pygame.image.load("assets/img/icon.png"))

select_inventory = 0

if not save.import_save():
    playerc.inventory = [item.Items.NONE for _ in range(0,8)]
    for i, j in enumerate(item.Items):
        playerc.inventory[i] = j

while is_running:
    dt: float = clock.tick(100) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_LEFT:
                    if player_dir == player.Direction.STOP:
                        player_dir = player.Direction.LEFT
                    if player_dir == player.Direction.UP:
                        player_dir = player.Direction.UP_LEFT
                    if player_dir == player.Direction.DOWN:
                        player_dir = player.Direction.DOWN_LEFT
                case pygame.K_RIGHT:
                    if player_dir == player.Direction.STOP:
                        player_dir = player.Direction.RIGHT
                    if player_dir == player.Direction.UP:
                        player_dir = player.Direction.UP_RIGHT
                    if player_dir == player.Direction.DOWN:
                        player_dir = player.Direction.DOWN_RIGHT
                case pygame.K_UP:
                    if player_dir == player.Direction.STOP:
                        player_dir = player.Direction.UP
                    if player_dir == player.Direction.LEFT:
                        player_dir = player.Direction.UP_LEFT
                    if player_dir == player.Direction.RIGHT:
                        player_dir = player.Direction.UP_RIGHT
                case pygame.K_DOWN:
                    if player_dir == player.Direction.STOP:
                        player_dir = player.Direction.DOWN
                    if player_dir == player.Direction.LEFT:
                        player_dir = player.Direction.DOWN_LEFT
                    if player_dir == player.Direction.RIGHT:
                        player_dir = player.Direction.DOWN_RIGHT
                case pygame.K_d:
                    playerc.farm_tile(playerc.tile_pos())
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_LEFT:
                    if player_dir == player.Direction.LEFT:
                        player_dir = player.Direction.STOP
                    if player_dir == player.Direction.UP_LEFT:
                        player_dir = player.Direction.UP
                    if player_dir == player.Direction.DOWN_LEFT:
                        player_dir = player.Direction.DOWN
                case pygame.K_RIGHT:
                    if player_dir == player.Direction.RIGHT:
                        player_dir = player.Direction.STOP
                    if player_dir == player.Direction.UP_RIGHT:
                        player_dir = player.Direction.UP
                    if player_dir == player.Direction.DOWN_RIGHT:
                        player_dir = player.Direction.DOWN
                case pygame.K_UP:
                    if player_dir == player.Direction.UP:
                        player_dir = player.Direction.STOP
                    if player_dir == player.Direction.UP_LEFT:
                        player_dir = player.Direction.LEFT
                    if player_dir == player.Direction.UP_RIGHT:
                        player_dir = player.Direction.RIGHT
                case pygame.K_DOWN:
                    if player_dir == player.Direction.DOWN:
                        player_dir = player.Direction.STOP
                    if player_dir == player.Direction.DOWN_LEFT:
                        player_dir = player.Direction.LEFT
                    if player_dir == player.Direction.DOWN_RIGHT:
                        player_dir = player.Direction.RIGHT
                
                    
    
    screen.fill(SKYBLUE)
    
    tilePos = pygame.math.Vector2(0, 0)
    for line in farm.tile_map:
        for tile in line:
            screen.blit(ground_images[farm.Tiles.DIRT], tilePos)
            screen.blit(ground_images[tile], tilePos)
            tilePos.y += 32
        tilePos.x += 32
        tilePos.y = 0
        
    playerc.draw()
    playerc.move(player_dir, dt)
    
    screen.blit(pygame.transform.scale(pygame.image.load("assets/img/ui/item_bar.png"), (256, 32)), [28 * 32 - (256 - 64), 20 * 32 - 32])
    screen.blit(pygame.image.load("assets/img/ui/select_item_bar.png"), [28 * 32 - (256 - 64) + (select_inventory * 32), 20 * 32 - 32])
    for index, i in enumerate(playerc.inventory):
        screen.blit(pygame.image.load(f"assets/img/items/{i.name.lower()}.png"), [28 * 32 - (256 - 64) + (index * 32), 20 * 32 - 32])
    try:
        for i in range(1,9):
            keys = pygame.key.get_pressed()
            if keys[getattr(pygame, f"K_{i}")]:
                select_inventory = i-1
        playerc.hendle_item = playerc.inventory[select_inventory]
    except:pass
    
    pygame.display.update()

logger.info("로그, 세이브저장, 종료를 시작합니다.")
save.write_save()
logger.save()
logger.info("저장성공!")
pygame.quit()
sys.exit()