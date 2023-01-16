#Import Required Libraries
import random
import pickle

#Import Neural Network Module Functions
from custom_neural_net_creator.model import Model
from custom_neural_net_creator.dense import Dense
from custom_neural_net_creator.activation_layer import ActivationLayer
from custom_neural_net_creator.activation_functions import relu, relu_derivative, sigmoid, sigmoid_derivative
from custom_neural_net_creator.loss_functions import mean_squared_error, mean_squared_error_derivative

#Import Variables
f = open('model.pckl', 'rb')
model = pickle.load(f)
f.close()

f = open('scaler.pckl', 'rb')
scaler = pickle.load(f)
f.close()

f = open('Y_test.pckl', 'rb')
Y_test = pickle.load(f)
f.close()

f = open('X_test.pckl', 'rb')
X_test = pickle.load(f)
f.close()



def generate_data():
    random_index = random.randint(0,len(X_test)-1)
    actual = Y_test[random_index][0]

    inversed = scaler.inverse_transform([X_test[random_index][0]])[0]
    inversed = [float("{:.8f}".format(float(i))) for i in inversed]

    return (inversed, actual)

def get_prediction(inputs):
    inputs = scaler.transform([inputs])
    return model.predict([[inputs]])[0][0][0][0] * 100
