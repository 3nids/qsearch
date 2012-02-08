"""
qSearch
QGIS plugin

Denis Rouzaud
denis.rouzaud@gmail.com
Feb. 2012
"""

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
		#QObject.connect(self , SIGNAL( "accepted()" ) , self.applySettings)
		
	def showEvent(self, e):
		self.progressBar.setVisible(False)
		for i in range(self.itemsLayout.count()): self.itemsLayout.itemAt(i).widget().close()

		
	def setLayer(self,layer):
		self.layer = layer
		self.layerName.setText(layer.name())
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
		item = searchItem(self.iface,self.layer,self.fields)
		self.itemsLayout.addWidget(item)
		
		
		
		
class searchItem(QFrame, Ui_searchItem ):
	def __init__(self,iface,layer,fields):
		self.iface = iface
		QDialog.__init__(self)
		self.setupUi(self)
		self.layer = layer
		self.fields = fields
		self.settings = QSettings("qSearch","qSearch")
		for f in fields:
			self.fieldCombo.addItem(f[1])				
		
	@pyqtSignature("on_fieldCombo_currentIndexChanged(int)")
	def on_fieldCombo_currentIndexChanged(self,i):
		if i < 0: return
		self.valueCombo.clear()
		ix = self.fields[i][0]
		maxUnique = self.settings.value("maxUnique",30).toInt()[0]
		for value in self.layer.dataProvider().uniqueValues(ix,maxUnique):
			self.valueCombo.addItem(value.toString())					

	@pyqtSignature("on_deleteBox_clicked()")
	def on_deleteBox_clicked(self):
		self.close()
