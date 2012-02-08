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
from types import *

from ui_chooselayer import Ui_chooseLayer

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class chooseLayer(QDialog, Ui_chooseLayer ):
	def __init__(self,iface):
		self.iface = iface
		QDialog.__init__(self)
		self.setupUi(self)
		self.groups = []
		
	def showEvent(self, e):
		self.groupCombo.clear()
		self.layerCombo.clear()
		
		setGroup = 0
		setLayer = 0
		curLayerId = ""
		curLayer = self.iface.mapCanvas().currentLayer()
		if type(curLayer) != NoneType:	curLayerId = curLayer.id()
		self.groups = []
		self.groups.append( layerGroup("ungroupped") )
		g = 0
		self.groupCombo.addItem(_fromUtf8(""))
		self.groupCombo.setItemText(g, "ungroupped")
		for group in self.iface.legendInterface().groupLayerRelationship():
			if group[0] == "":
				add2group = 0
			else:
				g += 1
				self.groups.append( layerGroup(group[0]) )
				self.groupCombo.addItem(_fromUtf8(""))
				self.groupCombo.setItemText(g, self.groups[g].name)	
				add2group = g			
			for layer in group[1]:
				if self.getLayer(layer).type() == QgsMapLayer.VectorLayer:
					l = len(self.groups[g].layers)
					self.groups[g].addLayer(layer)
					if layer == curLayerId:
						setGroup = g
						setLayer = l
		self.groupCombo.setCurrentIndex(setGroup)
		self.on_groupCombo_currentIndexChanged(setGroup)
		self.layerCombo.setCurrentIndex(setLayer)
					
	@pyqtSignature("on_groupCombo_currentIndexChanged(int)")
	def on_groupCombo_currentIndexChanged(self,g):
		self.layerCombo.clear()
		for i,layer in enumerate(self.groups[g].layers):	
			self.layerCombo.addItem(_fromUtf8(""))
			self.layerCombo.setItemText(i, self.getLayer(layer).name())		
			
	def getLayer(self,layerid):
		for layer in self.iface.legendInterface().layers():
			if layer.id() == layerid:
				return layer
		return False
	
	def selectedLayer(self):
		g = self.groupCombo.currentIndex()	
		l = self.layerCombo.currentIndex()	
		return self.getLayer(self.groups[g].layers[l])
	
class layerGroup():
	def __init__(self,name):
		self.name = name
		self.layers = []
		
	def addLayer(self,layerid):
		self.layers.append(layerid)

