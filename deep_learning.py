import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras import layers, models, initializers, regularizers, Model

#%% Importando o modelo VGG16 e retirando a última camada 

model_transfered = VGG16()
#flat1 = layers.Flatten(name='flatten_custom')(model_transfered.layers[-2].output)
class1 = layers.Dense(1024, activation='relu', name='dense_custom')(model_transfered.layers[-2].output)
output = layers.Dense(8, activation='softmax', name='out_custom')(class1)

model = Model(inputs=model_transfered.inputs, outputs=output)

print(model.summary())

#%% Congelando as primeiras camadas e habilitando somente as 4 últimas para treinamento
for layers in model.layers:
    layers.trainable = False
    
model.get_layer('fc1').trainable = True
model.get_layer('fc2').trainable = True
model.get_layer('dense_custom').trainable = True
model.get_layer('out_custom').trainable = True
#%% Compilando o modelo

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#%% Criando datagenerator

from tensorflow.keras.preprocessing.image import ImageDataGenerator

batch_size = 64

datagen = ImageDataGenerator(rescale=1./255,
                             horizontal_flip=True,
                             preprocessing_function=preprocess_input)

train_it = datagen.flow_from_directory('/content/drive/My Drive/trabalho_PI/progressive_data/train', class_mode='categorical', batch_size=batch_size, target_size=(224,224))
test_it = datagen.flow_from_directory('/content/drive/My Drive/trabalho_PI/progressive_data/test', class_mode='categorical', batch_size=batch_size, target_size=(224,224))
val_it = datagen.flow_from_directory('/content/drive/My Drive/trabalho_PI/progressive_data/validation', class_mode='categorical', batch_size=batch_size, target_size=(224,224))

#%% Treinando na GPU

with tf.device('/gpu:0'):
  model.fit(train_it,
            batch_size=batch_size,
            epochs=20,
            steps_per_epoch=4359//batch_size,
            validation_data=val_it,
            validation_steps=541//batch_size)
  
#%% Somente se já tiver os pesos salvos

model.load_weights('/content/drive/My Drive/trabalho_PI/progressive_data/trabalho.h5')
  
#%% Medindo resultados no test

acc = model.evaluate(test_it)[1]
print(acc)

#%% Printando a matriz de confusão

# Isso somente é necessário para setar o shuffle=False e não bugar a matriz
test_it = datagen.flow_from_directory('/content/drive/My Drive/trabalho_PI/progressive_data/test', class_mode='categorical', batch_size=batch_size, target_size=(224,224))

import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

Y_pred = model.predict(test_it)
y_pred = np.argmax(Y_pred, axis=1)
print('Confusion Matrix')
print(confusion_matrix(test_it.classes, y_pred))
print('Classification Report')
target_names = ['Águia', 'Urso', 'Cougar', 'Lobo', 'Corvo', 'Raposa', 'Sea Lions', 'Seals']
print(classification_report(test_it.classes, y_pred, target_names=target_names))