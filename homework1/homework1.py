# File: homework1.py

# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals
b = 1.5
print (b)
print(type(b)) # b is a float, a number with decimals
c = 3j
print (c)
print(type(c)) # c is complex, which contains both a real and imaginary part 
d = "hello"
print(d)
print(type(d)) # d is a string, a sequence of characters 
e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, an ordered collection of items
f = {"name":  "Ellen", "favorite fruit":  "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a data type used to store data values in key value pairs
g = (1, 2)
print(g)
print(type(g)) # g is a tuple, an ordered, immutable collection of items
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, an ordered collection of items
i = True
print(i)
print(type(i)) # i is a bool, a dara type that has one of two possible values, true or false
j = None
print(j)
print(type(j)) # j a is a NoneType, a data type that represents the absence of a value 
k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, an ordered collection of items
l = str(14)
print(l)
print(type(l)) # l is a string, a sequence of characters 
m = 1e4
print(m)
print(type(m)) # m is a float, a real number that can have fractional components
# 1) I found 8 differnt data types 
# 2) int, float, complex, str, list, dict, tuple, bool, NoneType
# 3) a and m are both numbers 
# e, h, and k are all lists 
# d and l are both strings 
# b and m are both floats 
# 4) the data type of l was a str. It is not an integer because str(14) converts the number 14 into a string using the str() function. str() converts a value into a string data type.
# 5) 
n = {1, 2, 3}
print(n)
print(type(n)) # n is a set, an unordered collection of unique items.

#--- Booleans ---

print(10 > 9) # True, 10 is greater than 9
print (10 == 9) # False, 10 is not equal to 9 
print (10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, non-empty strings are considered true
print(bool(123)) # True, any non-zero number is True 
print(bool(["apple", "cherry", "banana"])) # True, non empty list is true
print(bool(True)) # True, because True 
print(bool(False)) # False, because False 
print(bool(0)) # False, 0 is considered false in this context
print(bool("")) # False, empty string is False 
print(bool(" ")) # True, a string with space is still non-empty, so it's True
print(bool(())) # False, empty, tuple is False 
print(bool([])) # False, empty list is False
print(bool({})) # False, empty dictionary is False
print(bool(True and False)) # False --> 'and' needs both to be True, but one is False
print(bool(True and True)) # True --> both values are True 
print(bool(False and False)) # False, --> both values are False 
print(bool(True or False)) # True --> or needs at least one to be True
print(bool(True or True)) # True --> at least one is True 
print(bool(False or False)) # False, neither value is True 
print(bool(not(False))) # True --> not False is True 
print(bool(not(True))) # False --> not True is False
# 1) Expressions with 'and' require both sides to be True to return True. Expressions with 'or' return True if at least one side is True. 'not' flips the value.
# 2) I was surprised by print(bool(" ")) being True because of the empty space.
# 3) print(bool(5 > 3 and 2 !=4)) True because both statements are True 
# 4) print(bool(10 < 2 or 5 == 6)) False because 2 is not greater than 10 and 5 does not equal 6.

# --- Operators ---

print(10 + 5) # 15, + performs addition 
print(10 - 5) # 5, - performs subtraction 
print(2 * 4) # 8, * performs multiplication 
print(6 / 3) # 2.0, / performs division and returns a float 
print(5 % 2) # 1, % gives the remained of division 
print(3 ** 2) # 9, ** performs exponentiation
print(15 // 2) # 7, // performs floor division, returns the whole number part only

print(5 == 2) # False, == checks if values are equal 
print(10 != 10) # False, != checks if values are not equal 
print(2 < 5) # True, < checks if the left value is less than the right
print(12 > 5) # True, > checks if the left value is greater than the right 
print(5 <= 6) # True, <= checks if the left value is less than or equal to right 
print(1 >= 10) # False, >= checks if left is greater than or equal to right

x = 5 # Initial value of x is 5 
x += 5
print(x) # 10, x = x + 5
x -= 4 
print(x) # 6, x = x -4 
x *= 3 
print(x) # 18, x = x* 3

# 1) 'and' returns True only if both sides are True 
print(True and True) # True --> both are True 
print(True and False) # False --> one side is False 

# 2) 'or' returns True if at least one side is True 
print(True or False) # True --> one side is True 
print(False or False) # False --> both sides are False 

# 3) 'not' reverses the boolean value 
print(not False) # True --> not makes False into True 
print(not True) # False --> not makes True into False

# 1) / returns a float while // returns an integer 
# 2) % gives the remainder of the division while // gives the quotient 
# 3) I would use % 
print(17 % 4) # 1 --> 17 divided by 4 is 4 with remainder 1 
# 4) Assignment operators change the value of a variable based on an operation, they combine an operation with assigment to write code more cleanly.

# --- Strings ---

my_string = "hello"
# 1. Print the string 
print(my_string) # prints: hello
# 2. Print the first character 
print(my_string[0]) # h --> indexing starts at 0
# 3. Print the second character 
print(my_string[1]) # e
# 4. Print the third character 
print(my_string[2]) # l
# 5. Print the foruth character 
print(my_string[3]) # l
# 6. Print the fifth character
print(my_string[4]) # o
# 7. Print the last character using negative indexing 
print(my_string[-1]) # 0 --> 1 refers to the last character 
# 8. Slice from index 1 to 3 (not including 3)
print(my_string[1:3]) # el --> includes index 1 and 2
# 9. Slice from index 0 to 5 with a step of 2 
print(my_string[0:5:2]) # hlo --> indexes 0, 2, 4
# 10. Print the length of the string 
print(len(my_string)) # 5 --> "hello" has 5 characters 
# 11. Add another string (concatenation)
print(my_string + "goodbye") # hellogoodbye --> strings are joined 
# 12. Multiply string 7 times 
print(my_string * 7) # hellohellohellohellohellohellohello

# 1. Slicing is extracting a portion of a string using string[start:stop:step], the string was sliced in my_string[1:3] which sliced from index 1 to 2 and my_string[0:5:2] which sliced from index 0 to 4 with steps of 2
# 2. The output is "Hello, my name is Oski". This uses comma-separated printing, which inserts a space between strings and variables
# 3. The output is "Hello, my name is Oski". This uses an f string which is a formatted string literal. Variables inside the parenthesis are evaluated and inserted directly.
# 4. The difference between the last two print statements is that one uses a regular print with a comma and the other uses f string which is more flexible.

# --- Terminal Commands ---

# cd: changes the current directory 
# Usage: cd[directory-name]
# Example: cd python_decal_fa25

# ls: lists the files and directories in the current directory 
# Usage: ls 
# Example: ls 

# ls -a: Lists all files, including hidden files 
# Usage: ls -a
# Example: ls -a

# mkdir: Creates a new directory 
# Usage: mkdir [directory-name]
# Example: mkdir new_folder 

# cat: Displays the contents of a file
# Usage: cat [filename]
# Example: cat notes.txt

# pwd: Prints the current working directory 
# Usage: pwd 
# Example: pwd 

# cd .. : moves up one directory 
# Usage: cd .. 
# Example: If I was in lecture_notes, cd .. would take me to python_decal_fa25

# cd . : refers to the current directory, has no effect.
# Usage: cd .
# Example: cd .

# cd ~ : Moves to the home directory 
# Usage: cd ~
# Example: cd ~

# cp: copies files or directories 
# Usage: cp [source] [destination]
# Example: cp file1.txt backup.txt

# mv: moves or renames files and directories 
# Usage: mv [source] [destination]
# Example: mv oldname.txt newname.txt (renames file)
# Example: mv file.txt folder/ (moves file to folder)

# rm: deletes (removes) files or directories 
# Usage: rm [file]
# Exmaple: rm file.txt

# clear: clears the terminal screen 
# Usage: clear 
# Example: clear 

# grep: Searches for a pattern in a file or output 
# Usage: grep [pattern] [filename]
# Example: grep "error" log.txt 
# Example: ls | grep "txt"

# 1) a. touch: creates a new, empty file 
# Usage: touch [filename]
# Example: touch notes.txt

# b. man: Displays the manual page for a command (help)
# Usage: man [command]
# Example: man ls 

# c. history: shows the list of previously used commans 
# Usage: history 
# Example: history 

# 2) ls shows only visible files and folders while ls -a shows all files, including hidden files

# 3) A hidden file is a fule whose name starts with a dot and it does not appear in normal directory listings but will appear if you use ls -a

# 4) a. ls -l: lists files in long format 
# Example: ls -l

# b. rm -r: removes directories and their contents recursively 
# Example: rm -r my_folder

# c.  cp -r: copies directories recursively (including their contents) 
# Example: cp -r folder1 folder2


