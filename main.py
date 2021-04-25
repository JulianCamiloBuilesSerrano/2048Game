from ventana import  *
from game2048 import *
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.buttonUp.clicked.connect(self.up)
        self.buttonDown.clicked.connect(self.down)
        self.buttonRight.clicked.connect(self.right)
        self.buttonLeft.clicked.connect(self.left)
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
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()