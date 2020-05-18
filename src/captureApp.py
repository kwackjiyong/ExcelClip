import wx
import sys
import ctypes

from src.stcData import stcData



class captureApp(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title = "TEST")
        self.InitUI()
 
    def InitUI(self):
        self.Bind(wx.EVT_LEFT_DOWN, self.ShowMessage)
        self.Bind(wx.EVT_RIGHT_DOWN, self.ShowMessageR)
        
        #사이즈를 얻습니다.
        #self.SetSize(wx.GetDisplaySize())
        self.Maximize(True)
        self.Move(0, -200, 0)
        self.SetTitle('ExcelClip [캡처 준비]')
        #닫기 버튼
#         btn_cap = wx.Button(self, label='닫기', pos=(20, 30))
#         btn_cap.SetSize(20, 10, 100, 50)
#         btn_cap.Bind(wx.EVT_BUTTON, self.onclickbtn_close)
        wx.EVT_PAINT(self,self.OnPaint)
        self.Centre()
    def OnPaint(self,event):
        dc = wx.PaintDC(self)
        
        dc.DrawBitmap(stcData.bufferedImage, 0, 0)
        
    def ShowMessage(self, event):
        wx.MessageBox('왼쪽 클릭', 'EVT_LEFT_DOWN', wx.OK)

    def ShowMessageR(self,event):
        wx.MessageBox('닫습니다.', '닫기', wx.OK)
        self.Close()
    def onclickbtn_close(self,event):
        self.Close()
        
if __name__=="__main__":
    app = wx.App()
    cframe = captureApp()
    cframe.Show()
    app.MainLoop()