import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import generatingAnimation

'''First, we need to know what is the maximum value on each axis'''
MAX_VALUE_ON_EACH_AXIS = int(input("What is the maximum value on each axis: "))

'''Creating every single point'''
xvals = np.linspace(-MAX_VALUE_ON_EACH_AXIS, MAX_VALUE_ON_EACH_AXIS, 2*MAX_VALUE_ON_EACH_AXIS + 1)
yvals = np.linspace(-MAX_VALUE_ON_EACH_AXIS, MAX_VALUE_ON_EACH_AXIS, 2*MAX_VALUE_ON_EACH_AXIS + 1)
xygrid = np.column_stack([[x, y] for x in xvals for y in yvals])

# Apply linear transform
'''
To transform XYGRID, we need a compoisition
The newgrid contains new position of every vector after transforming
'''
print("Now, please input the compostion (input value should be an integer, otherwise, the program will crash)")
x1 = int(input("Value for x1: "))
y1 = int(input("Value for y1: "))
x2 = int(input("Value for x2: "))
y2 = int(input("Value for y2: "))

composition = np.column_stack([[x1, y1], [x2, y2]])
'''Now, the composition is
[[x1 x2],
 [y1  y2]]
 
or the new basis vector is:
iHat = [x1, y1]
jHat = [x2, y2]
'''

'''Calculating the target matrix'''
generatingAnimation.GeneratingAnimation(myGrid=xygrid ,compostion=composition, maximumValueOnEachAxis=MAX_VALUE_ON_EACH_AXIS)

