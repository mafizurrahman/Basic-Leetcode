def lemonadeChange(bills):
    bill_5 = 0
    bill_10 = 0

    for bill in bills:
        if bill == 5:
            bill_5 += 1
        elif bill == 10:
            bill_5 -= 1
            bill_10 += 1
        elif bill == 20:
            if bill_10 > 0:
                bill_10 -= 1
                bill_5 -= 1
            else:
                bill_5 -= 3

        if bill_5 < 0 or bill_10 < 0:
            return False

    return True


# Example 1
bills1 = [5, 5, 5, 10, 20]
print(lemonadeChange(bills1))  # Output: True
