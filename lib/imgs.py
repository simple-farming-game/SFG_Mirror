import pygame

imgs: dict[str, pygame.Surface] = {
    "mus" : pygame.image.load("assets/img/mouse_cus.png"),
    "item_bar" : pygame.transform.scale(pygame.image.load("assets/img/ui/item_bar.png"),(256,32))
}

def img(imgName):
    return imgs[imgName] # type: ignore