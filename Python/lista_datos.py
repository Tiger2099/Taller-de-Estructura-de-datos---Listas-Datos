class ListaNumeros:
    def init(self):
        self.lista_numero = []

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