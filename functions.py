import numpy as np

area = "area (m^2)"
price = "price($)"
address = "address"

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

def filterPriceByArea(pure_data,val):
	res_list = []
	for point in pure_data:	
		if (float(point[area]) == val):
			res_list.append(int(point[price]))
	return np.array(res_list)

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
