import math

def calculate_square_footage(length, width):
    
    
    area = length * width
    return area

def calculate_circumference(radius):
    
    circumference = 2 * math.pi * radius
    return circumference

# User input
choice = input("Enter '1' to calculate square footage, '2' to calculate circumference: ")

if choice == '1':
    # Calculate square footage
    length = float(input("Enter the length of the house: "))
    width = float(input("Enter the width of the house: "))
    square_footage = calculate_square_footage(length, width)
    print("The square footage of the house is:", square_footage, "square units")

elif choice == '2':
    # Calculate circumference
    radius = float(input("Enter the radius of the circle: "))
    circle_circumference = calculate_circumference(radius)
    print("The circumference of the circle is:", circle_circumference, "units")

else:
    print("Invalid choice. Please enter '1' or '2'.")
