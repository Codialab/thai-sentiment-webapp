from keras.models import model_from_json
from keras.models import Sequential
from keras.layers import Dense, LSTM , Embedding , TimeDistributed , Lambda , Flatten
from keras.layers import Conv1D , Bidirectional , Input , Dropout
from keras.layers import MaxPooling1D , Activation 
from keras.models import Model
import numpy as np

def classify(X):
    
    with open('./model/wongnai_architecture_3class.json', 'r') as f:
        model = model_from_json(f.read())
    model.load_weights('./model/wongnai_weights_3class.h5')
    
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    y_pred = model.predict(X)
    y_pred_class = np.argmax(y_pred , axis = 1)
    
    import keras.backend as K
    K.clear_session()
    
    return y_pred_class