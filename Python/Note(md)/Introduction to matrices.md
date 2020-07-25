## Introduction to matrices

### 1. Matrix Dimension

#### Example

$$
A_{4,3} = \begin{pmatrix}
	8 & 21 & 9 \\
	5 & 2 & 11 \\
	12 & 4 & 11 \\
	2 & 15 & 4
\end{pmatrix}
$$

This matrix has *4 rows* and *3 columns*, so the dimension of matrix A is *4 x 3* (read "four by three")

$$
A_{m,n} = \begin{pmatrix}
	a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
	a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
	\vdots & \vdots & \ddots & \vdots \\
	a_{m,1} & a_{m,2} & \cdots & a_{m,n}
\end{pmatrix}
$$


[^Note]: The number of rows is followed by the number of columns.

### 2. Vectors

**vector is matrix that has only one row or one column**

#### Example

$$
D_{1,4} = \begin{pmatrix}
	13 & 4 & 0 & 10
\end{pmatrix}
\hspace{50px}
U_{3,1} = \begin{pmatrix}
    2 \\ 21 \\ 6 \\
\end{pmatrix}
$$

### 3. Matrix Elements 

Each **element** has its own position, element in row ***m*** and column ***n*** is represented by ***a<sub>mn</sub>***

#### Example

***a<sub>12</sub>*** = 21 from earlier matrix

[^Note]: In computer graphics, matrices are used in such operations as translations, rotations, scaling and more. These concepts are relevant to the video game graphics. Understanding matrices is a basic necessity for programming 3D video games. Also the matrix, which we mention in the beginning, is real: computers can process photos precisely because the images are presented as matrices.

