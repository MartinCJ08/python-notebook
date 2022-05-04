import numpy as np

Xt = np.array([[ 1, 1, 1], 
               [-1, 1,-1], 
               [-1, 1,-1] 
              ])

Xo = np.array([[ 1, 1, 1], 
               [ 1,-1, 1], 
               [ 1, 1, 1] 
              ])

Xx = np.array([[ 1,-1, 1], 
               [-1, 1,-1], 
               [ 1,-1, 1] 
              ])


def matrixToVector(x):
  #x is a matrix
  m = x.shape[0]*x.shape[1]
  tmp1 = np.zeros(m)

  c = 0
  for i in range(x.shape[0]):
    for j in range(x.shape[1]):
      tmp1[c] = x[i,j]
      c +=1
  return tmp1

def vectXTrans(v):
  temp = np.zeros([len(v),len(v)])
 
  for i in range(len(v)):
    for j in range(len(v)):
      temp[i][j] = v[i] * v[j]
  return temp

def createW(x):
  # x is a vector
  if len(x.shape) != 1:
    print ("The input is not vector")
    return
  else:
    w = np.zeros([len(x),len(x)])
    for i in range(len(x)):
      for j in range(i,len(x)):
        if i == j:
          w[i,j] = 0
        else:
          w[i,j] = x[i]*x[j]
          w[j,i] = w[i,j]
  return w

def getFx(v):
  fx = np.zeros(len(v))

  for i in range(len(v)):
    if v[i] <= 0:
      fx[i] = -1
    else: 
      fx[i] = 1

  return fx
          
def isConvergent(v, weight, debug = 0):
  salida = v.dot(weight)
  fx = getFx(salida)

  if debug == 1:
    print("--------- Convergencia ---------")
    print("Vector:\n",v)
    print("Producto Cruz:\n",salida)
    print("F(x):\n",fx)
  
  for i in range(len(v)):
    if v[i] != fx[i]:
      return False
  return True

print("--------- Muestra 1 --------")
v1 = matrixToVector(Xt)
w1 = createW(v1)
print("Vector: ", v1)
print(w1)

print("--------- Muestra 2 ---------")
v2 = matrixToVector(Xo)
w2 = createW(v2)
print("Vector: ", v2)
print(w2)

print("--------- Muestra 3 --------")
v3 = matrixToVector(Xx)
w3 = createW(v3)
print("Vector: ", v3)
print(w3)

# W4 = W1 + W2 + W3
print("--------- W4 --------")
w4 = w1 + w2 + w3

print(w4)


# no debe converger 
test1 = np.array([[-1, 1, 1], 
                  [-1, 1,-1], 
                  [-1, 1,-1] 
                 ])

# debe converger 
test2 = np.array([[ 1, 1,-1], 
                  [-1, 1,-1], 
                  [-1, 1,-1] 
                 ])


tv1 = matrixToVector(test1)

if isConvergent(tv1, w4, 1) == True:
  print("Es convergente")
else: 
  print("No es convergente")

z = vectXTrans(v1)
print(z)