from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

train_url = 'data.csv'
train = pd.read_csv(train_url)

# Fill missing values with mean column values in the test set
train.fillna(train.mean(), inplace=True)

train[["X", "Y"]].groupby(['X'], as_index=False).mean().sort_values(by='Y', ascending=False)

#print(train.info())


#lets convert X which is nominal to numerical value :D
labelencoding = LabelEncoder()
labelencoding.fit(train['X'])
train['X'] = labelencoding.transform(train['X'])


X=np.array(train.drop(['subject'],axis=1))

############## AWESOME after playing with the data lets create the model :)

kmeans = KMeans(n_clusters=2,max_iter=25, random_state=0).fit(X)
print(kmeans.labels_)
print(kmeans.cluster_centers_)