# module of files for import_data
# use Python naming convention
# https://www.python.org/dev/peps/pep-0008/#naming-conventions
import pandas as pd
import os
import pymssql

class DataImport(object):
    """ A class for functions which import data. Functions have the following properties:
        
    Attributes:
        path: current pathname
        files: name of file
    
    """
    

    
    def __init__(self,path):
        ''' Constructor for this class. '''
        #
        self.path = path
        self.files = os.listdir(path)
        
    def read_bulk(self, path):
        files = os.listdir(path)
        result = pd.concat((pd.read_csv(path + f) for f in files), ignore_index = True)
        return result

#Func to join CSVs together
#import csv #
#import pandas as pd
#import os

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
    
    #SHOULD WE CONSIDER AXIS AS AN ARGUMENT?
    
#    result = pd.DataFrame()
#    for filename in files:
#        result = result.append(read_csv(path + filename), ignore_index = True)
    return result
    
#Func to call in an SQL table


def read_sqltable(SQLserver,SQLdbname,SQLtablename):
    if SQLdbname.isalnum():
        return("server name parmaeter must contain backslash")
    
    conn = pymssql.connect(server=SQLserver, database=SQLdbname)  
    data = pd.read_sql("SELECT * FROM " + SQLtablename,conn)
#    data = pd.read_sql("SELECT TOP 1000 * FROM _MCcpd",conn)
    return data;


    

