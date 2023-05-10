"""
magos = (["Harry Houdini"],["David Blaine"], ["Teller"])
cientificos = (["Newton"], ["Hawking"], ["Einstein"])
otros = (["Messi"], ["Pele"], ["Juanes"])
"""



def imprimir_nombres():
    magos = ("Harry Houdini, David Blaine, Teller")
    cientificos = ("Newton, Hawking, Einstein")
    otros = ("Messi, Pele, Juanes")
    
    nombres = (magos, cientificos, otros)
    return nombres

nombres = imprimir_nombres()
print(nombres)

def hacer_grandioso(a,b='El Gran '):
    grandioso = b + a
    return grandioso

cientificos = ("Newton, Hawking, Einstein")
otros = ("Messi, Pele, Juanes")   
magos = ["Harry Houdini", "David Blaine","Teller"]
el_resto = (cientificos, otros)
magos_grandiosos = [hacer_grandioso(nombre)for nombre in magos]
    
print(magos_grandiosos, el_resto)