# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_editsearch.ui'
#
# Created: Thu Apr 12 09:36:53 2012
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
        editSearch.resize(576, 357)
        editSearch.setWindowTitle(QtGui.QApplication.translate("editSearch", "qSearch", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_2 = QtGui.QGridLayout(editSearch)
        self.gridLayout_2.setMargin(6)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.progressBar = QtGui.QProgressBar(editSearch)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_2.addWidget(self.progressBar, 5, 0, 1, 6)
        self.closeButton = QtGui.QPushButton(editSearch)
        self.closeButton.setText(QtGui.QApplication.translate("editSearch", "close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout_2.addWidget(self.closeButton, 6, 5, 1, 1)
        self.layerName = QtGui.QLineEdit(editSearch)
        self.layerName.setEnabled(False)
        self.layerName.setObjectName(_fromUtf8("layerName"))
        self.gridLayout_2.addWidget(self.layerName, 0, 3, 1, 3)
        self.itemsScroll = QtGui.QScrollArea(editSearch)
        self.itemsScroll.setWidgetResizable(True)
        self.itemsScroll.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.itemsScroll.setObjectName(_fromUtf8("itemsScroll"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 562, 147))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setMargin(3)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.itemsLayout = QtGui.QVBoxLayout()
        self.itemsLayout.setSpacing(3)
        self.itemsLayout.setObjectName(_fromUtf8("itemsLayout"))
        self.gridLayout_3.addLayout(self.itemsLayout, 0, 0, 1, 1)
        self.itemsScroll.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.itemsScroll, 3, 0, 1, 6)
        self.layerLabel = QtGui.QLabel(editSearch)
        self.layerLabel.setText(QtGui.QApplication.translate("editSearch", "0 feature(s) currently selected in", None, QtGui.QApplication.UnicodeUTF8))
        self.layerLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.layerLabel.setObjectName(_fromUtf8("layerLabel"))
        self.gridLayout_2.addWidget(self.layerLabel, 0, 0, 1, 3)
        self.selectButton = QtGui.QPushButton(editSearch)
        self.selectButton.setEnabled(False)
        self.selectButton.setText(QtGui.QApplication.translate("editSearch", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.selectButton.setObjectName(_fromUtf8("selectButton"))
        self.gridLayout_2.addWidget(self.selectButton, 4, 4, 1, 2)
        self.addCurrentBox = QtGui.QCheckBox(editSearch)
        self.addCurrentBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addCurrentBox.setText(QtGui.QApplication.translate("editSearch", "add to current selection", None, QtGui.QApplication.UnicodeUTF8))
        self.addCurrentBox.setIconSize(QtCore.QSize(16, 16))
        self.addCurrentBox.setObjectName(_fromUtf8("addCurrentBox"))
        self.gridLayout_2.addWidget(self.addCurrentBox, 4, 3, 1, 1)
        self.saveButton = QtGui.QPushButton(editSearch)
        self.saveButton.setText(QtGui.QApplication.translate("editSearch", "save search", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.gridLayout_2.addWidget(self.saveButton, 1, 5, 1, 1)
        self.aliasBox = QtGui.QCheckBox(editSearch)
        self.aliasBox.setText(QtGui.QApplication.translate("editSearch", "Display only fields with aliases", None, QtGui.QApplication.UnicodeUTF8))
        self.aliasBox.setObjectName(_fromUtf8("aliasBox"))
        self.gridLayout_2.addWidget(self.aliasBox, 2, 3, 1, 3)
        self.addButton = QtGui.QPushButton(editSearch)
        self.addButton.setText(QtGui.QApplication.translate("editSearch", "Add item", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout_2.addWidget(self.addButton, 2, 0, 1, 1)
        self.searchName = QtGui.QLineEdit(editSearch)
        self.searchName.setText(QtGui.QApplication.translate("editSearch", "new search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchName.setObjectName(_fromUtf8("searchName"))
        self.gridLayout_2.addWidget(self.searchName, 1, 3, 1, 2)
        self.label = QtGui.QLabel(editSearch)
        self.label.setText(QtGui.QApplication.translate("editSearch", "Search name", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 2)
        self.searchButton = QtGui.QPushButton(editSearch)
        self.searchButton.setText(QtGui.QApplication.translate("editSearch", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.gridLayout_2.addWidget(self.searchButton, 4, 0, 1, 1)

        self.retranslateUi(editSearch)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), editSearch.accept)
        QtCore.QMetaObject.connectSlotsByName(editSearch)
        editSearch.setTabOrder(self.searchButton, self.layerName)
        editSearch.setTabOrder(self.layerName, self.itemsScroll)
        editSearch.setTabOrder(self.itemsScroll, self.selectButton)
        editSearch.setTabOrder(self.selectButton, self.addCurrentBox)
        editSearch.setTabOrder(self.addCurrentBox, self.saveButton)
        editSearch.setTabOrder(self.saveButton, self.aliasBox)
        editSearch.setTabOrder(self.aliasBox, self.addButton)
        editSearch.setTabOrder(self.addButton, self.searchName)
        editSearch.setTabOrder(self.searchName, self.closeButton)

    def retranslateUi(self, editSearch):
        pass

