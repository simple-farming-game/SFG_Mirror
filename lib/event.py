import pygame

import lib.save
from lib.plants import plants_list
from lib.items import Items
from lib import items
from lib import runtime_values
from lib import farm
<<<<<<< Updated upstream
from lib import player
from lib import sell
=======
from lib.farm import Tiles
from lib import shop_system
>>>>>>> Stashed changes
from lib import help
from lib.block import block_list
import random
from lib import chat
from lib import debug
from lib import sound

SELECT_KEY = {
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_5: 5,
    pygame.K_6: 6,
    pygame.K_7: 7,
    pygame.K_8: 8,
}
select_bar = 1


def use():
    x, y = map(int, runtime_values.players[0].get_tile_pos())
    tile = farm.tileMap[x][y]
    runtime_values.logs.info("using item")
    runtime_values.logs.info(f"at  X:{x} Y:{y}")

    if runtime_values.players[0].handle_item in plants_list.plants_list: # 식물 설치
        sound.sounds["planting"].play()
        runtime_values.logs.info(
            f"Try to plant:{runtime_values.players[0].handle_item.name}"
        )
        if runtime_values.players[0].plant_plant(runtime_values.screen):
            runtime_values.logs.info("success planting")
        else:
            runtime_values.logs.info("Fail planting")

    if runtime_values.players[0].handle_item in block_list.block_list: # 블록 설치
        runtime_values.logs.info(
            f"Try to put:{runtime_values.players[0].handle_item.name}"
        )
        if runtime_values.players[0].put_block(runtime_values.screen):
            runtime_values.logs.info("success put")
        else:
            runtime_values.logs.info("Fail put")

    elif (runtime_values.players[0].handle_item == Items.HOE) and ( # 괭이
        tile == farm.Tiles.DIRT
    ):  # 경작
        sound.sounds["farm"].play()
        farm.tileMap[x][y] = farm.Tiles.FARMLAND
        runtime_values.logs.info("Hoe")

    elif runtime_values.players[0].handle_item == Items.SICKLE:  # 낫
        if isinstance(tile, plants_list.plants_list):  # type: ignore
            sound.sounds["harvest"].play()
            runtime_values.players[0].farm_plant()
            runtime_values.logs.info(f"Sickle")

