#tire_volume.py

#import math function
import math

#explain the reason for th input of the numbers
print("Use the three numbers on a tire to compute the volume of space inside that tire.")

#Get user input for the volume of the tire
w = float(input("Enter the width of the tire in mm (ex 205):" ))
a = float(input("Enter the aspect ratio of the tire (ex 60):"))
d = float(input("Enter the diameter of the wheel in inches (ex 15):"))

#get the anwser to the top part of the equation first.
top_of_equation = math.pi * (w**2) * a *(w * a + 2540 * d)

#Now sollve the rest of the equation
v = top_of_equation/10000000000

#roud volume to 2 decimal places
v = round(v, 2)

#answer to equation

print("The approximate volume is", v , "litters.")