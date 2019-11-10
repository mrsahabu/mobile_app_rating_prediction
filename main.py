# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 01:38:33 2018

@author: Muhammad
"""

import sys
import pandas as pd
import numpy
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from sklearn import preprocessing
import pickle
path="E:\\Parhaii\\Semester 7\\Machine Learing\\Project\\"
Ui_MainWindow, QtBaseClass = uic.loadUiType(path+'Gui\\gui.ui')

       
class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.predict)
    
    def predict(self):
        
        cat = self.ui.text_cat.toPlainText()
        cot = self.ui.text_cot.toPlainText()
        gen = self.ui.text_genres.toPlainText()
        size = int(self.ui.text_size.toPlainText())
        ver = float(self.ui.text_ver.toPlainText())
        type1 = self.ui.text_type.toPlainText()
        data = [('Category', [cat]),
         ('Size', [size]),
         ('Type', [type1]),
         ('Content_Rating', [cot]),
         ('Genres', [gen]),
         ('Android_Ver', [ver])
         ]
        
        df = pd.DataFrame.from_items(data)

        catlabelEncoder = preprocessing.LabelEncoder()
        typelabelEncoder = preprocessing.LabelEncoder()
        cotlabelEncoder = preprocessing.LabelEncoder()
        genlabelEncoder = preprocessing.LabelEncoder()

        try:
            path =  'E:\\Parhaii\\Semester 7\\Machine Learing\\Project\\'
            model = pickle.load(open(str(path+'Model\\classfier.sav'), 'rb'))
            catlabelEncoder.classes_ = numpy.load(str(path +'Encoders\\catlabelEncoder.npy'))
            genlabelEncoder.classes_ = numpy.load(str(path +'Encoders\\genlabelEncoder.npy'))
            typelabelEncoder.classes_ = numpy.load(str(path +'Encoders\\typelabelEncoder.npy'))
            cotlabelEncoder.classes_ = numpy.load(str(path +'Encoders\\cotlabelEncoder.npy'))
        except Exception as e:
                print('ERROR!: '+ str(e))




#        catlabelEncoder.fit(df['Category'])
#        typelabelEncoder.fit(df['Type'])
#        cotlabelEncoder.fit(df['Content Rating'])
#        genlabelEncoder.fit(df['Genres'])

        df['Category'] = catlabelEncoder.transform(df['Category'])
        df['Type'] = typelabelEncoder.transform(df['Type'])
        df['Content_Rating'] = cotlabelEncoder.transform(df['Content_Rating'])
        df['Genres'] = genlabelEncoder.transform(df['Genres'])
        y = model.predict(df)
        y=round(y,2)
        self.ui.result.setText("Predicted Rating: " + str(y))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())