import math

from exercices import extract_decimal_from_number

# function Task 1
def calculate_pi_decimals(end):
    res = 0
    sign = 1
    for i in range(1, end, 2):
        res += sign * (4 / i)
        sign = -sign
    res = round(res, 6)
    return extract_decimal_from_number(res)

print(f"Decimal of Pi : {calculate_pi_decimals(100000)}")

# function Task 2
def calculate_pi_amazing_formula(start):
    res = 1
    for i in range(start, 0, -1):
        res = 6 + (i*2-1)**2 / res

    res = round(res,6)
    res -= 3
    return extract_decimal_from_number(res)

print(f"Decimal de Pi avec amazing formula : {calculate_pi_amazing_formula(10000000)}")

# function Task 3
def reduce_fraction(numerateur, denominateur):
    
    diviseur_commun = pgcd(numerateur, denominateur)

    reduced_num = numerateur // diviseur_commun
    reduced_den = denominateur // diviseur_commun

    return reduced_num, reduced_den

def pgcd(n, d):
    return math.gcd(n, d)

print(f"Fraction réduite au maximum : {reduce_fraction(42, 14)}")