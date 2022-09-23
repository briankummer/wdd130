#import the math module
import math

#input from user

items = int(input(f"Enter the number of items: "))
boxs = int(input(f"Enter the number of items per box: "))

num_boxs = math.ceil(items / boxs)

print(f'For {items} items, packing {boxs} itens per box, you will need {num_boxs} boxes')