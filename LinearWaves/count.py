def count_color(x):
    output = [0, 0, 0]
    if (x > 560) and (x <= 760):
        output[0] = 255
    if (x > 495) and (x <= 555):
        output[0] = 0
    if (x > 570) and (x <= 580):
        output[0] = round(127.5 + 127.5 * (x - 570) / 10)
    if (x > 555) and (x <= 570):
        output[0] = round(127.5 * (x - 555) / 15)
    if (x > 480) and (x <= 495):
        output[0] = round(127.5 - 127.5 * (x - 480) / 15)
    if (x > 380) and (x <= 480):
        output[0] = round(255 - 127.5 * (x - 380) / 100)

    if (x > 525) and (x <= 580):
        output[1] = 255
    if (x > 380) and (x <= 495):
        output[1] = 0
    if (x > 610) and (x <= 760):
        output[1] = round(63.5 - 63.5 * (x - 610) / 150)
    if (x > 600) and (x <= 610):
        output[1] = round(127.5 - 63.5 * (x - 600) / 10)
    if (x > 590) and (x <= 600):
        output[1] = round(190.5 - 63.5 * (x - 590) / 10)
    if (x > 580) and (x <= 590):
        output[1] = round(255 - 63.5 * (x - 580) / 10)
    if (x > 495) and (x <= 510):
        output[1] = round(127.5 * (x - 495) / 15)
    if (x > 510) and (x <= 525):
        output[1] = round(127.5 + 127.5 * (x - 510) / 15)
        
    if (x > 380) and (x <= 525):
        output[2] = 255
    if (x > 555) and (x <= 760):
        output[2] = 0
    if (x > 540) and (x <= 555):
        output[2] = round(127.5 - 127.5 * (x - 540) / 15)
    if (x > 525) and (x <= 540):
        output[2] = round(255 - 127.5 * (x - 525) / 15)

    return tuple(output)

