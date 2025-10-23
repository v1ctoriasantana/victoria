 # ---- 3.1 ----
# 1. Git vs. GitHub
# Git is a version control system that tracks changes in code.
# GitHub is an online platform that hosts Git repositories and helps with collaboration.

# 2. Terminal vs. Command Line
# The terminal is a program that lets you type and execute text commands.
# The command line is the interface within the terminal where you type commands.

# 3. Local vs. Remote Repository
# A local repository exists on your own computer.
# A remote repository is hosted online (for example, on GitHub).

# 4. Version Control
# A system that tracks changes to code over time and lets you revert or merge updates.

# 5. Staging Area
# The place where Git stores files that are ready to be committed.

# 6. git add
# Adds file changes to the staging area.

# 7. git commit
# Records the changes from the staging area to your local repository.

# 8. git push
# Uploads commits from your local repository to the remote repository.

# 9. git status
# Shows the current status of your repository (which files are modified, staged, or untracked).

# 10. git pull
# Downloads changes from the remote repository and merges them into your local one.

# 11. pwd
# Prints the current working directory path.

# 12. ls
# Lists files and directories in the current location.

# 13. cd
# Changes the current working directory.

# 14. nano
# Opens a simple text editor in the terminal.

# 15. touch
# Creates a new, empty file.

# 16. mv
# Moves or renames files or directories.

# 17. rm
# Removes (deletes) files.

# 18. cat
# Displays the contents of a file in the terminal.

# ---- 3.2 ----
# • You have been plopped into Judy’s directory system. 
#   What command will tell you what your current working directory is?
# pwd

# • The terminal responds by saying you are in ~/python_decal/judy_decal.
#   What command will list all the files in your current working directory?
# ls

# • Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py.
#   You will need to pull the brianna_repo repository to find the updated file.
#   What command(s) will let you move to the correct repository and pull the latest changes?
# cd ../brianna_repo
# git pull

# • How would you move this new homework.py to the homework/ folder in your personal repository?
# mv homework.py ../judy_decal/homework/

# • How would you move yourself to the same repository as homework.py?
# cd ../judy_decal/homework

# • You want to see the contents of homework.py in your terminal, how would you do this?
# cat homework.py

# • Great job! You just finished the homework for this week.
#   What command(s) allow you to save the changes and push from your local repository to your remote repository?
# git add .
# git commit -m "finished homework 5"
# git push origin main

# • Oh no! Git gave you the following error
#   What commands should you call to resolve this error and push your homework properly?
#   What does the error mean? (i.e. what did “Judy” do wrong when trying to push?)
# git pull origin main
# git push origin main
#
# The error means that the remote repository has commits that are not on Judy’s local repository.
# Judy tried to push without first pulling the latest version from GitHub, so Git rejected the push
# to prevent overwriting newer changes.

# • What absolute path will allow you to move to Recents/?
# cd ~/Recent

# --- 4.1 ----
def checkDataType(x):
    """Return the data type of the input as a string."""
    return type(x).__name__

# ---- 4.2 -----
def evenOrOdd(num):
    """Return 'Even' if the number is even, otherwise 'Odd'."""
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

# ----- 5 -----
def sumWithLoop(numbers):
    """Return the sum of a list of integers using a loop."""
    total = 0
    for n in numbers:
        total += n
    return total

# --- 6.1 ----
def duplicateList(lst):
    """Return a new list where each element is duplicated."""
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list

# --- 6.2 ----
def square(num):
    """Return the square of a number."""
    return num * num 

# --- 7.2 ---- 
if __name__ == "__main__":
    print("Testing Homework 5 Functions:\n")
    
    print("checkDataType(3.14) →", checkDataType(3.14))     
    print("checkDataType(True) →", checkDataType(True))      
    print("evenOrOdd(7) →", evenOrOdd(7))                  
    print("evenOrOdd(10) →", evenOrOdd(10))                 
    print("sumWithLoop([1, 2, 3, 4, 5]) →", sumWithLoop([1, 2, 3, 4, 5]))  
    print("duplicateList(['a', 'b', 'c']) →", duplicateList(['a', 'b', 'c']))  
    print("square(5) →", square(5))                        

    print("\nAll functions tested successfully!") 