import wx
import sys
from src.captureApp import captureApp
from src.stcData import stcData



class startApp(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title = "TEST")
        self.InitUI()
 
    def InitUI(self):
        self.SetSize((290, 110))
        self.SetTitle('ExcelClip [표 추출 프로그램]')
        self.Centre()
        btn_cap = wx.Button(self, label='캡처준비', pos=(20, 30))
        btn_cap.SetSize(20, 10, 100, 50, 0)
        btn_cap.Bind(wx.EVT_BUTTON, self.onclickbtn_cap)
        btn_close = wx.Button(self, label='닫기', pos=(20, 30))
        btn_close.SetSize(150, 10, 100, 50, 0)
        btn_close.Bind(wx.EVT_BUTTON, self.onclickbtn_close)

    
    def onclickbtn_cap(self, e): #캡처화면 켜기
        stcData.bufferedImage=stcData.capture(self)
        captureApp().Show()
        self.Close(True)
    def onclickbtn_close(self, e): #끄기
        self.Close(True)     
        
        
if __name__=="__main__":
    app = wx.App()
    frame = startApp()
    frame.Show()
    app.MainLoop()