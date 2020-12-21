from st7920 import Screen
import machine

# implicitly uses hardware spi; https://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html#hardware-spi-bus
spi = machine.SPI(1, baudrate=100000, polarity=1, phase=1)
screen = Screen(spi=spi)

def clear():
    screen.clear()
    screen.redraw()

def draw():

    # write zeroes to the buffer
    screen.clear()

    # draw some points, lines, rectangles, filled rectangles in the buffer
    screen.plot(5, 5)
    screen.line(10, 10, 15, 15)
    screen.rect(20, 20, 25, 25)
    screen.fill_rect(30, 30, 40, 40)
    screen.fill_rect(32, 32, 38, 38, False)

    # send the buffer to the display
    screen.redraw()

def run():
    clear()
    draw()

if __name__ == "__main__":
    run()
    
    
