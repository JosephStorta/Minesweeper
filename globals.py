from pygame import image

SCREEN_SIZE = (640, 480)
TILE_SIZE = (16, 16)
TILE_SCALE = 2
TILE_SPRITE = "./sprites/Tiles.png"

TILE_SPRITES = []

def readTiles():
    sheet = image.load(TILE_SPRITE).convert()

    for y in range(0, sheet.get_height(), TILE_SIZE[1]):
        for x in range(0, sheet.get_width(), TILE_SIZE[0]):
            sprite = sheet.get_rect(x = x, y = y, size = TILE_SIZE)
            TILE_SPRITES.append(sheet.subsurface(sprite))