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
		

	def setLayer(self,layer):
		self.selectButton.setEnabled(False)
		self.progressBar.setVisible(False)
		for i in range(self.itemsLayout.count()): self.itemsLayout.itemAt(i).widget().close()
		
		self.layer = layer
		self.layerName.setText(layer.name())
		self.selection = []
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
			self.items[itemIndex].andCombo.setCurrentIndex(item[0])
			self.items[itemIndex].fieldCombo.setCurrentIndex(item[1])
			self.items[itemIndex].isCombo.setCurrentIndex(item[2])
			self.items[itemIndex].operatorCombo.setCurrentIndex(item[3])
			self.items[itemIndex].valueCombo.setEditText(item[4])
		
	def readSearches(self):
		loadSearches = self.layer.customProperty("qSearch").toString()
		if loadSearches == '':
			currentSearches = []
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
		self.emit(SIGNAL("searchSaved ()"))	
		#print currentSearches
		
	@pyqtSignature("on_searchButton_clicked()")
	def on_searchButton_clicked(self):
		# index of fields used for search
		fields2select = []
		for item in self.items:
			fields2select.append( self.fields[item.fieldCombo.currentIndex()][0] )
		# create search test
		searchCmd = ""
		for i,item in enumerate(self.items):
			if i>0: searchCmd += " %s " % item.andCombo.currentText()
			searchCmd += " fieldmap[%u] " % fields2select[i]
			iOper = item.operatorCombo.currentIndex() 
			if iOper < 3: 
				searchCmd += " %s %s" % (item.operatorCombo.currentText(), item.valueCombo.currentText() )
			elif iOper == 3:
				print "TODO"
			print searchCmd
		# select fields, init search
		provider = self.layer.dataProvider()
		provider.select(fields2select)
		self.selection = []
		f = QgsFeature()
		# Init progress bar
		self.selectButton.setText("Select")
		self.selectButton.setEnabled(False)
		self.progressBar.setVisible(True)
		self.progressBar.setMinimum(0)
		self.progressBar.setMaximum(provider.featureCount())
		self.progressBar.setValue(0)
		k = 0
		# browse features
		while (provider.nextFeature(f)):
			k+=1
			self.progressBar.setValue(k)
			fieldmap=f.attributeMap()
			print fieldmap[13].toString() # TODO !!!
			return
			if eval(searchCmd):
				print "ok"
				self.selection.append(f.id())
		self.selectButton.setEnabled(False)
		self.selectButton.setText("Select %u features" % len(self.selection))
		
	@pyqtSignature("on_selectButton_clicked()")
	def on_selectButton_clicked(self):
		self.layer.setSelectedFeatures(self.selection)
		
class searchItem(QFrame, Ui_searchItem):
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
