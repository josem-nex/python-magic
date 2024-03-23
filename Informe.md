# Seminario 5 : Python mágico

## C312 Equipo # 6

### Integrantes:

- José Miguel Zayas Pérez
- Raimel Daniel Romaguera Puig
- Yoel Enriquez Sena

---

# Métodos especiales, Python

Los métodos especiales en Python son funciones que tienen nombres que comienzan y terminan con dos guiones bajos ( \_\_ ). Estos métodos permiten a los objetos definir comportamientos especiales para operaciones comunes en Python, algunos son la suma (\_\_add\_\_), la resta (\_\_sub\_\_), la multiplicación (\_\_mul\_\_), la indexación (\_\_getitem\_\_), la asignación de valores (\_\_setitem\_\_) y la representación en cadena (\_\_str\_\_). Estos métodos son parte de lo que se conoce como "magia" en Python, ya que permiten a los objetos personalizar su comportamiento en situaciones específicas sin necesidad de modificar el código de Python en sí.

## Otras funcionalidades utilizadas

### @classmethod

El decorador @classmethod en Python se utiliza para definir un método que está vinculado a la clase y no a una instancia de la clase. Esto significa que el método puede ser llamado en la clase en sí misma, en lugar de en una instancia de la clase. La principal diferencia entre un método de clase y un método de instancia es que el método de clase recibe la clase como primer argumento (convencionalmente llamado cls), mientras que un método de instancia recibe la instancia de la clase como primer argumento (convencionalmente llamado self). Los métodos de clase son útiles para crear métodos alternativos de construcción (constructores) o para operaciones que afectan a la clase en general, en lugar de a una instancia específica de la clase.

```python
    @classmethod
    def from_list(cls, matriz: List[List[int]]) -> 'Matriz':
        if not all(len(row) == len(matriz[0]) for row in matriz):
            raise ValueError("Todas las sublistas deben tener la misma longitud")
        rows = len(matriz)
        cols = len(matriz[0])
        newmatriz = cls(rows, cols)
        newmatriz.matriz = matriz
        return newmatriz
```

Además del constructor \_\_init\_\_ la clase Matriz tiene el método **from_list** con el decorador **@classmethod** que funciona como otro 'constructor', permite crear la matriz a partir de una lista de listas y funciona como se explicó anteriormente, ejemplo de uso:

```python
matrizfromlist = Matriz.from_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
```

### Typing.List y Typing.Tuple

Los módulos typing.List y typing.Tuple son parte de la biblioteca typing en Python, que proporciona anotaciones de tipo para mejorar la legibilidad y la verificación de tipos en el código. List se utiliza para anotar listas, y Tuple para anotar tuplas. Estas anotaciones ayudan a los desarrolladores a entender qué tipo de datos se espera que maneje una función o método, y pueden ser utilizadas por herramientas de análisis estático de código para detectar errores de tipo antes de ejecutar el código.

```python
from typing import List
from typing import Tuple
```

Se utiliza para especificar que el valor recibido debe ser de tipo List o Tuple, por ejemplo en el método anterior **from_list** se especifica que el parámetro matriz debe ser `List[List[int]]` :

```python
    def from_list(cls, matriz: List[List[int]]) -> 'Matriz':
```

# Clase Matriz

La clase Matriz en Python implementa una matriz bidimensional con operaciones básicas como suma, resta, multiplicación escalar y multiplicación de matrices; además tenemos el cálculo del determinante, menores, la matriz identidad y la matriz potencia.

# Implementación de Matriz

## Método \_\_init\_\_

Este método es el constructor de la clase Matriz. Inicializa una matriz con un número específico de filas y columnas, llenándola con un valor inicial dado. Utiliza listas anidadas para representar la matriz, donde cada lista interna representa una fila de la matriz.

```python
    def __init__(self, rows: int, cols: int, initial_value: int = 0) -> 'Matriz':
        matriz = [[initial_value for _ in range(cols)] for _ in range(rows)]
        self.matriz = matriz
        self.rows = rows
        self.cols = cols
        self.current_row = 0
        self.current_col = 0

```

