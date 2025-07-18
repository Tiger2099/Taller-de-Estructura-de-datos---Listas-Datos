from lista_datos import ListaNumeros

class Calculadora:
    def init(self):
        self.objlista = ListaNumeros()

    def pedir_numero(self):
        
        while True:
            try:
                numero1 = float(input("Ingrese número 1: "))
                numero2 = float(input("Ingrese número 2: "))
                return numero1, numero2
            except ValueError:
                print("Entrada inválida. Por favor, ingrese números válidos.")

    def menu(self):
        
        while True:
            print("\n--- MENÚ ---")
            print("1. Agregar dos números a la lista")
            print("2. Insertar número en posición específica")
            print("3. Eliminar número de la lista")
            print("4. Mostrar lista")
            print("5. Salir")

            opcion = input("Seleccione una opción (1-5): ")

            if opcion == "1":
                n1, n2 = self.pedir_numero()
                self.objlista.guardar_numero([n1,n2])
                

            elif opcion == "2":
                try:
                    pos = int(input("Ingrese posición para insertar: "))
                    n1 = float(input("Ingrese número 1 a insertar: "))
                    n2 = float(input("Ingrese número 2 a insertar: "))
                    self.objlista.insertar_dato(pos, [n1, n2])
                except ValueError:
                    print("Entrada inválida. Posición debe ser entero y los datos números.")

            elif opcion == "3":
                try:
                    n1 = float(input("Ingrese número 1 del par a eliminar: "))
                    n2 = float(input("Ingrese número 2 del par a eliminar: "))
                    self.objlista.eliminar_dato([n1, n2])
                except ValueError:
                    print("Entrada inválida. Debe ingresar números.")

            elif opcion == "4":
                self.objlista.ver_numero()

            elif opcion == "5":
                print("Saliendo del programa. ¡Hasta luego!")
                break

            else:
                print("Opción no válida. Intente de nuevo.")


if __name__ == "main":
    calc = Calculadora()
    calc.menu()