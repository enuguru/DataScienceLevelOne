
import pandas as pd

import numpy as np

 

dataMatrix = [(65,75,74,73,95,76,62,100),(101,102,103,107,157,160,191,192)];

        

dataFrame = pd.DataFrame(data=dataMatrix);

kurt = dataFrame.kurt(axis=1);

print("Data:");

print(dataFrame);

print("Kurtosis:");

print(kurt);

  

dataMatrix = [(70,90,90,100,120,120,100,121,125,115,112),

                        (58.22,39.33,-30.44,36.77,20.80,-73.95,-39.99,91.03,-138.01,-20,None)];

               

dataFrame = pd.DataFrame(data=dataMatrix);

kurt = dataFrame.kurt(axis=1);

print("Data:");

print(dataFrame);

print("Kurtosis:");

print(kurt);
