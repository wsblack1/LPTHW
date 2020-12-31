from sys import argv
# read the WYSS section for how to run this (must do something like: "py ex13.py var1 var2 var3")
script, first, second, third = argv  # this unpacks argv into 4 arguments that can be used later

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)