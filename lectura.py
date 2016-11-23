
def leertxt():
    archi=open('bloc.txt','r')
    linea=archi.readline()
    while linea!="":
        cont=0
        cont=cont+len('bloc.txt')
        print (linea)
        linea=archi.readline()
    print(cont)
    archi.close()

def leertxttenlista():
    archi=open('bloc.txt','r')
    lineas=archi.readlines()
    print (lineas)
    archi.close()

leertxt()

def creartxt():
    conP=open('datos2.txt','w')
    archF=open('bloc.txt','r')
    total=0
    linea=archF.readline()
    while linea!='':
        print(linea)
        linea=archF.readline()
        total=len(linea)+total
        print(total)
    conP.write(str(total))
    archF.close()
    conP.close()
creartxt()
