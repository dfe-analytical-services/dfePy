from dfe_python import import_data as dfe1

# Create a CSV import function
importCSV = dfe1.DataImport('dummy_data/bulk/')

print importCSV.files
print importCSV.path
data1 = importCSV.read_bulk(importCSV.path)

# read csv
data2 = dfe1.read_csv("dummy_data/bulk/dummy1.csv")

# read bulk csv
data3 = dfe1.read_csv_bulk('dummy_data/bulk/')

# read_sql_table
data4 = dfe1.read_sqltable("3DCPRI-PDB16\ACSQLS","SWFC_Project","[dbo].[ExternalData_Edubase_StandardExtract_20170814]")



from dfe_python import setup_project as dfe2
# create package
dfe2.create_project('./','testproj')



from dfe_python import proxy_connect as dfe3
# connect to proxy
dfe3.connect_to_proxy('echang','../../password.txt')