import json

data = str()
database = str()

def setDatabaseName(name):
	global database
	database = name
	
def getDatabaseName():
	return database

def makeData(db):
	with open(db, 'r') as file:
    		global data 
    		data = json.load(file)
    
def exportData():
	return data


