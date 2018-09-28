from sklearn.svm import LinearSVC
from sklearn import datasets

# Loading the dataset
irisdataset = datasets.load_iris()

# getting the data and response of the dataset
x = irisdataset.data
y = irisdataset.target

# fit Linear SVM model
model = LinearSVC(random_state=0)
model.fit(x, y)
print(model.predict([[7, 2, 3, 4], [2, 3, 4, 5]]))

print(model.score(x, y))