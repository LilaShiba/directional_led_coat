import argparse
from typing import Optional, Tuple

# Raspberry Pi-specific imports
import board
import busio
import adafruit_gps

# Constants
MAX_RETRIES = 5
RETRY_DELAY = 0.5


# 🛠️ Initialization Functions
class Sensors:
    """Handles the initialization of I2C and sensors."""
    
    def __init__(self, frequency: int = I2C_FREQUENCY):
        self.i2c = self.init_i2c(frequency)
        self.sensors = self.init_sensors()
        self.gps = self.sensors['gps']

    def init_i2c(self, frequency: int) -> busio.I2C:
        """Initializes and returns the I2C connection."""
        return busio.I2C(board.SCL, board.SDA, frequency=frequency)

    def init_sensors(self) -> dict:
        """Initializes all sensors and returns them as a dictionary."""
        return {
    
            "gps": adafruit_gps.GPS_GtopI2C(self.i2c, debug=False)
        }

    def read_gps(self) -> Optional[Tuple[float, float, float]]:
        self.gps.update()
        return self.gps.latitude, self.gps.longitude, self.gps.speed_knots
    
    @staticmethod
    def main(self, conditions):
        try:
            sensors = Sensors()
            sensors.configure_sensors()

        except KeyboardInterrupt:
            print("\n🛑 Data recording interrupted by user.")

        except Exception as e:
            print(f"🔥 Fatal error: {e}")

    @staticmethod
    def parse_args():
        """Parse command-line arguments."""
        parser = argparse.ArgumentParser(description="Record sensor data to CSV.")
        parser.add_argument('--duration', type=int, default=10,
                            help='Recording duration in seconds')
        parser.add_argument('--frequency', type=int, default=1,
                            help='Sampling frequency in Hz')
        return parser.parse_args()


if __name__ == "__main__":
    Sensors.main()
