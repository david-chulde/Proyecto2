def creartxt():
    archi=open('datos.txt','w')
    archi.close()

def grabartxt():
    archi=open('datos.txt','a')
    archi.write('Linea 1\n')
    archi.write('Linea 2\n')
    archi.write('Linea 3\n')
    archi.close()

creartxt()
grabartxt()

def leertxt():
    archi=open('datos.txt','r')
    linea=archi.readline()
    while linea!="":
        print (linea)
        linea=archi.readline()
    archi.close()

def leertxttenlista():
    archi=open('datos.txt','r')
    lineas=archi.readlines()
    print (lineas)
    archi.close()
    
leertxt()
leertxttenlista()
