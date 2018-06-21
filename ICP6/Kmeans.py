import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

#reading sample stock excel file using pand library
X = pd.read_csv(r'C:\Users\mural\Downloads\Python_Lesson6\Python_Lesson6\sample_stocks.csv',dtype={"dividend": float, "returns": int})

#converting excel data into array
X= np.array(X)

#using kmeans and assigning  values to cluster
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_
colors = ["g.","r.","c.","y."]
# Create an empty array
distortions = []
for i in range(len(X)):
    #print("coordinate:",X[i], "label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

    # USing elbow method to find the accurate cluster: calculating Sum of squared errors
    distortions.append(sum(np.min(cdist(X, centroids, 'euclidean'), axis=1)) / X.shape[0])

plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 5)
#plt.show()

# Plot the elbow
plt.plot(X, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()