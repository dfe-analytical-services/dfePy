# -*- coding: utf-8 -*-
# module of files for creating an analytical project
# use Python naming convention
# https://www.python.org/dev/peps/pep-0008/#naming-conventions
import os

#Func to set up reproducible workflow folder structure
def create_project(path,proj_name):
    baseDir = path + proj_name
    folder_list = ["doc","tests",proj_name]
    for f in folder_list:
        os.makedirs(os.path.join(baseDir,f))#, exist_ok = True)
