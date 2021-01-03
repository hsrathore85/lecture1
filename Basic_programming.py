# Let's create a very simple program called Hello World.
# A "Hello, World!" is a simple program that outputs Hello, World! on the screen.
# Since it's a very simple program, it's often used to introduce a new programming language to beginners.

print("Hello World")

# Congratulations! You just wrote your first program in Python.
# As you can see, this was a pretty easy task. This is the beauty of Python programming language.

# Python Keywords: We cannot use a keyword as a variable name, function name or any other identifier.
# They are used to define the syntax and structure of the Python language.
# In Python, keywords are case sensitive.

# All the keywords except True, False and None are in lowercase and they must be written as they are.

# The list of all the keywords is given below:-

# False, await, else, import, pass, none, break, except, in, raise
# True, class, finally, is , return, and, continue, for, lambda, try
# as, def, from, nonlocal, while, assert, del, global, not, with
# async, elif, if, or, yield.

# Python Identifiers
#
# An identifier is a name given to entities like class, functions, variables, etc.
# It helps to differentiate one entity from another.

# Rules for writing identifiers

# Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9)
# or an underscore _.
# Names like myClass, var_1 and print_this_to_screen, all are valid example.
# An identifier cannot start with a digit. 1variable is invalid, but variable1 is a valid name.
# Keywords cannot be used as identifiers.
# For an example:-

# global = 1

#  File "/Users/harwindersinghrathore/PycharmProjects/pythonProject1/Basic_programming.py", line 34
#     global = 1
#            ^
# SyntaxError: invalid syntax

# Things to Remember
#
# Python is a case-sensitive language.
# This means, Variable and variable are not the same.

# Python Statement, Indentation and Comments:-

# Python Statement
#
# Instructions that a Python interpreter can execute are called statements.
# For example, a = 1 is an assignment statement. if statement, for statement, while statement, etc.
# are other kinds of statements which will be discussed later.

# Multi-line statement

# In Python, the end of a statement is marked by a newline character.
# But we can make a statement extend over multiple lines with the line continuation character (\).
# For example:

A = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

print("Sum =", A)

# This is an explicit line continuation.
# In Python, line continuation is implied inside parentheses ( ), brackets [ ], and braces { }.
# For instance, we can implement the above multi-line statement as:

B = (1 + 2 + 3 +
     4 + 5 + 6 +
     7 + 8 + 9)

print("Sum =", B)

# Here, the surrounding parentheses ( ) do the line continuation implicitly.
# Same is the case with [ ] and { }.
# For example:

colors = ['red',
          'blue',
          'green']

print(colors)

# We can also put multiple statements in a single line using semicolons, as follows:

a = 1; b = 2; c = 5

Sum = a + b + c

print(Sum)

# Python Indentation:-

# Most of the programming languages like C, C++, and Java use braces { } to define a block of code.
# Python, however, uses indentation:-

# Generally, four whitespaces are used for indentation and are preferred over tabs.
# Here is an example:-

for i in range(1, 11):
    print(i)
    if i == 10:
        break

# The enforcement of indentation in Python makes the code look neat and clean.
# This results in Python programs that look similar and consistent.
#
# Indentation can be ignored in line continuation, but it's always a good idea to indent.
# It makes the code more readable.
# For example:
if True:
    print("HELLO")









