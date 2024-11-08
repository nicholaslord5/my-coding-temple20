# 1. Encapsulation in Personal Budget Management
# Objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, 
# focusing on the use of private attributes and getters and setters.

# Problem Statement: You are required to build a Personal Budget Management application. 
# The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

# Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for 
# category name and allocated budget. - Initialize these attributes in the constructor.

# - Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

# Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. 
# - Ensure that the setter methods include validation (e.g., budget should be a positive number).

# - Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

# Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust 
# the budget accordingly. - Validate the expense amount before making deductions from the budget.

# Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

# Task 4: Display Budget Details Create a method to display the details of a budget category, 
# including the name, allocated budget, and remaining budget after expenses.

# Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.

# Code Examples:

# class BudgetCategory:
    # Constructor and private attributes
    # ...

    # Getters and setters for category name and budget
    # ...

#    def add_expense(self, amount):
        # Method to add an expense to the category
        # ...

#    def display_category_summary(self):
        # Method to display the budget category details
        # ...

# food_category = BudgetCategory("Food", 500)
# food_category.add_expense(100)
# food_category.display_category_summary()

##########################

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, name):
        if isinstance(name, str) and name.strip():
            self.__category_name = name
        else:
            print("Invalid category name. Please enter a valid string.")

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, budget):
        if isinstance(budget, (int, float)) and budget > 0:
            self.__allocated_budget = budget
            self.__remaining_budget = budget
        else:
            print("Invalid budget amount. Budget should be a positive number.")

    def add_expense(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
                print(f"Expense of {amount} added to {self.__category_name}.")
            else:
                print("Expense exceeds the remaining budget.")
        else:
            print("Invalid expense amount. Please enter a positive number.")

    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: {self.__allocated_budget}")
        print(f"Remaining Budget: {self.__remaining_budget}")

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()