from PIL import Image, ImageDraw
from math import exp
import numpy as np
import time

WIDTH = 5000  # 5000
HEIGHT = 2500  # 2500

TAN = np.arange(-5.1, 5.3, 0.2)  # тангенсы угла между прямыми и осью OX
TAU = 625  # разница между двумя отверстиями в пикселях
A = (0, 200, 0)  # амплитуда Интенсивности одного луча
EPSILON = 0 / WIDTH * 255  # коэффициент затухания света
SIZE = 1  # Размер одного луча

ADDITITIONAL_SPACE = WIDTH ** 0.5 * max(TAN)


def main():
    time.clock()
    color = (0, 0, 0)
    image = Image.new('RGB', (WIDTH, HEIGHT), color)
    pixel = image.load()
    lasts = [0] * len(TAN)

    for delta in range(int(-ADDITITIONAL_SPACE), int(HEIGHT + ADDITITIONAL_SPACE), TAU):
        percents = (delta + ADDITITIONAL_SPACE) / (HEIGHT + ADDITITIONAL_SPACE * 2) * 100
        timing = time.clock()
        print(str(round((delta + ADDITITIONAL_SPACE) / (HEIGHT + ADDITITIONAL_SPACE * 2) * 100, 2)) + "%",
              round(time.clock(), 2), "Осталось времени: " + str((100 - percents) * timing / percents) + 'сек')
        for x in range(WIDTH):
            i = 0
            for tan in TAN:
                y1 = int(x ** 0.5 * tan + delta)
                y2 = lasts[i]

                y1 = (y1 if y1 < HEIGHT else HEIGHT) if y1 > 0 else 0
                y2 = (y2 if y2 < HEIGHT else HEIGHT) if y2 > 0 else 0
                if y1 < y2:
                    y2 = (y2 + SIZE) if (y2 + SIZE) < HEIGHT else HEIGHT
                    for y in range(y1, y2):
                        color = (
                            int(pixel[x, y][0] + A[0] - x * EPSILON),
                            int(pixel[x, y][1] + A[1] - x * EPSILON),
                            int(pixel[x, y][2] + A[2] - x * EPSILON)
                        )
                        pixel[x, y] = color
                else:
                    y1 = (y1 + SIZE) if (y1 + SIZE) < HEIGHT else HEIGHT
                    for y in range(y2, y1):
                        color = (
                            int(pixel[x, y][0] + A[0] - x * EPSILON),
                            int(pixel[x, y][1] + A[1] - x * EPSILON),
                            int(pixel[x, y][2] + A[2] - x * EPSILON)
                        )
                        pixel[x, y] = color

                lasts[i] = y1
                i += 1

    print(time.clock(), ' сек')
    print(type(pixel), type(image))

    image.save('Taldot.png')


if __name__ == "__main__":
    main()
