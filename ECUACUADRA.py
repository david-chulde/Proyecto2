import math



def creartxt():
    archi=open('ecuacion.txt','w')
    archi.close()

def grabartxt():
    archi=open('ecuacion.txt','a')
    
    
   
    print("CALCULO DE LAS RAICES DE UNA ECUACION DE SEGUNDO GRADO\n")
    print("forma: ax²+bx+c=0\n")
    a=int(input("ingresa valor a\n"))
    b=int(input("ingresa valor b\n"))
    c=int(input("ingresa valor c\n"))
    disc=b*b-4*a*c
    if(a!=0):
        if(disc<0):
            
            archi.write("tiene raices imaginarias")
        else:
            
            x1=(-b+(math.sqrt(disc)))/(2*a)
            x2=(-b-(math.sqrt(disc)))/(2*a)
            archi.write("El resultado de las raices son:\n")
            archi.write("X1 = "+str(x1)+"\nX2 = "+str(x2))
            
          
    else:     
        archi.write("coefiente cuadratico debe ser diferente de cero")
    archi.close()



def leertxt():
    archi=open('ecuacion.txt','r')
    linea=archi.readline()
    while linea!="":
        print (linea)
        linea=archi.readline()
    archi.close()

def leertxttenlista():
    archi=open('ecuacion.txt','r')
    lineas=archi.readlines()
    print (lineas)
    archi.close()
    
creartxt()
grabartxt()
leertxt()
#leertxttenlista()
         


