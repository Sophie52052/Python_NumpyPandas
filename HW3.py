# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

 

import numpy as np
import matplotlib.pyplot as plt
from contextlib import contextmanager
@contextmanager

def myplot(fig, subplot, size=5):
    ax = fig.add_subplot(subplot)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel('Precision')
    ax.set_ylabel('Recall')
    ax.grid(True)
    
    F1=np.arange(0.1,1,0.1)
    for F1_score in F1:
        p=np.sort(np.random.rand(1000)) #也可用 np.arange(0.1,1,0.001)
        r=F1_score*p/((2*p)-F1_score)
        ax.plot(p[r>0],r[r>0],color='blue',alpha=0.2)    
        plt.text(1.01,r[-1],'F={:0.1f}'.format(F1_score),color='gray')
    
    
    yield ax # Plot the data
    
    title = ax.get_title()
    ax.set_title(title)

fig = plt.figure(figsize=(6, 6))

with myplot(fig, 111) as ax:
     # plot the data
    ax.scatter(x=[0.4, 0.6, 0.65, 0.8], 
               y=[0.44, 0.43, 0.5, 0.75], 
               s=[10, 20, 30, 40], # size
               c=[0.3, 0.6, 0.9, 1.0], # scores for colormap
               cmap='viridis')

    # set the title
    ax.set_title('Precision, Recall, and F1')
    
    


