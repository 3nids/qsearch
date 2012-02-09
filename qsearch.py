"""
qSearch
QGIS plugin

Denis Rouzaud
denis.rouzaud@gmail.com
Feb. 2012
"""
# Import the PyQt and QGIS libraries
import PyQt4
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import resources

from chooselayer import chooseLayer
from editsearch import editSearch
from settings import settings

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class qSearch():
	triggered = pyqtSignal(QObject)
	
	def __init__(self, iface):
		self.iface = iface
		# init dialogs
		self.chooseLayerDialog = chooseLayer(self.iface)
		self.editSearchDialog  = editSearch(self.iface)
		# load searches when new layers are loaded or when a search is saved
		QObject.connect(self.iface.mapCanvas() , SIGNAL("layersChanged ()") , self.fillMenuEntries ) 
		QObject.connect(self.editSearchDialog  , SIGNAL("searchSaved ()")   , self.fillMenuEntries ) 
		
	def initGui(self):
		self.newSearchAction = QAction(QIcon(":/plugins/qsearch/icons/search.png"),"new search", self.iface.mainWindow())
		QObject.connect(self.newSearchAction, SIGNAL("triggered()"), self.newSearch)
		self.iface.addToolBarIcon(self.newSearchAction)
		self.iface.addPluginToMenu("&qSearch", self.newSearchAction)	
		# settings
		self.uisettings = settings(self.iface)
		self.uisettingsAction = QAction("settings", self.iface.mainWindow())
		QObject.connect(self.uisettingsAction, SIGNAL("triggered()"), self.uisettings.exec_)
		self.iface.addPluginToMenu("&qSearch", self.uisettingsAction)	
				
	def unload(self):
		# Remove the plugin menu item and icon
		self.iface.removePluginMenu("&qSearch",self.newSearchAction)
		self.iface.removePluginMenu("&qSearch", self.uisettingsAction)	
		
	def newSearch(self):
		if self.chooseLayerDialog.exec_():
			self.editSearchDialog.setLayer(self.chooseLayerDialog.selectedLayer())
			self.editSearchDialog.exec_()
	
	def fillMenuEntries(self):
		signalMapper = QSignalMapper()
		for layer in self.iface.legendInterface().layers():
			searches = layer.customProperty("qSearch","").toString()
			print searches
			if searches != "":
				exec("searches = %s" % searches)
				for i,search in enumerate(searches):
					action = QAction("%s :: %s" % (layer.name(),search[0]), self.iface.mainWindow())
					#QObject.connect(action, SIGNAL("triggered()"), self.showSearch)
					signalMapper.setMapping(action, qSearchMenuItem(i,layer))
					action.triggered.connect(signalMapper.map)  
							
					#QObject.connect(signalMapper, SIGNAL("mapped(QObject)"), action, SIGNAL("showSearch(qSearchMenuItem)") )
					self.iface.addPluginToMenu("&qSearch",action)
		signalMapper.mapped.connect(self.showSearch) 
		
	def showSearch(self,item):
		print "JFDGFDGFDGF"
		sender = QObject.sender()
		print sender.layer.name()
		print sender.isearch
		

class qSearchMenuItem( QObject ):
	def __init__(self,layer,isearch):
		QObject.__init__(self)
		self.layer = layer
		self.isearch = isearch
