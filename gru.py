# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 22:42:41 2020

    INPUT TO NN: (FINAL VECTOR, PSEDUOLOG RETURN) OF T, T-1, T-2
    TOTAL INPUTS: 27
    OUTPUT OF NN:  PREDICTED PSEUDOLOG RETURN T+1 USED TO SOLVE FOR PREDICTED AVG PRICE T+1
    TOTAL OUTPUTS:1
    NN ARCHITECTURE: 
    5 hidden layers - 27 22 17 11 6 1 neurons, tahn AF in cells, LINEAR IN OUTPUT
    GATED RECURRENT UNIT NEURAL NETWORK

Total trainable parameters  11,100 
Total training time  100.55 s (200 epochs)
Total time per prediction  57.75 µs
    TRAINING: MEAN SQUARE ERROR LOSS FN, ADAM

x[t] = input vector
h[t] = output/hidden vector
z[t] = update gate activation
r[t] = reset gate activation

w[t] = weight matrix for input vector (3: update, hidden, reset)
u[t] = weight matrix for output/hidden vector(3: update, hidden, reset)
b[t] = bias (3: update, hidden, reset)

@author: mecap
"""
import numpy as np
import math


x = np.random.uniform(low=-5, high=5, size=(27))
h1 = np.zeros(22)
y1 = np.zeros(22)

#layer 1 computation
wz1 = np.random.uniform(low=-5, high=5, size=(27,22))
wr1 = np.random.uniform(low=-5, high=5, size=(27,22))
wh1 = np.random.uniform(low=-5, high=5, size=(27,22))
uz1 = np.random.uniform(low=-5, high=5, size=(22,22))
ur1 = np.random.uniform(low=-5, high=5, size=(22,22))
uh1 = np.random.uniform(low=-5, high=5, size=(22,22))
bz1 = np.random.uniform(low=-5, high=5, size=(22))
br1 = np.random.uniform(low=-5, high=5, size=(22))
bh1 = np.random.uniform(low=-5, high=5, size=(22))

sigz1 = np.matmul(x,wz1) + np.matmul(h1, uz1) + bz1
z1 = np.zeros(len(sigz1))
for i in range(0,len(sigz1)):
    z1[i] = 1 / (1 + math.exp(-1* sigz1[i]))
    
sigr1 = np.matmul(x, wr1) + np.matmul(h1, ur1) + br1
r1 = np.zeros(len(sigr1))
for i in range(0, len(sigr1)):
    r1[i] = 1 / (1 + math.exp(-1 * sigr1[i]))
    
sigh1 = np.matmul(x, wh1) + np.matmul(uh1, np.multiply(r1, h1)) + bh1
hyph1 = np.zeros(len(sigh1))
for i in range(0, len(sigh1)):
        hyph1[i] = math.tanh(sigh1[i])
h1 = np.multiply((1-z1), h1) + np.multiply(z1, hyph1)

y1 = h1

#layer 2 computation
wz2 = np.random.uniform(low=-5, high=5, size=(22,17))
wr2 = np.random.uniform(low=-5, high=5, size=(22,17))
wh2 = np.random.uniform(low=-5, high=5, size=(22,17))
uz2 = np.random.uniform(low=-5, high=5, size=(17,17))
ur2 = np.random.uniform(low=-5, high=5, size=(17,17))
uh2 = np.random.uniform(low=-5, high=5, size=(17,17))
bz2 = np.random.uniform(low=-5, high=5, size=(17))
br2 = np.random.uniform(low=-5, high=5, size=(17))
bh2 = np.random.uniform(low=-5, high=5, size=(17))

sigz2 = np.matmul(x,wz1) + np.matmul(h1, uz1) + bz1
z1 = np.zeros(len(sigz1))
for i in range(0,len(sigz1)):
    z1[i] = 1 / (1 + math.exp(-1* sigz1[i]))
    
sigr1 = np.matmul(x, wr1) + np.matmul(h1, ur1) + br1
r1 = np.zeros(len(sigr1))
for i in range(0, len(sigr1)):
    r1[i] = 1 / (1 + math.exp(-1 * sigr1[i]))
    
sigh1 = np.matmul(x, wh1) + np.matmul(uh1, np.multiply(r1, h1)) + bh1
hyph1 = np.zeros(len(sigh1))
for i in range(0, len(sigh1)):
        hyph1[i] = math.tanh(sigh1[i])
h1 = np.multiply((1-z1), h1) + np.multiply(z1, hyph1)

y = h1