# FUNCIÓN PARA EL CÁLCULO DEL CORTANTE EN EL CONCRETO
# fiv: Factor de reducción de cortante
# fc: Resistencia del concreto _ N/mm^2
# b: Base del elemento _ cm
# d: Altura efetiva _ cm

def f_Vc (fiv, fc, b, d):
  b=b*10
  d=d*10
  Vc = (0.17*fiv*(fc)**0.5*b*d)/1000;
  return (Vc)