Las propiedades current_row y current_col en la clase Matriz se utilizan para mantener un seguimiento de la posición actual durante la iteración a través de los elementos de la matriz.

### Parámetros:

rows: Número de filas de la matriz.

cols: Número de columnas de la matriz.

initial_value: Valor inicial para llenar la matriz. Por defecto es 0.

## Método identity

Devuelve una nueva matriz identidad de n filas, la matriz identidad es la que tiene el valor 1 en la diagonal y 0 en el resto de posiciones.

```python
    def identity(cls, n: int) -> 'Matriz':
        return Matriz.from_list([[1 if i == j else 0 for j in range(n)] for i in range(n)])
```

## Método sum

Realiza la suma de dos matrices. Verifica que las matrices tengan las mismas dimensiones antes de proceder con la suma.

```python
    def sum(self, matriz: 'Matriz') -> 'Matriz':
        if matriz.cols != self.cols or matriz.rows != self.rows:
            raise ValueError("Para sumar 2 matrices es necesario que tenga la misma dimensión")

        result: List[List[int]] = [[self.matriz[i][j] + matriz.matriz[i][j] for j in range(self.cols)] for i in range(self.rows)]

        return Matriz.from_list(result)
```

Devuelve una nueva matriz que es el resultado de la operación entre las dos matrices anteriores.

### Parámetros:

matriz: Matriz a sumar con la matriz actual.

## Método sub

Realiza la resta de dos matrices. Verifica que las matrices tengan las mismas dimensiones antes de proceder con la resta.

```python
    def sub(self, matriz: 'Matriz') -> 'Matriz':
        if matriz.cols != self.cols or matriz.rows != self.rows:
            raise ValueError("Para restar 2 matrices es necesario que tenga la misma dimensión")
        result: List[List[int]] = [[self.matriz[i][j] - matriz.matriz[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matriz.from_list(result)
```

Devuelve una nueva matriz que es el resultado de la operación entre las dos matrices anteriores.

### Parámetros:

matriz: Matriz a restar de la matriz actual.

## Método \_\_add\_\_

Sobrecarga del operador + para permitir la suma de matrices mediante A + B. Llama al método sum para realizar la suma.

```python
    def __add__(self, other):
        if not isinstance(other, Matriz):
            raise ValueError("Solo se pueden sumar matrices")
        return self.sum(other)
```

Verifica que se está realizando la suma con otra matriz, en ese caso devuelve el resultado de llamar al método **sum** explicado anteriormente.
Ejemplo de uso:

```python
m1 = Matriz.from_list([[1, 2], [3, 4]])
m2 = Matriz.from_list([[5, 6], [7, 8]])

m3 = m1 + m2
print(m3)  # Implrime [[6, 8], [10, 12]]
```

### Parámetros:

other: Matriz a sumar con la matriz actual.

## Método \_\_sub\_\_

Sobrecarga del operador - para permitir la resta de matrices mediante A - B. Llama al método sub para realizar la resta.

```python
    def __sub__(self, other):
        if not isinstance(other, Matriz):
            raise ValueError("Solo se pueden restar matrices")
        return self.sub(other)
```

Verifica que se está realizando la suma con otra matriz, en ese caso devuelve el resultado de llamar al método **sub** explicado anteriormente.

### Parámetros:

other: Matriz a restar de la matriz actual.

## Método scalar_multiply

Multiplica cada elemento de la matriz por un escalar.

```python
    def scalar_multiply(self, scalar: int) -> 'Matriz':
        result: List[List[int]] = [[self.matriz[i][j] * scalar for j in range(self.cols)] for i in range(self.rows)]
        return Matriz.from_list(result)
```

### Parámetros:

scalar: Escalar por el cual se multiplicará cada elemento de la matriz.

## Método multiply

Realiza la multiplicación de matrices. Verifica que el número de columnas de la matriz actual sea igual al número de filas de la matriz con la que se está multiplicando.

