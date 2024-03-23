from typing import List
from typing import Tuple

class Matriz:
    def __init__(self, rows: int, cols: int, initial_value: int = 0) -> 'Matriz':
        matriz = [[initial_value for _ in range(cols)] for _ in range(rows)]
        self.matriz = matriz
        self.rows = rows
        self.cols = cols
        self.current_row = 0
        self.current_col = 0
        
    @classmethod
    def from_list(cls, matriz: List[List[int]]) -> 'Matriz':
        if not all(len(row) == len(matriz[0]) for row in matriz):
            raise ValueError("Todas las sublistas deben tener la misma longitud")
        rows = len(matriz)
        cols = len(matriz[0])
        newmatriz = cls(rows, cols)
        newmatriz.matriz = matriz
        return newmatriz
    
    @classmethod
    def identity(cls, n: int) -> 'Matriz':
        return Matriz.from_list([[1 if i == j else 0 for j in range(n)] for i in range(n)])
        
    def sum(self, matriz: 'Matriz') -> 'Matriz':
        if matriz.cols != self.cols or matriz.rows != self.rows: 
            raise ValueError("Para sumar 2 matrices es necesario que tenga la misma dimensión")
        
        result: List[List[int]] = [[self.matriz[i][j] + matriz.matriz[i][j] for j in range(self.cols)] for i in range(self.rows)]

        return Matriz.from_list(result)
    
    def sub(self, matriz: 'Matriz') -> 'Matriz':
        if matriz.cols != self.cols or matriz.rows != self.rows: 
            raise ValueError("Para restar 2 matrices es necesario que tenga la misma dimensión")
        
        result: List[List[int]] = [[self.matriz[i][j] - matriz.matriz[i][j] for j in range(self.cols)] for i in range(self.rows)]

        return Matriz.from_list(result)
    
    def __add__(self, other):
        if not isinstance(other, Matriz):
            raise ValueError("Solo se pueden sumar matrices")
        return self.sum(other)
    
    def __sub__(self, other):
        if not isinstance(other, Matriz):
            raise ValueError("Solo se pueden restar matrices")
        return self.sub(other)

    def __mul__(self, other):
        if isinstance(other, Matriz):
            return self.multiply(other)
        if isinstance(other, int):
            return self.scalar_multiply(other)
        raise ValueError("Solo se pueden multiplicar matrices o escalar")
    
    def scalar_multiply(self, scalar: int) -> 'Matriz':
        result: List[List[int]] = [[self.matriz[i][j] * scalar for j in range(self.cols)] for i in range(self.rows)]
        return Matriz.from_list(result)
    
    def multiply(self, matriz: 'Matriz') -> 'Matriz':
        if matriz.rows != self.cols:
            raise ValueError("Para multiplicar 2 matrices, el número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")
        
        result: List[List[int]] = [[0 for _ in range(matriz.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(matriz.cols):
                for k in range(matriz.rows):
                    result[i][j] += self.matriz[i][k] * matriz.matriz[k][j]
        
        return Matriz.from_list(result)
    
    def determinant(self) -> int:
        if self.rows != self.cols:
            raise ValueError("La matriz debe ser cuadrada para calcular el determinante")
        if self.rows == 1:
            return self.matriz[0][0]
        if self.rows == 2:
            return self.matriz[0][0] * self.matriz[1][1] - self.matriz[0][1] * self.matriz[1][0]
        det = 0
        for i in range(self.rows):
            det += ((-1) ** i) * self.matriz[0][i] * self.minor(0, i).determinant()
        return det
    
    def minor(self, row: int, col: int) -> 'Matriz':
        if self.rows < 2 or self.cols < 2:
            raise ValueError("La matriz debe ser de al menos 2x2 para calcular el menor")
        result = [[self.matriz[i][j] for j in range(self.cols) if j != col] for i in range(self.rows) if i != row]
        return Matriz.from_list(result)
    
    def __pow__(self, exponent: int) -> 'Matriz':
        if self.rows != self.cols:
            raise ValueError("La matriz debe ser cuadrada para elevarla a una potencia")
        if exponent < 0:
            raise ValueError("El exponente debe ser un número entero positivo")
        if exponent == 0:
            return Matriz.identity(self.rows)
        if exponent == 1:
            return self
        return self * (self ** (exponent - 1))
    
    
    
    def __getitem__(self, index: Tuple[int, int]):
        row, col = index
        return self.matriz[row][col]
    
    def __setitem__(self, index: Tuple[int, int], value: int):
        row, col = index
        self.matriz[row][col] = value

    def __str__(self):
        return '\n'.join(['\t'.join([str(celda) for celda in fila]) for fila in self.matriz])
    
    def as_type(self, newtype):
        new_matriz = Matriz.from_list([[newtype(celda) for celda in fila] for fila in self.matriz])
        return new_matriz
    
    def __getattr__(self, name):
        if name.startswith('_'):
            try:
                row, col = map(int, name.strip('_').split('_'))
                return self.matriz[row][col]
            except (ValueError, IndexError):
                raise AttributeError(f"'{type(self).__name__}' no tiene el atributo '{name}'")
        if name.startswith('as_'):
            conversion = name[3:]
            conversion = conversion.replace('()', '')
            try:
                get_type = eval(conversion)
                return lambda: self.as_type(get_type)
            except NameError:
                raise AttributeError(f"No se puede convertir a '{conversion}'")
            
            
    def __setattr__(self, name, value):
        try:
            row, col = map(int, name.strip('_').split('_'))
            self.matriz[row][col] = value
        except ValueError:
            super().__setattr__(name, value)
        except IndexError:
            raise IndexError("Índices fuera de rango")
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.current_row >= len(self.matriz) or self.current_col >= len(self.matriz[0]):
            raise StopIteration
        value = self.matriz[self.current_row][self.current_col]
        self.current_col += 1
        if self.current_col >= len(self.matriz[0]):
            self.current_row += 1
            self.current_col = 0
        return value

m1 = Matriz.from_list([[1, 2], [3, 4]])
m2 = Matriz.from_list([[5, 6], [7, 8]])
print(m1)  # Debería imprimir [[1, 2], [3, 4]]
print("\n"+str(m2))  # Debería imprimir [[5, 6], [7, 8]]

# Suma
print("\nSuma")
m3 = m1 + m2
print(m3)  # Debería imprimir [[6, 8], [10, 12]]

# Resta
print("\nResta")
m4 = m1 - m2
print(m4)  # Debería imprimir [[-4, -4], [-4, -4]]

# Multiplicación
print("\nMultiplicación")
m5 = m1 * m2
print(m5)  # Debería imprimir [[19, 22], [43, 50]]

# Potencia
print("\nPotencia")
m6 = m1 ** 2
print(m6)  # Debería imprimir [[7, 10], [15, 22]]

# Utilizando notación de corchetes
print("\nUtilizando notación de corchetes")
m1[0, 0] = 10
print(m1)  # Debería imprimir [[10, 2], [3, 4]]
print(m1[0, 0])  # Debería imprimir 10

# Utilizando nombres de atributos
print("\nUtilizando nombres de atributos")
m1._0_1 = 20
print(m1)  # Debería imprimir [[10, 20], [3, 4]]
print(m1._0_1)  # Debería imprimir 20

# Conversión a float
print("\nConversión a float")
float_matrix = m1.as_float()
print(float_matrix)  # Debería imprimir [[10.0, 20.0], [3.0, 4.0]]

# Iteración a través de los elementos de la matriz
print("\nIteración a través de los elementos de la matriz")
for element in m1:
    print(element)