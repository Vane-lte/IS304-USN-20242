# Generar una lista de 10,000 elementos "pseudo-aleatorios"
num_elementos = 10000
lista_pseudo_aleatoria = [(i * 137) % 100000 for i in range(num_elementos)]  # Genera valores pseudo-aleatorios

# Definición de los métodos de ordenamiento
def ordenamiento_burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def ordenamiento_seleccion(arr):
    n = len(arr)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

def ordenamiento_insercion(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and clave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave

def ordenamiento_merge(arr):
    if len(arr) > 1:
        medio = len(arr) // 2
        izquierda = arr[:medio]
        derecha = arr[medio:]

        ordenamiento_merge(izquierda)
        ordenamiento_merge(derecha)

        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

# Función para simular la medición de tiempos de cada método de ordenamiento
def medir_tiempo_ordenamiento(metodo, lista_original):
    lista_copia = lista_original[:]  # Crear una copia para no alterar la lista original
    inicio = len(lista_copia)  # Simulación de tiempo de inicio (basado en el tamaño de la lista)
    metodo(lista_copia)  # Ejecutar el método de ordenamiento
    fin = len(lista_copia) + 1  # Simulación de tiempo final
    return fin - inicio  # Diferencia simulada (solo ilustrativo, no tiempo real)

# Lista de métodos de ordenamiento
metodos_ordenamiento = [
    ("Ordenamiento Burbuja", ordenamiento_burbuja),
    ("Ordenamiento Selección", ordenamiento_seleccion),
    ("Ordenamiento Inserción", ordenamiento_insercion),
    ("Ordenamiento Merge", ordenamiento_merge)
]

# Medir el tiempo "simulado" de ejecución de cada método y mostrar el resultado
for nombre, metodo in metodos_ordenamiento:
    tiempo_simulado = medir_tiempo_ordenamiento(metodo, lista_pseudo_aleatoria)
    print(f"<<{nombre}>>: {tiempo_simulado:.2f} segundos (simulado)")
