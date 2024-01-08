
"""
This is a docstring, it provides documentation regarding the file. It goes at the top of the script.
You usually write what the script is about. For example,
this script is intended to teach me how to use Pylint.
"""
# Its best if the lines in the docstring are no longer than 100 characters

def add(number1, number2):
    """
    This function is just a test. It will add 2 numbers.
    """
    # Function docstrings go inside the function
    return number1 + number2

NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)
print("The sum of {} and {} is {}".format(NUM1, NUM2, TOTAL))
