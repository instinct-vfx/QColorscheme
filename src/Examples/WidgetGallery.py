"""Example for QColorScheme
A Widget Gallery UI is loaded that also contains controls
to play with the colors of the color generator in a live
application
"""
import sys
import os.path

from QColorScheme import QColorScheme

from PyQt4.QtGui import QApplication, QMainWindow, QColor, QColorDialog, QPalette
from PyQt4 import uic

class WidgetGallery( QMainWindow ):
    """Load widget gallery  ui for demonstration
    """
    def __init__( self ):
        # Init the baseclass
        QMainWindow.__init__( self )
        
        # Load widgetGallery ui file
        uic.loadUi( os.path.split( __file__ )[0] + "\UI\widgetGallery.ui", self )
        
        # Connect disable checkbox
        self.disableWidgets.toggled.connect(self.mainWidget.setDisabled)
        
        # Connect spread sliders to the scheme spread
        self.spreadSlider.sliderMoved.connect(self.spreadSliderChange)
        
        # Connect color pickers to base- and highlight-colors
        self.pickBaseColor.clicked.connect(self.slotBaseColor)
        self.pickHighlightColor.clicked.connect(self.slotHighlightColor)
        
        # Create ColorSchemer and apply to the whole app
        self.ColorScheme = QColorScheme()
        self.ColorScheme.loadSimpleScheme(os.path.split( __file__ )[0] + "\..\QColorScheme\Presets\SimpleNuke.ini")
        
        # Set initial values on the colorchips and spread slider to match the loaded scheme
        self.spreadSlider.setValue(self.ColorScheme.spread*1000)
        self.setBackgroundColor(self.chipBaseColor, self.ColorScheme.baseColor)
        self.setBackgroundColor(self.chipHighlightColor, self.ColorScheme.highlightColor)
        
        #self.ColorScheme.setColor(self.mainWidget, Group=None, Role="Window", Color=QColor(255,0,0))
    
    def setBackgroundColor(self, widget, color):
        """Helper function to set the background on the color chips
        """
        pal = widget.palette()
        pal.setColor(QPalette.Background, color)
        widget.setPalette(pal)         
        
    def spreadSliderChange(self):
        """Slot function to update spread when the slider is changed
        """
        self.ColorScheme.spread = self.spreadSlider.value()/1000.0
        self.ColorScheme.generateScheme()
        
    def slotBaseColor(self):
        """Slot function to update the basecolor if the color has been changed
        """
        self.ColorScheme.baseColor=QColorDialog.getColor(self.ColorScheme.baseColor, self, "ColorDialog")
        self.ColorScheme.generateScheme()
        self.setBackgroundColor(self.chipBaseColor, self.ColorScheme.baseColor)        

    def slotHighlightColor(self):
        """Slot function to update the highlightcolor if the color has been changed
        """        
        self.ColorScheme.highlightColor=QColorDialog.getColor(self.ColorScheme.highlightColor, self, "ColorDialog")
        self.ColorScheme.generateScheme()        
        self.setBackgroundColor(self.chipHighlightColor, self.ColorScheme.highlightColor)
                  

# Create application instance
app = QApplication(sys.argv)

# Create mainwindow
widgetGallery = WidgetGallery()
widgetGallery.show()

# Enter application loop
sys.exit(app.exec_()) 