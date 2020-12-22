# Micropython ST7920

Micropython library for simple graphic primitives on ST7920 128x64 monochrome LCD panel using ESP8266 and SPI

# Features

Can initialise a screen and framebuffer with...

```python
import st7920 
screen = st7920.Screen()
```

Can draw points, lines and rectangles to a framebuffer with e.g.

```
screen.plot(10, 10)
screen.line(10, 10, 20, 20)
screen.rect(25, 25, 50, 50)
screen.fill_rect(5, 5, 95, 95)
```

Can draw inverse with e.g.

```
screen.plot(10, 10, False)
screen.line(10, 10, 20, 20, False)
screen.rect(25, 25, 50, 50, False)
screen.fill_rect(5, 5, 95, 95, False)
```

Then send finished 1kbyte frame to the screen at 1.8Mbaud with...

```
screen.redraw()
```

Finally clear again with...
```
screen.clear()
screen.redraw()
```

# Included Example

Install ampy by running...

```bash
pip install adafruit-ampy
```

Then change to this directory and upload files...

```bash
ampy --port /dev/ttyUSB0 put st7920.py
ampy --port /dev/ttyUSB0 put example.py
```

You should then be able to interactively run the following from the REPL...

```python
import example
example.run
```

Alternatively upload the main.py file as well as follows...

```bash
ampy --port /dev/ttyUSB0 put main.py
```

...and the example will automatically run on boot


# Typography

See also @ShrimpingIt's [bitfont project](https://github.com/ShrimpingIt/bitfont) 
for pixel typography logic which can be used with micropython-st7920 and 
other bit-rendering environments.

# Credits

Developed by @cefn of @ShrimpingIt based on @JMW95's incredibly useful reference Raspberry Pi python SPI port at https://github.com/JMW95/pyST7920, funded by the Milecastles project

# Todo

Consider use of Micropython's [framebuf](https://docs.micropython.org/en/latest/esp8266/library/framebuf.html) Framebuffer library to see if it offers any acceleration, or just for conformance with other libraries - draw primitives look like they are the same.



# See also

[ST7920 Datasheet](http://www.hpinfotech.ro/ST7920.pdf)

[Micropython SPI reference](https://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html#software-spi-bus)

[Arduino U8G2 reference setup for ST7920 128x64 SPI display](https://github.com/olikraus/u8g2/wiki/setup_tutorial#identify-the-display)
