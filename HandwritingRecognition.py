# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:08:33 2016

@author: JS
"""

"""
This is a example (Handwriting Digit Recognition) by use keras.
"""
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
#from keras.

model = Sequential()

model.add(Dense(input_dim=28*28,output_dim=500))
model.add(Activation('sigmoid'))

model.add(Dense(output_dim=500))
model.add(Activation('sigmoid'))

model.add(Dense(output_dim=10))
model.add(Activation('softmax'))

#mse(Mean Square Error)计算预测值与真值的均方差
#𝑤 ←𝑤−𝜂𝜕𝐿𝜕𝑤  lr=𝜂=0.1
model.compile(loss='mse',optimizer=SGD(lr=0.1),metrices=['accuracy'])
#Training data(Images):x_train,Labels(digits):y_train
model.fit(x_train,y_train,batch_size=100,nb_epoch=20)

score = model.evaluate(x_test.y_test)
print('Total loss on Testing set:',score[0])
print('Accuracy of Testing set:',score[1])

result = model.predict(x_test)




















