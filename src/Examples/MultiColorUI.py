"""Example on using multiple Schemes for multiple widgets and/or widget groups
Could be used to differentiate parts of the UI or to indicate states like error,
warning etc.
"""

import sys
import os.path

from QColorScheme import QColorScheme

from PyQt4.QtGui import QApplication, QMainWindow, QColor, QColorDialog, QPalette
from PyQt4 import uic

class MultiColorUI( QMainWindow ):
    """Load widget gallery  ui for demonstration
    """
    def __init__( self ):
        # Init the baseclass
        QMainWindow.__init__( self )
        
        # Load widgetGallery ui file
        uic.loadUi( os.path.split( __file__ )[0] + "\UI\multiColorUI.ui", self )
        
        MainScheme = QColorScheme()
        leftScheme = QColorScheme(QColor(100,100,0),QColor(200,150,150),2.5,apply=False)
        rightScheme = QColorScheme(QColor(50,100,50),QColor(200,150,150),2.5,apply=False)
        
        errorScheme = QColorScheme(QColor(250,100,100),QColor(200,50,50),5,monochromeText=True,apply=False)
        
        leftScheme.applyScheme(self.leftWidget)
        rightScheme.applyScheme(self.rightWidget)
        
        errorScheme.applyScheme(self.pushButton_7)
        errorScheme.applyScheme(self.pushButton_8)
        

# Create application instance
app = QApplication(sys.argv)

# Create mainwindow
multiColorUI = MultiColorUI()
multiColorUI.show()

# Enter application loop
sys.exit(app.exec_())     