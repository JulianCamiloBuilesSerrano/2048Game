import random
from copy import deepcopy
import training
class game2048:

    def __init__(self):
        self.mat = [[0 for i in range(4)]for i in range(4)]
        self.points = 0
        self.random()
        self.random()
        self.Print()
        pass
    #end

    def random(self):
        l = [2,4]  
        random.choice(l)
        i =  random.randint(0,3)
        j =  random.randint(0,3)

        while self.mat[i][j] !=0:
            i =  random.randint(0,3)
            j =  random.randint(0,3)
        self.mat[i][j] = random.choice(l)
        return self.mat
    #end
    def Print(self):
        print("------------------------")
        for i in self.mat:
            for j in i:
                print("\t",j,end = "")
            #end for
            print()
        #end for
    #end
    def status(self):
        stat = "lose"
        #Win

        for i in self.mat:
            for j in i:
                if j == 2048:
                    stat = "win"
                #end if
            #end for
        #en for
        if stat != "win":            
            for i in self.mat:
                for j in i:
                    if j == 0:
                        stat = "continue"
                    #endif
                #endfor
            #endfor
            #end if
        #end if
        if stat == "lose":
            for i in range(0,4):
                for j in range(0,4):
                    if i < 3 and i > 0 and j < 3 and j >0:
                        if self.mat[i][j] == self.mat[i+1][j] or self.mat[i][j] == self.mat[i-1][j] or self.mat[i][j] == self.mat[i][j-1] or self.mat[i][j] == self.mat[i][j+1]:
                            stat = "continue" 
                        #end if
                    elif i > 0 and i < 3 and j == 0: #left side
                        if self.mat[i][j] == self.mat[i+1][j] or self.mat[i][j] == self.mat[i-1][j]or self.mat[i][j] == self.mat[i][j+1]:
                            stat = "continue"
                        #end if
                    elif i == 3  and j > 0 and j < 3:#down side
                        if self.mat[i][j] == self.mat[i-1][j] or self.mat[i][j] == self.mat[i][j-1]or self.mat[i][j] == self.mat[i][j+1]:
                            stat = "continue"
                        #end if
                    elif i > 0 and i < 3 and j == 3:#right side
                        if self.mat[i][j] == self.mat[i+1][j] or self.mat[i][j] == self.mat[i-1][j]or self.mat[i][j] == self.mat[i][j-1]:
                            stat = "continue"
                        #end if
                    elif i == 0  and j > 0 and j < 3:#up side
                        if self.mat[i][j] == self.mat[i+1][j] or self.mat[i][j] == self.mat[i][j-1]or self.mat[i][j] == self.mat[i][j+1]:
                            stat = "continue"
                        #end if
                    elif i == 0 and j == 0: #left up corner
                        if  self.mat[i][j] == self.mat[i][j+1]  or self.mat[i+1][j] == self.mat[i][j]:
                            stat = "continue"
                        #end if 
                    elif  i == 3 and j == 0:#left down corner
                        if  self.mat[i][j] == self.mat[i][j+1] or self.mat[i][j] == self.mat[i-1][j]:
                            stat = "continue"
                        #end if 
                    elif i == 3 and j == 3: #righ down corner
                        if  self.mat[i][j] == self.mat[i][j-1] or self.mat[i][j] == self.mat[i-1][j]:
                            stat = "continue"
                        #end if 
                    elif i == 0 and j == 3: #right up corner
                        if  self.mat[i][j] == self.mat[i+1][j]or self.mat[i][j] == self.mat[i][j-1]:
                            stat = "continue"



                        #end if
                #end for
            #end for
        return stat
    #end
    def up(self): 
        temp =  deepcopy(self.mat)
        #sum same numbers
        def subup():
            for j in range(4):
                for i in range(1,4):
                    while i !=0 and self.mat[i-1][j] == 0 and self.mat[i][j] != 0:
                        self.mat[i-1][j] = self.mat[i][j]
                        self.mat[i][j] = 0
                        i = i -1
                    #end while
                #end for
            #end for
        subup()
        
        for j in range(4):
            for i in range(3):
                if self.mat[i][j] == self.mat[i+1][j] and i < 3:
                    self.mat[i][j] = self.mat[i][j] +self.mat[i+1][j]
                    self.points = self.points +  self.mat[i][j] +self.mat[i+1][j]
                    self.mat[i+1][j] = 0
                    subup()
                #end if
            #end for
        #end for
        if(temp != self.mat):
            training.writeArribaAbajo(self.mat,0)
            self.random()
        self.Print()
    #end

    def down(self):
        temp =  deepcopy(self.mat)
        def subdown():
            for j in range(4):
                for i in [2,1,0]:
                    while i != 3 and self.mat[i+1][j] == 0 and self.mat[i][j] != 0  :   
                        self.mat[i+1][j] = self.mat[i][j]
                        self.mat[i][j] = 0
                        i = i + 1
                    #endw hile
                #end for
            #end for
        #end
        subdown()
        for j in range(4):
            for i in [3,2,1]:
                if i != 0 and self.mat[i][j] == self.mat[i-1][j] :
                    self.mat[i][j] = self.mat[i][j] + self.mat[i-1][j]
                    self.points = self.points + self.mat[i][j] + self.mat[i-1][j]
                    self.mat[i-1][j] = 0
                    subdown()
                #end if
            #end for
        #end for
        if(temp != self.mat):
            training.writeArribaAbajo(self.mat,1)
            self.random()
        self.Print()
    #end
    def left(self):
        temp =  deepcopy(self.mat)
        def subleft():
            for i in range(4):
                for j in range(1,4):
                    while j !=0 and self.mat[i][j-1] == 0 and self.mat[i][j] != 0:
                        self.mat[i][j-1] = self.mat[i][j]
                        self.mat[i][j] = 0
                        j = j -1
                    #end while
                #end  for
            #end for
        subleft()
        for i in range(4):
            for j in range(3):
                if self.mat[i][j] == self.mat[i][j+1] and j < 3:
                    self.mat[i][j] = self.mat[i][j] +self.mat[i][j+1]
                    self.points = self.points + self.mat[i][j] +self.mat[i][j+1]
                    self.mat[i][j+1] = 0
                    subleft()
                #endif
            #endfor
        #endfor
        if(temp != self.mat):
            training.writeDerecchaIzquierda(self.mat,1)
            self.random()
        self.Print()
    #end

    def right(self):
        temp =  deepcopy(self.mat)
        def subright():
            for i in range(4):
                for j in [2,1,0]:
                    while j != 3 and self.mat[i][j+1] == 0 and self.mat[i][j] != 0  :   
                        self.mat[i][j+1] = self.mat[i][j]
                        self.mat[i][j] = 0
                        j = j + 1
                    #endwhile
                #endfor
            #endfor
        #end
        subright()
        
        for i in range(4):
            for j in [3,2,1]:
                if j != 0 and self.mat[i][j] == self.mat[i][j-1] :
                    self.mat[i][j] = self.mat[i][j] + self.mat[i][j-1]
                    self.points = self.points + self.mat[i][j] + self.mat[i][j-1]
                    self.mat[i][j-1] = 0
                    subright()
                #endif
            #endfor
        #end for
        if(temp != self.mat):
            training.writeDerecchaIzquierda(self.mat,0)
            self.random()
        self.Print()
    #end

#endClass
'''

game = game2048()
while game.status() == "continue":
    res = input("digite letra ")
    if res == 'w':
        game.up()
    elif res == 's':
        game.down()
    elif res == 'd':
        game.right()
    elif res == 'a':
        game.left()
    print(game.points)
    '''