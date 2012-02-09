"""
qSearch
QGIS plugin

Denis Rouzaud
denis.rouzaud@gmail.com
Feb. 2012
"""

import PyQt4
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from ui_editsearch import Ui_editSearch
from ui_searchitem import Ui_searchItem

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

# create the dialog to connect layers
class editSearch(QDialog, Ui_editSearch ):
	def __init__(self,iface):
		self.iface = iface
		QDialog.__init__(self)
		self.setupUi(self)
		self.layer = []
		self.settings = QSettings("qSearch","qSearch")
		QObject.connect(self.saveButton , SIGNAL( "clicked()" ) , self.saveSearches)
		
	def showEvent(self, e):
		self.progressBar.setVisible(False)
		for i in range(self.itemsLayout.count()): self.itemsLayout.itemAt(i).widget().close()
		self.items = []

		
	def setLayer(self,layer):
		self.layer = layer
		self.layerName.setText(layer.name())
		self.items = []
		self.searchIndex = len(self.readSearches())
		# create list of displayed fields
		self.fields = []
		for i in layer.dataProvider().fields():
			alias = layer.attributeAlias(i)
			if alias == "":
				if self.settings.value("onlyAlias",0).toInt()[0] == 1: continue
				alias = layer.dataProvider().fields().get(i).name()			
			self.fields.append([i,alias])

	
	@pyqtSignature("on_addButton_clicked()")
	def on_addButton_clicked(self):
		itemIndex = len(self.items)
		self.items.append( searchItem(self.layer,self.fields,itemIndex) )
		QObject.connect(self.items[itemIndex],SIGNAL("itemDeleted(int)"),self.deleteItem)
		self.itemsLayout.addWidget(self.items[itemIndex])
		
	def deleteItem(self,itemIndex):
		self.items.pop(itemIndex)
		
	def loadSearch(self,i):
		self.items = []
		searches = self.readSearches()
		self.searchIndex = i
		search = searches[i]
		searchItems = search[1]
		for itemIndex,item in enumerate(searchItems):
			self.items.append( searchItem(self.layer,self.fields,itemIndex) )
			QObject.connect(self.items[itemIndex],SIGNAL("itemDeleted(int)"),self.deleteItem)
			self.itemsLayout.addWidget(self.items[itemIndex])
			self.items[itemIndex].andCombo.setCurrentText(item[0])
			self.items[itemIndex].fieldCombo.setCurrentText(item[1])
			self.items[itemIndex].isCombo.setCurrentText(item[2])
			self.items[itemIndex].operatorCombo.setCurrentText(item[3])
			self.items[itemIndex].valueCombo.setCurrentText(item[4])
		
	def readSearches(self):
		loadSearches = self.layer.customProperty("qSearch").toString()
		if loadSearches == '':
			currentSearches = [[]]
		else:
			exec("currentSearches = %s" % loadSearches)
		return currentSearches
			
	def saveSearches(self):
		saveSearch = []
		for item in self.items:
			saveSearch.append( [ item.andCombo.currentIndex(),item.fieldCombo.currentIndex(),item.isCombo.currentIndex(),item.operatorCombo.currentIndex(),item.valueCombo.currentText()] )
		currentSearches = self.readSearches()
		if self.searchIndex > len(currentSearches)-1: currentSearches.append([])
		currentSearches[self.searchIndex] = [self.searchName.text(),saveSearch]
		self.layer.setCustomProperty("qSearch",repr(currentSearches))
		
		
		
class searchItem(QFrame, Ui_searchItem ):
	def __init__(self,layer,fields,itemIndex):
		QFrame.__init__(self)
		self.setupUi(self)
		self.layer = layer
		self.fields = fields
		self.itemIndex = itemIndex
		self.settings = QSettings("qSearch","qSearch")
		if itemIndex > 0: self.andCombo.setEnabled(True)
		for f in fields: self.fieldCombo.addItem(f[1])		

		
	@pyqtSignature("on_fieldCombo_currentIndexChanged(int)")
	def on_fieldCombo_currentIndexChanged(self,i):
		if i < 0: return
		self.valueCombo.clear()
		ix = self.fields[i][0]
		maxUnique = self.settings.value("maxUnique",30).toInt()[0]
		for value in self.layer.dataProvider().uniqueValues(ix,maxUnique):
			self.valueCombo.addItem(value.toString())					

	@pyqtSignature("on_deleteButton_clicked()")
	def on_deleteButton_clicked(self):
		self.close()
		self.emit(SIGNAL("itemDeleted(int)",self.itemIndex))
			
		
