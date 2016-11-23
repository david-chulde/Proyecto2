
def leertxt():
    archi=open('bloc.txt','r')
    linea=archi.readline()
    while linea!='':
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
