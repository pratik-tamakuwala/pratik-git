#Identifying the species of iris specimen
#
#Evaluate the performnce of decision tree
#KNN and random forest on iris dataset
#

#Importing the iris dataset and storing it into a dataframe:
import pandas as pd
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
data = pd.DataFrame(iris.data, columns=[iris.feature_names])
data = data.assign(target=pd.Series(iris.target))
print(data)


# Performing train test split onto the data:
X=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)


# Training the data with the decision tree classifier:
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)

from sklearn.metrics import(classification_report,confusion_matrix)
print('---- Train Performance: Decision tree -------------------')
y_pred=clf.predict(X_train)
print(confusion_matrix(y_train,y_pred))
print(classification_report(y_train,y_pred))
from sklearn.metrics import accuracy_score
a=accuracy_score(y_pred, y_train)
print(a)
print('---- Test Performance:Decision tree --------------------')
y_pred = clf.predict(X_test) 
print(confusion_matrix(y_test, y_pred)) 
print(classification_report(y_test, y_pred))
b=accuracy_score(y_pred, y_test)
print(b)


# 
# Precision: It is the ratio of correctly predicted positive observations to the total predicted positive observations.
# 
# Recall: Itis the ratio of correctly predicted positive observations to the all observations in actual class.
# 
# F1 Score: It is the weighted average of Precision and Recall. Therefore, this score takes both false positives and false negatives into account. Intuitively it is not as easy to understand as accuracy, but F1 is usually more useful than accuracy, especially if you have an uneven class distribution. 
# 
# Accuracy:It is simply a ratio of correctly predicted observation to the total observations. It is the most intuitive performance measure.
# 
# The above Train and Test Performance Report shows that:
# It gives 100% accuracy on training data and about 97.7% accuracy on test data which is quite good.

# Applying KNN classifier on the dataset with one neighbour:
from sklearn.neighbors import KNeighborsClassifier
neigh_1 = KNeighborsClassifier(n_neighbors=1)
neigh_1.fit(X_train, y_train)

print('---- Train Performance: one neighbour -------------------')
y_pred=neigh_1.predict(X_train)
print(confusion_matrix(y_train,y_pred))
print(classification_report(y_train,y_pred))
from sklearn.metrics import accuracy_score
a=accuracy_score(y_pred, y_train)
print(a)
print('---- Test Performance: one neighbour --------------------')
y_pred = neigh_1.predict(X_test) 
print(confusion_matrix(y_test, y_pred)) 
print(classification_report(y_test, y_pred))
b=accuracy_score(y_pred, y_test)
print(b)


# The above Train and Test Performance Report shows that:
# It gives 100% accuracy on training data and about 97.7% accuracy on test data.

# Applying KNN classifier on the dataset with ten neighbours:
from sklearn.neighbors import KNeighborsClassifier
neigh_10 = KNeighborsClassifier(n_neighbors=10)
neigh_10.fit(X_train, y_train)

print('---- Train Performance: ten neighbours -------------------')
y_pred=neigh_10.predict(X_train)
print(confusion_matrix(y_train,y_pred))
print(classification_report(y_train,y_pred))
from sklearn.metrics import accuracy_score
a=accuracy_score(y_pred, y_train)
print(a)

print('---- Test Performance: ten neighbours --------------------')
y_pred = neigh_10.predict(X_test) 
print(confusion_matrix(y_test, y_pred)) 
print(classification_report(y_test, y_pred))
b=accuracy_score(y_pred, y_test)
print(b)


# The above Train and Test Performance Report shows that:
# It gives 97% accuracy on training data and about 97.7% accuracy on test data.

# Applying KNN classifier on the dataset with twenty neighbours:
from sklearn.neighbors import KNeighborsClassifier
neigh_20 = KNeighborsClassifier(n_neighbors=20)
neigh_20.fit(X_train, y_train)

print('---- Train Performance: twenty neighbours -------------------')
y_pred=neigh_20.predict(X_train)
print(confusion_matrix(y_train,y_pred))
print(classification_report(y_train,y_pred))
from sklearn.metrics import accuracy_score
a=accuracy_score(y_pred, y_train)
print(a)

print('---- Test Performance: twenty neighbours --------------------')
y_pred = neigh_20.predict(X_test) 
print(confusion_matrix(y_test, y_pred)) 
print(classification_report(y_test, y_pred))
b=accuracy_score(y_pred, y_test)
print(b)


# The above Train and Test Performance Report shows that:
# It gives 96% accuracy on training data and about 97.7% accuracy on test data.

# Applying KNN classifier on the dataset with fifty neighbours:
from sklearn.neighbors import KNeighborsClassifier
neigh_50 = KNeighborsClassifier(n_neighbors=50)
neigh_50.fit(X_train, y_train)

print('---- Train Performance: fifty neighbours -------------------')
y_pred=neigh_50.predict(X_train)
print(confusion_matrix(y_train,y_pred))
print(classification_report(y_train,y_pred))
from sklearn.metrics import accuracy_score
a=accuracy_score(y_pred, y_train)
print(a)

print('---- Test Performance: fifty neighbours --------------------')
y_pred = neigh_50.predict(X_test) 
print(confusion_matrix(y_test, y_pred)) 
print(classification_report(y_test, y_pred))
b=accuracy_score(y_pred, y_test)
print(b)


# The above Train and Test Performance Report shows that:
# It gives 92% accuracy on training data and about 91% accuracy on test data.

# Applying KNN classifier on the dataset with eighty neighbours:
from sklearn.neighbors import KNeighborsClassifier
neigh_80 = KNeighborsClassifier(n_neighbors=80)
neigh_80.fit(X_train, y_train)

print('---- Train Performance: eighty neighbours -------------------')
y_pred=neigh_80.predict(X_train)
print(confusion_matrix(y_train,y_pred))
print(classification_report(y_train,y_pred))
from sklearn.metrics import accuracy_score
a=accuracy_score(y_pred, y_train)
print(a)

print('---- Test Performance: eighty neighbours --------------------')
y_pred = neigh_80.predict(X_test) 
print(confusion_matrix(y_test, y_pred)) 
print(classification_report(y_test, y_pred))
b=accuracy_score(y_pred, y_test)
print(b)


# The above Train and Test Performance Report shows that:
# It gives 79% accuracy on training data and about 64% accuracy on test data.
# 
# It is quite evident that as the number of neighbours increases, the model's performance decreases. With 80 neighbours it gives the worst results. This is because,as we increase the number of data points contributing to the label of our new data point, we take into account points that are less and less similar to the new data point. 

# Applying Random forest classifier to the training data:
from sklearn.ensemble import RandomForestClassifier
random_clf = RandomForestClassifier(n_estimators=10)
random_clf.fit(X_train, y_train)

print('---- Train Performance: random classifier -------------------')
y_pred=random_clf.predict(X_train)
print(confusion_matrix(y_train,y_pred))
print(classification_report(y_train,y_pred))
from sklearn.metrics import accuracy_score
c=accuracy_score(y_pred, y_train)
print(c)
print('---- Test Performance: random classifier --------------------')
y_pred = random_clf.predict(X_test) 
print(confusion_matrix(y_test, y_pred)) 
print(classification_report(y_test, y_pred))
d=accuracy_score(y_pred, y_test)
print(d)


# The above Train and Test Performance Report shows that:
# It gives 99% accuracy on training data and about 97% accuracy on test data.
# 
# The results imply that the Random Forest model does not perform as good as the Decision tree classifier on the given dataset. This maybe because the Random forest technique fails to accurately select the one best tree which would give 100% accuracy.
