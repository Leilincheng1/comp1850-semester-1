"""Demonstrate progressive income tax using the exercise's fixed bands.

This is the simplified course model, not a current UK tax calculator.
"""


def income_tax_calculator(annual_income):
    """Return the rounded tax, or 0.0 for a nonpositive or nonnumeric income."""
    if isinstance(annual_income, bool) or not isinstance(annual_income, (int, float)):
        return 0.0
    if annual_income <= 0:
        return 0.0
    taxable = float(annual_income)
    tax = (min(max(taxable - 12570, 0), 50270 - 12570) * 0.20
           + min(max(taxable - 50270, 0), 125140 - 50270) * 0.40
           + max(taxable - 125140, 0) * 0.45)
    return round(tax, 1)


if __name__ == "__main__":
    for income in (12000, 14000, 25000, 100000):
        print(income_tax_calculator(income))
