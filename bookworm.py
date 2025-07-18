import numpy as np
import json
import basereader as br
import functions as fun


name = input("Database: ")
data = []

br.setDatabaseName(name)
br.makeData(br.getDatabaseName())
data = br.exportData()

floors = fun.createFloorData(data)
prices = fun.createPriceData(data)
areas = fun.createAreaData(data)
bedrooms = fun.createBedroomData(data)
mat = fun.arrayOfArrays(areas, floors, bedrooms)
#b_vec = 
b_vec = fun.calculateBVector(mat,prices)
b0 = fun.calculateB0(mat,prices,b_vec)
print(b_vec)
print(b0)
"""
x = np.linspace(0,200,40)
y = np.linspace(0,200,8)
X, Y = np.meshgrid(x,y)
Z = b0 + X*b_vec[1] + Y*b_vec[2]

fig = fun.plt.figure("Vake rent")
ax = fig.add_subplot(projection='3d')
ax.scatter(floors, bedrooms, prices)
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('Floors')
ax.set_ylabel('Bedrooms')
ax.set_zlabel('prices')
#fun.plt.show()
"""
