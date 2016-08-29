#-------------------------------------------------------------------------------
# coding=utf8
# Name:        模块1
# Purpose:
#
# Author:      zhx
#
# Created:     19/05/2016
# Copyright:   (c) zhx 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
def main():
    traindata = open("trainnew.txt")
    testdata  = open("testnew.txt")
    traindata.readline() # 跳过第一行
    testdata.readline()
    train = np.loadtxt(traindata)
    test = np.loadtxt(testdata)
    X = train[0:4628,0:27]
    y = train[0:4628,27]
    test_x = test[0:1437,0:27]
    test_y = test[0:1437,27]

    model1 = LinearSVC()
    model2 = LogisticRegression()
    model3 = GaussianNB()
    model4 = RandomForestClassifier()
    model5 = KNeighborsClassifier()
    model1.fit(X,y)
    model2.fit(X,y)
    model3.fit(X,y)
    model4.fit(X,y)
    model5.fit(X,y)
    predicted1 = model1.predict(test_x)
    predicted2 = model2.predict(test_x)
    predicted3 = model3.predict(test_x)
    predicted4 = model4.predict(test_x)
    predicted5 = model5.predict(test_x)
    classname = ['popular','not_popular']
    print "1 Svm-linear"
    print(classification_report(test_y,predicted1))#,classname))
    print "2 Logistci regression"
    print(classification_report(test_y,predicted2))#,classname))
    print "3 NB - gaussian"
    print(classification_report(test_y,predicted3))#,classname))
    print "4 Random Forest"
    print(classification_report(test_y,predicted4))#,classname))
    print "5 KNN"
    print(classification_report(test_y,predicted5))#,classname))
main()

