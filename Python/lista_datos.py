# Datos persistentes (base de datos)
tupla_pares_global = ()
tupla_impares_global = ()

class ListaNumeros:
    def __init__(self):
        self.lista_numero = []
        self.tupla_pares = tupla_pares_global
        self.tupla_impares = tupla_impares_global

    def guardar_numero(self, dato_numero):
        self.lista_numero.append(dato_numero)
        print(f"Lista actual: {self.lista_numero}")

    def incluir_lista(self, datos):
        self.lista_numero.extend(datos)
        print(f"Lista actual: {self.lista_numero}")

    def insertar_dato(self, posicion, dato):
        if 0 <= posicion <= len(self.lista_numero):
            self.lista_numero.insert(posicion, dato)
            print(f"Lista actual: {self.lista_numero}")
        else:
            print("Posición inválida.")

    def eliminar_dato(self, dato):
        if dato in self.lista_numero:
            self.lista_numero.remove(dato)
            print(f"'{dato}' eliminado. Lista actual: {self.lista_numero}")
        else:
            print(f"'{dato}' no encontrado en la lista.")

    def ver_numero(self):
        print(f"Lista completa: {self.lista_numero}")
        return self.lista_numero

    def crear_tupla_pares(self):
        global tupla_pares_global
        self.tupla_pares = tuple(num for num in self.lista_numero if num % 2 == 0)
        tupla_pares_global = self.tupla_pares
        print(f"Tupla de pares creada: {self.tupla_pares}")
        return self.tupla_pares

    def crear_tupla_impares(self):
        global tupla_impares_global
        self.tupla_impares = tuple(num for num in self.lista_numero if num % 2 != 0)
        tupla_impares_global = self.tupla_impares
        print(f"Tupla de impares creada: {self.tupla_impares}")
        return self.tupla_impares

    def modificar_tupla(self, tipo):
        global tupla_pares_global, tupla_impares_global
        
        if tipo == "pares":
            temp_list = list(self.tupla_pares)
            print(f"Tupla actual de pares: {self.tupla_pares}")
        else:
            temp_list = list(self.tupla_impares)
            print(f"Tupla actual de impares: {self.tupla_impares}")
            
        print("\nOpciones:")
        print("1. Agregar número")
        print("2. Eliminar número")
        print("3. Cancelar")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                num = float(input("Ingrese el número a agregar: "))
                if (tipo == "pares" and num % 2 == 0) or (tipo == "impares" and num % 2 != 0):
                    temp_list.append(num)
                    if tipo == "pares":
                        self.tupla_pares = tuple(temp_list)
                        tupla_pares_global = self.tupla_pares
                    else:
                        self.tupla_impares = tuple(temp_list)
                        tupla_impares_global = self.tupla_impares
                    print(f"Tupla actualizada: {tuple(temp_list)}")
                else:
                    print(f"El número no es {tipo}. No se agregó.")
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")
                
        elif opcion == "2":
            try:
                num = float(input("Ingrese el número a eliminar: "))
                if num in temp_list:
                    temp_list.remove(num)
                    if tipo == "pares":
                        self.tupla_pares = tuple(temp_list)
                        tupla_pares_global = self.tupla_pares
                    else:
                        self.tupla_impares = tuple(temp_list)
                        tupla_impares_global = self.tupla_impares
                    print(f"Tupla actualizada: {tuple(temp_list)}")
                else:
                    print("Número no encontrado en la tupla.")
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")
                
        elif opcion == "3":
            return
        else:
            print("Opción inválida.")

    def ver_tuplas(self):
        print(f"\nTupla de números pares: {self.tupla_pares}")
        print(f"Tupla de números impares: {self.tupla_impares}")