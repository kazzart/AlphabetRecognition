import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
from RandomSample import imgToArray
model = tf.keras.Sequential()
model.add(layers.Dense(100, activation='relu', input_shape=(784,)))
model.add(layers.Dense(50, activation='relu'))
model.add(layers.Dense(17, activation='sigmoid'))

optimizer = tf.train.GradientDescentOptimizer(0.2)

model.compile(loss='binary_crossentropy', optimizer=optimizer)

#model.summary()
order = []
def generateTrain(qua, path = "learn"):
    from RandomSample import Rand,take_a_pic
    s = Rand(qua,path)
    order = s.getObjs()
    imgNext = s.next
    if s.notEmpty():
        image, num = imgNext()
        X1, y1 = take_a_pic(image, num,len(order))
        X_train = np.array([X1]).T
        y_train = np.array([y1]).T
    while(s.notEmpty()):
        image, num = imgNext()
        X1, y1 = take_a_pic(image, num,len(order))
        X2 = np.array([X1]).T
        y2 = np.array([y1]).T
        X_train = np.concatenate((X_train, X2), axis = 1)
        y_train = np.concatenate((y_train, y2), axis = 1)
    return X_train/255,y_train
a,b = generateTrain(50)
print(a.shape)
print(b.shape)
dataset = tf.data.Dataset.from_tensor_slices((a.T,b.T))
dataset = dataset.batch(128).repeat()
val_dataset = tf.data.Dataset.from_tensor_slices((a.T,b.T))
val_dataset = val_dataset.batch(32).repeat()
model.fit(dataset, epochs=20, steps_per_epoch=300,
          validation_data=val_dataset,
          validation_steps=3)
data = imgToArray("D:\learn_c1.jpg").T
result = model.predict(data, batch_size=32)
print(result)