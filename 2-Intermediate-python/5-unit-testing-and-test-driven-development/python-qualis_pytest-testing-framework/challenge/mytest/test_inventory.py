"""
Python FP - pytest hands-on

"""


import sys
import os
sys.path.append(os.getcwd())

from proj.inventory import MobileInventory, InsufficientException
import pytest
# Use assert statement for assert, and to check. Ex: assert 1 == 1

# Define a pytest test class **'TestingInventoryCreation'**
class TestingInventoryCreation:

    # Define a pytest test method **'test_creating_empty_inventory'**, which creates an empty inventory and checks if its 'balance_inventory' is an empty dict using assert.
    def test_creating_empty_inventory(self):
        assert MobileInventory().balance_inventory=={}

    # Define a pytest test method **'test_creating_specified_inventory'**, which checks if inventory instance with input {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25}.
    def test_creating_specified_inventory(self):
        my_dict={"iPhone Model X":100,'Xiaomi Model Y':1000,'Nokia Model Z':25}
        assert MobileInventory({"iPhone Model X":100,'Xiaomi Model Y':1000,'Nokia Model Z':25}).balance_inventory== my_dict

    # Define a pytest test method  **'test_creating_inventory_with_list'**, which checks if the  method raises a TypeError with the message "Input inventory must be a dictionary" when a list "['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z']" is passed as input using assert.
    def test_creating_inventory_with_list(self):
        with pytest.raises(TypeError) :
            assert "Input inventory must be a dictionary" == MobileInventory(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])

    # Define a pytest test method **'test_creating_inventory_with_numeric_keys'**, which checks if the  method raises a ValueError with the message "Mobile model name must be a string" using assert, when the dict {1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'} is passed as input.
    def test_creating_inventory_with_numeric_keys(self):
        message="Mobile model name must be a string"
        with pytest.raises(ValueError):
            assert  MobileInventory( {1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'})==message

    # Define a pytest test method **'test_creating_inventory_with_nonnumeric_values'**, which checks if the  method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert, when the dict {'iPhone Model X':'100', 'Xiaomi Model Y': '1000', 'Nokia Model Z':'25'} is passed as input.
    def test_creating_inventory_with_nonnumeric_values(self):
        with pytest.raises(ValueError):
            message="No. of mobiles must be a positive integer"            
            assert message == MobileInventory({ 'iPhone Model X':'100', 'Xiaomi Model Y': '1000','Nokia Model Z':'25'})

    # Define a pytest test method **'test_creating_inventory_with_negative_value'**, which checks if the  method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert, when the dict {'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25} is passed as input.
    def test_creating_inventory_with_negative_value(self):
        with pytest.raises(ValueError):
            message="No. of mobiles must be a positive integer"
            assert message==MobileInventory({'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25})

# Define another pytest test class **'TestInventoryAddStock'**, which tests the behavior of the **'add_stock'** method, with the following tests
class TestInventoryAddStock:

    # Define a pytest class fixture 'setup_class', which creates an **'MobileInventory'** instance with input {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25} and assign it to class attribute **'inventory'**.
    @classmethod
    def setup_class(cls):
        cls.inventory=MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25} )

    # Define a pytest test method **'test_add_new_stock_as_dict'**, which adds the new stock {'iPhone Model X':50, 'Xiaomi Model Y': 2000, 'Nokia Model A':10} to the existing inventory, and update the **balance_inventory** attribute. Also, check if the updated **balance_inventory** equals {'iPhone Model X':150, 'Xiaomi Model Y': 3000, 'Nokia Model Z':25, 'Nokia Model A':10} using assert.
    def test_add_new_stock_as_dict(self):
        self.inventory.add_stock({'iPhone Model X':50, 'Xiaomi Model Y': 2000, 'Nokia Model A':10})

        assert self.inventory.balance_inventory=={'iPhone Model X':150, 'Xiaomi Model Y': 3000, 'Nokia Model Z':25, 'Nokia Model A':10}

    # Define a pytest test method **'test_add_new_stock_as_list'**, which adds the new stock ['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'] to the existing inventory, and which checks if the method raises a TypeError with the message "Input stock must be a dictionary" using assert.
    def test_add_new_stock_as_list(self):
        my_dict_as_list =  ['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z']
        message="Input stock must be a dictionary" 
        with pytest.raises(TypeError):
            assert message == self.inventory.add_stock(my_dict_as_list)

    # Define a pytest test method **'test_add_new_stock_with_numeric_keys'**, which adds the new stock {1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'} to the existing inventory, and which checks if the method raises a ValueError with the message "Mobile model name must be a string" using assert.
    def test_add_new_stock_with_numeric_keys(self):
        my_dict_as_list = {1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'} 
        message= "Mobile model name must be a string"  
        with pytest.raises(ValueError):
            assert message ==self.inventory.add_stock(my_dict_as_list)


    # Define a pytest test method **'test_add_new_stock_with_nonnumeric_values'**, which adds the new stock {'iPhone Model A':'50', 'Xiaomi Model B':'2000', 'Nokia Model C':'25'} to the existing inventory, and which checks if the method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert.
    def test_add_new_stock_with_nonnumeric_values(self):
        message= "No. of mobiles must be a positive integer"
        my_dict_as_string= {'iPhone Model A':'50', 'Xiaomi Model B':'2000', 'Nokia Model C':'25'}
        with pytest.raises(ValueError):
            assert message==MobileInventory.add_stock(self,my_dict_as_string)

    # Define a pytest test method **'test_add_new_stock_with_float_values'**, which adds the new stock {'iPhone Model A':50.5, 'Xiaomi Model B':2000.3, 'Nokia Model C':25} to the existing inventory, and which checks if the method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert.
    def test_add_new_stock_with_float_values(self):
        message= "No. of mobiles must be a positive integer"
        my_dict_as_float = {'iPhone Model A':50.5, 'Xiaomi Model B':2000.3, 'Nokia Model C':25} 
        with pytest.raises(ValueError):
            assert message==MobileInventory.add_stock(self,my_dict_as_float)

# Define another pytest test class **'TestInventorySellStock'**, which tests the behavior of the **'sell_stock'** method, with the following tests
class TestInventorySellStock:
    stock_as_list_message="Requested stock must be a dictionary" 
    stock_as_numeric_key_message="Mobile model name must be a string" 
    stock_as_float_values_message= "No. of mobiles must be a positive integer" 
    stock_as_non_numeric_message= "No. of mobiles must be a positive integer" 
    # Define a pytest class fixture 'setup_class', which creates an **'MobileInventory'** instance with the input {'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1}, and assign it to the class attribute **'inventory'**.
    @classmethod
    def setup_class(cls):
        my_dict= {'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1}
        cls.inventory=MobileInventory(my_dict)

    # Define a pytest test method **'test_sell_stock_as_dict'**, which sells the requested stock {'iPhone Model A':2, 'Xiaomi Model B':20, 'Sony Model D':1} from the existing inventory, and update the **balance_inventory** attribute. Also check if the updated **balance_inventory** equals {'iPhone Model A':48, 'Xiaomi Model B': 1980, 'Nokia Model C':10, 'Sony Model D':0} using assert.
    def test_sell_stock_as_dict(self):
        my_dict_as_sell_stock= {'iPhone Model A':2, 'Xiaomi Model B':20, 'Sony Model D':1} 
        my_dict_balance= {'iPhone Model A':48, 'Xiaomi Model B': 1980, 'Nokia Model C':10, 'Sony Model D':0}
        self.inventory.sell_stock(my_dict_as_sell_stock)
        assert my_dict_balance ==  self.inventory.balance_inventory

    # Define a pytest test method **'test_sell_stock_as_list'**, which tries selling the requested stock ['iPhone Model A', 'Xiaomi Model B', 'Nokia Model C'] from the existing inventory, and which checks if the method raises a TypeError with the message "Requested stock must be a dictionary" using assert.
    def test_sell_stock_as_list(self):
        my_dict_as_list= ['iPhone Model A', 'Xiaomi Model B', 'Nokia Model C']
        with pytest.raises(TypeError):
            assert TestInventorySellStock.stock_as_list_message== MobileInventory.sell_stock(self,my_dict_as_list)

    # Define a pytest test method **'test_sell_stock_with_numeric_keys'**, which tries selling the requested stock {1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'} from the existing inventory, and which checks if the method raises ValueError with the message "Mobile model name must be a string" using assert.
    def test_sell_stock_with_numeric_keys(self):
        my_dict_as_int = {1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'}
        with pytest.raises(ValueError):
            assert TestInventorySellStock.stock_as_numeric_key_message == self.inventory.sell_stock(my_dict_as_int)

    # Define a pytest test method **'test_sell_stock_with_nonnumeric_values'**, which tries selling the requested stock {'iPhone Model A':'2', 'Xiaomi Model B':'3', 'Nokia Model C':'4'} from the existing inventory, and which checks if the method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert.
    def test_sell_stock_with_nonnumeric_values(self):
        my_dict_as_str =  {'iPhone Model A':'2', 'Xiaomi Model B':'3', 'Nokia Model C':'4'}
        with pytest.raises(ValueError):
            assert TestInventorySellStock.stock_as_non_numeric_message == self.inventory.sell_stock(my_dict_as_str)

    # Define a pytest test method **'test_sell_stock_with_float_values'**, which tries selling the requested stock {'iPhone Model A':2.5, 'Xiaomi Model B':3.1, 'Nokia Model C':4} from the existing inventory, and which checks if the method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert.
    def test_sell_stock_with_float_values(self):
        my_dict_as_float={'iPhone Model A':2.5, 'Xiaomi Model B':3.1, 'Nokia Model C':4}
        with pytest.raises(ValueError):
            assert TestInventorySellStock.stock_as_float_values_message == self.inventory.sell_stock(my_dict_as_float)

    # Define a pytest test method **'test_sell_stock_of_Nonexisting_model'**, which tries selling the requested stock {'iPhone Model B':2, 'Xiaomi Model B':5} from the existing inventory, and which checks if the method raises an InsufficientException with the message "No Stock. New Model Request" using assert.
    def test_sell_stock_of_Nonexisting_model(self):
        my_dict_Nonexisting = {'iPhone Model B':2, 'Xiaomi Model B':5} 
        message= "No Stock. New Model Request" 
        with pytest.raises(InsufficientException):
            assert message == self.inventory.sell_stock(my_dict_Nonexisting)

    # Define a pytest test method **'test_sell_stock_of_insufficient_stock'**, which tries selling the requested stock {'iPhone Model A':2, 'Xiaomi Model B':5, 'Nokia Model C': 15} from the existing inventory, and which checks if the method raises an InsufficientException with the message "Insufficient Stock" using assert.
    def test_sell_stock_of_insufficient_stock(self):
        my_dict_insufficient={'iPhone Model A':2, 'Xiaomi Model B':5, 'Nokia Model C': 15}
        message= "Insufficient Stock"
        with pytest.raises(InsufficientException):
            assert message == MobileInventory.sell_stock(self.inventory, my_dict_insufficient)
