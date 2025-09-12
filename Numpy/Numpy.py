#Install numpy if not already installed.
#Add ! before pip to install in google colab or jupyter notebook

#pip install numpy

import numpy as np
np.__version__ #check numpy version

#Array Initialization

a=np.array([6,9,2,3]) #1D array
b=np.array([(6,9,2,3),(1,2,3,4)]) #2D array
c=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) #3D array 

#Generating array

d=np.arange(1,10,2) #start, stop, step - Easier than using for loop
e=np.linspace(1,10,5) #start, stop, number of elements

#Array Properties

a.ndim #number of dimensions
b.shape #shape of the array 
a.size #number of elements in the array
a.dtype #data type of the array
a.itemsize #size of each element in bytes
a.nbytes #total size of the array in bytes

b.dtype.name #data type name
b.T #transpose of the array


