#!/usr/bin/env python2.3
# generated by wxGlade 0.3.3 on Mon Jun 28 20:48:23 2004

from Matrix import *
import wx
import sys

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        self.window_1 = LEDMatrix(self.panel_1, -1)
        self.button_1 = wx.Button(self.panel_1, -1, "ESCI")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
    	self.Bind(wx.EVT_BUTTON, self.OnClick, self.button_1)
	
	self.window_1.SetValue("NOPQRSTUVZ")
	
	self.timer = wx.Timer(self)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.window_1.EVTUpdate)

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        self.SetSize((300, 120))
        self.window_1.SetSize((300, 80))
        self.button_1.SetSize((300, 30))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.window_1, 1, wx.EXPAND, 0)
        sizer_2.Add(self.button_1, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.panel_1.SetAutoLayout(1)
        self.panel_1.SetSizer(sizer_2)
        sizer_2.Fit(self.panel_1)
        sizer_2.SetSizeHints(self.panel_1)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def OnClick(self, event):
	self.window_1.ShiftLeft()	
# end of class MyFrame


class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame_1 = MyFrame(None, -1, "")
        self.SetTopWindow(frame_1)
        frame_1.Show(1)
        return 1

# end of class MyApp

if __name__ == "__main__":
    testmatrix = MyApp(0)
    testmatrix.MainLoop()