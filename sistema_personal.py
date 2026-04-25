class Empleado:
    def __init__(self, id_empleado, nombre, edad, puesto):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto

    def actualizar_datos(self, nombre=None, edad=None, puesto=None):
        if nombre:
            self.nombre = nombre
        if edad:
            self.edad = edad
        if puesto:
            self.puesto = puesto

    def __str__(self):
        return f"ID: {self.id_empleado} | Nombre: {self.nombre} | Edad: {self.edad} | Puesto: {self.puesto}"


class SistemaPersonal:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def listar_empleados(self):
        if not self.empleados:
            print("No hay empleados registrados.")
        else:
            for emp in self.empleados:
                print(emp)

    def buscar_empleado(self, id_empleado):
        for emp in self.empleados:
            if emp.id_empleado == id_empleado:
                return emp
        return None

    def eliminar_empleado(self, id_empleado):
        emp = self.buscar_empleado(id_empleado)
        if emp:
            self.empleados.remove(emp)
            print("Empleado eliminado.")
        else:
            print("Empleado no encontrado.")

    def actualizar_empleado(self, id_empleado):
        emp = self.buscar_empleado(id_empleado)
        if emp:
            print("Deja en blanco si no deseas cambiar algún dato.")
            nombre = input("Nuevo nombre: ")
            edad = input("Nueva edad: ")
            puesto = input("Nuevo puesto: ")

            emp.actualizar_datos(
                nombre if nombre else None,
                int(edad) if edad else None,
                puesto if puesto else None
            )
            print("Empleado actualizado.")
        else:
            print("Empleado no encontrado.")


def menu():
    sistema = SistemaPersonal()

    while True:
        print("\n--- SISTEMA DE REGISTRO DE PERSONAL ---")
        print("1. Registrar empleado")
        print("2. Listar empleados")
        print("3. Buscar empleado")
        print("4. Actualizar empleado")
        print("5. Eliminar empleado")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_emp = input("ID: ")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            puesto = input("Puesto: ")

            empleado = Empleado(id_emp, nombre, edad, puesto)
            sistema.agregar_empleado(empleado)
            print("Empleado registrado.")

        elif opcion == "2":
            sistema.listar_empleados()

        elif opcion == "3":
            id_emp = input("ID a buscar: ")
            emp = sistema.buscar_empleado(id_emp)
            if emp:
                print(emp)
            else:
                print("Empleado no encontrado.")

        elif opcion == "4":
            id_emp = input("ID del empleado a actualizar: ")
            sistema.actualizar_empleado(id_emp)

        elif opcion == "5":
            id_emp = input("ID del empleado a eliminar: ")
            sistema.eliminar_empleado(id_emp)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()