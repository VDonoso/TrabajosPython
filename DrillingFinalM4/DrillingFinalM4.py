import csv

class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def guardar_datos_csv(self):
        try:
            with open('vehiculos.csv','a',newline="") as archivo:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)
        except FileNotFoundError:
            print('No se encentra el archivo vehiculos.cvs')
        except Exception as error:
            print('Se ha generado un error no previsto', type(error).__name__)  

    def leer_datos(self):
        try:
            with open('vehiculos.csv',"r") as archivo:
                vehiculos = csv.reader(archivo) 
                print(f'Lista de Vehiculos {type(self).__name__}')
                for item in vehiculos:
                    vehiculo_tipo = str(self.__class__)
                    if vehiculo_tipo in item [0]:
                        print(item[1])
                print("")                  
        except FileNotFoundError:
            print("No existe el archivo vehiculos.csv")
        except Exception as e:
            print("Error reportado: ",e)

    def __str__(self):
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, '
 
class Automovil(Vehiculo):
    def __init__(self,marca,modelo,nro_ruedas,velocidad,cilindraje):
        super().__init__(marca,modelo,nro_ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        return super().__str__() + f'{self.velocidad}, {self.cilindraje} cc'

class Particular(Automovil):
    def __init__(self, marca,modelo,nro_ruedas,velocidad,cilindraje,nro_puestos):
        super().__init__(marca,modelo,nro_ruedas,velocidad,cilindraje)
        self.nro_puestos = nro_puestos

    def get_nro_puestos(self):
        return self.nro_puestos
    
    def set_nro_puestos(self, npuestos):
        self.nro_puestos = npuestos

    def __str__(self):
        return super().__str__() + f' Puestos: {self.nro_puestos}'
    
class Carga(Automovil):
    def __init__(self, marca,modelo,nro_ruedas,velocidad,cilindraje,peso_carga):
        super().__init__(marca,modelo,nro_ruedas,velocidad,cilindraje)
        self.peso_carga = peso_carga
    
    def __str__(self):
        return super().__str__() + f', {self.peso_carga}'
    
class Bicicleta(Vehiculo):
    def __init__(self,marca,modelo,nro_ruedas,tipo):
        super().__init__(marca,modelo,nro_ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f',  {self.tipo}'
    
class Motocicleta(Bicicleta):
    def __init__(self,marca,modelo,nro_ruedas,tipo,nro_radios,cuadro,motor):
        super().__init__(marca,modelo,nro_ruedas,tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return super().__str__() + f'nro radio: {self.nro_radios}, cuadro: {self.cuadro}, motor: {self.motor}'
    
