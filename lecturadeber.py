def creartxt():
##archivo vacio a quien se va a llenar
    conP=open('deber2.txt','w')
##archivo lleno con texto
    archF=open('harry.txt','r')
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
