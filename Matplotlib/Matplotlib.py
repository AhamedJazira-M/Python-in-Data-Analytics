#Install matplotlib if not already installed.
#Add ! before pip to install in google colab or jupyter notebook

#pip install matplotlib
#pip install numpy

import matplotlib.pyplot as plt
import numpy as np

#BASIC PLOT

x=[1,2,3,4,5,6,7,8,9]
y=[10,2,8,3,9,6,4,5,8]
plt.plot(x,y)
plt.show()

#MARKER

x=np.array([0,6,20,40])
y=np.array([0,100,200,450])
plt.plot(x,y,"s") #s for square marker
plt.show()

#d - diamond marker
#o - circle marker
#^ - triangle marker
#* - star marker
#h - hexagon marker
#x - x marker
#p - pentagon marker

#DOTTED PLOT WITH LINE

plt.plot(x,y,"s:r") #s for square marker, : for dotted line, r for red color
plt.show()

#- for solid line
#-- for dashed line
#-. for dash-dot line
#: for dotted line

#MARKER SIZE
plt.plot(x,y,"s:r",ms=10) #ms for marker size
plt.show()

#change the around and inside color of the marker (plot)

plt.plot(x,y,"s-.b", s=20,mec="b",mfc="y") #mec for marker edge color, mfc for marker face color
plt.show()

#change the style of the plot line

plt.plot(x,y,"s--g",s=20,color="y",ls="-", linewidth="10") #ls for line style
plt.show()

#Title

plt.title("My first plot", fontsize=20, color="r", loc="left") #loc for location of the title
plt.xlabel("X axis", fontsize=15, color="b")
plt.ylabel("Y axis", fontsize=15, color="b")

#Grid format

plt.grid()
plt.grid(axis="x") #to show grid only for x axis
plt.grid(axis="y") #to show grid only for y axis

#Double plot

x=np.array([0,6,20,40])
y=np.array([0,100,200,450])
x2=np.array([0,5,10,15])
y2=np.array([0,50,100,150])
plt.plot(x,y,"s--g",s=20,color="y",ls="-", linewidth="3", label="First line") #label for legend
plt.plot(x2,y2,"o:r",ms=10, label="Second line")
plt.plot(x,y,"ro") #to show only the marker of the first line
plt.plot(x2,y2,"go") #to show only the marker of the second line

#Legend

plt.plot(x,y,"r",label="Profit")

#Bar Graph

x=["A","B","C","D","E"]
y=[10,20,15,25,30]
plt.bar(x,y, color="g", width=0.5) #width for the width of the bar
plt.show()

#Horizontal Bar Graph

plt.barh(x,y, color="b", height=0.5) #height for the height of the bar
plt.show()

#Double Bar Graph

x=["A","B","C","D","E"]
y1=[10,20,15,25,30]
y2=[5,15,10,20,25]
plt.bar(x,y1,color="g", width=0.3, label="Profit")
plt.bar(x,y2,color="b", width=0.3, label="Tax", bottom=y1) #bottom to stack the bars

