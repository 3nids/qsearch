# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_settings.ui'
#
# Created: Wed Feb  8 14:36:00 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName(_fromUtf8("settings"))
        settings.resize(294, 132)
        settings.setWindowTitle(QtGui.QApplication.translate("settings", "qSearch :: settings", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(settings)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.aliasBox = QtGui.QCheckBox(settings)
        self.aliasBox.setText(QtGui.QApplication.translate("settings", "Display only fields with aliases", None, QtGui.QApplication.UnicodeUTF8))
        self.aliasBox.setObjectName(_fromUtf8("aliasBox"))
        self.gridLayout.addWidget(self.aliasBox, 0, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(settings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.maxUnique = QtGui.QLineEdit(settings)
        self.maxUnique.setMaximumSize(QtCore.QSize(50, 16777215))
        self.maxUnique.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.maxUnique.setText(QtGui.QApplication.translate("settings", "30", None, QtGui.QApplication.UnicodeUTF8))
        self.maxUnique.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.maxUnique.setObjectName(_fromUtf8("maxUnique"))
        self.gridLayout.addWidget(self.maxUnique, 1, 1, 1, 1)
        self.label = QtGui.QLabel(settings)
        self.label.setText(QtGui.QApplication.translate("settings", "Maximum unique values population", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.retranslateUi(settings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), settings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), settings.reject)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        pass

