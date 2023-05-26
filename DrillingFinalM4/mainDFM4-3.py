from DrillingFinalM4 import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta

particular = Particular('Ford', 'Fiesta', 4, '180', '500', 5)
carga = Carga('Daft Trucks', 'G38 ', 10, 120, '1000', '20000')
bicicleta = Bicicleta('Shimano', 'MT Ranger', 2, 'Carrera')
motocicleta = Motocicleta('BMW', 'F800s', 2, ", Deportiva ", ', 2T', "Doble Viga", 21)

particular.guardar_datos_csv()
carga.guardar_datos_csv()
bicicleta.guardar_datos_csv()
motocicleta.guardar_datos_csv()

particular.leer_datos()
carga.leer_datos()
bicicleta.leer_datos()
motocicleta.leer_datos()


