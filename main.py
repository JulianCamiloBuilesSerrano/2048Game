from ventana import  *
from game2048 import *
from  player1 import movimiento
from threading import *
from logistic_regression import *
import training
import time
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.buttonUp.clicked.connect(self.up)
        self.buttonDown.clicked.connect(self.down)
        self.buttonRight.clicked.connect(self.right)
        self.buttonLeft.clicked.connect(self.left)
        self.player1.clicked.connect(self.autoPlayer1)
        self.player2.clicked.connect(self.autoPlayer2)
        self.game = game2048()
        self.setmat()
        self.entranando = False
        self.entrenando2 = False

    def setmat(self):
        if self.game.mat[0][0] != 0:
            self.p00.setText(str (self.game.mat[0][0]))
        else:
            self.p00.setText("")

        if self.game.mat[0][1] != 0:
            self.p01.setText(str (self.game.mat[0][1]))
        else:
            self.p01.setText("")

        if self.game.mat[0][2] != 0:
            self.p02.setText(str (self.game.mat[0][2]))
        else:
            self.p02.setText("") 

        if self.game.mat[0][3] != 0:
            self.p03.setText(str (self.game.mat[0][3]))
        else:
            self.p03.setText("")
        #--------- next row

        if self.game.mat[1][0] != 0:
            self.p10.setText(str (self.game.mat[1][0]))
        else:
            self.p10.setText("")

        if self.game.mat[1][1] != 0:
            self.p11.setText(str (self.game.mat[1][1]))
        else:
            self.p11.setText("")

        if self.game.mat[1][2] != 0:
            self.p12.setText(str (self.game.mat[1][2]))
        else:
            self.p12.setText("") 

        if self.game.mat[1][3] != 0:
            self.p13.setText(str (self.game.mat[1][3]))
        else:
            self.p13.setText("")
        #--------- next row

        if self.game.mat[2][0] != 0:
            self.p20.setText(str (self.game.mat[2][0]))
        else:
            self.p20.setText("")

        if self.game.mat[2][1] != 0:
            self.p21.setText(str (self.game.mat[2][1]))
        else:
            self.p21.setText("")

        if self.game.mat[2][2] != 0:
            self.p22.setText(str (self.game.mat[2][2]))
        else:
            self.p22.setText("") 

        if self.game.mat[2][3] != 0:
            self.p23.setText(str (self.game.mat[2][3]))
        else:
            self.p23.setText("")

        #--------- next row

        if self.game.mat[3][0] != 0:
            self.p30.setText(str (self.game.mat[3][0]))
        else:
            self.p30.setText("")

        if self.game.mat[3][1] != 0:
            self.p31.setText(str (self.game.mat[3][1]))
        else:
            self.p31.setText("")

        if self.game.mat[3][2] != 0:
            self.p32.setText(str (self.game.mat[3][2]))
        else:
            self.p32.setText("") 

        if self.game.mat[3][3] != 0:
            self.p33.setText(str (self.game.mat[3][3]))
        else:
            self.p33.setText("")
        self.Puntaje.setText(str(self.game.points))
        if self.game.status() == "lose":
            self.Estado.setText("Perdiste")
            self.Estado.setStyleSheet("color: red;")
            self.end()
        if self.game.status() == "win":
            self.Estado.setText("Ganaste")
            self.Estado.setStyleSheet("color: green;")

        
    def end(self):
        self.buttonUp.setEnabled(False)
        self.buttonDown.setEnabled(False)
        self.buttonRight.setEnabled(False)
        self.buttonLeft.setEnabled(False)
    def up(self):
        if self.entranando:
            training.writeArribaAbajo(self.game.mat,0)
        if self.entrenando2:
            c = self.trainingOption()
            training.writeOpcion(c,0) 
        self.game.up()
        self.setmat()
    def down(self):
        if self.entranando:
            training.writeArribaAbajo(self.game.mat,1)
        if self.entrenando2:
            c = self.trainingOption()
            training.writeOpcion(c,0) 
        self.game.down()
        self.setmat()    
    def right(self):
        if self.entranando:
            training.writeDerecchaIzquierda(self.game.mat,0)
        if self.entrenando2:
            c = self.trainingOption()
            training.writeOpcion(c,1) 
        self.game.right()
        self.setmat() 
    def left(self):
        if self.entranando:
            training.writeDerecchaIzquierda(self.game.mat,1)
        if self.entrenando2:
            c = self.trainingOption()
            training.writeOpcion(c,1) 
        self.game.left()
        self.setmat() 
    
    def autoPlayer1(self):
        while self.game.status() == "continue":
            time.sleep(0.5)
            m =  movimiento()
            if m == 0:
                self.down()
            elif m == 1:
                self.right()
            elif m == 2:
                self.left()
            elif m == 3:
                self.up()
    
    def ecuation(self, W, b, X ):
        return ( 1.0 / ( 1.0 + numpy.exp( -( ( W @ X ) + b ) ) ) )[ 0 ]

    def decition(self,W1,b1,W2,b2):
        
        X = []
        for i in self.game.mat:
            for j in i:
                X.append(j)
        #calculate the values
        v1 = self.ecuation(W1,b1,X)
        v2 = self.ecuation(W2,b2,X)
        return v1,v2
    def trainingOption(self):
        #get the values for W and b for up and down
        W1,b1 = logisticUpDown()
        #get the values for W and b for right and left
        W2,b2 = logisticRightLetf()
        return self.decition(W1,b1,W2,b2)
   
    def autoPlayer2(self):
        #get the values for W and b for up and down
        W1,b1 = logisticUpDown()
        #get the values for W and b for right and left
        W2,b2 = logisticRightLetf()
        Wc,bc = logisticOption()
        temp = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        flag = -1
        while self.game.status()  == "continue":
            time.sleep(0.5)
            v1,v2 = self.decition(W1,b1,W2,b2)
            vc = self.ecuation(Wc,bc,[v1,v2])
            print("vc ",vc, " v1 ",v1, ", v2 ",v2)
            if vc >= 0.5 or ( vc < 0.5 and self.game.mat == temp and (flag == 3 or flag == 2)) :
                if v2 >= 0.5 or (v2 < 0.5  and flag == 1 and self.game.mat == temp)  :
                    flag = 0
                    temp =  deepcopy(self.game.mat)
                    print("left")
                    self.left()
                    print("flag ", flag, " iguales Matrices: ", self.game.mat == temp )
                elif v2 < 0.5 or (v2 >= 0.5 and flag == 0 and self.game.mat ==  temp):
                    flag = 1
                    temp =  deepcopy(self.game.mat)
                    print("right")
                    self.right()
                    print("flag ", flag, " iguales Matrices: ", self.game.mat == temp )
            elif vc < 0.5 or ( vc >= 0.5 and self.game.mat == temp and (flag == 0 or flag == 1)):
                if v1 >= 0.5 or (v1 < 0.5 and flag == 3 and self.game.mat == temp):
                    flag = 2
                    temp =  deepcopy(self.game.mat)
                    print("down")
                    self.down()
                    print("flag ", flag, " iguales Matrices: ", self.game.mat == temp )
                elif v1 < 0.5 or (v1 >= 0.5  and flag ==2 and self.game.mat == temp):
                    flag = 3
                    temp =  deepcopy(self.game.mat)
                    print("up")
                    self.up()
                    print("flag ", flag, " iguales Matrices: ", self.game.mat == temp )
            
            
            

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()