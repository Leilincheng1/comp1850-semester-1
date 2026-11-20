"""Find failed login requests from the provided web server log."""
import csv
from pathlib import Path

path = Path(__file__).with_name("site.log")
try:
    with path.open(encoding="utf-8", newline="") as log_file:
        for row in csv.DictReader(log_file):
            if row["Request"].strip() == "POST /login" and row["Status_Code"].strip() == "401":
                print(f"IP address {row['IP_Address']} failed to login "
                      f"at {row['Time']} on {row['Date']}")
except (OSError, KeyError, csv.Error) as error:
    print(f"Could not analyse log: {error}")
