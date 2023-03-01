# Linear Tranformation Visualisation
## Description
This repository aims to visualise the linear tranformation process for 2D matrix. Considering this scenario, given basis vector in two-dimensional coordinates system, we would like to perform the changing basis with the support of Python 3, in other words, we will visualise the process of transforming matrix A to matrix B, where:

$$
A = \begin{bmatrix}
  1 & 0 \\
  0 & 1
\end{bmatrix}
\quad\text{and}\quad
B = \begin{bmatrix}
  1 & 2 \\
  2 & 1
\end{bmatrix}
$$

Our final result will be the animation of our linear transformation as below:

<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzQwNjQxY2EwY2VhNDllOWNkN2JhZWNmYjFhODk2ZTc5MGRhYTcyMyZjdD1n/26KbJvIaedrGg2TPUE/giphy.gif" alt="Linear transformation" width="400" height="400">
</p>

## Installation
Using pakage manager [pip](https://pypi.org/project/pip/) to install these libraries:

``pip install numpy``

``pip install matplotlib``

## Methodology
1. Create an array of every single point in the grid
2. Taking the new basis from user input
3. Generating a series of transformations from the original grid to the transformed grid
4. Making GIF by using external tool

## Background knownledge
### Basis vectors
Given a 2 dimensional coordinates system, to get to a specific point having a coordinate `(3, -2)`, we need to use the basis vectors and perform the formula below:

$$
3\vec{i} - 2\vec{j} = 
\begin{bmatrix}
  3 \\
  -2 
\end{bmatrix}
$$

where $\vec{i}$ and $\vec{j}$ are basis vectors, their values are:

$$
\vec{i} = \begin{bmatrix}
  1 \\
  0 
\end{bmatrix}
\quad\text{and}\quad
\vec{j} = \begin{bmatrix}
  0 \\
  1 
\end{bmatrix}
$$

The picture below shows $\vec{i}$ and $\vec{j}$ and the point `(3, -2)`

<p align="center">
  <img src="https://media5.datahacker.rs/2020/03/Picture2-2-1024x993.jpg" alt="Basis vectors" width="300" height="300" caption=>
</p>

### Other basis vectors
A 2 dimensional coordinates system only has a set of unique basis vectors $\vec{i}$ and $\vec{j}$, but those basis vectors could be any vectors

For example, the grid below is 2D coordinates system where:

$$
\vec{i} = \begin{bmatrix}
  1 \\
  1 
\end{bmatrix}
\quad\text{and}\quad
\vec{j} = \begin{bmatrix}
  0 \\
  1 
\end{bmatrix}
$$

<p align="center">
  <img src="https://www.mathworks.com/matlabcentral/mlc-downloads/downloads/submissions/64955/versions/1/screenshot.png" alt="different basis vectors" width="300" height="300" caption=>
</p>

### Changing basis

Considering the scenario at the beginning, our transformed matrix is: 

$$B = \begin{bmatrix} 
      1 & 2\\ 
      2 & 1  
      \end{bmatrix}$$

where its basis vectors $\vec{i}$ and $\vec{j}$ are:

$$
\vec{i} = \begin{bmatrix}
  1 \\
  2 
\end{bmatrix}
\quad\text{and}\quad
\vec{j} = \begin{bmatrix}
  2 \\
  1 
\end{bmatrix}
$$

And the original matrix is the 2x2 [Identify Matrix](https://byjus.com/maths/identity-matrix/#:~:text=Identity%20Matrix%20Definition,result%20will%20be%20given%20matrix.)

$$
A = \begin{bmatrix}
  1 & 0 \\
  0 & 1
\end{bmatrix}
$$

where its basis vectors $\vec{i}$ and $\vec{j}$ are:

$$
\vec{i} = \begin{bmatrix}
  1 \\
  0 
\end{bmatrix}
\quad\text{and}\quad
\vec{j} = \begin{bmatrix}
  0 \\
  1 
\end{bmatrix}
$$

To get the transformed grid, we perform the dot product:

$$
\begin{bmatrix}
  1 & 2 \\
  2 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
  1 & 0 \\
  0 & 1
\end{bmatrix} = 
\begin{bmatrix}
  1 & 2 \\
  2 & 1
\end{bmatrix}
$$

In general, to get the transformed matrix, perform this formula: 
composition $\cdot$ original = transformed

To have a deep insight about these concepts above, you can take a look at this [video](https://www.youtube.com/watch?v=P2LTAUO1TdA)

### Interpolated matrix

In linear transformations, an interpolation between two matrices A and B can be expressed as a linear combination of the two matrices, where the weighting of each matrix is controlled by a parameter $t$, where $0 \leq t \leq 1$, specifically, the interpolated matrix $X$ is given by:

$$X = (1 - t) \cdot A + t \cdot B$$

The scope of this repository is visualising the linear transformation from [Identify Matrix](https://byjus.com/maths/identity-matrix/#:~:text=Identity%20Matrix%20Definition,result%20will%20be%20given%20matrix.) to the target matrix $A$, therefore, our interpolated matrix $X$ is:

$$X = (1 - t) \cdot I + t \cdot A$$

When $t = 0$, our interpolated matrix is [Identify Matrix](https://byjus.com/maths/identity-matrix/#:~:text=Identity%20Matrix%20Definition,result%20will%20be%20given%20matrix.), if $t = 1$, the interpolated matrix is $A$, which is our transformed matrix. Here, the [Identify Matrix](https://byjus.com/maths/identity-matrix/#:~:text=Identity%20Matrix%20Definition,result%20will%20be%20given%20matrix.) serves as a starting point for the interpolation, and the parameter $t$ controls the "distance" between the [Identify Matrix](https://byjus.com/maths/identity-matrix/#:~:text=Identity%20Matrix%20Definition,result%20will%20be%20given%20matrix.) and the target matrix $A$. But first, we need to find another expression of $X$:

$$X = (1 - t) \cdot I + t \cdot A$$

$$\Leftrightarrow X = 1 \cdot I - t \cdot I + t \cdot A$$

$$\Leftrightarrow X = I + t \cdot (A - I)$$


We would like to generate a sequence of interpolated matricies in order to make our transforming animation smoothly. Suppose that we want to generate 60 frames for our transformed visualisation, the interpolated matrix $X_j$ at the time $j^{th}$ can be expressed as:

$$ X_j = I + \frac{j}{60} \cdot (A - I), \quad 0 \leq j \leq 60 $$

### Generating the grid

Suppose our grid contains 9 poins on x-axis and 9 points on y-axis, we need to create a matrix to store the coordinates of 81 points:

$$
Grid = \begin{bmatrix}
  -4 & -4 & -4 & -4 & . & . & . & 4 & 4 & 4 & 4\\
  -4 & -3 & -2 & -1 & . & . & . & 1 & 2 & 3 & 4
\end{bmatrix}
$$

The matrix $Grid$ above stores the coordinates of 81 points when our interpolated matrix is [Identify Matrix](https://byjus.com/maths/identity-matrix/#:~:text=Identity%20Matrix%20Definition,result%20will%20be%20given%20matrix.) or $X_0$. The transformed animation can be created by finding the coordinates of 81 points at each time $j^{th}$, where $0 \leq j \leq 60$, the matrix of new coordinates is the result of a dot product, which is expressed below:

$$
NewGrid_j = X_j \cdot Grid
$$

When we have the matrix $NewGrid_j$, using [Matplotlib](https://matplotlib.org) to plot the grid before exporting the picture of $NewGrid_j$. For example, this is the picture of $NewGrid_0$:

<p align="center">
  <img src="https://images2.imgbox.com/2d/12/Wa82YAG8_o.png" alt="Grid at 0th" width="300" height="300">
</p>

And this is the picture of $NewGrid_1$:

<p align="center">
  <img src="https://images2.imgbox.com/00/3c/2cFzmaFP_o.png" alt="Grid at 1th" width="300" height="300">
</p>

## Usage

Run the file `main.py`

```
python3 main.py
```

Enter the the maximum value on each axis (if we input 4, there will be 9 points on each a-xis: from -4 to 4)

```
What is the maximum value on each axis:
```

Input the transformed matrix that we need

```
Now, please input the compostion (input value should be an integer, otherwise, the program will crash)
Value for x1: 1
Value for y1: 2
Value for x2: 2
Value for y2: 1
```

We can find the output at the folder `outputForLinearTransformation`, then you can use an external tool such as [GIPHY](https://giphy.com) to create the GIF file.

## Authors and acknowledgment

This project is inspired by these following sources:

* [dododas](https://github.com/dododas)
* [3Blue1Brown](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

Contact me if you need help:

* [tamvoforwork@gmail.com](mailto:tamvoforwork@gmail.com)
* [Linkedin](https://www.linkedin.com/in/heytamvo/)
