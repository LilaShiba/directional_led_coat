from utils import control 
import time

class CyberCoat:
    def __init__(self):
        self.sensors = control.Sensors()

    def startup_protocol(self):
        self.sensors.init_i2c()
        self.sensors.init_sensors()

    def get_location(self):
        start_time = time.time()
        x, y, z = 0, 0, 0
        for _ in range(5):
            lat, lon, speed = self.sensors.read_gps()
            x += lat
            y += lon
            z += speed
        end_time = time.time()
        lapse = end_time - start_time
        return (x / 5, y / 5, z / 5, lapse)

    def main(self):
        self.startup_protocol()