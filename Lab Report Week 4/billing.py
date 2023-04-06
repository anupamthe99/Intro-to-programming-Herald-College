"""
Unit Price
First 100 units no charge
Next 100 units Rs 5 per unit
After 200 units Rs 10 per unit
"""

units = int(input("Enter the number of units: "))

bill_amount = 0
unit_rate = 0

if units <= 100:
    bill_amount = 0
    unit_rate = 0
elif units <= 200:
    unit_rate = 5
    bill_amount = (units - 100) * unit_rate
else:
    unit_rate = 10
    bill_amount = (100 * 5) + (units - 200) * unit_rate

print("Unit rate: Rs.", unit_rate)
print("Bill amount: Rs.", bill_amount)
