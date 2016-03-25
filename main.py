# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 18:48:50 2016

@author: chc
"""
from iof_lib import *
import scipy
filename='./io.txt'
matrix,name_list=transform_txt_matrix(filename,sp=',',perturbation=0)
way_name='forward'
IOF_mat=IOF_martix(matrix,way=way_name)
iof_range=IOF_range(IOF_mat,name_list)
with open('range_'+way_name+'.txt','wt') as f:
	for item in iof_range:
		f.write(item[0]+'\t'+str(item[1])+'\n')
