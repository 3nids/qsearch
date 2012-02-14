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

	def initUi(self,layer):
		self.selectButton.setEnabled(False)
		self.progressBar.setVisible(False)
		for i in range(self.itemsLayout.count()): self.itemsLayout.itemAt(i).widget().close()
		self.layer = layer
		self.layerName.setText(layer.name())
		self.selection = []
		self.items = []
		self.searchIndex = len(self.readSearches())
		self.aliasBox.setChecked(self.settings.value("onlyAlias",0).toInt()[0])
		self.layerLabel.setText("%u feature(s) currently selected in" % layer.selectedFeatureCount())

	def fields(self,aliasMode=-1):
		# create list of displayed fields
		# aliasMode: -1: auto, 0: all, 1: only alias
		if aliasMode == 0: aliasMode = False
		elif aliasMode == 1: aliasMode = True
		else: aliasMode = self.aliasBox.isChecked()
		fields = []
		for i in self.layer.dataProvider().fields():
			alias = self.layer.attributeAlias(i)
			if alias == "":
				if aliasMode is True: continue
				alias = self.layer.dataProvider().fields().get(i).name()
			fields.append({'index':i,'alias':alias})
		return fields

	@pyqtSignature("on_aliasBox_stateChanged(int)")
	def on_aliasBox_stateChanged(self,i):
		if i==2: aliasMode = 0
		else: aliasMode = 1
		for itemIndex,item in enumerate(self.items):
			currentField = self.fields(aliasMode)[item.fieldCombo.currentIndex()].get('index')
			item.fieldCombo.clear()
			for i,field in enumerate(self.fields()):
				item.fieldCombo.addItem(field.get('alias'))	
				if field.get('index') == currentField:
					item.fieldCombo.setCurrentIndex(i)

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
		self.searchName.setText(search.get('name'))
		self.aliasBox.setChecked(search.get('alias'))
		for itemIndex,item in enumerate(search.get('items')):
			idx = -1
			for i,field in enumerate(self.fields()):
				if field.get('index') == item.get('index'):
					idx = i
					break
			if idx==-1: # i.e. the field apparently does not exist anymore
				continue
			self.items.append( searchItem(self.layer,self.fields,itemIndex) )
			QObject.connect(self.items[itemIndex],SIGNAL("itemDeleted(int)"),self.deleteItem)
			self.itemsLayout.addWidget(self.items[itemIndex])
			self.items[itemIndex].andCombo.setCurrentIndex(item.get('andor'))
			self.items[itemIndex].fieldCombo.setCurrentIndex(i)
			self.items[itemIndex].operatorCombo.setCurrentIndex(item.get('operator'))
			self.items[itemIndex].valueCombo.setEditText(item.get('value'))

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
			saveSearch.append( {'andor': item.andCombo.currentIndex(),
								'index': self.fields()[item.fieldCombo.currentIndex()].get('index') ,
								'operator': item.operatorCombo.currentIndex(),
								'value': item.valueCombo.currentText() } )
		currentSearches = self.readSearches()
		if self.searchIndex > len(currentSearches)-1: currentSearches.append([])
		currentSearches[self.searchIndex] = {'name': self.searchName.text(), 'alias': int(self.aliasBox.isChecked()) ,'items': saveSearch}
		self.layer.setCustomProperty("qSearch",repr(currentSearches))
		self.emit(SIGNAL("searchSaved ()"))	
		#print currentSearches

	@pyqtSignature("on_searchButton_clicked()")
	def on_searchButton_clicked(self):
		# index of fields used for search
		fields2select = []
		for item in self.items:
			fields2select.append( self.fields()[item.fieldCombo.currentIndex()].get('index'))
		operators = ['==','!=','>=','>','<=','<','True','False','==','!=']
		# create search test
		searchCmd = ""
		for i,item in enumerate(self.items):
			if i>0: searchCmd += " %s " % item.andCombo.currentText()
			operator = operators[item.operatorCombo.currentIndex()]
			iOper = item.operatorCombo.currentIndex() 
			if iOper < 6: # => numeric
				searchCmd += " fieldmap[%u].toDouble()[0] %s %s " % ( fields2select[i] , operator , item.valueCombo.currentText() )
			elif iOper < 8: 
				searchCmd += " fieldmap[%u].toString().contains(\"%s\") is %s" % ( fields2select[i] , item.valueCombo.currentText(), operator )	
			elif iOper < 10: 
				searchCmd += " fieldmap[%u].toString() %s \"%s\" " % ( fields2select[i] , operator , item.valueCombo.currentText() )	
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
		try:
			while (provider.nextFeature(f)):
				k+=1
				self.progressBar.setValue(k)
				fieldmap=f.attributeMap()
				if eval(searchCmd):
					self.selection.append(f.id())
			self.selectButton.setText("Select %u features" % len(self.selection))
			if len(self.selection)>0:
				self.selectButton.setEnabled(True)
		except NameError:
			QMessageBox.warning( self.iface.mainWindow() , "qSearch","If you are trying to detect text, you should use text equals." )
		self.progressBar.setVisible(False)
			
	@pyqtSignature("on_selectButton_clicked()")
	def on_selectButton_clicked(self):
		selection = []
		if self.addCurrentBox.isChecked():
			selection = self.layer.selectedFeaturesIds()
		selection.extend( self.selection )
		self.layer.setSelectedFeatures(selection)
		self.layerLabel.setText("%u feature(s) currently selected in" % self.layer.selectedFeatureCount())

class searchItem(QFrame, Ui_searchItem):
	def __init__(self,layer,fields,itemIndex):
		QFrame.__init__(self)
		self.setupUi(self)
		self.layer = layer
		self.fields = fields
		self.itemIndex = itemIndex
		self.settings = QSettings("qSearch","qSearch")
		if itemIndex > 0: self.andCombo.setEnabled(True)
		for f in fields(): self.fieldCombo.addItem(f.get('alias'))

	@pyqtSignature("on_fieldCombo_currentIndexChanged(int)")
	def on_fieldCombo_currentIndexChanged(self,i):
		if i < 0: return
		self.valueCombo.clear()
		ix = self.fields()[i].get('index')
		maxUnique = self.settings.value("maxUnique",30).toInt()[0]
		for value in self.layer.dataProvider().uniqueValues(ix,maxUnique):
			self.valueCombo.addItem(value.toString())

	@pyqtSignature("on_deleteButton_clicked()")
	def on_deleteButton_clicked(self):
		self.close()
		self.emit(SIGNAL("itemDeleted(int)",self.itemIndex))
