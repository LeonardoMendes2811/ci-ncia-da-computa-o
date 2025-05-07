'''Python'''
# Arrays (vetores/matrizes utilizando a biblioteca NumPy)
import numpy as np

# Criando em array NumPy unidimensional a partir de uma lista
array = np.array([1, 2, 3, 4, 5])
print("array:", array)

# Acessando elementos do array:
# - Índices começam em 0
# - Índices megativos acessam a partir do final
print("Primeiro elemento:", array[0])
print("Último elemento:", array[-1])

# Slicing (fatiamento) de arrys:
# - Sintaxe: [início:fim]
# - Índice final não é incluido
print("Elementos do índice 1 a 3 (exclusivo)", array[1:3])

# Listas (estrutura mutavél de elementos)
# Criando uma lista básica
my_list = [1, 2, 3, 4, 5]
print("Lista original:", my_list)

# Adicionando um elemento ao final da lista
my_list.append(6)
print("Lista após adicionar 6:", my_list)

# Inserindo um elemento em posição específica:
# - Sintaxe: insert(índice, valor)
# - Desloca elementos existentes para a direita
my_list.insert(2, 7)
print("Lista após inserir 7 posição 2", my_list)

# Removendo a primeira ocorrência de um elemento
print("Último elemento:", array[-1])

my_list.remove(4)
print("Lista após remover o valor 4:", my_list)