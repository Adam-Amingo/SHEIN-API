import numpy as np
import matplotlib.pyplot as plt

#Generate a simple data
np.random.seed(42)
X = np.linspace(0,10,50)
true_m , true_c = 2,1 
y_true = true_m * X + true_c + np.random.normal(0, 2, X.shape)


#Initializing the parameters
m , c = 0.0 , 0.0 
learning_rate= 0.01
iterations = 1500 

#store loss for plotting 
loss_history = []

#calculate the gradient descent
for i in range(iterations):
    #prediction
    y_pred = m * X + c

    #compute gradient
    m_grad = (-2 / len(X))* np.sum(X * (y_true - y_pred))
    c_grad = (-2 / len(X))* np.sum(y_true - y_pred)

    #update paramters 
    m = m - learning_rate * m_grad
    c = c - learning_rate * c_grad

    #compute loss
    loss = np.mean((y_true - y_pred)**2)
    loss_history.append(loss)

    #print updates every 100 iterations
    if i % 100 == 0 :
        print(f"Iteraion {i}: Loss = {loss: .4f} , m = {m: .4f} , c = {c: .4f}")
    

#print final parameters
print(f"final parameters : m = {m: .4f} , c = {c: .4f}")

#plot the dataset and the fitted line
plt.figure(figsize= (10 , 6))
plt.scatter(X , y_true ,label = "Data point" , color = "red")
plt.title("Gradient Descent : Line Fitting")
plt.xlabel("X")
plt.ylabel("y_true")
plt.legend()
plt.show()