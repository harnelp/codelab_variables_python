# 1. Definir una variable de cada tipo primitivo y concatenarlas
# Variables primitivas
my_int = 10
my_float = 20.5
my_string = "Hello"
my_bool = True

# 2. Concatenación
result = my_string + " " + str(my_int) + " " + str(my_float) + " " + str(my_bool)

# 3. Límite de enteros y flotantes:
"""
En Python, los enteros tienen precisión arbitraria y solo están limitados por la memoria disponible.
Los flotantes tienen precisión limitada pero un rango muy amplio.
"""

# 4. Suma de los primeros n números pares 
#para números pares, la fórmula se modifica a n(n+1).
n = my_int
sum_even_numbers = n * (n + 1)

# Imprimir los resultados de las tareas anteriores
print(f"""
===================================================
Resultados primera actividad: {result}
===================================================
Resultados de suma numeros r: {sum_even_numbers}
===================================================
"""
)