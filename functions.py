import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

area = "area (m^2)"
price = "price($)"
bedrooms = "bedrooms"
floor = "floor"
location = "address"

def selectDataPointByIndex(data,index):
	return data[index]

def createPriceData(pure_data):
	res_list = []
	for point in pure_data:
		res_list.append(int(point[price]))
	res = np.array(res_list)
	return res
	
def createAreaData(pure_data):
	res_list = []
	for point in pure_data:
		res_list.append(float(point[area]))
	res = np.array(res_list)
	return res

def createBedroomData(pure_data):
	res_list = []
	for point in pure_data:
		res_list.append(int(point[bedrooms]))
	res = np.array(res_list)
	return res

def createFloorData(pure_data):
	res_list = []
	for point in pure_data:
		if (point[floor] != ''):
			to_shorten = point[floor]
			to_add = to_shorten[0:to_shorten.find("/")]
			res_list.append(int(to_add))
	res = np.array(res_list)
	return res

def filterPriceByArea(pure_data,val):
	res_list = []
	for point in pure_data:	
		if (float(point[area]) >= val):
			res_list.append(int(point[price]))
	return np.array(res_list)

def filterAreaByPrice(pure_data,val):
	res_list = []
	for point in pure_data:	
		if (float(point[price]) >= val):
			res_list.append(int(point[area]))
	return np.array(res_list)
	
def filterPriceByLocation(pure_data,val):
	res_list = []
	for point in pure_data:	
		if (point[location].find(val) != -1):
			res_list.append(int(point[price]))
	return np.array(res_list)
	
def filterAreaByLocation(pure_data,val):
	res_list = []
	for point in pure_data:	
		if (point[location].find(val) != -1):
			res_list.append(float(point[area]))
	return np.array(res_list)

def filterDataByLocation(pure_data,val):
	res = []
	for point in pure_data:
		if(point[location].find(val) != -1):
			res.append(point)
	return res

def filterDataByArea(pure_data, val):
	res = []
	for point in pure_data:
		if(float(point[area]) >= val):
			res.append(point)
	return res
			

def createQuantifiableData(pure_data):
	res = dict()
	res.update({price: createPriceData(pure_data)})
	res.update({area: createAreaData(pure_data)})
	return res

def calculateStdDev(rev_data,index = 0):
	return np.std(rev_data, index)
	
"""
def findDataPoints(data, **kwargs):
	res = []
	for kwarg in kwargs:
		for point in data:
			
	return res
"""
def getPrices(data):
	res_list = []
	for point in data:
		res_list.append(int(point[price]))
	return np.array(res_list)

def getLocations(data):
	res= []
	for point in data:
		res.append(point[address])
	return res

def getAreas(data):
	res_list = []
	for point in data:
		res_list.append(float(point[area]))
	return np.array(res_list)

def calculateMeanAverage(ls):
	return np.round(np.mean(ls),2)
	
def calculateMedianAverage(ls):
	return np.median(ls)
		
	
def getSQMeterPriceData(prices,areas):
	res_list = []
	lp = len(prices)
	la = len(areas)
	if(lp == la):
		for i in range(0,len(prices)):
			p = float(prices[i])
			a = float(areas[i])
			res_list.append(np.round(p/a,2))
	return np.array(res_list)


def takeNatLog(data):
	return np.log(data)

def calculateB1(data1, data2):
	b1 = 0
	den = 0
	num = 0
	avg1 = calculateMeanAverage(data1)
	avg2 = calculateMeanAverage(data2)
	for index, (val1, val2) in enumerate(zip(data1, data2)):
		num += (val1 - avg1)*(val2 - avg2)
		den += (val1 - avg1)**2
	b1 = num/den
	return b1
	
def calculateB0(data_mat, val_vec,b_vec):
	b0 = calculateMeanAverage(val_vec)
	for index, (val_mat, val_b) in enumerate(zip(data_mat,b_vec)):
		b0 = b0 - val_b*(calculateMeanAverage(val_mat))
	return b0
	
def arrayOfArrays(*args):
	a = []
	for index, val in enumerate(args):
		a.append(val) 
	return np.asarray(a)

def calculateBVector(mat, vals):
	mat_avgs = np.empty(len(mat))
	c1 = 0
	c2 = 0
	for index, val in enumerate(mat):
		mat_avgs[index] = calculateMeanAverage(val)
	val_avg = (calculateMeanAverage(vals))
	b_vec = np.empty(len(mat))
	for j, (val_avg_x, vec_x) in enumerate(zip(mat_avgs, mat)):
		for i, (val_x, val_y) in enumerate(zip(vec_x,vals)):
			c1 += (val_y - val_avg)*(val_x - val_avg_x)
			c2 += (val_avg_x - val_x)**2
		b_vec[j] = c1/c2
		c1 = 0
		c2 = 0
	return b_vec
	
