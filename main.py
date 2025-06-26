from utils import control 
import time
from dotenv import load_dotenv
import os
import numpy as np

class CyberCoat:
    def __init__(self):
        self.sensors = control.Sensors()
        self.location = (None, None)
        self.lat = int(os.getenv('LAT'))
        self.lon = int(os.getenv('LON'))
        self.home = (self.lat, self.lon)
        self.dx, self.dy = self.lat, self.lon
        self.bearing_deg = 0

    def startup_protocol(self):
        self.sensors.init_i2c()
        self.sensors.init_sensors()

    def get_location(self):
        start_time = time.time()
        x, y, z, = 0, 0, 0
        for _ in range(5):
            lat, lon, speed = self.sensors.read_gps()
            x += lat
            y += lon
            z += speed
        end_time = time.time()
        lapse = end_time - start_time
        return (x / 5, y / 5, z / 5, lapse)

    def euclidean(self):
        return np.sqrt( (self.lat - self.dx)**2 + (self.lon - self.dy)**2 )
    
    def manhattan(self):
        return abs(self.lat - self.dx) + abs(self.lon - self.dy)

    def get_bearng(self):
        angle_rad = np.atan2(self.dx, self.dy)  
        self.bearing_deg = (np.degrees(angle_rad) + 360) % 360
        return self.bearing_deg

    def get_me_home(self):
        while self.location != self.home:
            self.get_location()
            self.get_bearng()


    def main(self):
        self.startup_protocol()
        self.get_location()
        self.get_bearng()