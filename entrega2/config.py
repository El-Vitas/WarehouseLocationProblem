
# Rangos para generar ubicaciones I y J
INSTANCIAS = (
    ((5, 7), (6, 10)),
    ((8, 12), (10, 20)),
    ((13, 18), (20, 30)),
    ((19, 23), (30, 40)),
    ((24, 30), (40, 50)),
    ((32, 38), (50, 65)),
    ((39, 45), (65, 80)),
    ((46, 53), (80, 95)),
    ((54, 65), (95, 110)),
    ((66, 72), (110, 125)),
    ((72, 81), (125, 145)),
    ((82, 91), (145, 165)),
    ((92, 101), (165, 185)),
    ((102, 111), (185, 205)),
    ((112, 131), (205, 225))
)

# Rangos para ubicaciones I celestes (C), verdes claros (VC) y verde oscuro (VO)
RANGOC1 = (1, 99, 1, 500)
RANGOC2 = (100, 600, 1, 99)
RANGOC3 = (501, 600, 100, 600)
RANGOC4 = (1, 500, 501, 600)

RANGOVC1 = (100, 224, 100, 375)
RANGOVC2 = (225, 500, 100, 224)
RANGOVC3 = (376, 500, 225, 500)
RANGOVC4 = (100, 375, 376, 500)

RANGOVO = (225, 375, 225, 375)

class Instancia:
    """
    Descripción: Clase que representa una instancia con información sobre ubicaciones, costos, capacidad y emisiones.
    """
    def __init__(self):
        self.ubicaciones_I_C = []
        self.ubicaciones_I_V = []
        self.ubicaciones_J = []
        self.costos_instalacion_C = []
        self.costos_instalacion_V = []
        self.capacidad_bodegas_C = []
        self.capacidad_bodegas_V = []
        self.emisiones_operacion_C = []
        self.emisiones_operacion_V = []
        self.distancias_C = []
        self.distancias_V = []

    def get_ubicaciones_I_C(self):
        return self.ubicaciones_I_C

    def append_ubicaciones_I_C(self, nueva_ubicacion_I_C):
        self.ubicaciones_I_C.append(nueva_ubicacion_I_C)

    def get_ubicaciones_I_V(self):
        return self.ubicaciones_I_V

    def append_ubicaciones_I_V(self, nueva_ubicacion_I_V):
        self.ubicaciones_I_V.append(nueva_ubicacion_I_V)

    def get_ubicaciones_J(self):
        return self.ubicaciones_J

    def append_ubicaciones_J(self, nueva_ubicacion_J):
        self.ubicaciones_J.append(nueva_ubicacion_J)

    def get_costos_instalacion_C(self):
        return self.costos_instalacion_C

    def append_costos_instalacion_C(self, nuevo_costo_instalacion_C):
        self.costos_instalacion_C.append(nuevo_costo_instalacion_C)

    def get_costos_instalacion_V(self):
        return self.costos_instalacion_V

    def append_costos_instalacion_V(self, nuevo_costo_instalacion_V):
        self.costos_instalacion_V.append(nuevo_costo_instalacion_V)

    def get_capacidad_bodegas_C(self):
        return self.capacidad_bodegas_C

    def append_capacidad_bodegas_C(self, nueva_capacidad_bodegas_C):
        self.capacidad_bodegas_C.append(nueva_capacidad_bodegas_C)

    def get_capacidad_bodegas_V(self):
        return self.capacidad_bodegas_V

    def append_capacidad_bodegas_V(self, nueva_capacidad_bodegas_V):
        self.capacidad_bodegas_V.append(nueva_capacidad_bodegas_V)

    def get_emisiones_operacion_C(self):
        return self.emisiones_operacion_C

    def append_emisiones_operacion_C(self, nueva_emision_operacion_C):
        self.emisiones_operacion_C.append(nueva_emision_operacion_C)

    def get_emisiones_operacion_V(self):
        return self.emisiones_operacion_V

    def append_emisiones_operacion_V(self, nueva_emision_operacion_V):
        self.emisiones_operacion_V.append(nueva_emision_operacion_V)

    def get_distancias_C(self):
        return self.distancias_C

    def append_distancias_C(self, nueva_distancia_C):
        self.distancias_C.append(nueva_distancia_C)

    def get_distancias_V(self):
        return self.distancias_V

    def append_distancias_V(self, nueva_distancia_V):
        self.distancias_V.append(nueva_distancia_V)
