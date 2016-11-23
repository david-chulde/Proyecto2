import math
a=int(input("ingresa valor a\n"))
b=int(input("ingresa valor b\n"))
c=int(input("ingresa valor c\n"))
disc=b*b-4*a*c
if(a!=0):
 if(disc<0):
  print("tiene raices imaginarias")
 else:
  x1=(-b+(math.sqrt(disc)))/(2*a)
  x2=(-b-(math.sqrt(disc)))/(2*a)
  print("X1 = "+str(x1)+"\t X2 = "+str(x2))
else:
 print("coefiente cuadratico debe ser diferente de cero")
