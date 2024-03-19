from enum import Enum

class CategoriaEmpleado(Enum):
    SALARIO_FIJO = 1
    A_COMISION = 2

class Empleado:
    def __init__(self, dni, nombre, apellido, año_ingreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.año_ingreso = año_ingreso

    def calcular_salario(self):
        return 0  # Podríamos definir un comportamiento predeterminado aquí

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class EmpleadoSalarioFijo(Empleado):
    def __init__(self, dni, nombre, apellido, año_ingreso, salario_basico):
        super().__init__(dni, nombre, apellido, año_ingreso)
        self.salario_basico = salario_basico

    def calcular_salario(self):
        años_en_empresa = 2024 - self.año_ingreso
        porcentaje_adicional = 0
        if años_en_empresa >= 5:
            porcentaje_adicional = 0.10
        elif años_en_empresa >= 2:
            porcentaje_adicional = 0.05
        return self.salario_basico * (1 + porcentaje_adicional)

class EmpleadoComision(Empleado):
    def __init__(self, dni, nombre, apellido, año_ingreso, salario_min, clientes_captados, monto_por_cliente):
        super().__init__(dni, nombre, apellido, año_ingreso)
        self.salario_min = salario_min
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    def calcular_salario(self):
        salario = self.clientes_captados * self.monto_por_cliente
        return max(salario, self.salario_min)

def mostrarSalarios(empleados):
    for empleado in empleados:
        print(f"{empleado}: {empleado.calcular_salario()}")

def empleadoConMasClientes(empleados):
    max_clientes = 0
    empleado_max_clientes = None
    for empleado in empleados:
        if isinstance(empleado, EmpleadoComision) and empleado.clientes_captados > max_clientes:
            max_clientes = empleado.clientes_captados
            empleado_max_clientes = empleado
    return empleado_max_clientes

# Crear 10 empleados de ejemplo
empleados = [
    EmpleadoSalarioFijo(111, "Juan", "Perez", 2019, 2000),
    EmpleadoSalarioFijo(222, "Maria", "Gomez", 2017, 2500),
    EmpleadoSalarioFijo(333, "Carlos", "Lopez", 2020, 1800),
    EmpleadoSalarioFijo(444, "Ana", "Rodriguez", 2018, 2200),
    EmpleadoComision(555, "Pedro", "Martinez", 2016, 1000, 15, 50),
    EmpleadoComision(666, "Laura", "Diaz", 2015, 1200, 20, 60),
    EmpleadoComision(777, "Daniel", "Sanchez", 2017, 1500, 25, 55),
    EmpleadoComision(888, "Sofia", "Garcia", 2019, 900, 10, 45),
    EmpleadoComision(999, "Elena", "Fernandez", 2014, 1100, 18, 58),
    EmpleadoComision(1010, "Gabriel", "Romero", 2018, 1300, 22, 62)
]

# Mostrar salarios de los empleados
print("Salarios de los empleados:")
mostrarSalarios(empleados)

# Encontrar empleado con más clientes captados
empleado_mayor_clientes = empleadoConMasClientes(empleados)
if empleado_mayor_clientes:
    print(f"\nEl empleado con más clientes captados es: {empleado_mayor_clientes.nombre} {empleado_mayor_clientes.apellido}")
else:
    print("\nNo hay empleados a comisión.")