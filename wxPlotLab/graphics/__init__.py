# -*-coding:Utf-8 -*

import wx
# Plot Panel111
from GraphicPanel import GraphicPanel
def newWxPlotPanel(parent):
    return GraphicPanel(parent)

# Plot Frame
from MainWin import MainWin
def newWxPlotFrame():
    return MainWin()
