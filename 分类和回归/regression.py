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
from sklearn.linear_model import LinearRegression
from sklearn import tree

def main():
    traindata = open("trainreg.txt")
    testdata  = open("testnew.txt")
    traindata.readline() # 跳过第一行
    testdata.readline()
    train = np.loadtxt(traindata)
    test = np.loadtxt(testdata)
    #X = train[0:4628,0:27]
    #y = train[0:4628,27]
    X = train[20:4628,0:27]
    y = train[20:4628,27]
    #test_x = test[0:1437,0:27]
    test_x = test[0:15,0:27]
    test_y = test[0:1437,27]

    model1 =  LinearRegression()
    model2 = tree.DecisionTreeRegressor()
    model1.fit(X,y)
    model2.fit(X,y)
    opt_which = 6
    tmp = test_x[opt_which,0] 
    predicted2 = model2.predict(test_x)
    p = predicted2[opt_which]
    res = tmp
    for i in range(1,3):
        test_x[opt_which,0] = tmp+i
	p1 = model2.predict(test_x)
	if p<p1[opt_which]:
	    res = tmp+i 
	    p = p1[opt_which]	
	test_x[opt_which,0] = tmp-i
	p2 = model2.predict(test_x)
	if p<p2[opt_which]:
	    res = tmp-i 
	    p = p2[opt_which]	
    print "initial len of title: " ,tmp
    print "better len of title: ", res
    test_x[opt_which,0]=res 
    predicted2 = model2.predict(test_x)
    res = test_x[opt_which,3]
    tmp = test_x[opt_which,3]
    for i in range(7):
        test_x[opt_which,3] = tmp+i
	p1 = model2.predict(test_x)
	if p<p1[opt_which]:
	    res = tmp+i 
	    p = p1[opt_which]	
	test_x[opt_which,3] = tmp-i
	p2 = model2.predict(test_x)
	if p<p2[opt_which]:
	    res = tmp-i 
	    p = p2[opt_which]	
    print "initial num of pic: " ,tmp
    print "better num of pic: ", res
    test_x[opt_which,3]=res 
    predicted2 = model2.predict(test_x)
    res = test_x[opt_which,5]
    tmp = test_x[opt_which,5]
    for i in range(60):
        test_x[opt_which,5] = tmp+i
	p1 = model2.predict(test_x)
	if p<p1[opt_which]:
	    res = tmp+i 
	    p = p1[opt_which]	
	test_x[opt_which,5] = tmp-i
	p2 = model2.predict(test_x)
	if p<p2[opt_which]:
	    res = tmp-i 
	    p = p2[opt_which]	
    print "initial public time " ,tmp
    print "better public time ", res


main()

