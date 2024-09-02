import inspect
import re
import unittest
import math

# Define class 'Circle' and its methods:
class Circle:
    
    def __init__(self, radius):
        # Define initialization method:
        self.radius = radius
        if (not isinstance(radius, int)) and (not isinstance(radius, float)):
            raise TypeError("radius must be a number")
                
        if self.radius<0 or self.radius>1000:
            raise ValueError("radius must be between 0 and 1000 inclusive")
        
    def area(self):
        # Define area functionality:
        pi=math.pi
        area=pi* self.radius**2
        return round(area, 2)
               
    def circumference(self):
        # Define circumference functionality:
        area=math.pi*(self.radius*2)
        return round(area, 2)
        
class TestCircleCircumference(unittest.TestCase):
    
    def test_circlecircum_with_random_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5, and check if
        # its circumference is 15.71.
        self.assertEqual(Circle(2.5).circumference(), 15.71)
        
    def test_circlecircum_with_min_radius(self):
        # Define a circle 'c2' with radius 0, and check if
        # its circumference is 0.
        self.assertEqual(Circle(0).circumference(), 0)
        
    def test_circlecircum_with_max_radius(self):
        # Define a circle 'c3' with radius 1000, and check if
        # its circumference is 6283.19.
        self.assertEqual(Circle(1000).circumference(), 6283.19)

if __name__ == '__main__':
    
    fptr = open('output.txt', 'w')
    
    runner = unittest.TextTestRunner(fptr)
    
    unittest.main(testRunner=runner, exit=False)
    
    fptr.close()
    
    with open('output.txt') as fp:
        output_lines = fp.readlines()
    
    
    pass_count = [ len(re.findall(r'\.', line)) for line in output_lines if (line.startswith('.') or line.startswith('E') or line.startswith('F')) and line.endswith('\n')]
    
    pass_count = pass_count[0]
                       
    print(str(pass_count))
                       
    doc1 = inspect.getsource(TestCircleCircumference.test_circlecircum_with_random_numeric_radius)
    doc2 = inspect.getsource(TestCircleCircumference.test_circlecircum_with_min_radius)
    doc3 = inspect.getsource(TestCircleCircumference.test_circlecircum_with_max_radius)
    
    assert1_count = len(re.findall(r'assertEqual', doc1))
    
    print(str(assert1_count))
    
    assert1_count = len(re.findall(r'assertEqual', doc2))
    
    print(str(assert1_count))
    
    assert1_count = len(re.findall(r'assertEqual', doc3))
    
    print(str(assert1_count))

    
