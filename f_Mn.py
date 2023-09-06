# FUNCIÓN PARA EL CÁLCULO DE MOMENTO NOMINAL
# fc: resistencia del concreto _ N/mm^2
# Fy: Fluencia del acero _ N/mm^2
# Asc: Acero colocado _ cm²
# b: Base del elemento _ cm
# d: Altura efetiva _ cm

def f_Mn (fc, fy, Asc, b, d):
    Mn = 0.9*Asc*fy/10*(d-(Asc*fy/10)/(1.7*fc/10*b))
    return (Mn)