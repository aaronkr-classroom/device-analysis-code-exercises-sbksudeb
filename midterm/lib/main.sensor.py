# main.py - Main application [1]
from lib.room_sensor import RoomSensor # Importing the class module [1]

# Part 3: Create at least 3 RoomSensor objects and store them in a list [4]
# Uses a list structure as demonstrated in source examples [5]
sensors = [
    RoomSensor("Kitchen", 31, 72, 180),
    RoomSensor("Bedroom", 24, 50, 250),
    RoomSensor("Balcony", 28, 45, 500)
]

# Part 5: Initialize totals for the Extra Challenge [4, 6]
comfortable_count = 0
normal_count = 0
warning_count = 0

# Part 4: Use a for loop to iterate through the list [4]
for s in sensors:
    # Print the sensor info [4]
    s.show_info()
    
    # Get comfort and light details
    comfort = s.comfort_level()
    light = s.light_status()
    
    # Print the combined output line [4]
    print(f"Comfort Level: {comfort} Light Status: {light}")
    
    # Part 5: Update the totals for each category [6]
    if comfort == "Comfortable":
        comfortable_count += 1
    elif comfort == "Normal":
        normal_count += 1
    elif comfort == "Warning":
        warning_count += 1

# Part 5: Print final totals [6]
print(f"\nComfortable: {comfortable_count} Normal: {normal_count} Warning: {warning_count}")
