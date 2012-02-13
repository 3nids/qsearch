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
from ui_settings import Ui_settings

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

# create the dialog to connect layers
class settings(QDialog, Ui_settings ):
	def __init__(self,iface):
		self.iface = iface
		QDialog.__init__(self)
		# Set up the user interface from Designer.
		self.setupUi(self)
		QObject.connect(self , SIGNAL( "accepted()" ) , self.applySettings)
		# load settings
		self.settings = QSettings("qSearch","qSearch")
		
		self.aliasBox.setChecked( self.settings.value("onlyAlias",  0).toInt()[0] )
		self.maxUnique.setText(   self.settings.value("maxUnique",100).toString() )

	def applySettings(self):
		self.settings.setValue( "onlyAlias" , int(self.aliasBox.isChecked()) )
		self.settings.setValue( "maxUnique" , self.maxUnique.text() )

