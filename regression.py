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

    model1 =  svm.SVR()
    model1.fit(X,y)
    predicted1 = model1.predict(test_x)
    for i in xrange(10):
        print predicted1[i]


main()

