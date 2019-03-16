import machine
from display import ssd1306

display = None
run = 0

def setup():
    global display

    from machine import I2C, Pin
    import uos

    _, nodename, _, _, _ = uos.uname()
    if nodename == 'esp32':
        i2c = I2C(freq=400000, scl=machine.Pin(22), sda=machine.Pin(21))
    elif nodename == 'pyboard':
        i2c = I2C(freq=400000, scl=machine.Pin('X9'), sda=machine.Pin('X10'))
    else:
        raise Exception('No compatible board found')

    display = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)

def stress(show=True):
    global display, run

    display.fill(0)

    run += 1

    display.text('CLT2019 %i uPython' % (run), 0, 0)

    i = 0

    for y in range(8, 56, 8):
        for x in range(0, 119, 8):
            display.text('%c' % (ord('0') + (((run + i) * 17) % 36)), x, y)
            i += 1

    if show:
        display.show()

def loop():
    loops = 100

    print('Stressing library and io ...')
    for i in range(loops):
        stress(show=True)
    print('Done')

try:
    setup()
    while True:
        loop()
except:
    pass
