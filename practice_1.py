import numpy as np 
import matplotlib.pyplot as plt

t=np.linspace(1, 100, 100)
a=0.5
position=(a*t**2)/2

position_noise=position+np.random.normal(0, 120, size=(t.shape[0])) #制造噪音
plt.plot(t, position, label='actual position')
plt.plot(t, position_noise, label='measured position')
#plt.show()

# 初始位置=测量位置
predicts=[position_noise[0]]
position_predict=predicts[0]

predict_var=0
odo_var=120**2 #自行设定的位置测量仪器方差，越大测量值占比越低
v_std=50 #测量仪器的方差
for i in range(1, t.shape[0]): 
    dv=(position[i]-position[i-1])+np.random.normal(0, 50) #模拟IMU惯性传感器读取的速度
    position_predict=position_predict+dv #利用上个时刻的位置和速度预测当前位置
    predict_var+=v_std**2 #更新预测数据的方差

    position_predict = position_predict*odo_var/(predict_var+odo_var)+position_noise[i]*predict_var/(predict_var + odo_var)
    predict_var = (predict_var * odo_var)/(predict_var + odo_var)**2
    predicts.append(position_predict)
plt.plot(t, predicts, label='kalman filtered position')

plt.legend()
plt.show()
