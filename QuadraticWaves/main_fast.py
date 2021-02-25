from PIL import Image, ImageDraw
from math import exp
import numpy as np
import time
time.clock()

WIDTH = 500  # 5000
HEIGHT = 20000  # 2500

TAN = np.arange(-20.1, 20.3, 0.2)  # тангенсы угла между прямыми и осью OX
TAU = 5000  # разница между двумя отверстиями в пикселях
A = (0, 200, 0)  # амплитуда Интенсивности одного луча
EPSILON = 0 / WIDTH * 255  # коэффициент затухания света
SIZE = 1  # Размер одного луча

ADDITITIONAL_SPACE = WIDTH * max(TAN)


def main():
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
                y1 = int(x ** 0.5 * tan + delta)
                y2 = y1 + SIZE

                y1 = (y1 if y1 < HEIGHT else HEIGHT) if y1 > 0 else 0
                y2 = (y2 if y2 < HEIGHT else HEIGHT) if y2 > 0 else 0

                for y in range(y1, y2):
                    color = (int(pixel[x, y][0] + A[0] - x * EPSILON),
                             int(pixel[x, y][1] + A[1] - x * EPSILON),
                             int(pixel[x, y][2] + A[2] - x * EPSILON)
                            )
                    pixel[x, y] = color

    print(time.clock())
    print(type(pixel), type(image))

    image.save('Talbot fast.png')


if __name__ == "__main__":
    main()
