import draw
import numpy as np
import matplotlib.pyplot as plt
import os

def GeneratingAnimation(myGrid ,compostion, maximumValueOnEachAxis):
    if not os.path.exists("outputForLinearTransformation"):
        os.makedirs("outputForLinearTransformation")
    steps = 60
    count = 0
    numberOfPoints = 2 * maximumValueOnEachAxis + 1
    identifyMatrix = np.column_stack([[1, 0], [0, 1]])
    
    while (count <= steps):
        arrayResult = [[], []]
        temp = np.subtract(compostion, identifyMatrix, dtype="f")
        temp *= (count / steps)
        stepWiseMatrix = np.add(identifyMatrix, temp)
        for i in range(0, len(myGrid[0])):
            point = np.array([[myGrid[0, i]], [myGrid[1, i]]])
            stepWiseCoordinate = np.dot(stepWiseMatrix, point)
            arrayResult[0].append(stepWiseCoordinate[0][0])
            arrayResult[1].append(stepWiseCoordinate[1][0])
        

        arrayTemp = np.array(arrayResult)
        plt.figure(figsize=(6, 6), facecolor="w")
        # Set axis limits
        plt.grid(False)
        plt.axis("equal")
        plt.title("Grid in x-y space")
        draw.Drawing(grid=arrayTemp, numberOfPointsOnEachAxis=numberOfPoints)
        # save as png
        outfile = os.path.join("outputForLinearTransformation", "pic-" + str(count) + ".png")
        plt.savefig(outfile)
        
        count += 1
        
'''
identifyMatrix = np.column_stack([[1, 0], [0, 1]])
arr = np.array([[1, 1], [1, 1]])

r = np.add(identifyMatrix, arr)
GeneratingAnimation(r, 1)'''

    

