# Definicion de clase Cliente
class Cliente:
    def __init__(self, numero, nombre):
        self.numero = numero
        self.nombre = nombre

    def __repr__(self):
        return f"Cliente({self.numero}, '{self.nombre}')"

# Algoritmo de ordenamiento Bubble Sort adaptado para objetos de tipo Cliente
def bubble_sort_clientes(clientes):
    n = len(clientes)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparamos por el número de cliente
            if clientes[j].numero > clientes[j + 1].numero:
                clientes[j], clientes[j + 1] = clientes[j + 1], clientes[j]

# Algoritmo de busqueda binaria adaptado para objetos de tipo Cliente
def busqueda_binaria_clientes(clientes, numero_buscado):
    inicio = 0
    fin = len(clientes) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if clientes[medio].numero == numero_buscado:
            return medio
        elif clientes[medio].numero < numero_buscado:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Lista de clientes (desordenada)
clientes = [
    Cliente(102, "Julian Alvarez"),
    Cliente(56, "Alexis Macallister"),
    Cliente(78, "Emiliano Martinez"),
    Cliente(33, "Lisandro Martinez"),
    Cliente(150, "Cristian Romero")
]

# Mostrar lista original
print("Lista original de clientes:")
for cliente in clientes:
    print(cliente)

# Ordenar la lista
bubble_sort_clientes(clientes)

# Mostrar lista ordenada
print("\nLista de clientes ordenada por número:")
for cliente in clientes:
    print(cliente)

# Buscar un cliente por numero de cliente.
numero_a_buscar = 78 # Deberia encontrar al cliente Emiliano Martinez
indice_encontrado = busqueda_binaria_clientes(clientes, numero_a_buscar)

# Mostrar resultado de la búsqueda
if indice_encontrado != -1:
    print(f"\nCliente con número {numero_a_buscar} encontrado en la posición {indice_encontrado}:")
    print(clientes[indice_encontrado])
else:
    print(f"\nCliente con número {numero_a_buscar} no encontrado.")