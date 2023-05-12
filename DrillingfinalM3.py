# Identificar el 3° grupo "otros"
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]

todos = nombres + magos + cientificos
otros = []

for no_repetido in todos:
    if todos.count(no_repetido) == 1:
     otros.append(no_repetido)

#print(otros)

# Funcion que imprime el nombre de cada persona en la lista
def imprimir_nombres():
    magos = ("Harry Houdini, David Blaine, Teller")
    cientificos = ("Newton, Hawking, Einstein")
    otros = ("Messi, Pele, Juanes")
    
    nombres = (magos, cientificos, otros)
    return nombres

nombres = imprimir_nombres()
#print(nombres)

# Funcion para hacer granciodosos a los magos
def hacer_grandioso(a,b='El Gran '):
    grandioso = b + a
    return grandioso

cientificos = ("Newton, Hawking, Einstein")
otros = ("Messi, Pele, Juanes")   
magos = ["Harry Houdini", "David Blaine","Teller"]

magos_grandiosos = [hacer_grandioso(nombre)for nombre in magos]
    
#print(magos_grandiosos)

# Mostrar el nombre de todos más modificaciones
def imprime_todos():
    completo = (magos_grandiosos, cientificos, otros)
    return completo
completo = imprime_todos()
#print(completo)

#Recorrido de todo en una sola lista
todos_juntos = (nombres, completo)
final = []

for item in todos_juntos:
   juntos = imprime_todos()
   final.append(item)
print(final)
