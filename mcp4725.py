# Copyright (c) 2016 Adafruit Industries
# Initial Author: Tony DiCola
# Copyright (c) 2021 Robert Hammelrath
# Changed for genuine Micropython
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Register values:
WRITEDAC         = 0x40
WRITEDACEEPROM   = 0x60

# Default I2C address:
DEFAULT_ADDRESS  = 0x60


class MCP4725():
    """Base functionality for MCP4725 digital to analog converter."""

    def __init__(self, i2c, address=DEFAULT_ADDRESS):
        """Create an instance of the MCP4725 DAC."""
        self.i2c = i2c
        self.msg = bytearray(3)
        self.address = address

    def set(self, value, persist=False):
        """Set the output voltage to specified value.  Value is a 12-bit number
        (0-4095) that is used to calculate the output voltage from:

          Vout =  (VDD*value)/4096

        I.e. the output voltage is the VDD reference scaled by value/4096.
        If persist is true it will save the voltage value in EEPROM so it
        continues after reset (default is false, no persistence).
        """
        # Clamp value to an unsigned 12-bit value.
        if value > 4095:
            value = 4095
        if value < 0:
            value = 0
        # Generate the register bytes and send them.
        # See datasheet figure 6-2:
        self.msg[0] = WRITEDACEEPROM if persist else WRITEDAC
        self.msg[1] = value >> 4
        self.msg[2] = (value << 4) & 0xFF
        self.i2c.writeto(self.address, self.msg)
