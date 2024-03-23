# Seminar 5 (Python Magic)

The requirements for each exercise in the seminar will be presented from both a practical and theoretical perspective; that is, for its presentation, each team will base itself on the practical case in question to introduce and explain the required theoretical element. The presentation is not merely a statement of code. Questions such as: _Why?, Based on what?, How is this achieved in language X?_ among others, must be asked.

All team members must participate in solving the exercise and be prepared to present all the work. **The person to present** is decided on the day of the presentation. Whoever is not present at the presentation of their team gets `0` in the evaluation. (Note that these grades are averaged and there is a distinction between `0` and `2`).

---

In `Python`, there is no predefined `array` type for multidimensional arrays.

1. Implement the `Matrix` class to represent matrices with addition and multiplication operations. Implement additional functionalities that you deem necessary.
1. Implement indexing for the `Matrix` class so that constructions like the following can be made: `a = matrix[0, 6]` or `matrix[1, 2] = 9`.
1. Implement indexing for the `Matrix` class through field access in the form: `a = matrix._0_6` or `matrix._1_2 = 9`.
1. Matrix objects must be iterable. The iterator of a matrix with `n` rows and `m` columns must return the elements in the following order: `matrix_1_1, matrix_1_2, ..., matrix_1_m, matrix_2_1, ..., matrix_n_m`
1. The matrix type can always be applied to the `as_type()` method, which returns a new matrix with all types converted to `type`. Assume that there is a constructor in `type` that converts from any type to `type`. For example:

```python
m = Matrix(2, 3) # creates a matrix of int with value 0s.
mf = m.as_float() # mf is a matrix of 0s but of type float.
```

> Analyze: Resolution of members and methods in `Python`. Magic methods. Iterators. The builtin `eval`. The functionality of `super`.

# Seminario 5 (Python Mágico)

Los requerimientos de cada ejercicio del seminario serán expuestos desde el punto de vista práctico y teórico; es decir, para su exposición, cada equipo se basará en el caso práctico en cuestión para introducir y explicar el elemento teórico requerido. La exposición no es una mera enunciación de código. Preguntas como: _¿Por qué?, ¿Basándose en qué?, ¿Cómo se logra esto en el lenguaje X?_ entre otras, deben hacerse.

Todos los miembros del equipo deben participar en la solución del ejercicio y estar preparados para exponer todo el trabajo. **La persona a exponer**. se decide el día de la exposición. Quién no esté presente en la exposición de su equipo tiene `0` en la evaluación. (Note que estas notas se promedian y hay distinción entre `0` y `2`).

---

En `Python` no existe el tipo predefinido `array` multidimensional.

1. Implemente la clase `Matriz`, para representar matrices con las operaciones de suma y producto. Implemente además otras funcionalidades que crea necesarias.
1. Implemente la indización para la clase `Matriz` de forma tal que se puedan hacer construcciones como las siguientes: `a = matriz[0, 6]` o `matriz[1, 2] = 9`.
1. Implemente la indización para la clase `Matriz` por medio de acceso a campos de la forma: `a = matriz._0_6` o `matriz._1_2 = 9`.
1. Los objetos matrices deberán ser iterables. El iterador de una matriz con `n` filas y `m` columnas debe devolver los elementos en el siguiente orden: `matriz_1_1, matriz_1_2, ..., matriz_1_m, matriz_2_1, ..., matriz_n_m`
1. Al tipo matriz se podrá aplicar siempre el método `as_type()` que devuelve una nueva matriz con todos los tipos convertidos al tipo `type`. Suponga que existe un constructor en `type` que convierte de cualquier tipo a type. Por ejemplo:

```python
m = Matriz(2, 3) # crea una matriz de int con valor 0s.
mf = m.as_float() # mf es una matriz de 0s pero de tipo float.
```

> Analizar: Resolución de miembros y métodos en `Python`. Métodos mágicos. Iteradores. El builtin `eval`. El funcionamiento de `super`.
