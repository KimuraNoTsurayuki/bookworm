import numpy as np
import json
import basereader as br
import functions as fun

name = "../clicker/databases/database_1_1_3_100000_110000_40_45.json"
data = []

br.setDatabaseName(name)
br.makeData(br.getDatabaseName())
data = br.exportData()


print(fun.getPrices(data))
print(fun.calculateMedianAverage(fun.getPrices(data)))
print(fun.calculateMeanAverage(fun.getPrices(data)))
print(fun.calculateStdDev(fun.getPrices(data)))
print(fun.filterPriceByArea(data,43))
print(fun.calculateMeanAverage(fun.filterPriceByArea(data,43)))
print(fun.calculateStdDev(fun.filterPriceByArea(data,43)))
