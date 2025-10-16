# -----3.1-----
# List of favorite foods
foods = ["pizza", "sushi", "tacos", "ramen", "ice cream"]

# 1. Print the second food
print(foods[1])

# 2. Print the last food
print(foods[-1])

# 3. Add new food
foods.append("noodles")

# 4. Insert "apple" at the start
foods.insert(0, "apple")

# 5. Remove the third item
del foods[2]

# 6. Print length
print(len(foods))

# 7. Loop and print in uppercase
for food in foods:
    print(food.upper())

# 8. First and last food
first_last = [foods[0], foods[-1]]
print(first_last)

# 9. Check for potato
if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")
# ----- 3.2 ------
# Create list 0 to 20
numbers = list(range(21))

# 1. Get first 15
def get_first_15(numbers):
    return numbers[:15]

# 2. Get every 5th
def get_every_5th(lst):
    return lst[::5]

# 3. Reverse and stride
def reverse_and_stride(lst):
    return lst[::-1][::3]

# Putting it together
step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)
print("Final result from step3:", step3)
# ----- 3.3 -----
# Nested list
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Print third row
print(numbers[2])

# 2. Second item in second row
print(numbers[1][1])

# 3. Append new row
numbers.append([10, 11, 12])

# 4. Sum nested list
def sum_nested(nested_list):
    total = 0
    for row in nested_list:
        total += sum(row)
    return total

print("Sum of nested:", sum_nested(numbers))
#----- 3.4 ------
# 1. Create 5x5 grid
def create_5x5():
    grid = []
    count = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(count)
            count += 1
        grid.append(row)
    return grid

grid = create_5x5()

# 2. Replace multiples of 3 with '?'
def replace_multiples_of_3(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for val in row:
            if val % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(val)
        new_grid.append(new_row)
    return new_grid

grid_with_question = replace_multiples_of_3(grid)

# 3. Sum non-'?' values
def sum_non_question(grid):
    total = 0
    for row in grid:
        for val in row:
            if val != "?":
                total += val
    return total

print("Sum of non-? values:", sum_non_question(grid_with_question))
# ------ 4.1 -------
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

# 1. Print Katie's age
print(ages["Katie"])

# 2. Change Mira’s age
ages["Mira"] = 100

# 3. Add Milana
ages["Milana"] = 52

# 4. Remove Mariam
del ages["Mariam"]

# 5. Print all names and ages
for name, age in ages.items():
    print(f"{name}: {age}")
#----5.2-----
if __name__ == "__main__":
    # Favorite function: sum_non_question
    grid = create_5x5()
    grid_with_question = replace_multiples_of_3(grid)
    total = sum_non_question(grid_with_question)
    print("Final total from favorite function:", total)
