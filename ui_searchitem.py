# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_searchitem.ui'
#
# Created: Fri Feb 10 14:52:22 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_searchItem(object):
    def setupUi(self, searchItem):
        searchItem.setObjectName(_fromUtf8("searchItem"))
        searchItem.resize(540, 35)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(searchItem.sizePolicy().hasHeightForWidth())
        searchItem.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        searchItem.setFont(font)
        searchItem.setWindowTitle(QtGui.QApplication.translate("searchItem", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        searchItem.setFrameShape(QtGui.QFrame.StyledPanel)
        searchItem.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(searchItem)
        self.gridLayout.setMargin(3)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.operatorCombo = QtGui.QComboBox(searchItem)
        self.operatorCombo.setMaximumSize(QtCore.QSize(110, 16777215))
        self.operatorCombo.setObjectName(_fromUtf8("operatorCombo"))
        self.operatorCombo.addItem(_fromUtf8(""))
        self.operatorCombo.setItemText(0, QtGui.QApplication.translate("searchItem", "==", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorCombo.addItem(_fromUtf8(""))
        self.operatorCombo.setItemText(1, QtGui.QApplication.translate("searchItem", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorCombo.addItem(_fromUtf8(""))
        self.operatorCombo.setItemText(2, QtGui.QApplication.translate("searchItem", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorCombo.addItem(_fromUtf8(""))
        self.operatorCombo.setItemText(3, QtGui.QApplication.translate("searchItem", "text search", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout.addWidget(self.operatorCombo, 1, 4, 1, 1)
        self.valueCombo = QtGui.QComboBox(searchItem)
        self.valueCombo.setEditable(True)
        self.valueCombo.setObjectName(_fromUtf8("valueCombo"))
        self.gridLayout.addWidget(self.valueCombo, 1, 5, 1, 1)
        self.isCombo = QtGui.QComboBox(searchItem)
        self.isCombo.setMaximumSize(QtCore.QSize(75, 16777215))
        self.isCombo.setObjectName(_fromUtf8("isCombo"))
        self.isCombo.addItem(_fromUtf8(""))
        self.isCombo.setItemText(0, QtGui.QApplication.translate("searchItem", "IS", None, QtGui.QApplication.UnicodeUTF8))
        self.isCombo.addItem(_fromUtf8(""))
        self.isCombo.setItemText(1, QtGui.QApplication.translate("searchItem", "IS NOT", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout.addWidget(self.isCombo, 1, 3, 1, 1)
        self.fieldCombo = QtGui.QComboBox(searchItem)
        self.fieldCombo.setObjectName(_fromUtf8("fieldCombo"))
        self.gridLayout.addWidget(self.fieldCombo, 1, 2, 1, 1)
        self.deleteButton = QtGui.QToolButton(searchItem)
        self.deleteButton.setText(QtGui.QApplication.translate("searchItem", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.gridLayout.addWidget(self.deleteButton, 1, 0, 1, 1)
        self.andCombo = QtGui.QComboBox(searchItem)
        self.andCombo.setEnabled(False)
        self.andCombo.setMaximumSize(QtCore.QSize(60, 16777215))
        self.andCombo.setObjectName(_fromUtf8("andCombo"))
        self.andCombo.addItem(_fromUtf8(""))
        self.andCombo.setItemText(0, QtGui.QApplication.translate("searchItem", "and", None, QtGui.QApplication.UnicodeUTF8))
        self.andCombo.addItem(_fromUtf8(""))
        self.andCombo.setItemText(1, QtGui.QApplication.translate("searchItem", "or", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout.addWidget(self.andCombo, 1, 1, 1, 1)

        self.retranslateUi(searchItem)
        QtCore.QMetaObject.connectSlotsByName(searchItem)

    def retranslateUi(self, searchItem):
        pass

