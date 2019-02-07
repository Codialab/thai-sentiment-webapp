import util
from model import classify
import numpy as np

def classsification(file_dir):
    
    X = util.preprocessing(file_dir)
    y_pred =classify(X)
	
    class0 = 0
    class1 = 0
    class2 = 0
	
    for k in y_pred:
        if k == 0:
            class0 += 1 
        elif k == 1:
            class1 += 1 
        elif k == 2:
            class2 += 1
  
    return class0,class1,class2