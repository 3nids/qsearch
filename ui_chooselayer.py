# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_chooselayer.ui'
#
# Created: Wed Feb  8 11:40:47 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_chooseLayer(object):
    def setupUi(self, chooseLayer):
        chooseLayer.setObjectName(_fromUtf8("chooseLayer"))
        chooseLayer.resize(313, 111)
        chooseLayer.setWindowTitle(QtGui.QApplication.translate("chooseLayer", "qSearch", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(chooseLayer)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(chooseLayer)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setText(QtGui.QApplication.translate("chooseLayer", "Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.layerCombo = QtGui.QComboBox(chooseLayer)
        self.layerCombo.setObjectName(_fromUtf8("layerCombo"))
        self.gridLayout.addWidget(self.layerCombo, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(chooseLayer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.label_2 = QtGui.QLabel(chooseLayer)
        self.label_2.setText(QtGui.QApplication.translate("chooseLayer", "Group", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.groupCombo = QtGui.QComboBox(chooseLayer)
        self.groupCombo.setObjectName(_fromUtf8("groupCombo"))
        self.gridLayout.addWidget(self.groupCombo, 0, 1, 1, 1)

        self.retranslateUi(chooseLayer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), chooseLayer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), chooseLayer.reject)
        QtCore.QMetaObject.connectSlotsByName(chooseLayer)

    def retranslateUi(self, chooseLayer):
        pass

