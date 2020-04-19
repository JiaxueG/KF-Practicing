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

def mileagePrediction(v, a, t): 
    result=v*t+0.5*a*t**2
    return result

def Kalman(prediction, sensor, Kn):  # prediction and sensor are data
    result = (1-Kn)*prediction+Kn*sensor
    return result


if __name__ == "__main__":
    x_actual=list(range(-100, 100))
    y_actual=[]
    y_measured=[]
    y_predicted=[]
    y_kalman=[]
    prediction_var=0.1
    odo_var=0.9
    for i in x_actual: 
        y_actual.append(makeCurve(1, -2, 1000, i))
        y_measured.append(addNoise(makeCurve(1, -2, 1000, i), 350))
        # Kalman
        y_predicted.append(y_measured[len(y_measured)-1]-y_measured[len(y_measured)-2]+y_measured[-1])
        Kn = KnCalculate(prediction_var, odo_var)
        y_kalman.append(y_predicted[-1]*(1-Kn)+y_measured[-1]*Kn)
        # Kn1 = odo_var/(prediction_var + odo_var)
        # Kn2 = prediction_var/(prediction_var + odo_var)
        # y_kalman.append(y_predicted[-1]*Kn1+y_measured[-1]*Kn2)
        prediction_var = (prediction_var * odo_var) / (prediction_var + odo_var)**2

    plt.plot(x_actual, y_actual, label='actual')
    plt.plot(x_actual, y_measured, 'ro', markersize=1, label='measured')
    plt.plot(x_actual, y_predicted, label='predicted')
    plt.plot(x_actual, y_kalman, label='kalman')
    
    plt.legend()
    plt.show()
