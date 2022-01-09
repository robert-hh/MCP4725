# Simple MCP4725 class

Derived from the Adafruit MCP4725 class.

## Class

dac = MCP4725(i2c, * address=0x60)

Create the DAC instance. Parameters:

  *i2c*      The I2C object used for communication
  *address*  The I2C address. The default value is 0x60 

## Method

dac.set(value)

Set the ouput value of the DAC to Vdd * value / 4096. The input value is
silently clamped to the range 0..4095

## Example

```
# Simple demo of setting the output voltage of the MCP4725 DAC.
# Will alternate setting 0V, 1/2VDD, and VDD each second.
# Author: Tony DiCola
# License: Public Domain
import time
from machine import I2C

# Create the I2C object
i2c = I2C(0)

# Import the MCP4725 module.
import MCP4725

# Create a DAC instance.
dac = MCP4725.MCP4725(i2c)

# Note you can change the I2C address from its default (0x60), and/or the I2C
# bus by passing in these optional parameters:
#dac = MCP4725.MCP4725(i2c, address=0x62)

# Loop forever alternating through different voltage outputs.
print('Press Ctrl-C to quit...')
while True:
    print('Setting voltage to 0!')
    dac.set(0)
    time.sleep(2.0)
    print('Setting voltage to 1/2 Vdd!')
    dac.set(2048)  # 2048 = half of 4096
    time.sleep(2.0)
    print('Setting voltage to Vdd!')
    dac.set(4096, True)
    time.sleep(2.0)
```
