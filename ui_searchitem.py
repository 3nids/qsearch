# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_searchitem.ui'
#
# Created: Wed Feb  8 16:20:59 2012
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
        self.operatorCombo.setItemText(0, QtGui.QApplication.translate("searchItem", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorCombo.addItem(_fromUtf8(""))
        self.operatorCombo.setItemText(1, QtGui.QApplication.translate("searchItem", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorCombo.addItem(_fromUtf8(""))
        self.operatorCombo.setItemText(2, QtGui.QApplication.translate("searchItem", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorCombo.addItem(_fromUtf8(""))
        self.operatorCombo.setItemText(3, QtGui.QApplication.translate("searchItem", "text equals", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorCombo.addItem(_fromUtf8(""))
        self.operatorCombo.setItemText(4, QtGui.QApplication.translate("searchItem", "text search", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout.addWidget(self.operatorCombo, 1, 3, 1, 1)
        self.valueCombo = QtGui.QComboBox(searchItem)
        self.valueCombo.setEditable(True)
        self.valueCombo.setObjectName(_fromUtf8("valueCombo"))
        self.gridLayout.addWidget(self.valueCombo, 1, 4, 1, 1)
        self.boolCombo = QtGui.QComboBox(searchItem)
        self.boolCombo.setMaximumSize(QtCore.QSize(75, 16777215))
        self.boolCombo.setObjectName(_fromUtf8("boolCombo"))
        self.boolCombo.addItem(_fromUtf8(""))
        self.boolCombo.setItemText(0, QtGui.QApplication.translate("searchItem", "IS", None, QtGui.QApplication.UnicodeUTF8))
        self.boolCombo.addItem(_fromUtf8(""))
        self.boolCombo.setItemText(1, QtGui.QApplication.translate("searchItem", "IS NOT", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout.addWidget(self.boolCombo, 1, 2, 1, 1)
        self.fieldCombo = QtGui.QComboBox(searchItem)
        self.fieldCombo.setObjectName(_fromUtf8("fieldCombo"))
        self.gridLayout.addWidget(self.fieldCombo, 1, 1, 1, 1)
        self.deleteBox = QtGui.QToolButton(searchItem)
        self.deleteBox.setText(QtGui.QApplication.translate("searchItem", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteBox.setObjectName(_fromUtf8("deleteBox"))
        self.gridLayout.addWidget(self.deleteBox, 1, 0, 1, 1)

        self.retranslateUi(searchItem)
        QtCore.QMetaObject.connectSlotsByName(searchItem)

    def retranslateUi(self, searchItem):
        pass

