import wx


class MyFrame(wx.MDIParentFrame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)

        win = wx.MDIChildFrame(self, -1, 'Child Window', size=(300, 150))
        win.Show()


app = wx.App()

frame = MyFrame(None, title='Main Window')
frame.Show()

app.MainLoop()
