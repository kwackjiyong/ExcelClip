import wx
class stcData:
    _instance = None
    bufferedImage = None
    @classmethod
    def _getInstance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance

    def __init__(self):
        self._dict = {}

    def setitem(self, key, item):
        self._dict[key] = item
        
    def capture(self):
        screen = wx.ScreenDC()
        bmp = wx.Bitmap(1920,1080)
        mem = wx.MemoryDC(bmp)
        mem.Blit(0,0,1920,1080,screen,0,0)
        del mem
        bmp.SaveFile('wx1.bmp',wx.BITMAP_TYPE_BMP)
        bufferedImage =bmp
        return bufferedImage