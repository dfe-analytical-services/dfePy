import dfe_functions
#print dfe_functions.add_two_nums(3,6)

# read csv
#data1 = dfe_functions.read_csv("../dummy_data/MakeModel2016.csv")

# read bulk csv
data2 = dfe_functions.read_csv_bulk('../dummy_data/bulk/')

# read_sql_table
#print dfe_functions.read_sqltable("3DCPRI-PDB16\ACSQLS","SWFC_Project","_MCcpd")
#data = dfe_functions.read_sqltable("3DCPRI-PDB16\ACSQLS","SWFC_Project","_MCcpd")


# create package
dfe_functions.create_project('./','test')