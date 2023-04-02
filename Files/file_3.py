import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        menubar = wx.MenuBar()
        filemenu = wx.Menu()

        expmenu = wx.Menu()
        expmenu.Append(wx.ID_ANY, 'Экспорт изображения')
        expmenu.Append(wx.ID_ANY, 'Экспорт видео')
        expmenu.Append(wx.ID_ANY, 'Экспорт данных')

        filemenu.Append(wx.ID_NEW, '&Новый\tCTRL+N')
        filemenu.Append(wx.ID_NEW, '&Открыть\tCTRL+O')
        filemenu.Append(wx.ID_NEW, '&Сохранить\tCTRL+S')
        filemenu.AppendSubMenu(expmenu, '&Экспорт')
        filemenu.AppendSeparator()



        # item = wx.MenuItem(filemenu, wx.ID_EXIT, 'Выход', 'Выход из приложения')
        # filemenu.Append(item)
        # можно записать одной строкой:
        item = filemenu.Append(wx.ID_EXIT, 'Выход\tCtrl+Q', 'Выход из приложения')

        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onQuit, item)


    def onQuit(self, event):
        self.Close()


app = wx.App()

frame = MyFrame(None, title='Main Window')
frame.Show()

app.MainLoop()
