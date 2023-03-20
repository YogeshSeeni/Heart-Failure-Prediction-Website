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

def get_inputs(inputs):
    age = int(inputs[0])
    rbp = int(request.form["rbp"])
    cholesterol = int(request.form["sc"])
    fastingBS = int(request.form["fbs"])
    maxHR = int(request.form["mhr"])
    oldPeak = float(request.form["op"])
    sex = inputs[1]
    chestPain = inputs[2]
    restingECG = request.form["restingECG"]
    exerciseAngina = request.form["eia"]
    stSlope = request.form["stSlope"]
    inputs = [age, rbp, cholesterol, fastingBS, maxHR, oldPeak, "Normal", "ST", "ATA", "NAP", "TA", "Y", "Flat", "Up", "M"]




import csv

with open('heart.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            inputs = row
            for i in range(len(inputs)):
                if inputs[i] == sex or inputs[i] == chestPain or inputs[i] == restingECG or inputs[i] == exerciseAngina or inputs[i] == stSlope:
                    inputs[i] = 1

            for i in range(len(inputs)):
                if type(inputs[i]) == str:
                    inputs[i] = 0
            inputs = [float(x) for x in inputs]
            print(inputs)
