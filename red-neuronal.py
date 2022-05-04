# pip install numypy
import numpy as np 

# definimos la función sigmoid
def sigmoid(z):
  return 1.0/(1 + np.exp(-z))

# Defenimos la función para calcular el error
def loss(y, y_hat):
  loss = y - y_hat
  return float(loss)

# Calcular los nuevos pesos
def calculateWeight(myXs,ws1,ws2,ws3, error):  
  dw1 = ws1 + (0.5 * error * myXs[0]) 
  dw2 = ws2 + (0.5 * error * myXs[1])  
  dw3 = ws3 + (0.5 * error * myXs[2])  

  return dw1, dw2, dw3

def calculateZ(Xs, Ws):
  z = 0

  for i, j in enumerate(Xs):
    z = z + Xs[i] * Ws[i]

  return z

def funcBipolar(y_hat):
  if y_hat >= 0:
    return 1
  else:
    return -1

def train(X, y, Ws, isSigmoid):
  # X --> Input.
  # y --> true/target value.
        
  # m-> number of training examples
  # n-> number of features 
  m, n = X.shape
    
  # Reshaping y.
  y = y.reshape(m,1)

  dw1 = Ws[0]
  dw2 = Ws[1]
  dw3 = Ws[2]

  for epoch in range(m):
    myXs = X[epoch]
    
    z = calculateZ(myXs, Ws)

    # Calculating hypothesis/prediction.
    if isSigmoid == 1: 
      y_hat = sigmoid(z)
    else:
      y_hat = funcBipolar(z)

    newError = loss(y[epoch], y_hat)

    # Calcular nuevos pesos
    print("-----------------")
    print("MyXs:", myXs)
    print("Y:", y[epoch])
    print("w1:", dw1)
    print("w2:", dw2)
    print("w3:", dw3)
    print("Z:", z)
    print("f(x):", y_hat)
    print("New Error:", newError)
    dw1, dw2, dw3 = calculateWeight(myXs,dw1, dw2, dw3, newError)
    
    Ws[0] = dw1
    Ws[1] = dw2
    Ws[2] = dw3
    
    print("dw1:", dw1)
    print("dw2:", dw2)
    print("dw3:", dw3)
    print("-----------------")

  # returning weights
  return dw1, dw2, dw3

def predict(X, y, Ws, isSigmoid):   
  # X --> Input.
  m, n = X.shape
  
  y = y.reshape(m,1)

  # Calculating presictions/y_hat.
  for epoch in range(m):
    myXs = X[epoch]
    
    z = calculateZ(myXs, Ws)

    # Calculating hypothesis/prediction.
    if isSigmoid == 1: 
      y_hat = sigmoid(z)
    else:
      y_hat = funcBipolar(z)

    print("y hat: ", y_hat)
    print("y: ", y[epoch])

# Calcular la precisión 
def accuracy(y, y_hat):
  accuracy = np.sum(y == y_hat) / len(y)
  return accuracy

"""
5	9.5 -> -1
5	2   -> 1 
7	3   -> 1
3	7   -> -1
3.5	9 -> -1

"""

# X = np.array([[5.0, 9.5, 1], 
#               [5.0,2.0 ,1], 
#               [7.0,3.0, 1],
#               [3.0,7.0, 1], 
#               [3.5,9.0, 1]])

X = np.array([[5.0, 9.5, 1], 
              [4.0, 7.8, 1], 
              [6.0, 7.5, 1],
              [2.0, 1.5, 1], 
              [1.0, 3.0, 1]])
              

# y = np.array([-1, 1, 1, -1, -1])
y = np.array([-1, -1, -1, 1, 1])

X_test = np.array([[6.0, 2, 1], [2.0,5.0, 1]])
y_test = np.array([1, -1])

# Pesos iniciales
initWs = np.array([1,2,3])

# Bit para indicar si utilizamos la función de actiavción sigmoid o bipolar
isSigmoid = 0

# Training 
w1_train, w2_train, w3_train = train(X, y, initWs, isSigmoid)

Ws_train = [w1_train,w2_train,w3_train]

print("---- Predicción ----")
predict(X_test, y_test, Ws_train, isSigmoid)