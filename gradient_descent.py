# We need m(coeficent) = 2 and b(intercept) = 3
import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0 # Initialize the value of m and b to 0
    iteration = 1000 # Initialize the iteration (how many times we iterate for getting best fit line)
    n = len(x) 
    learning_rate = 0.08 # Initialize the LR it will tell how much steps you need to go you can assume any value you need to change according to try and error
    for i in range(iteration):
        y_predict = m_curr * x + b_curr # Predict the y value
        cost = (1/n) * sum([val**2 for val in (y-y_predict)]) # Calculate error cost
        md = -(2/n)*sum(x*(y-y_predict)) # Calculate the derivative of m
        bd = -(2/n)*sum(y-y_predict) # Calculate the derivative of b
        m_curr = m_curr - learning_rate * md # Calculate the value of m
        b_curr = b_curr - learning_rate * bd # Calculate the value of b
        print(f"M : {m_curr}, B : {b_curr}, cost : {cost}, iteration {i}")

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)