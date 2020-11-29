import wx
import wx.grid
import sys
import ctypes
import cv2
import numpy
import pytesseract
import clipboard
import os
import pandas as pd
from src.stcData import stcData
from wx import Bitmap
import time




class saveApp(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title = "TEST" , style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        self.SetSize(0,0,600,230, 0)
        #패널 생성
        panel = wx.Panel(self, -1,pos=(20, 30)) 
        #패널->멀티라인 텍스트박스 생성 
        multiLabel = wx.StaticText(panel, -1, "검출 결과", pos=(20, 30))
        #Tesseract OCR 부분
        stcData.bufferedImage_cut = stcData.cut()#드래그한만큼 자릅니다.
        
        
        #stcData.resultText = pytesseract.image_to_string('images/wx2.png',lang='kor+eng', config='--psm 1 -c preserve_interword_spaces=1') # OCR
        
        try:
            stcData.dataframe = stcData.tabledetection()
            stcData.dataframe
        except Exception as ex:
            wx.MessageBox('표를 찾을 수 없었습니다.', '닫기', wx.OK)
        #멀티라인 텍스트
        multiText = wx.TextCtrl(panel, -1,stcData.dataframe.to_string(),size=(500, 100), style=wx.TE_MULTILINE)
        multiText.SetInsertionPoint(0)
        
        #그리드 
        
        
        
        
        #닫기버튼
        btn_clip = wx.Button(panel, label='클립보드 저장', pos=(10, 150))
        btn_clip.Bind(wx.EVT_BUTTON, self.onclickbtn_clip)
        
        #처음버튼
        btn_excel = wx.Button(panel, label='엑셀로 저장', pos=(120, 150))
        btn_excel.Bind(wx.EVT_BUTTON, self.onclickbtn_excel)
        
        #닫기버튼
        btn_close = wx.Button(panel, label='닫기', pos=(220, 150))
        btn_close.Bind(wx.EVT_BUTTON, self.onclickbtn_close)
        
        #사이저
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([multiLabel, multiText])
        panel.SetSizer(sizer)
        self.InitUI()
        
    def InitUI(self):
        
        #사이즈를 얻습니다.
        #self.SetSize(wx.GetDisplaySize())
        self.SetTitle('ExcelClip [저장하기]')
        self.SetIcon(wx.Icon('images/clipicon.ico', wx.BITMAP_TYPE_ICO))
        pt = wx.Point(stcData.x1,stcData.y1) #포인트
        sz = wx.Size(stcData.x2-stcData.x1,stcData.y2-stcData.y1)#사이즈
        #self.SetSize(0,0,sz.x+10,sz.y+40, 0)
        
        
        self.Centre()
        
        
        #wx.EVT_PAINT(self,self.OnPaint)
        
    def OnPaint(self,event):
        dc = wx.PaintDC(self)
        
        dc.DrawBitmap(stcData.bufferedImage_cut, 60, 300,useMask=False)
        
        
    def ShowMessageR(self,event):
        wx.MessageBox('닫습니다.', '닫기', wx.OK)
        self.Close()
    def onclickbtn_close(self,event):
        self.Close()
    def onclickbtn_excel(self,event):
        filepath = os.path.join(os.path.expanduser('~'),'Downloads')
        now = time.localtime()
        timestr = str(now.tm_year)+'년'+str(now.tm_mon)+'월'+ str(now.tm_mday)+'일'+str(now.tm_hour)+'시'+str(now.tm_min)+'분'+str(now.tm_sec) +'초'

        stcData.dataframe.to_excel(filepath+"\ExcelClip_OutPut_"+timestr+".xlsx")
        wx.MessageBox('Downloads/ExcelClip_OutPut_'+timestr+'.xlsx로 저장되었습니다.', '확인', wx.OK)
        
    def onclickbtn_clip(self,event):
        #clipboard.copy(stcData.resultText)
        stcData.dataframe.to_clipboard()
        wx.MessageBox('클립보드에 저장되었습니다.', '확인', wx.OK)
if __name__=="__main__":
    app = wx.App()
    sframe = saveApp()
    sframe.Show()
    app.MainLoop()