# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 23:12:05 2020

@author: felip
"""
## IN
#   |_resized_img
#         |_class1
#           |_ images        
#       |_class2
#           |_ images       

## OUT
#   |progressive_data
#       |_train
#         |_class1
#         |_class2
#       |_test
#         |_class1
#         |_class2
#       |_validation
#         |_class1
#         |_class2
import os
import numpy as np
#import shutil

from skimage import io

_percentage_cut_w = .2
_percentage_cut_h = .2

#copia o arquivo para a pasta correta
def save_arq(path, path_img, arqs):
    for arq in arqs:
        #shutil.copy(path_img+arq, path+arq)
        img = io.imread(path_img+arq)
        w,h,r = img.shape
        _p_w = int(w*_percentage_cut_w)
        _p_h = int(h*_percentage_cut_h)
        img = img[_p_w:w-_p_w,_p_h:h-_p_h,:]
        io.imsave(path+arq, (img).astype('uint8'))
        

        
_percentage_train = .8
_percentage_test = .1 
_percentage_validation = .1

_path_resized_img = 'resized_img/'
_progressive_data = 'progressive_data/'

folders = os.listdir(_path_resized_img)

for folder in folders:
    _path_img = _path_resized_img+folder+'/'
    arqs = os.listdir(_path_img)
    arqs = np.array(arqs)
    #Seperar de forma aleatoria 
    _shape_arqs = arqs.shape[0]
    indices = np.arange(_shape_arqs)
    rng = np.random.RandomState(123)
    # para não separar de forma aleatoria permuted_indices = indices
    permuted_indices = rng.permutation(indices)
    
    train_size, test_size, valid_size = int(_percentage_train * _shape_arqs), int(_percentage_test*_shape_arqs), int(_percentage_validation*_shape_arqs)
    _train_ind = permuted_indices[:train_size]
    _test_ind = permuted_indices[train_size:(train_size + test_size)]
    _valid_ind = permuted_indices[(train_size + test_size):(train_size + test_size+valid_size)]
    
    #Separa os arquivos para cada categoria
    train, test, validation = arqs[_train_ind], arqs[_test_ind], arqs[_valid_ind]
    
    #cria a pasta para salvar 
    _path_train = _progressive_data+'train/'+folder+'/'
    save_arq(_path_train, _path_img, train)
    
    _path_test = _progressive_data+'test/'+folder+'/'
    save_arq(_path_test, _path_img, test)
    
    _path_validation = _progressive_data+'validation/'+folder+'/'
    save_arq(_path_validation, _path_img, validation)