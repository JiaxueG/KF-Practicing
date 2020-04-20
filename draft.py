import numpy as np 
import matplotlib.pyplot as plt 

t=np.linspace(1, 100, 100)
a=0.5
position=(a*t**2)/2 

position_noise=position+np.random.normal(0, 120, size=(t.shape[0]))
plt.plot(t, position, label='actual position')
plt.plot(t, position_noise, label='measured position')

# the 1st prediction uses measured value
predicts=[position_noise[0]]
position_predict=predicts[0]

predict_var=0 # GPS
odo_var = 120**2  # location sensor
v_std=50 # velocity sensor
for i in range(1, t.shape[0]): 
    dv=(position[i]-position[i-1])+np.random.normal(0, 50)
    position_predict=position_predict+dv
    predict_var=predict_var+v_std**2 
    # Kalman
    position_predict=position_predict*odo_var/(predict_var+odo_var)+position_noise[i]*predict_var/(predict_var+odo_var)
    predict_var = (predict_var*odo_var)/(predict_var + odo_var)**2
    predicts.append(position_predict)

plt.plot(t, predicts, label='kalman filtered position')

plt.legend()
plt.show()
