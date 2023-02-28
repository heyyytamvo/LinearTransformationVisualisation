import matplotlib.pyplot as plt
def Drawing(grid, numberOfPointsOnEachAxis):
    #drawing horizontal line
    for i in range(0, numberOfPointsOnEachAxis):
        x = [grid[0, i], grid[0, len(grid[0]) - numberOfPointsOnEachAxis + i]]
        y = [grid[1, i], grid[1, len(grid[1]) - numberOfPointsOnEachAxis + i]]
        plt.plot(x, y, color="black")

    #drawing vertical line
    for i in range(0, len(grid[0]), numberOfPointsOnEachAxis):
        x = [grid[0, i], grid[0, i + numberOfPointsOnEachAxis - 1]]
        y = [grid[1, i], grid[1, i + numberOfPointsOnEachAxis - 1]]
        plt.plot(x, y, color="black")
    
    #drawing the x-Axis
    x = [int(grid[0, 0]), int(grid[0, len(grid[0]) - 1])]
    y = [0, 0]
    plt.plot(x, y, color="red")
    #drawing the y-Axis
    x = [0, 0]
    y = [int(grid[1, 0]), int(grid[1, len(grid[1]) - 1])]
    plt.plot(x, y, color="red")
