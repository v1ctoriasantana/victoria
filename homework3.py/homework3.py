# 3.1
def say_goodbye(name):
    print("Goodbye,", name)
# 3.2 
def area_of_circle(radius):
    area = 3.14 * (radius ** 2)
    print(f"The area of the circle with radius {radius} is {area}")
#4.1 
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
#5.1
def min_max_temp(temperatures):
    return (min(temperatures), max(temperatures))
#5.2 
def is_weekend_num(day):
    return day == 6 or day == 7
#5.3
def fuel_efficiency(distance, fuel_used):
    if fuel_used != 0:
        return distance / fuel_used
    else:
        return "Fuel used cannot be zero"
#5.4
def encrypt_number(n):
    last_digit = n % 10
    rest = n // 10
    num_digits = len(str(rest))
    return last_digit * (10 ** num_digits) + rest
#6.1 
def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result
#6.2.1
def find_min_for(nums):
    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val

def find_max_for(nums):
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val
#6.2.2
def find_min_while(nums):
    i = 0
    min_val = nums[0]
    while i < len(nums):
        if nums[i] < min_val:
            min_val = nums[i]
        i += 1
    return min_val
def find_max_while(nums):
    i = 0
    max_val = nums[0]
    while i < len(nums):
        if nums[i] > max_val:
            max_val = nums[i]
        i += 1
    return max_val
#6.3 
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
#7.1
if __name__ == "__main__":
    x = 2
    y = 3
    result = power(x, y)
    print(f"The result of Oski Stole Your Power (6.1) with x = {x} and y = {y} is {result}.")