# FUNCIÓN PARA EL CALCULO DE CUANTÍAS PARA UN MOMENTO DADO
# fc: resistencia del concreto _ N/mm^2
# Fy: Fluencia del acero _ N/mm^2
# Mu: Momento de diseño _ kN.cm
# b: Base del elemento _ cm
# d: Altura efetiva _ cm

def f_pcal(fc, fy, Mu, b, d):
    k = (Mu/(b*d**2))
    m = (fy/(0.85*fc))
    pcal = 1/m*(1-(1-(2*m*k)/(0.90*fy/10))**0.5)
    return (pcal)