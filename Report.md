# Seminar 5: Python Magic

## C312 Team # 6

### Members:

- José Miguel Zayas Pérez
- Raimel Daniel Romaguera Puig
- Yoel Enriquez Sena

---

# Special Methods, Python

Special methods in Python are functions that have names that start and end with two underscores ( \_\_ ). These methods allow objects to define special behaviors for common operations in Python, such as addition (\_\_add\_\_), subtraction (\_\_sub\_\_), multiplication (\_\_mul\_\_), indexing (\_\_getitem\_\_), value assignment (\_\_setitem\_\_), and string representation (\_\_str\_\_). These methods are part of what is known as "magic" in Python, as they allow objects to customize their behavior in specific situations without needing to modify the Python code itself.

## Other functionalities used

### @classmethod

The @classmethod decorator in Python is used to define a method that is bound to the class and not to an instance of the class. This means that the method can be called on the class itself, rather than on an instance of the class. The primary difference between a class method and an instance method is that the class method receives the class as the first argument (conventionally called cls), while an instance method receives the instance of the class as the first argument (conventionally called self). Class methods are useful for creating alternative construction methods (constructors) or for operations that affect the class as a whole, rather than a specific instance of the class.

```python
    @classmethod
    def from_list(cls, matriz: List[List[int]]) -> 'Matriz':
        if not all(len(row) == len(matriz[0]) for row in matriz):
            raise ValueError("All sublists must have the same length")
        rows = len(matriz)
        cols = len(matriz[0])
        newmatriz = cls(rows, cols)
        newmatriz.matriz = matriz
        return newmatriz
```

In addition to the constructor \_\_init\_\_ the Matrix class has the method **from_list** with the decorator **@classmethod** that works as another 'constructor', allows creating the matrix from a list of lists and works as explained above, example of use:

```python
matrizfromlist = Matrix.from_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
```

### Typing.List and Typing.Tuple

The typing.List and typing.Tuple modules are part of the typing library in Python, which provides type annotations to improve code readability and type checking. List is used to annotate lists, and Tuple to annotate tuples. These annotations help developers understand what type of data a function or method expects to handle, and can be used by static code analysis tools to detect type errors before the code is run.

```python
from typing import List
from typing import Tuple
```

It is used to specify that the value received should be of type List or Tuple, for example in the method above **from_list** it specifies that the parameter matrix should be `List[List[int]]` :

```python
    def from_list(cls, matriz: List[List[int]]) -> 'Matriz':
```

# Matrix Class

The Matrix class in Python implements a two-dimensional matrix with basic operations such as addition, subtraction, scalar multiplication, and matrix multiplication; in addition, we have the calculation of the determinant, minors, the identity matrix, and the matrix power.

# Matrix Implementation

## \_\_init\_\_ Method

This method is the Matrix class constructor. It initializes a matrix with a specific number of rows and columns, filling it with an initial value given. Nested lists are used to represent the matrix, where each inner list represents a row of the matrix.

```python
    def __init__(self, rows: int, cols: int, initial_value: int = 0) -> 'Matriz':
        matriz = [[initial_value for _ in range(cols)] for _ in range(rows)]
        self.matriz = matriz
        self.rows = rows
        self.cols = cols
        self.current_row = 0
        self.current_col = 0
```

The current_row and current_col properties in the Matrix class are used to keep track of the current position during iteration through the matrix elements.

### Parameters:

- rows: Number of rows of the matrix.
- cols: Number of columns of the matrix.
- initial_value: Initial value to fill the matrix. Default is 0.

## identity Method

Returns a new identity matrix of n rows, the identity matrix is the one that has the value 1 on the diagonal and 0 in the rest of the positions.

```python
    def identity(cls, n: int) -> 'Matriz':
        return Matrix.from_list([[1 if i == j else 0 for j in range(n)] for i in range(n)])
```

## sum Method