```python
    def multiply(self, matriz: 'Matriz') -> 'Matriz':
        if matriz.rows != self.cols:
            raise ValueError("Para multiplicar 2 matrices, el número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")

        result: List[List[int]] = [[0 for _ in range(matriz.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(matriz.cols):
                for k in range(matriz.rows):
                    result[i][j] += self.matriz[i][k] * matriz.matriz[k][j]

        return Matriz.from_list(result)

```

En el caso de la multiplicación de matrices solo es permitida si el número de columnas de la primera es igual al número de filas de la segunda, luego se hacen los cálculos correspondientes y se devuelve una nueva matriz.

### Parámetros:

matriz: Matriz con la que se multiplicará la matriz actual.

## Método \_\_mul\_\_

Sobrecarga del operador \* para permitir la multiplicación de matrices mediante A \* B y la multiplicación escalar mediante A \* n. Llama a los métodos multiply para la multiplicación de matrices y scalar_multiply para la multiplicación escalar.

```python
    def __mul__(self, other):
        if isinstance(other, Matriz):
            return self.multiply(other)
        if isinstance(other, int):
            return self.scalar_multiply(other)
        raise ValueError("Solo se pueden multiplicar matrices o escalar")
```

Se verifica si _other_ es una Matriz o es un valor entero, en esos casos se realiza la operación correspondiente.

### Parámetros:

other: Matriz a multiplicar con la matriz actual o escalar para la multiplicación escalar.

## Método Pow

El método **pow** es un método especial en Python que se llama cuando utilizas el operador de potencia (\*\*) en un objeto. Se utiliza para elevar una matriz a una potencia.

```python
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
```

Una matriz solo se puede elevar a un exponente si es cuadrada y si el exponente es un valor mayor o igual a 0.
Si el exponente es mayor que 1, se calcula la potencia de la matriz de forma recursiva. La matriz se multiplica por sí misma elevada a la potencia de exponent - 1.

### Parámetros

exponent: Número entero que representa el valor al que se va a elevar la matriz.

## Método minor

Calcula el menor de una matriz para una fila y columna específicas. Lanza una excepción si la matriz no es de al menos 2x2.

```python
    def minor(self, row: int, col: int) -> 'Matriz':
        if self.rows < 2 or self.cols < 2:
            raise ValueError("La matriz debe ser de al menos 2x2 para calcular el menor")
        result = [[self.matriz[i][j] for j in range(self.cols) if j != col] for i in range(self.rows) if i != row]
        return Matriz.from_list(result)
```

El cálculo del menor es utilizado para el determinante, es una operación importante en el álgebra de matrices. Se verifica que sea se de al menos 2x2 la matriz pues en caso contrario no tiene sentido calcular el menor.

### Parámetros:

row: Índice de la fila para la cual se calculará el menor.
col: Índice de la columna para la cual se calculará el menor.

## Método determinant

Calcula el determinante de una matriz cuadrada. Lanza una excepción si la matriz no es cuadrada.

```python
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
```

Solo se puede calcular el determinante en matrices cuadradas, se realizan los cálculos correspondientes y se utilizan los menores necesarios.

## Método \_\_getitem\_\_

Este método se llama cuando intentas acceder a un elemento de un objeto utilizando la notación de corchetes. El valor index es una tupla que contiene los índices de fila y columna. Se utiliza para obtener el valor de un elemento de la matriz en la posición especificada.

```python
    def __getitem__(self, index: Tuple[int, int]):
        row, col = index
        return self.matriz[row][col]

```

Ejemplo de uso:

```python
matrizfromlist = Matriz.from_list( [[1, 2, 3],
                                    [4, 5, 6],
                                    [7, 8, 9]])
print(matrizfromlist[0,1])   # print 2
```

### Parámetros:

index: Tupla que contiene el índice de la fila y la columna del elemento a acceder.

## Método \_\_setitem\_\_

Este método se llama cuando intentas establecer el valor de un elemento de un objeto utilizando la notación de corchetes.

```python
    def __setitem__(self, index: Tuple[int, int], value: int):
        row, col = index
        self.matriz[row][col] = value
```

Seria similar a lo anterior, pero en vez de leer esa posición se modificaía al valor recibido, ejemplo:

```python
matrizfromlist[0,1] = 10
print(matrizfromlist[0,1])   # print 10
```

