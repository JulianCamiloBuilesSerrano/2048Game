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
    #end with
#end def
def readDerecchaIzquierda():
    X = []
    Y = []
    with open("derecha_izquierda.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            r = row[0].split(";")
            t_x = []
            for i in range(17):
                if i == 16:
                    Y.append(int(r[i]))
                else:
                    t_x.append(int(r[i]))
                #end if
            #end for
        #end for
    #end with
            X.append(t_x)
       
    return X,Y
#end def

def readArribaAbajo():
    X = []
    Y = []
    with open("arriba_abajo.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            r = row[0].split(";")
            t_x = []
            for i in range(17):
                if i == 16:
                    Y.append(int(r[i]))
                else:
                    t_x.append(int(r[i]))
                #end if 
            #end for
        #end for
    #end with
            X.append(t_x)
       
    return X,Y
#end def

def writeOpcion(mat,movimineto):
    #poption up down 0
    #option right left 1
    info = []
    for i in mat:
        for j in i:
            info.append(j)
        #end for
    #end for
    info.append(movimineto)
    with open("deicision.csv", "a+", newline='') as fd:
        writer =  csv.writer(fd,delimiter=";")
        writer.writerow(info)
#end def
def readOption():
    X = []
    Y = []
    with open("deicision.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            r = row[0].split(";")
            t_x = []
            for i in range(3):
                if i == 2:
                    Y.append(float(r[i]))
                else:
                    t_x.append(float(r[i]))
                #end if 
            #end for
        #end for
    #end with
            X.append(t_x)
       
    return X,Y
#end def
