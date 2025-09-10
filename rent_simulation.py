import basereader as br
import functions as fn
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

data_sale = br.makeData("/home/aleksandre/clicker/Yanagihara_databases/sale/new/database_2025-09-03_10:33:43_sale_Vake_3_1_1000000_1_1000filtered.json")
data_rent = br.makeData("/home/aleksandre/clicker/Yanagihara_databases/rent/database_2025-09-03_10:56:19_rent_Vake_3_1_10000_1_1000filtered.json")

empirical_rent_prices = fn.createPriceData(data_rent)
empirical_rent_area = fn.createAreaData(data_rent)
empirical_rent_bedrooms = fn.createBedroomData(data_rent)
empirical_rent_floors = fn.createFloorData(data_rent)
empirical_rent_rooms = fn.createRoomData(data_rent)
empirical_rent_locations = fn.createLocationData(data_rent)
empirical_rent_data = fn.createDateData(data_rent)
point_mat = fn.dataPerPoint(empirical_rent_area,empirical_rent_floors,empirical_rent_rooms,empirical_rent_bedrooms)
rent_empirical = fn.testPolynomialModel(point_mat,empirical_rent_prices,6)

sale_prices = fn.createPriceData(data_sale)
sale_area = fn.createAreaData(data_sale)
sale_bedrooms = fn.createBedroomData(data_sale)
sale_floors = fn.createFloorData(data_sale)
sale_rooms = fn.createRoomData(data_sale)
sale_locations = fn.createLocationData(data_sale)
sale_data = fn.createDateData(data_sale)
point_mat_sale = fn.dataPerPoint(sale_area,sale_floors,sale_rooms,sale_bedrooms)
poly_features = PolynomialFeatures(degree=6, include_bias=False)

sale_empirical = fn.testPolynomialModel(point_mat_sale,sale_prices,6)

X_Poly = poly_features.fit_transform(point_mat_sale)
rent_predicted = rent_empirical[0].predict(X_Poly)
ARI_array = []
for index,(value_rent, value_sale) in enumerate(zip(rent_predicted,sale_prices)):
	ARI_array.append(value_rent*1200/value_sale)
	
#--------------------------------------------------------
X_Poly_rent = poly_features.fit_transform(point_mat)
sale_predicted = sale_empirical[0].predict(X_Poly_rent)
ARI_rent_property_array = []
for index,(value_rent,value_sale) in enumerate(zip(empirical_rent_prices,sale_predicted)):
	ARI_rent_property_array.append(value_rent*1200/value_sale)
	#print(value_rent)
	#print(value_sale)
#print(rent_predicted)
#--------------------------------------------------------
X_Poly_sale = poly_features.fit_transform(point_mat_sale)
sale_price_predicted = sale_empirical[0].predict(X_Poly_sale)
ARI = []
for index,(rents,sales) in enumerate(zip(rent_predicted,sale_price_predicted)):
	ARI.append(rents*1200/sales)
premium = []
for index,(G,g) in enumerate(zip(ARI_array,ARI)):
	premium.append(G/g)
	print(premium[-1])
print(fn.calculateMedianAverage(premium))
	
