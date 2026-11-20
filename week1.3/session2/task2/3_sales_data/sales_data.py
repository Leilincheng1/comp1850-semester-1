# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.3, Session 2: Sales Data Statistics
#
# We want to analyse a set of sales data in sales.csv
#
# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format
#
#
# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget
#
#
# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows
# ============================================================================
# Completed solution
# ============================================================================
"""Analyse sales rows and summarize products and regions."""
import csv
from collections import Counter, defaultdict
from pathlib import Path

try:
    with (Path(__file__).parent / "sales.csv").open(encoding="utf-8", newline="") as source:
        rows = list(csv.DictReader(source))
except OSError as error:
    print(f"Cannot read sales data: {error}")
else:
    if not rows:
        print("No sales data available.")
    else:
        largest = max(rows, key=lambda row: int(row["Sales_Amount"]))
        average = sum(int(row["Sales_Amount"]) for row in rows) / len(rows)
        units = Counter()
        region_totals = defaultdict(int)
        region_units = defaultdict(Counter)
        product_totals = defaultdict(int)
        for row in rows:
            product, region = row["Product"], row["Region"]
            quantity, amount = int(row["Units_Sold"]), int(row["Sales_Amount"])
            units[product] += quantity
            region_totals[region] += amount
            region_units[region][product] += quantity
            product_totals[product] += amount
        print(f"Largest sale day: {largest['Date']} (£{int(largest['Sales_Amount'])})")
        print(f"Average sale amount: £{average:.2f}")
        print(f"Most sold widget: {units.most_common(1)[0][0]}")
        print(f"Regional sales totals: {dict(region_totals)}")
        for region, totals in region_units.items():
            print(f"Most sold in {region}: {totals.most_common(1)[0][0]}")
        print(f"Product sales totals: {dict(product_totals)}")
