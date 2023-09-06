# FUNCIÓN PARA EL CALCULO DE MOMENTO MÁXIMO
# fc: Resistencia del concreto _ N/mm^2
# Fy: Fluencia del acero _ N/mm^2
# pcal: Cuantía de acero calculada
# b: Base del elemento _ cm
# d: Altura efetiva _ cm

def f_Mmax(fc, fy, pcal, b, d):
    Mmax = (-9*fy*b*(d**2)*pcal*(10*fy*pcal-17*fc))/(1700*fc)
    return (Mmax)