Performs the addition of two matrices. Checks that the matrices have the same dimensions before proceeding with the addition.

```python
    def sum(self, matriz: 'Matriz') -> 'Matriz':
        if matriz.cols != self.cols or matriz.rows != self.rows:
            raise ValueError("To add 2 matrices, they must have the same dimension")

        result: List[List[int]] = [[self.matriz[i][j] + matriz.matriz[i][j] for j in range(self.cols)] for i in range(self.rows)]

        return Matrix.from_list(result)
```

Returns a new matrix that is the result of the operation between the two previous matrices.

### Parameters:

- matriz: Matrix to add to the current matrix.

## sub Method

Performs the subtraction of two matrices. Checks that the matrices have the same dimensions before proceeding with the subtraction.

```python
    def sub(self, matriz: 'Matriz') -> 'Matriz':
        if matriz.cols != self.cols or matriz.rows != self.rows:
            raise ValueError("To subtract 2 matrices, they must have the same dimension")
        result: List[List[int]] = [[self.matriz[i][j] - matriz.matriz[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix.from_list(result)
```

Returns a new matrix that is the result of the operation between the two previous matrices.

### Parameters:

- matriz: Matrix to subtract from the current matrix.

## \_\_add\_\_ Method

Overloading of the + operator to allow matrix addition through A + B. Calls the sum method to perform the addition.

```python
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Only matrices can be added")
        return self.sum(other)
```

Checks that the addition is being done with another matrix, in that case it returns the result of calling the **sum** method explained above.
Example of use:

```python
m1 = Matrix.from_list([[1, 2], [3, 4]])
m2 = Matrix.from_list([[5, 6], [7, 8]])

m3 = m1 + m2
print(m3) # Prints [[6, 8], [10, 12]]
```

### Parameters:

- other: Matrix to add to the current matrix.

## \_\_sub\_\_ Method

Overloading of the - operator to allow matrix subtraction through A - B. Calls the sub method to perform the subtraction.

```python
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Only matrices can be subtracted")
        return self.sub(other)
```

Checks that the subtraction is being done with another matrix, in that case it returns the result of calling the **sub** method explained above.

### Parameters:

- other: Matrix to subtract from the current matrix.

## scalar_multiply Method

Multiplies each element of the matrix by a scalar.

```python
    def scalar_multiply(self, scalar: int) -> 'Matriz':
        result: List[List[int]] = [[self.matriz[i][j] * scalar for j in range(self.cols)] for i in range(self.rows)]
        return Matrix.from_list(result)
```

### Parameters:

- scalar: Scalar by which each element of the matrix will be multiplied.

## multiply Method

Performs the multiplication of matrices. Checks that the number of columns of the current matrix is equal to the number of rows of the matrix with which it is multiplying.

```python
    def multiply(self, matriz: 'Matriz') -> 'Matriz':
        if matriz.rows != self.cols:
            raise ValueError("To multiply 2 matrices, the number of columns of the first matrix must be equal to the number of rows of the second matrix")

        result: List[List[int]] = [[0 for _ in range(matriz.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(matriz.cols):
                for k in range(matriz.rows):
                    result[i][j] += self.matriz[i][k] * matriz.matriz[k][j]

        return Matrix.from_list(result)
```

In the case of matrix multiplication, it is only allowed if the number of columns of the first is equal to the number of rows of the second, then the calculations are made and a new matrix is returned.

### Parameters:

- matriz: Matrix with which the current matrix will be multiplied.

## \_\_mul\_\_ Method

Overloading of the _ operator to allow matrix multiplication through A _ B and scalar multiplication through A \* n. Calls the multiply method for matrix multiplication and scalar_multiply for scalar multiplication.

```python
    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self.multiply(other)
        if isinstance(other, int):
            return self.scalar_multiply(other)
        raise ValueError("Only matrices or scalar can be multiplied")
```

Checks if _other_ is a Matrix or is an integer value, in those cases the corresponding operation is performed.