<<<<<<< Updated upstream
    elif (runtime_values.players[0].handle_item == Items.SHOVEL) and ( # 삽 
        (tile == farm.Tiles.FARMLAND)
=======
    elif (runtime_values.players[0].handle_item == Items.SHOVEL) and (
        (tile == Tiles.FARMLAND)
>>>>>>> Stashed changes
    ):  # 삽
        farm.tileMap[x][y] = farm.Tiles.DIRT
        runtime_values.logs.info(f"Shovel")
    elif runtime_values.players[0].handle_item == Items.NONE: # 없을때
        pass

    elif (runtime_values.players[0].handle_item == Items.WATER) and ( # 물
        isinstance(tile, plants_list.plants_list)
    ):  # 경작 # type: ignore
        sound.sounds["watering"].play()
        farm.tileMap[x][y].water = True  # type: ignore
        runtime_values.logs.info("Warter")

    elif (runtime_values.players[0].handle_item == Items.VITAMIN) and ( # 비타민
        isinstance(tile, plants_list.plants_list)
    ):  # 경작 # type: ignore
        if farm.tileMap[x][y].water and runtime_values.players[0].inventory["VITAMIN"] > 0:  # type: ignore
            farm.tileMap[x][y].growCount += random.randint(500, 1000)  # type: ignore
            runtime_values.players[0].inventory["VITAMIN"] -= 1
        else:
            runtime_values.logs.info("Fail to using")
        runtime_values.logs.info("Vitamin")

    else:
        runtime_values.logs.info("Fail to using")


def block_use():
    x, y = map(int, runtime_values.players[0].get_tile_pos())
    tile = farm.tileMap[x][y]
    if isinstance(tile, block_list.block_list[1]):  # type: ignore
        farm.tileMap[x][y].interact()  # type: ignore


def process(nick):
    global select_bar
    x, y = map(int, runtime_values.players[0].get_tile_pos())  # type: ignore
    for event in pygame.event.get():
        moving(event)
        select(event)
        debug.debug(event)
        if event.type == pygame.QUIT:
            runtime_values.running = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_d:
                    use()

                # group: change handle item
                case pygame.K_z:  # 선택 해제
                    runtime_values.players[0].handle_item = Items.NONE

                case pygame.K_m:  # 블록 선택
                    if runtime_values.players[0].handle_item in block_list.block_list:
                        if (
                            runtime_values.players[0].handle_item
                            == block_list.block_list[-1]
                        ):
                            runtime_values.players[
                                0
                            ].handle_item = block_list.block_list[0]
                        else:
                            runtime_values.players[
                                0
                            ].handle_item = block_list.next_block(
                                runtime_values.players[0].handle_item
                            )
                    else:
                        runtime_values.players[0].handle_item = block_list.block_list[0]

                case pygame.K_a:  # 판매
                    sell.sell(runtime_values.players[0].handle_item)  # type: ignore

                case pygame.K_SPACE:  # 달리기
                    runtime_values.players[0].speed = 4.5

                case pygame.K_k:
                    lib.save.write_save()
                case pygame.K_l:
                    lib.save.import_save()

                # case pygame.K_0:  # TODO:cheat
                #     if int(input("dev code\n")) == 100000:
                #         playerClass.speed = 3
                #         playerClass.inventory = {
                #             "rice": 100000, "riceSeed": 100000, "gold": 100000}
                #         growCount = 5000
                case pygame.K_ESCAPE:  # 메뉴
                    runtime_values.on_setting = not runtime_values.on_setting

                case pygame.K_f:  # 블록 사용
                    block_use()

                case pygame.K_h:
                    help.help()
                case pygame.K_n:
                    pygame.mouse.set_visible(True)
                    chat.sand(input("msg : "), nick)
                    pygame.mouse.set_visible(False)

        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_SPACE:
                    runtime_values.players[0].speed = 3


def select(event: pygame.event.Event):
    global select_bar
    if event.type == pygame.KEYDOWN:
        if event.key in SELECT_KEY.keys():
            select_bar = SELECT_KEY[event.key]
            try:
                if (
                    list(runtime_values.players[0].inventory.items())[select_bar - 1][0]
                    in block_list.block_name
                ):
                    runtime_values.players[0].handle_item = block_list.block_list[
                        block_list.block_name.index(
                            list(runtime_values.players[0].inventory.items())[
                                select_bar - 1
                            ][0]
                        )
                    ]
                elif (
                    list(runtime_values.players[0].inventory.items())[select_bar - 1][0]
                    in plants_list.plants_seed_name
                ):
                    runtime_values.players[0].handle_item = plants_list.plants_list[
                        plants_list.plants_seed_name.index(
                            list(runtime_values.players[0].inventory.items())[
                                select_bar - 1
                            ][0]
                        )
                    ]
                elif (
                    list(runtime_values.players[0].inventory.items())[select_bar - 1][0]
                    in plants_list.plants_name
                ):
                    runtime_values.players[0].handle_item = list(runtime_values.players[0].inventory.items())[select_bar - 1][0]  # type: ignore
                else:
                    runtime_values.players[0].handle_item = list(items.Items)[items.value_name.index(list(runtime_values.players[0].inventory.items())[select_bar - 1][0])]  # type: ignore
            except:
                pass


def moving(event: pygame.event.Event):
    if event.type == pygame.KEYDOWN:
        match event.key:
            case pygame.K_LEFT:
                if runtime_values.my_dir == player.Direction.STOP:
                    runtime_values.my_dir = player.Direction.LEFT
                if runtime_values.my_dir == player.Direction.UP:
                    runtime_values.my_dir = player.Direction.UP_LEFT
                if runtime_values.my_dir == player.Direction.DOWN:
                    runtime_values.my_dir = player.Direction.DOWN_LEFT
            case pygame.K_RIGHT:
                if runtime_values.my_dir == player.Direction.STOP:
                    runtime_values.my_dir = player.Direction.RIGHT
                if runtime_values.my_dir == player.Direction.UP:
                    runtime_values.my_dir = player.Direction.UP_RIGHT
                if runtime_values.my_dir == player.Direction.DOWN:
                    runtime_values.my_dir = player.Direction.DOWN_RIGHT
            case pygame.K_UP:
                if runtime_values.my_dir == player.Direction.STOP:
                    runtime_values.my_dir = player.Direction.UP
                if runtime_values.my_dir == player.Direction.LEFT:
                    runtime_values.my_dir = player.Direction.UP_LEFT
                if runtime_values.my_dir == player.Direction.RIGHT:
                    runtime_values.my_dir = player.Direction.UP_RIGHT
            case pygame.K_DOWN:
                if runtime_values.my_dir == player.Direction.STOP:
                    runtime_values.my_dir = player.Direction.DOWN
                if runtime_values.my_dir == player.Direction.LEFT:
                    runtime_values.my_dir = player.Direction.DOWN_LEFT
                if runtime_values.my_dir == player.Direction.RIGHT:
                    runtime_values.my_dir = player.Direction.DOWN_RIGHT
    if event.type == pygame.KEYUP:
        match event.key:
            case pygame.K_LEFT:
                if runtime_values.my_dir == player.Direction.LEFT:
                    runtime_values.my_dir = player.Direction.STOP
                if runtime_values.my_dir == player.Direction.UP_LEFT:
                    runtime_values.my_dir = player.Direction.UP
                if runtime_values.my_dir == player.Direction.DOWN_LEFT:
                    runtime_values.my_dir = player.Direction.DOWN
            case pygame.K_RIGHT:
                if runtime_values.my_dir == player.Direction.RIGHT:
                    runtime_values.my_dir = player.Direction.STOP
                if runtime_values.my_dir == player.Direction.UP_RIGHT:
                    runtime_values.my_dir = player.Direction.UP
                if runtime_values.my_dir == player.Direction.DOWN_RIGHT:
                    runtime_values.my_dir = player.Direction.DOWN
            case pygame.K_UP:
                if runtime_values.my_dir == player.Direction.UP:
                    runtime_values.my_dir = player.Direction.STOP
                if runtime_values.my_dir == player.Direction.UP_LEFT:
                    runtime_values.my_dir = player.Direction.LEFT
                if runtime_values.my_dir == player.Direction.UP_RIGHT:
                    runtime_values.my_dir = player.Direction.RIGHT
            case pygame.K_DOWN:
                if runtime_values.my_dir == player.Direction.DOWN:
                    runtime_values.my_dir = player.Direction.STOP
                if runtime_values.my_dir == player.Direction.DOWN_LEFT:
                    runtime_values.my_dir = player.Direction.LEFT
                if runtime_values.my_dir == player.Direction.DOWN_RIGHT:
                    runtime_values.my_dir = player.Direction.RIGHT

def grow_plants(event: pygame.event.Event):
    for line in farm.tileMap:
        for tile in line:
            if isinstance(tile, plants_list.plants_list):  # type: ignore
                if event.type == tile.GROW_EVENT:
                    tile.grow() # type: ignore
