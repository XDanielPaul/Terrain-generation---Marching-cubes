# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=bad-whitespace
# pylint: disable=trailing-whitespace
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=singleton-comparison
from tkinter import *
from itertools import cycle
import copy
import random


gap = 10
height = 1920
width = 1080

class MarchingCubes(Tk):

    points = []

    def __init__(self):
        super(MarchingCubes, self).__init__()
        self.title("Marching cubes")
        self.minsize(800 , 600)
        self.canvas = Canvas(self, bg="white", height=600, width=800)
        self.draw()
        self.canvas.pack()

    def draw(self):
        i=gap
        j=gap
        u=0
        for u in range(int(800/gap)):
            self.points.append([])
            for _ in range(int(800/gap)):
                self.points[u].append(Point(self.canvas,i,j))
                i += gap
            j += gap
            i=gap

        # I am using values 0/1 to find out which corners of square are "active" and converting those values into "binary" string
        binary = ""
        #ABCD = corners of a square
        for k in range(60):   #60
            for l in range(79): #79
                A = self.points[k][l]
                binary = binary + str(self.points[k][l].value)
                B = self.points[k][l+1]
                binary = binary + str(self.points[k][l+1].value)
                C = self.points[k+1][l]
                binary = binary + str(self.points[k+1][l].value)
                D = self.points[k+1][l+1]
                binary = binary + str(self.points[k+1][l+1].value)
                self.draw_line(A,B,C,D,binary)
                binary = ""


    def draw_line(self, A,B,C,D,binary):    
        #1011 == 0100
        if(binary == "1011" or binary == "0100"):
            self.canvas.create_line((A.x+B.x)/2, A.y,B.x , (A.y+D.y)/2)
            print("1011 == 0100")
        #1000 == 0111
        elif(binary == "1000" or binary == "0111"):
            self.canvas.create_line(A.x, (A.y + C.y)/2,(A.x+B.x)/2 , A.y)
            print("1000 == 0111")
        #1100 == 0011
        elif(binary == "1100" or binary == "0011"):
            self.canvas.create_line(A.x, (A.y + C.y)/2,B.x , (B.y+D.y)/2)
            print("1100 == 0011")
        #1101 == 0010
        elif(binary == "1101" or binary == "0010"):
            self.canvas.create_line(A.x, (A.y + C.y)/2, (C.x + D.x)/2, D.y)
            print("1101 == 0010")
        #1110 == 0001
        elif(binary == "1110" or binary == "0001"):
            self.canvas.create_line((C.x+D.x)/2, C.y, D.x, (B.y + D.y)/2)
            print("1110 == 0001")
        #1111 == 0000
        elif(binary == "1111" or binary == "0000"):
            pass
        #1010 == 0101
        elif(binary == "1010" or binary == "0101"):
            self.canvas.create_line((A.x+B.x)/2, A.y, (C.x+D.x)/2, D.y)
            print("1010 == 0101")
        #1001
        elif( binary == "1001"):
            self.canvas.create_line((A.x+B.x)/2,A.y,B.x,(B.y+D.y)/2)
            self.canvas.create_line(A.x,(A.y+C.y)/2,(C.x+D.x)/2,C.y)
            print("1001")
        elif( binary == "0110"):
            self.canvas.create_line(A.x,(A.y+C.y)/2, (A.x+B.x)/2, A.y)
            self.canvas.create_line((C.x+D.x)/2, C.y, D.x, (B.y+D.y)/2)
            print("0110")

class Point:

    def __init__(self, canvas,x,y):
        self.value = random.uniform(0, 1)
        self.point = self.assign_color(canvas,x,y)
        self.x = x
        self.y = y

    def assign_color(self, canvas,x,y):
        if(self.value>0.5):
            self.value = 1
            return canvas.create_rectangle(x, y, x, y, fill="red", outline = 'red')
        else:
            self.value = 0
            return canvas.create_rectangle(x, y, x, y, fill="black", outline = 'black')

if __name__ == '__main__':
    root = MarchingCubes()
    root.mainloop()