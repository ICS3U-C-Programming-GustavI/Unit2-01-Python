#!/usr/bin/env python3
# Created By: Gustav I
# Date: Feb 15, 2025
# This program calculates the area & perimeter of a  rectangle based on user input

#Defining the function in this section
def calculate_area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

#User input section
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

#Telling the computer to follow and call the function
area, perimeter = calculate_area_and_perimeter(length, width)

#Printing the results based on user input
print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")
