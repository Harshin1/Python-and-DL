from sklearn.svm import SVC
from sklearn import datasets

# Loading the dataset
irisdataset = datasets.load_iris()

# getting the data and response of the dataset
x = irisdataset.data
y = irisdataset.target

# fitting RBF kernel SVM    
model = SVC(kernel='rbf', C=1, gamma=2)
model.fit(x, y)
print(model.predict([[7, 2, 3, 4], [2, 3, 4, 5]]))

print(model.score(x, y))