import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Hilloy')


app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
