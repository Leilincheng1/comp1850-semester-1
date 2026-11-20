"""Convert each student's lateness from minutes into days, hours and minutes."""
from pathlib import Path

data_file = Path(__file__).parent / "_data" / "lateness_data.csv"
with data_file.open(encoding="utf-8") as f:
    data = [line.strip().split(",") for line in f]

for row in data:
    minutes_late = int(row[1])
    days = minutes_late // 1440
    hours = (minutes_late % 1440) // 60
    minutes = minutes_late % 60
    print(f"Student {row[0]}: {days}D {hours}H {minutes}M")
