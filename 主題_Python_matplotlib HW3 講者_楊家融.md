# 主題:Python/matplotlib HW3 講者:楊家融
###### tags: `Python` `Matplotlib` `Numpy`

```
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
    A=ax.scatter(x=[0.4, 0.6, 0.65, 0.8], 
               y=[0.44, 0.43, 0.5, 0.75], 
               s=[10, 20, 30, 40], # size
               c=[0.3, 0.6, 0.9, 1.0], # scores for colormap
               cmap='viridis')
    
    
    # Plot the data
    yield ax
    
    
    
    title = ax.get_title()
    ax.set_title(title)


fig = plt.figure(figsize=(6, 6))

```