import wx
import sys
import ctypes
from src.stcData import stcData
from src.saveApp import saveApp



class captureApp(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title = "TEST", style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        self.InitUI()
 
    def InitUI(self):
        self.Bind(wx.EVT_LEFT_DOWN, self.MouseCheck_st)
        self.Bind(wx.EVT_LEFT_UP, self.MouseCheck_ls)
        self.Bind(wx.EVT_RIGHT_DOWN, self.ShowMessageR)
        self.Maximize(True)
        self.Move(0, -200, 0)
        self.SetTitle('ExcelClip [캡처 준비]    캡처할 부분을 마우스로 드래그 해주세요!')
        self.SetIcon(wx.Icon('images/clipicon.ico', wx.BITMAP_TYPE_ICO))
        wx.EVT_PAINT(self,self.OnPaint)
        self.Centre()
    def OnPaint(self,event):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(stcData.bufferedImage, 0, 0,useMask=False)
        
    def MouseCheck_st(self, event):
        x, y = event.GetPosition() #마우스 포지션 겟
        stcData.x1 = x
        stcData.y1 = y
    def MouseCheck_ls(self,event):
        x, y = event.GetPosition() #마우스 포지션 겟
        stcData.x2 = x
        stcData.y2 = y
        #self.Hide()
        self.Close()
        saveApp().Show()
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