"""Monitor a factory machine's operating temperature and pressure."""
from datetime import datetime


def evaluate(temperature, pressure, operating):
    """Return status messages for temperature, pressure and machine state."""
    messages = []
    if temperature > 80:
        messages.append("Temperature too high: shut down the machine.")
    elif temperature >= 50:
        messages.append("Temperature is within safe limits.")
    else:
        messages.append("Temperature is low: no action needed.")

    if pressure > 100:
        messages.append("High pressure detected: perform maintenance.")
    elif pressure >= 70:
        messages.append("Pressure is stable.")
    else:
        messages.append("Pressure is low: system is operating normally.")

    if operating == 1:
        if temperature > 80 or pressure > 100:
            messages.append("Machine is running in unsafe conditions: shut it down.")
        else:
            messages.append("Machine is running normally.")
    else:
        messages.append("Machine is stopped: no immediate action needed.")
    return messages


def main():
    """Read sensor inputs, report status and append a timestamped log."""
    try:
        temperature = int(input("Temperature (°C): "))
        pressure = int(input("Pressure (PSI): "))
        operating = int(input("Operating (1=yes, 0=no): "))
    except ValueError:
        print("Error: enter integer values for all inputs.")
        return
    if operating not in (0, 1):
        print("Error: operational status must be 0 or 1.")
        return

    messages = evaluate(temperature, pressure, operating)
    for message in messages:
        print(message)

    with open("machine_log.txt", "a", encoding="utf-8") as logfile:
        logfile.write(f"[{datetime.now().isoformat(timespec='seconds')}] "
                      f"temperature={temperature}°C, pressure={pressure} PSI, "
                      f"operating={operating}\n")
        for message in messages:
            logfile.write(f"  {message}\n")


if __name__ == "__main__":
    main()
