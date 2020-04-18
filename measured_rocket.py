import numpy as np 
import matplotlib.pyplot as plt 

noise=np.random.normal()
def addNoise(target, scale): 
    result=np.random.normal(target, scale)
    return result

def makeCurve(a, b, c, x): 
    y=-(a*x**2+b*x)+c
    return y

def KnCalculate(prediction, sensor): # prediction and sensor are accuracy
    Kn=sensor/(prediction+sensor)
    return Kn

def Kalman(prediction, sensor, Kn): # prediction and sensor are data
    result=(1-Kn)*prediction+Kn*sensor
    return result

if __name__ == "__main__":
    x=list(range(-100, 100))
    y=[]
    for i in x: 
        y.append(addNoise(makeCurve(1, -2, 1000, i), 200))
    plt.plot(x, y, 'ro', markersize=1)
    plt.show()
