from PIL import Image, ImageDraw
from math import pi, exp, tan, sin, asin
import numpy as np
import time


STEP = 0.5
N = 9
MAX_K = STEP * (N + 0.5)
OPEN = 1  # количество пикселей открытой части
CLOSE = 1000  # количество пикселей закрытой части
PERIOD = OPEN + CLOSE  # Период решетки
K = np.arange(-MAX_K, MAX_K + STEP, STEP)

HEIGHT = PERIOD * 3  # 2500
WIDTH = int(2 * PERIOD / min(map(abs, K)) / 2) + 200  # 5000
TAN = [i for i in K]  # [i * LAMBDA / PERIOD for i in K]  # тангенсы угла между прямыми и осью OX
TAU = PERIOD  # разница между двумя отверстиями в пикселях
A = (0, 150, 0)  # амплитуда Интенсивности одного луча
EPSILON = 0 / WIDTH * 255  # коэффициент затухания света
SIZE = OPEN  # Размер одного луча

ADDITIONAL_SPACE = WIDTH * max(TAN)


def normalization(a):
    if a[0] >= 256:
        if a[1] >= 256:
            if a[2] >= 256:
                a = (255, 255, 255)
            else:
                a = (255, 255, a[2])
        else:
            if a[2] >= 256:
                a = (255, a[1], 255)
            else:
                a = (255, a[1], a[2])
    else:
        if a[1] >= 256:
            if a[2] >= 256:
                a = (a[0], 255, 255)
            else:
                a = (a[0], 255, a[2])
        else:
            if a[2] >= 256:
                a = (a[0], a[1], 255)
            else:
                pass  # color = color
    return a


def format_angle(x):
    print(x)
    while -2 * pi < x < 2 * pi:
        x = (x + 2 * pi) if x < 0 else (x - 2 * pi)
    return x


def talbot(step=STEP, n=N, max_k=None, open=OPEN, close=CLOSE, period=None, height=None,
           width=None,
           tan=None, tau=None, a=A, epsilon=None, size=None, additional_space=None,
           filename='Talbot.png'):

    if max_k is None:
        max_k = step * (n + 0.5)
    if period is None:
        period = open + close

    k = np.arange(-max_k, max_k + step, step)
    if height is None:
        height = period * 3
    if width is None:
        print(1, 2 * period / float(min(map(abs, k))))
        width = int(2 * period / float(min(map(abs, k))) / 2) + 200
    if tan is None:
        tan = [i for i in k]
    if tau is None:
        tau = period
    if epsilon is None:
        epsilon = 0 / width * 255
    if size is None:
        size = open
    if additional_space is None:
        additional_space = width * max(tan)

    print("period:", period, "step:", step, "min", min(map(abs, k)))
    print("Height:", height, "Width", width)

    time.clock()
    color = (0, 0, 0)
    image = Image.new('RGB', (width, height), color)
    pixel = image.load()

    for i in range(len(tan)):
        tan_step = tan[i]
        percents = i / (len(tan)) * 100 + 0.0001
        timing = time.clock()
        print(str(round(percents, 2)) + "%",
              round(time.clock(), 2), "Осталось времени: " + str((100 - percents) * timing / percents) + 'сек')
        for delta in range(int(-additional_space), int(height + additional_space), tau):
            last = delta
            for x in range(100, width - 100):
                y1 = int((x - 100) * tan_step + delta)
                add = int(size)
                y2 = last
                last = y1

                if y1 > y2:
                    y1, y2 = y2, y1
                if y1 < 0:
                    y1 = 0
                if y2 > height:
                    y2 = height

                y1 = y1 if (y1 > 0) else 0
                y2 = (y2 + add) if (y2 + add) < height else height
                for y in range(y1, y2):
                    color = (
                        int(pixel[x, y][0] + a[0] - x * epsilon),
                        int(pixel[x, y][1] + a[1] - x * epsilon),
                        int(pixel[x, y][2] + a[2] - x * epsilon)
                    )  # pixel
                    pixel[x, y] = normalization(color)
    print(time.clock(), ' сек')
    image.save(filename)

'''
    for y in range(HEIGHT // 20):
        for x in range(- WIDTH // 500, WIDTH // 500 + 1):
            pixel[int(round(range_talbot + x + 100)), y] = (255, 255, 255)
            pixel[int(round(range_talbot // 2 + x + 100)), y] = (255, 255, 255)
            pixel[int(round(range_talbot // 3 + x + 100)), y] = (255, 255, 255)
            pixel[int(round(range_talbot // 4 + x + 100)), y] = (255, 255, 255)
            pixel[int(round(range_talbot // 5 + x + 100)), y] = (255, 255, 255)
'''

