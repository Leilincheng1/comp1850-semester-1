"""Identify sensors below 20 percent battery charge."""
home_sensors = {"Living Room Thermostat": 85, "Front Door Lock": 15,
                "Kitchen Smoke Detector": 90, "Basement Flood Sensor": 8}
low_battery = {name: level for name, level in home_sensors.items() if level < 20}
print(low_battery)
