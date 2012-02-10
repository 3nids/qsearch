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
		
class qSearch(QObject):
	def __init__(self, iface):
		QObject.__init__(self)
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
		for layer in self.iface.legendInterface().layers():
			searches = layer.customProperty("qSearch","").toString()
			print searches
			if searches != "":
				exec("searches = %s" % searches)
				for i,search in enumerate(searches):
					action = searchAction("%s :: %s" % (layer.name(),search[0]), self.iface.mainWindow() , layer, i)		
					QObject.connect(action, SIGNAL("triggered()"), self.showSearch)	
					self.iface.addPluginToMenu("&qSearch",action)

	
	def showSearch(self):
		search = self.sender()
		self.editSearchDialog.setLayer(search.layer)
		self.editSearchDialog.loadSearch(search.isearch)
		self.editSearchDialog.exec_()
		
	
		
class searchAction(QAction):
	def __init__(self,str,win,layer,isearch):
		QAction.__init__(self,str,win)
		self.layer = layer
		self.isearch = isearch
		


