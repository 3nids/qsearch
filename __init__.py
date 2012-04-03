"""
Item Browser
QGIS plugin

Denis Rouzaud
denis.rouzaud@gmail.com
Jan. 2012
"""

def name():
    return "qSearch"
def description():
    return "This plugin produces a friendly interface to perform and save searches in a layer."
def version():
    return "Version 1.2.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.7"
def classFactory(iface):
    from qsearch import qSearch
    return qSearch(iface)
