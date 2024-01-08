# Unit Testing
Unit testing is used to validate if units of code are operating as designed. 
Unit testing is performed first in your local machine, then in a server, then you test in production. 

# Static code analysis
Analysing code without running it

# Modules, Packages and Libraries 
- Module: Python file with functions

-  Package: A collection of modules with a __init__.py file.
    - Python modules into a dictionary

- Library: Collection of packages or a single package
    - Numpy, Pandas, Pytorch


# PEP8
- 4 spaces is better than using tab

- Use spaces to separate functions:
  
     ``` 
     def function_1 (a, b):
         c = a + b
         return c 

    def function_2 (a, b):
        c = a * b 
        return c
     ```
- Use spaces around operators and commas

    ```
    # Correct:
    a = b + c

    # Incorrect:
    a=b+c
    ```
- Create functions for blocks of code -> if you notice yourself using a piece of code often, build a function for that. Create your own tool box.

- Name functions with lowercase and underscore:
    ```
    # Correct
    calculate_function ():
        return

    # Incorrect
    CalculateFunction ():
    ```
  Note: Some built in Python functions use upercase, so it might be confusing for the computer or yourself.

- Package naming convention:
  
```
# Correct:
mypackage

# Incorrect:
my_package

```
- Further indentation required as indentation is not distinguishable.

```
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

- Name classes with camel case:

```
# Correct:
LamSquirrelCage:

# Incorrect:
Lam_Squirrel_Cage
```

