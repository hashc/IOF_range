# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 11:34:50 2016

@author: chc
"""


def transform_txt_matrix(filename,sp=',',perturbation=0):
	"""
	transform txt into matrix
	name1 \t name2 \t num
	…\t …\t …
	"""
	import numpy as np
	with open(filename,'rt') as f:
		txt=f.read()
	info= txt.split('\n')[:-1]
	name_dict={}
	name_list=[]
	num=0
	for item in info:
		temp=item.split(sp)
		temp1=temp[0]
		temp2=temp[1]
		if temp1 not in name_dict:
			name_dict[temp1]=num
			name_list.append(temp1)
			num+=1
		if temp2 not in name_dict:
			name_dict[temp2]=num
			name_list.append(temp1)
			num+=1
	matrix=np.zeros((num,num))
	for item in info:
		temp=item.split(sp)
		temp1=temp[0]
		temp2=temp[1]
		temp3=temp[2]
		matrix[name_dict[temp1],name_dict[temp2]]=float(temp3)+perturbation
	return matrix,name_list

def IOF_martix(matrix,way='forward'):
	"""
	if way is 'forward'
	B[i,j]=x[i,j]/X^j
	-------------------------------------
	if way is 'backward'
	B[i,j]=x[i,j]/X_i

	"""
	import numpy as np
	n=len(matrix)
	IOF_mat=np.zeros((n,n))
	if way=='forward':
		row_sum=np.sum(matrix,axis=1)
		for j in range(0,n):
			if row_sum[j]:
				IOF_mat[:,j]=matrix[:,j]/row_sum[j]
	if way=='backward':
		col_sum=np.sum(matrix,axis=0)
		for i in range(0,n):
			if col_sum[i]:
				IOF_mat[i,:]=matrix[i,:]/col_sum[i]
	return IOF_mat

def max_eigenvalue(matrix,types='sparse',perturbation=0.001):
	"""
	find largest eigenvalue of matrix
	"""
	import scipy
	import numpy as np
	import scipy.sparse.linalg
	matrix=matrix+np.eye(len(matrix))
	if types=='sparse':
		sp_matrix=scipy.sparse.coo_matrix(matrix)
	eig_value=scipy.sparse.linalg.eigs(sp_matrix,k=1, return_eigenvectors=False)
	eig_value=float(eig_value[0].real)-1
	return eig_value

def IOF_range(matrix,name_list):
	import copy
	n=len(matrix)
	#ev_0=max_eigenvalue(matrix,types='sparse')
	ev_0=1
	iof={}
	for i in range(0,n):
		print(i+1,'/',n)
		temp_matrix=copy.deepcopy(matrix)
		temp_matrix[i,:]=0
		temp_matrix[:,i]=0
		temp_ev=max_eigenvalue(temp_matrix,types='sparse')
		iof[name_list[i]]=ev_0-temp_ev
	from operator import itemgetter
	iof_range=sorted(iof.items(), key=itemgetter(1), reverse=True)
	return iof_range














