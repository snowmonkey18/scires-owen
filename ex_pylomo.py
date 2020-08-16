from local_models.local_models import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

X_train = np.linspace(0,6,100).reshape(-1,2)
y_train = np.sin(X_train) + np.random.normal(loc=0,scale=0.3,size=X_train.shape)
y_train = y_train.flatten()
X_test = np.linspace(-1,7,1000).reshape(-1,2)

kernel = GaussianKernel(bandwidth = 1.)
LOESS = LocalModels(sklearn.linear_model.LinearRegression(), kernel=kernel)
LOESS.fit(X_train,y_train) # This just builds an index and stores x and y

y_pred = LOESS.predict(X_test) # This makes local predictions at these various points
model_features = LOESS.transform(X_test) 
# model_features is a (X_test.shape[0], X_test.shape[1] + 1) shaped array, containing the coefficients of the
# various independent variables and also the intercept of the individual local models

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs=X_test[:,0], ys=X_test[:,1], zs=y_pred)
ax.plot_wireframe(X=X_test[:,0], Y=X_test[:,1], Z=y_pred, rstride=5, cstride=5)
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)