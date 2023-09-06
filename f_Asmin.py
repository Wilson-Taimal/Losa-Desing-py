# FUNCIÓN PARA EL CALCULO DE ACERO MÍNIMO
# pmin: Cuantía de refuerzo mínimo
# b: Base del elemento _ cm
# d: Altura efetiva _ cm

def f_Asmin(pmin, b, h):
    Asmin = pmin*b*h
    return (Asmin)