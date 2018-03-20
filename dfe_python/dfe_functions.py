def add_two_nums(x,y):
	return x + y;

#Func to join CSVs together
#import csv #
import pandas as pd
import os

def read_csv(filename):
    df = pd.read_csv(filename)
    return df
#Considered using builtin Pyhon module csv    
#    with open(filename) as csvDataFile:
#        csvReader = csv.DictReader(csvDataFile) # allows col names to be preserved
#        for row in csvReader:
#            print(row)
##    return csvReader

def read_csv_bulk(path):
    files = os.listdir(path)
    result = pd.concat((pd.read_csv(path + f) for f in files), ignore_index = True)
    
    #DO WE NEED TO CONSIDER AXIS AS AN ARGUMENT?
    
#    result = pd.DataFrame()
#    for filename in files:
#        result = result.append(read_csv(path + filename), ignore_index = True)
    return result
    
#Func to call in an SQL table
#import pandas as pd
import pymssql

def read_sqltable(SQLserver,SQLdbname,SQLtablename):
    conn = pymssql.connect(server=SQLserver, database=SQLdbname)  
    data = pd.read_sql("SELECT * FROM " + SQLtablename,conn)
#    data = pd.read_sql("SELECT TOP 1000 * FROM _MCcpd",conn)
    return data;


#Func to set up reproducible workflow folder structure
def create_project(path,proj_name):
    baseDir = path + proj_name
    folder_list = ["data","code"]
    for f in folder_list:
        os.makedirs(os.path.join(baseDir,f), exist_ok = True)