### Parámetros:

index: Tupla que contiene el índice de la fila y la columna del elemento a modificar.
value: Nuevo valor para el elemento.

## Método \_\_str\_\_

Este método se llama cuando intentas convertir un objeto a una cadena de texto, como cuando intentas imprimir el objeto. Devuelve una representación en cadena de la matriz, donde cada fila se imprime en una línea separada.

```python
    def __str__(self):
        return '\n'.join(['\t'.join([str(celda) for celda in fila]) for fila in self.matriz])
```

El método join se usa para concatenar los strings recibidos, unidos por el caracter al que se le aplica, el que se encuentra a la izquierda. Ejemplo:

```python
'.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
```

## Método \_\_getattr\_\_

El método \_\_getattr\_\_ es un método especial en Python que se llama automáticamente cuando intentas acceder a un atributo que no existe en un objeto.

```python
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
```

Si el nombre del atributo comienza con un guión bajo, se asume que estás intentando acceder a un elemento de la matriz. Por ejemplo, \_1_2 se interpretaría como el elemento en la fila 1, columna 2.
Si el nombre del atributo comienza con as\_, se asume que estás intentando convertir la matriz a otro tipo. Por ejemplo, as_list se interpretaría como una solicitud para convertir la matriz a una lista.
El método eval() en Python toma una cadena de texto como entrada y la evalúa como una expresión de Python.
Se utiliza para convertir el nombre del tipo (que es una cadena de texto) en el tipo real. Por ejemplo, si conversion es "list", entonces eval(conversion) sería el tipo list.
El `return lambda` se utiliza para devolver una función que, cuando se llama, convierte la matriz al tipo especificado.
Finalmente se llama al método as_type que convierte a la matriz al tipo determinado.

### Parámetros:

name: Nombre del atributo que se intenta acceder.

## Método as_type

Convierte los elementos de la matriz a un tipo específico.

```python
    def as_type(self, newtype):
        new_matriz = Matriz.from_list([[newtype(celda) for celda in fila] for fila in self.matriz])
        return new_matriz
```

Este método realiza una iteración por la matriz creando una nueva matriz donde cada elemento es convertido al tipo solicitado. Devuelve un nuevo objeto Matriz.

### Parámetros:

newtype: Tipo al que se convertirán los elementos de la matriz.

## Método \_\_setattr\_\_

El método \_\_setattr\_\_ es un método especial en Python que se llama automáticamente cuando intentas establecer el valor de un atributo en un objeto.

```python
    def __setattr__(self, name, value):
        try:
            row, col = map(int, name.strip('_').split('_'))
            self.matriz[row][col] = value
        except ValueError:
            super().__setattr__(name, value)
        except IndexError:
            raise IndexError("Índices fuera de rango")
```

El método super() en Python se utiliza para llamar a métodos en la superclase de una clase. En el caso del método \_\_setattr\_\_, se utiliza para llamar al método \_\_setattr\_\_ de la superclase cuando el nombre del atributo no se puede dividir en dos números enteros.
Ejemplo de uso:

```python
m._1_2 = 10  # Ahora, el elemento en la fila 1, columna 2 es 10
```

### Parámetros:

name: Nombre del atributo que se intenta modificar.
value: Nuevo valor para el atributo.

## Método \_\_iter\_\_

El método \_\_iter\_\_ es un método especial en Python que se llama cuando intentas iterar sobre un objeto. Este método simplemente devuelve el objeto actual, lo que significa que el objeto es su propio iterador.

```python
    def __iter__(self):
        return self
```

## Método \_\_next\_\_

El método \_\_next\_\_ es otro método especial en Python que se llama para obtener el siguiente elemento en una iteración. Este método se utiliza para iterar sobre los elementos de la matriz en orden de fila y columna.

```python
    def __next__(self):
        if self.current_row >= len(self.matriz) or self.current_col >= len(self.matriz[0]):
            raise StopIteration
        value = self.matriz[self.current_row][self.current_col]
        self.current_col += 1
        if self.current_col >= len(self.matriz[0]):
            self.current_row += 1
            self.current_col = 0
        return value
```
