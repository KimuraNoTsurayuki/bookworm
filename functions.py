import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

area = "area (m^2)"
price = "price($)"
bedrooms = "bedrooms"
floor = "floor"
location = "address"
rooms = "rooms"
date = "date" 

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
	for index,point in enumerate(pure_data):
		res_list.append(int(point[bedrooms]))
	res = np.array(res_list)
	return res

def createFloorData(pure_data):
	res_list = []
	for index,point in enumerate(pure_data):
		if (point[floor] != ''):
			to_shorten = point[floor]
			to_add = to_shorten[0:to_shorten.find("/")]
			res_list.append(int(to_add))
		else:
			print(f"Floor not added at point {index}")
	res = np.array(res_list)
	return res
	
def createRoomData(pure_data):
	res_list = []
	for index,point in enumerate(pure_data):
		res_list.append(int(point[rooms]))
	res = np.array(res_list)
	return res

def createLocationData(pure_data):
	res_list = []
	for index,point in enumerate(pure_data):
		if(point[location] != ""):
			res_list.append(point[location])
		else:
			print(f"Location not added at point {index}")
	return res_list
	
def createDateData(pure_data):
	res_list = []
	for index,point in enumerate(pure_data):
		if(point[date] != ""):
			res_list.append(point[date])
		else:
			print(f"Date not added at point {index}")
	return res_list

def filterPriceByArea(pure_data,val):
	res_list = []
	for index,point in enumerate(pure_data):
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
		if(float(point[area]) == val):
			res.append(point)
	return res
	
def filterDataByPrice(pure_data, val):
	res = []
	for point in pure_data:
		if(float(point[price]) <= val):
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
			p = prices[i]
			a = areas[i]
			res_list.append(np.round(p/a,2))
	return np.array(res_list)



def takeNatLog(data):
	return np.log(data)


	
def arrayOfArrays(*args):
	a = []
	for index, val in enumerate(args):
		a.append(val) 
	return np.asarray(a)



def dataPerPoint(*args):
	res = []
	for i in range(0,len(args[0])):
		temp = np.empty(len(args))
		for j in range(0,len(args)):	
			temp[j] = args[j][i]
		res.append(temp)
	return np.asarray(res)



def predictedValues(point_mat, b0, b_vec):
	res = np.empty(len(point_mat))	
	for i, point in enumerate(point_mat):
		pred_price = b0
		for index,  (val_point,val_b) in enumerate(zip(point, b_vec)):
			pred_price += val_point*val_b
		res[i] = pred_price
	return res


	
def calculateMSE(arr1,arr2):
	res = 0
	for index, (val1,val2) in enumerate(zip(arr1,arr2)):
		res += ((val1-val2)**2)/len(arr1)
	return res

def getAmountOf(data,prop,val1,val2):
	n = 0
	for point in data:
		if(data[prop] >= val1 and data[prop] < val2):
			n = n + 1
	return n	
	
def getLowestPrice(data):
	res = 0
	for index,price in enumerate(data):
		if(index == 0):
			res = int(price)
		elif(res > int(price)):
			res = int(price)
	return res
	
def getHighestPrice(data):
	res = 0
	for index,point in enumerate(data):
		if(index == 0):
			res = point[price]
		elif(res < point[price]):
			res = point[price]
	return res
	
def getPercentile(data, p):
	return np.percentile(data,p)
#-----------------------------

def testLinearModel(point_mat, vals):
	reg = linear_model.LinearRegression()
	reg.fit(point_mat,vals)
	b0 = reg.intercept_
	b_vec = reg.coef_
	r2 = reg.score(point_mat,vals)
	res = (b0,b_vec,r2)
	return res

def testPolynomialModel(point_mat, vals, degree = 3):
	poly_features = PolynomialFeatures(degree=degree, include_bias=False)
	X_Poly = poly_features.fit_transform(point_mat)
	reg = linear_model.LinearRegression(positive = True)
	reg.fit(X_Poly, vals)
	b0 = reg.intercept_
	b_vec = reg.coef_
	r2 = reg.score(X_Poly,vals)
	res = (reg,b0,b_vec,r2)
	return res
	
