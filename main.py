from ventana import  *
from game2048 import *
from  player1 import movimiento
from threading import *
from logistic_regression import *
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
        self.game.up()
        self.setmat()
    def down(self):
        self.game.down()
        self.setmat()    
    def right(self):
        self.game.right()
        self.setmat() 
    def left(self):
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
    def decition(self,W1,b1,W2,b2):
        def ecuation( W, b, X ):
            return ( 1.0 / ( 1.0 + numpy.exp( -( ( W @ X ) + b ) ) ) )[ 0 ]
        X = []
        for i in self.game.mat:
            for j in i:
                X.append(j)
        print(X)

        #calculate the values
        v1 = ecuation(W1,b,X)
        v2 = ecuation(W2,b2,X)
        return v1,v2
    
    def autoPlayer2(self):
        #get the values for W and b for up and down
        W1,b1 = logisticUpDown()
        #get the values for W and b for right and left
        W2,b2 = logisticRightLetf()
        while self.game.status():
            time.sleep(0.5)
            v1,v2 = self.decition(W1,b1,W2,b2)
            print(v1,v2)
            
            if v2 >= 0.5:
                print("left")
                self.left()
            elif v2 < 0.5:
                print("right")
                self.right()
            elif v1 >= 0.5:
                print("down")
                self.down()
            else:
                print("up")
                self.up()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()