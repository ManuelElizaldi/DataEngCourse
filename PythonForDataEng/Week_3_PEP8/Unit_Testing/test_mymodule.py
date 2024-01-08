
import unittest

from mymodule import square, double, add

print(add(2,4))
print(add('hello', 'world'))

class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEquals(square(2), 2) # type: ignore # test when 2 is given, 4 is the output
        self.assertEquals(square(3.0), 9.0) # test when 3 is given, 9 is the output # type: ignore
        self.assertNotEquals(square(-3), -9) # type: ignore

class TestDouble(unittest.TestCase): 
    def test2(self):
        self.assertEquals(double(2), 4) # test when 2 is given 4 is the output # type: ignore
        self.assertEquals(double(-3.1), -6.2) # test when -3.1 is given, the output should be -6.2 # type: ignore
        self.assertEquals(double(0), 0) # test when - is given, the output should be  # type: ignore

class TestAdd(unittest.TestCase):        
    def test3(self):
        self.assertEquals(add(2, 4), 6) # type: ignore
        self.assertNotEquals(add('hello', 'world'), 'hello world') # type: ignore
        self.assertNotEquals(add(-2, -2), 0) # type: ignore

unittest.main()

"""
When 2 and 4 are given as input the output must be 6.

When 0 and 0 are given as input the output must be 0.

When 2.3 and 3.6 are given as input the output must be 5.9.

When the strings ‘hello’ and ‘world’ are given as input the output must be ‘helloworld’.

When 2.3000 and 4.300 are given as input the output must be 6.6.

When -2 and -2 are given as input the output must not be 0. (Hint : Use assertNotEqual)
"""