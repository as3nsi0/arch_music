# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 23:13:40 2017

@author: Victor
"""

import os
import shutil

# This functions remove directory and generate with the directory 
def makeDirectory(directory):
    if(os.path.exists(directory)):
        shutil.rmtree(directory)
    os.mkdir(directory)