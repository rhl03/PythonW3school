# Tip Calculator


def calculate_tip(bill: float, tip_percent: int):
    # Calculate tip and total
    tip = bill * tip_percent / 100
    total = bill + tip
    # Print formatted results
    print(f"Bill: ${bill:.2f}")
    print(f"Tip: ${tip:.2f}")
    print(f"Total: ${total:.2f}")


# Read input
bill = float(input())
tip_percent = int(input())

calculate_tip(bill, tip_percent)
