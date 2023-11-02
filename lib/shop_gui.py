import pygame

btn_list = []

def init(plants_list, block_list):
    from lib.lang import text
    from lib import ui
    btn_y = 10
    index = 1
    for item in plants_list:
        btn_list.append(ui.Btn(f"{index}. {text(f'items.{item.name}')} {text(f'gold')} : {item.price}", lambda: buy(item.name), pygame.math.Vector2(10,btn_y)))
        index+=1
        btn_y+=30
    for item in block_list:
        btn_list.append(ui.Btn(f"{index}. {text(f'blocks.{item.name}')} {text(f'gold')} : {item.price}", lambda: buy(item.name), pygame.math.Vector2(10,btn_y)))
        index+=1
        btn_y+=30

def buy(name):
    from lib import shop_system

    shop_system.buy(name)

def shop_open():
    from lib.new_screen import background
    from lib.new_screen import color
    from lib import draw
    from lib.lang import text
    from lib import runtime_values
    
    font_renderer = runtime_values.font
    SKYBLUE = pygame.Color(113, 199, 245)
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)

    
    background(color.SKYBLUE)
    draw.draw_text_with_border(  # 좌표
                runtime_values.screen,
                font_renderer,
                f"{text(f'gold')} : {runtime_values.players[0].gold}",
                WHITE,
                BLACK,
                2,
                pygame.math.Vector2(5,runtime_values.window_size[1]-25),
            )
    
    for btn in btn_list:
        btn.draw()