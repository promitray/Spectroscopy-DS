from sklearn import datasets
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from lr import LinearRegression
import numpy as np

def mse(y_test, y_predictions):
    return np.mean((y_test - y_predictions) ** 2)

#X, y = datasets.make_regression(n_samples=100, n_features=1, noise = 20, random_state = 4)
X, y = datasets.make_regression(n_features = 2, noise = 20 )
#print (X, y)

fig = plt.figure()

print (X.shape)
print (y.shape)

plt.scatter (X[:, 0], y)
plt.savefig('test.png')

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 1234)

reg = LinearRegression()
reg.fit(X_train, y_train)

predictions = reg.predict(X_test)


 
print (predictions)
print (y_test) 
print (mse(y_test, predictions ))