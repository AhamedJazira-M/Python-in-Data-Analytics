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

plt.plot(x,y,"s-.b" , s=20,mec="b",mfc="y") #mec for marker edge color, mfc for marker face color
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