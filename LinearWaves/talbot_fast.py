from PIL import Image, ImageDraw
from math import exp
import numpy as np
import time
time.clock()

WIDTH = 10000     # 5000
HEIGHT = 2500  # 2500

TAN = np.arange(-5.1, 5.3, 0.2)  # тангенсы угла между прямыми и осью OX
TAU = 1000  # разница между двумя отверстиями в пикселях
A = (0, 200, 0)  # амплитуда Интенсивности одного луча
EPSILON = 0 / WIDTH * 255  # коэффициент затухания света
SIZE = 1  # Размер одного луча

ADDITITIONAL_SPACE = WIDTH * max(TAN)


def Talbot():
    time.clock()
    color = (0, 0, 0)
    image = Image.new('RGB', (WIDTH, HEIGHT), color)
    pixel = image.load()

    for delta in range(int(-ADDITITIONAL_SPACE), int(HEIGHT + ADDITITIONAL_SPACE), TAU):
        percents = (delta + ADDITITIONAL_SPACE) / (HEIGHT + ADDITITIONAL_SPACE * 2) * 100
        timing = time.clock()
        print(str(round((delta + ADDITITIONAL_SPACE) / (HEIGHT + ADDITITIONAL_SPACE * 2) * 100, 2)) + "%",
              round(time.clock(), 2), "Осталось времени: " + str((100 - percents) * timing / percents) + 'сек')
        for x in range(WIDTH):
            for tan in TAN:
                y1 = int(x * tan + delta)
                y2 = y1 + SIZE

                if y1 > HEIGHT or y1 < 0:
                    continue
                if y2 > HEIGHT or y2 < 0:
                    continue

                for y in range(y1, y2):
                    color = (
                             int(pixel[x, y][0] + A[0] - x * EPSILON),
                             int(pixel[x, y][1] + A[1] - x * EPSILON),
                             int(pixel[x, y][2] + A[2] - x * EPSILON)
                            )
                    pixel[x, y] = color

    print(time.clock())
    print(type(pixel), type(image))

    image.save('Talbot fast.png')


if __name__ == "__main__":
    main()
