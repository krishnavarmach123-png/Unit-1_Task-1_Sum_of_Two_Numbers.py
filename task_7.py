P = float(input("Enter the principle amount:"))
R = float(input("Enter the rate of interest:"))
T = float(input("Enter the time :"))

Amount = P * (1 + R/100) ** T
CI = Amount - P

print(f"TOTAL AMOUNT:{Amount}COMPOUNT INTREST {CI}")