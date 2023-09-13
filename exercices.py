# function Task 1 
def compute_series_sum(num_terms):
    series_sum = 0
    term = 1
    for _ in range(num_terms):
        series_sum += term
        term = term * 10 + 1
    return series_sum

num_terms = 6  
result = compute_series_sum(num_terms)
print("Sum of the series:", result)

# function Task 2 
def is_even(n):
    return n%2 == 0

number = 7
result = is_even(number)
print('is', number, 'even : ', result)

# function Task 3
def calc_sum_digits(sum_digits):
    somme = 0
    transform = str(sum_digits)
    for digit in transform:
        somme += int(digit)
    return somme

digits = 123434565
result = calc_sum_digits(digits)
print(f"Sum of every number of {digits} : {result} ")

# function Task 4
def extract_integer(floatN):
    return int(floatN)

fNumber = 12.24
result = extract_integer(fNumber)
print(f"The integer part of {fNumber} is : {result}")

# function Task 5
def extract_decimal_from_number(number):
    transform = str(number)
    trouve = False
    final = ''
    for n in transform:
        if n == '.' or trouve:
            trouve = True
            if n != '.':
                final += n
    if final == '':
        return 0
    return int(final)

def extract_decimal_from_number2(number):
    return int(str(number)[str(number).index('.')+1:])


fNumber = 12.24
result = extract_decimal_from_number(fNumber)
result2 = extract_decimal_from_number2(fNumber)
print(f"The decimal part of {fNumber} is : {result}")
print(f"The decimal 2 part of {fNumber} is : {result2}")