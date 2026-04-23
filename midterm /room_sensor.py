# room_sensor.py - Class module [1]

class RoomSensor:
    def __init__(self, name, temperature, humidity, light):
        # Part 1: Constructor receiving all 4 values [1]
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light

    def show_info(self):
        # Part 2: Print sensor information in a readable format [1, 2]
        # Uses f-string formatting similar to source examples [3]
        print(f"Sensor: {self.name} Temperature: {self.temperature} Humidity: {self.humidity} Light: {self.light}", end=" ")

    def comfort_level(self):
        # Part 2: Return comfort level based on temperature and humidity conditions [2]
        if 20 <= self.temperature <= 26 and 40 <= self.humidity <= 60:
            return "Comfortable"
        elif self.temperature >= 30 or self.humidity >= 70:
            return "Warning"
        else:
            return "Normal"

    def light_status(self):
        # Part 2: Return status based on light level [2]
        if self.light < 200:
            return "Dark"
        else:
            return "Bright"
