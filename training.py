import csv
def writeDerecchaIzquierda(mat,movimineto):
    #right is 0
    #left is 1
    info = []
    for i in mat:
        for j in i:
            info.append(j)
        #end for
    #end for
    info.append(movimineto)
    with open("derecha_izquierda.csv", "a+", newline='') as fd:
        writer =  csv.writer(fd,delimiter=";")
        writer.writerow(info)
    
#end def
def writeArribaAbajo(mat,movimineto):
    #up is 0
    #down is 1
    info = []
    for i in mat:
        for j in i:
            info.append(j)
        #end for
    #end for
    info.append(movimineto)
    with open("arriba_abajo.csv", "a+", newline='') as fd:
        writer =  csv.writer(fd,delimiter=";")
        writer.writerow(info)
#end def

