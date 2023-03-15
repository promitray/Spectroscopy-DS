Assume that the dataset has a linear pattern. Estimate a linear line that fits the data best. 
Mean squared error - estimate squared errors for all points and then average over all points. Minimize it. 

Gradient descent:
Loss function - derivative with respect to weight and bias
How many points will you have per y : linear regression 1
                                      multiple linear regression n (number of independent features)


Gradient of MSE with respect to weight(s) and bias: minimize the loss function 
Update the parameters in the direction of gradient (partial derivative with respect to each of the variables)
w = w - (lr * partial derivative)
same with b

Steps:

Training:
1. Initialize weight as zero
2. bias as zero

Given a data point: 
1. Predict result from a hypothesis 
2. Get the mean error over the whole training batch
3. Use gradient descent to get new weight, new bias
4. Repeat till you have minimized your loss function