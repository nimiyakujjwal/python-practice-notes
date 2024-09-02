from proj.circle import Circle
from nose.tools import assert_raises, eq_, eq_
# Define a nose test class 'TestingCircleCreation'
class TestingCircleCreation:
    # Define a nose test method 'test_creating_circle_with_numeric_radius', which creates a circle with radius 2.5, and check if its radius value is 2.5 using eq_ method.
    def test_creating_circle_with_numeric_radius(self):
        eq_(Circle(2.5).radius,2.5)


    # Define a nose test method 'test_creating_circle_with_negative_radius', which checks if the ValueError exception is raised with the error message "radius must be between 0 and 1000 inclusive" using eq_ method, while creating a circle of radius -2.5.
    # Hint: Use assert_raises and with.
    def test_creating_circle_with_negative_radius(self):
        with assert_raises(ValueError) as e:          
            Circle(-2.5)
        message="radius must be between 0 and 1000 inclusive"      
        eq_( str(e.exception),message)


    # Define a nose test method 'test_creating_circle_with_greaterthan_radius', which checks if the ValueError exception is raised with the error message "radius must be between 0 and 1000 inclusive" using eq_ method, while creating circle of radius 1000.1 .
    # Hint: Use assert_raises and with
    def test_creating_circle_with_greaterthan_radius(self):
        with assert_raises(ValueError) as e:
            Circle(1000.1)
        message="radius must be between 0 and 1000 inclusive"
        eq_(str(e.exception) , message)

    # Define a nose test method 'test_creating_circle_with_nonnumeric_radius', which checks if the TypeError exception is raised with the error message "radius must be a number" using eq_ method, while creating circle of radius 'hello' .
    # Hint: Use assert_raises and with.
    def test_creating_circle_with_nonnumeric_radius(self):
        with assert_raises(TypeError) as e:
            c=Circle("hello")
        message= "radius must be a number"
        eq_(str(e.exception) , message)



#Define a nose test class 'TestCircleArea'
class TestCircleArea:
    # Define a nose test method 'test_circlearea_with_random_numeric_radius', which creates a circle 'c1' with radius 2.5, and check if its computed area is 19.63 using eq_ method.
    def test_circlearea_with_random_numeric_radius(self):
        eq_(Circle(2.5).area(),19.63)

    # Define a nose test method 'test_circlearea_with_min_radius', which creates a circle 'c2' with radius 0, and check if its computed area is 0 using eq_ method.
    def test_circlearea_with_min_radius(self):
        eq_(Circle(0).area(),0)

    # Define a nose test method 'test_circlearea_with_max_radius', which creates a circle 'c3' with radius 1000, and check if its computed area is 3141592.65 using eq_ method.
    def test_circlearea_with_max_radius(self):
        eq_(Circle(1000).area(),3141592.65)

# Define a nose test class 'TestCircleCircumference'
class TestCircleCircumference:
    # Define a nose test method 'test_circlecircum_with_random_numeric_radius', which creates a circle 'c1' with radius 2.5, and check if its computed circumference is 15.71 using eq_ method.
    def test_circlecircum_with_random_numeric_radius(self):
        eq_(Circle(2.5).circumference(),15.71)

    # Define a nose test method 'test_circlecircum_with_min_radius', which creates a circle 'c2' with radius 0, and check if its computed circumference is 0 using eq_ method.
    def test_circlecircum_with_min_radius(self):
        eq_(Circle(0).circumference(),0)

    # Define a nose test method 'test_circlecircum_with_max_radius', which creates a circle 'c3' with radius 1000, and check if its computed circumference is 6283.19 using eq_ method.
    def test_circlecircum_with_max_radius(self):
        eq_(Circle(1000).circumference(),6283.19)