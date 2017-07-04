# -*- coding: utf-8 -*-
import numpy as np
import scipy.io as sio

# Cargar archivos .mat que contienen las variables u1 y u2
u1_mat = sio.loadmat('u1.mat')
u2_mat = sio.loadmat('u2.mat')

# Guardar variables u1 y u2 (coordenadas de los puntos en las imágenes)
u1 = u1_mat['u1']
u2 = u2_mat['u2']

# print "u1:", u1
# print "u2:", u2
# print u1[0,1]
