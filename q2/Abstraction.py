from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self, data):
        pass

class PHSensor(Sensor):
    def get_reading(self, data):
        print(f"pH data: {data}")
        
class TempSensor(Sensor):
    def get_reading(self, data):
        print(f"Temperature data: {data}")


water = PHSensor()
water.get_reading(7.0)

temp = TempSensor()
temp.get_reading(25.0)

my_sensor = Sensor() 