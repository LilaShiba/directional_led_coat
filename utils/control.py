import argparse
from typing import Optional, Tuple
from leds import Leds
# Raspberry Pi-specific imports
import board # type: ignore
import busio # type: ignore
import adafruit_gps # type: ignore


# Constants
MAX_RETRIES = 5
RETRY_DELAY = 0.5
I2C_FREQUENCY = 100_000



# 🛠️ Initialization Functions
class Sensors:
    """Handles the initialization of I2C and sensors."""
    
    def __init__(self, frequency: int = I2C_FREQUENCY):
        self.i2c = self.init_i2c(frequency)
        self.sensors = self.init_sensors()
        self.gps = self.sensors['gps']
        self.led = self.sensors['leds']

    def init_i2c(self, frequency: int) -> busio.I2C:
        """Initializes and returns the I2C connection."""
        return busio.I2C(board.SCL, board.SDA, frequency=frequency)

    def init_sensors(self) -> dict:
        """Initializes all sensors and returns them as a dictionary."""
        return {
    
            "gps": adafruit_gps.GPS_GtopI2C(self.i2c, debug=False),
            "leds": Leds(self.i2c),
        }

    def read_gps(self) -> Optional[Tuple[float, float, float]]:
        self.gps.update()
        return (self.gps.latitude, self.gps.longitude, self.gps.speed_knots)
    

