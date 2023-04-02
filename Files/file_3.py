import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)


app = wx.App()

frame = MyFrame(None, title='Main Window')
frame.Show()

app.MainLoop()
