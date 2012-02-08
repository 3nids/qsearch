# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_editsearch.ui'
#
# Created: Wed Feb  8 11:40:45 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_editSearch(object):
    def setupUi(self, editSearch):
        editSearch.setObjectName(_fromUtf8("editSearch"))
        editSearch.resize(398, 363)
        editSearch.setWindowTitle(QtGui.QApplication.translate("editSearch", "qSearch", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_2 = QtGui.QGridLayout(editSearch)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(editSearch)
        self.label.setText(QtGui.QApplication.translate("editSearch", "Search name", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.searchName = QtGui.QLineEdit(editSearch)
        self.searchName.setText(QtGui.QApplication.translate("editSearch", "new search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchName.setObjectName(_fromUtf8("searchName"))
        self.gridLayout_2.addWidget(self.searchName, 1, 1, 1, 1)
        self.frame = QtGui.QFrame(editSearch)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.searchField = QtGui.QComboBox(self.frame)
        self.searchField.setObjectName(_fromUtf8("searchField"))
        self.gridLayout.addWidget(self.searchField, 0, 0, 1, 1)
        self.searchOperator = QtGui.QComboBox(self.frame)
        self.searchOperator.setObjectName(_fromUtf8("searchOperator"))
        self.searchOperator.addItem(_fromUtf8(""))
        self.searchOperator.setItemText(0, QtGui.QApplication.translate("editSearch", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.searchOperator.addItem(_fromUtf8(""))
        self.searchOperator.setItemText(1, QtGui.QApplication.translate("editSearch", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.searchOperator.addItem(_fromUtf8(""))
        self.searchOperator.setItemText(2, QtGui.QApplication.translate("editSearch", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.searchOperator.addItem(_fromUtf8(""))
        self.searchOperator.setItemText(3, QtGui.QApplication.translate("editSearch", "text search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchOperator.addItem(_fromUtf8(""))
        self.searchOperator.setItemText(4, QtGui.QApplication.translate("editSearch", "text equals", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout.addWidget(self.searchOperator, 0, 2, 1, 1)
        self.searchValue = QtGui.QLineEdit(self.frame)
        self.searchValue.setObjectName(_fromUtf8("searchValue"))
        self.gridLayout.addWidget(self.searchValue, 0, 3, 1, 1)
        self.searchAdd = QtGui.QToolButton(self.frame)
        self.searchAdd.setText(QtGui.QApplication.translate("editSearch", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.searchAdd.setObjectName(_fromUtf8("searchAdd"))
        self.gridLayout.addWidget(self.searchAdd, 0, 4, 1, 1)
        self.searchBool = QtGui.QComboBox(self.frame)
        self.searchBool.setMaximumSize(QtCore.QSize(75, 16777215))
        self.searchBool.setObjectName(_fromUtf8("searchBool"))
        self.searchBool.addItem(_fromUtf8(""))
        self.searchBool.setItemText(0, QtGui.QApplication.translate("editSearch", "IS", None, QtGui.QApplication.UnicodeUTF8))
        self.searchBool.addItem(_fromUtf8(""))
        self.searchBool.setItemText(1, QtGui.QApplication.translate("editSearch", "IS NOT", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout.addWidget(self.searchBool, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 3)
        self.columnView = QtGui.QColumnView(editSearch)
        self.columnView.setObjectName(_fromUtf8("columnView"))
        self.gridLayout_2.addWidget(self.columnView, 3, 0, 1, 3)
        self.progressBar = QtGui.QProgressBar(editSearch)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_2.addWidget(self.progressBar, 5, 0, 1, 3)
        self.saveButton = QtGui.QPushButton(editSearch)
        self.saveButton.setText(QtGui.QApplication.translate("editSearch", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.gridLayout_2.addWidget(self.saveButton, 1, 2, 1, 1)
        self.selectButton = QtGui.QPushButton(editSearch)
        self.selectButton.setText(QtGui.QApplication.translate("editSearch", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.selectButton.setObjectName(_fromUtf8("selectButton"))
        self.gridLayout_2.addWidget(self.selectButton, 4, 2, 1, 1)
        self.searchButton = QtGui.QPushButton(editSearch)
        self.searchButton.setText(QtGui.QApplication.translate("editSearch", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.gridLayout_2.addWidget(self.searchButton, 4, 0, 1, 1)
        self.closeButton = QtGui.QPushButton(editSearch)
        self.closeButton.setText(QtGui.QApplication.translate("editSearch", "close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout_2.addWidget(self.closeButton, 6, 2, 1, 1)
        self.label_2 = QtGui.QLabel(editSearch)
        self.label_2.setText(QtGui.QApplication.translate("editSearch", "Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.layerName = QtGui.QLineEdit(editSearch)
        self.layerName.setEnabled(False)
        self.layerName.setObjectName(_fromUtf8("layerName"))
        self.gridLayout_2.addWidget(self.layerName, 0, 1, 1, 1)

        self.retranslateUi(editSearch)
        QtCore.QMetaObject.connectSlotsByName(editSearch)

    def retranslateUi(self, editSearch):
        pass

