from DrillingFinalM4 import Vehiculo, Automovil

instance = []

n = int(input('Cuantos vehiculos desea conocer: '))

for i in range (n):
    print(f'Datos del automovil {i+1}')
    marca = input("Inserte marca del automovil: ")
    modelo = input("Inserte modelo del automovil: ")
    nro_ruedas = input("Inserte numero de ruedas: ")
    velocidad = input("Inserte la velociad en km/hr: ")
    cilindraje = input("Inserte el cilindraje en cc: ")
    print(" ")
    auto = Automovil(marca, modelo, nro_ruedas,velocidad,cilindraje)
    instance.append(auto)

print("Imprimiendo por pantalla los vehiculos: ")

for index, item in enumerate (instance):
    print(f'Datos del automovil {index +1}: Marca {item.marca}, Modelo {item.modelo}, {item.nro_ruedas} ruedas, {item.velocidad} Km/hr, {item.cilindraje} cc')