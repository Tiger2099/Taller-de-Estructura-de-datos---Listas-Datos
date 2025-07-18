from lista_datos import ListaNumeros

class Calculadora:
    def __init__(self):
        self.objlista = ListaNumeros()

    def pedir_numero(self):
        while True:
            try:
                numero1 = float(input("Ingrese número 1: "))
                numero2 = float(input("Ingrese número 2: "))
                return numero1, numero2
            except ValueError:
                print("Entrada inválida. Por favor, ingrese números válidos.")

    def menu_tuplas(self):
        while True:
            print("\n--- SUBMENÚ TUPLAS ---")
            print("1. Crear tupla con números pares")
            print("2. Crear tupla con números impares")
            print("3. Modificar tupla de pares")
            print("4. Modificar tupla de impares")
            print("5. Mostrar tuplas actuales")
            print("6. Volver al menú principal")
            
            opcion = input("Seleccione una opción (1-6): ")

            if opcion == "1":
                self.objlista.crear_tupla_pares()
                
            elif opcion == "2":
                self.objlista.crear_tupla_impares()
                
            elif opcion == "3":
                self.objlista.modificar_tupla("pares")
                
            elif opcion == "4":
                self.objlista.modificar_tupla("impares")
                
            elif opcion == "5":
                self.objlista.ver_tuplas()
                
            elif opcion == "6":
                break
                
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu(self):
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Agregar dos números a la lista")
            print("2. Insertar número en posición específica")
            print("3. Eliminar número de la lista")
            print("4. Mostrar lista")
            print("5. Menú de tuplas (pares/impares)")
            print("6. Salir")

            opcion = input("Seleccione una opción (1-6): ")

            if opcion == "1":
                n1, n2 = self.pedir_numero()
                self.objlista.guardar_numero(n1)
                self.objlista.guardar_numero(n2)

            elif opcion == "2":
                try:
                    pos = int(input("Ingrese posición para insertar: "))
                    n1 = float(input("Ingrese número 1 a insertar: "))
                    n2 = float(input("Ingrese número 2 a insertar: "))
                    self.objlista.insertar_dato(pos, n1)
                    self.objlista.insertar_dato(pos+1, n2)
                except ValueError:
                    print("Entrada inválida. Posición debe ser entero y los datos números.")

            elif opcion == "3":
                try:
                    n1 = float(input("Ingrese número a eliminar: "))
                    self.objlista.eliminar_dato(n1)
                except ValueError:
                    print("Entrada inválida. Debe ingresar números.")

            elif opcion == "4":
                self.objlista.ver_numero()

            elif opcion == "5":
                self.menu_tuplas()

            elif opcion == "6":
                print("Saliendo del programa. ¡Hasta luego!")
                break

            else:
                print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    calc = Calculadora()
    calc.menu()