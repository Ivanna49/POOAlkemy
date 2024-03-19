from enum import Enum

# Enum TipoInstrumento
class TipoInstrumento(Enum):
    PERCUSION = 1
    VIENTO = 2
    CUERDA = 3

class Fabrica:
    def __init__(self):
        self.sucursales = []

    def porc_instrumentos_por_tipo(self, nombre_sucursal):
        sucursal = self.buscar_sucursal(nombre_sucursal)
        if sucursal:
            return sucursal.porc_instrumentos_por_tipo()
        else:
            return [0] * len(TipoInstrumento)

    def buscar_sucursal(self, nombre_sucursal):
        for sucursal in self.sucursales:
            if sucursal.nombre == nombre_sucursal:
                return sucursal
        return None

    def borrar_instrumento(self, ID):
        for sucursal in self.sucursales:
            if sucursal.borrar_instrumento(ID):
                return True
        return False

    def listar_instrumentos(self):
        for sucursal in self.sucursales:
            print(f"Instrumentos en {sucursal.nombre}:")
            sucursal.listar_instrumentos()

    def instrumentos_por_tipo(self, tipo):
        inst_encontrados = []
        for sucursal in self.sucursales:
            inst_encontrados.extend(sucursal.instrumentos_por_tipo(tipo))
        return inst_encontrados

    def agregar_sucursal(self, sucursal):
        self.sucursales.append(sucursal)

class Instrumento:
    def __init__(self, ID, precio, tipo):
        self.ID = ID
        self.precio = precio
        self.tipo = tipo

    def __str__(self):
        return f"Instrumento(ID={self.ID}, precio={self.precio}, tipo={self.tipo})"

class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def borrar_instrumento(self, ID):
        for instrumento in self.instrumentos:
            if instrumento.ID == ID:
                self.instrumentos.remove(instrumento)
                return True
        return False

    def porc_instrumentos_por_tipo(self):
        cant_instrumentos = len(self.instrumentos)
        porcentajes = [0] * len(TipoInstrumento)
        for instrumento in self.instrumentos:
            porcentajes[instrumento.tipo.value - 1] += 1
        porcentajes = [(count / cant_instrumentos) * 100 for count in porcentajes]
        return porcentajes

    def agregar_instrumento(self, ins):
        self.instrumentos.append(ins)

    def listar_instrumentos(self):
        for instrumento in self.instrumentos:
            print(instrumento)

    def instrumentos_por_tipo(self, tipo):
        inst_encontrados = [instrumento for instrumento in self.instrumentos if instrumento.tipo == tipo]
        return inst_encontrados

if __name__ == "__main__":
    f = Fabrica()

    s1 = Sucursal("Sucursal 1")
    s2 = Sucursal("Sucursal 2")

    s1.agregar_instrumento(Instrumento("id64", 66, TipoInstrumento.CUERDA))
    s1.agregar_instrumento(Instrumento("id35", 55, TipoInstrumento.VIENTO))
    s1.agregar_instrumento(Instrumento("id32", 44, TipoInstrumento.PERCUSION))

    s2.agregar_instrumento(Instrumento("id64", 66, TipoInstrumento.CUERDA))
    s2.agregar_instrumento(Instrumento("id66", 33, TipoInstrumento.VIENTO))

    f.agregar_sucursal(s1)
    f.agregar_sucursal(s2)

    print("Todos los instrumentos:")
    f.listar_instrumentos()

    print("\nInstrumentos de tipo 'Cuerda':")
    lista = f.instrumentos_por_tipo(TipoInstrumento.CUERDA)
    for instrumento in lista:
        print(instrumento)

    print("\nBorrando instrumento con ID '64'...")
    borrado = f.borrar_instrumento("64")
    if borrado:
        print("Instrumento eliminado.")
    else:
        print("Instrumento no encontrado.")

    print("\nPorcentaje de instrumentos por tipo en 'Sucursal 2':")
    porcs = f.porc_instrumentos_por_tipo("Sucursal 2")
    for tipo, porc in zip(TipoInstrumento, porcs):
        print(f"{tipo.name}: {porc}%")