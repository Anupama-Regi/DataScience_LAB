from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

X,y=load_iris(return_X_y=True)

xtrain,xtest,ytrain,ytest=train_test_split(X,y,test_size=0.5,random_state=0)
gnb=GaussianNB()
ypred=gnb.fit(xtrain,ytrain).predict(xtest)
print(ypred)
sample=[[5,5,4,5]]
ynew=gnb.fit(xtrain,ytrain).predict(sample)
print(ynew)

from sklearn import metrics
print("Accuracy : ",metrics.accuracy_score(ytest,ypred))