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
    return "Nice UI to search within a table and save searches to run them later."
def version():
    return "Version 1.0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.7"
def classFactory(iface):
    from qsearch import qSearch
    return qSearch(iface)
