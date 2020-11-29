import wx
import sys
from src.captureApp import captureApp
from src.stcData import stcData



class startApp(wx.Frame,stcData):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title = "TEST", style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        panel = wx.Panel(self, -1) 
        btn_cap = wx.Button(panel, label='캡처준비', pos=(20, 30))
        btn_cap.SetSize(20, 10, 100, 50, 0)
        btn_cap.Bind(wx.EVT_BUTTON, self.onclickbtn_cap)
        btn_close = wx.Button(panel, label='닫기', pos=(20, 30))
        btn_close.SetSize(150, 10, 100, 50, 0)
        btn_close.Bind(wx.EVT_BUTTON, self.onclickbtn_close)
        self.InitUI()
 
    def InitUI(self):
        self.SetSize((280, 110))
        self.SetTitle('ExcelClip')
        self.SetIcon(wx.Icon('images/clipicon.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        
        
    def onclickbtn_cap(self, e): #캡처화면 켜기
        #self.Close(True)
        self.SetTransparent(0)
        stcData.bufferedImage=stcData.capture()
        self.SetTransparent(255)
        captureApp().Show()
        
    def onclickbtn_close(self, e): #끄기
        self.Close(True)     
        
if __name__=="__main__":
    app = wx.App()
    frame = startApp()
    frame.Show()
    app.MainLoop()