import wx

ID_EXIT = 1
VIEW_STATUS = 2
RGB = 3
SRGB = 4


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        menubar = wx.MenuBar()  # Создание панели меню.
        filemenu = wx.Menu()  # Создание вкладки меню

        expmenu = wx.Menu()
        expmenu.Append(wx.ID_ANY, 'Экспорт изображения')
        expmenu.Append(wx.ID_ANY, 'Экспорт видео')
        expmenu.Append(wx.ID_ANY, 'Экспорт данных')

        filemenu.Append(wx.ID_NEW, '&Новый\tCTRL+N')
        filemenu.Append(wx.ID_NEW, '&Открыть\tCTRL+O')
        filemenu.Append(wx.ID_NEW, '&Сохранить\tCTRL+S')
        filemenu.AppendSubMenu(expmenu, '&Экспорт')
        filemenu.AppendSeparator()

        # item = wx.MenuItem(filemenu, wx.ID_EXIT,
        #                    'Выход', 'Выход из приложения')
        # filemenu.Append(item)
        # можно записать одной строкой:
        item = filemenu.Append(wx.ID_EXIT, 'Выход\tCtrl+Q',
                               'Выход из приложения')

        viewmenu = wx.Menu()
        self.vstatus = viewmenu.Append(VIEW_STATUS, 'Статусная строка',
                                       kind=wx.ITEM_CHECK)
        viewmenu.AppendSeparator()
        self.vRGB = viewmenu.Append(RGB, 'Тип RGB',
                                    'Тип RGB', kind=wx.ITEM_RADIO)
        self.vsRGB = viewmenu.Append(SRGB, 'Тип sRGB',
                                     'Тип sRGB', kind=wx.ITEM_RADIO)

        menubar.Append(filemenu, '&File')
        menubar.Append(viewmenu, '&Вид')

        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.onQuit, item)
        self.Bind(wx.EVT_MENU, self.onstatus, id=VIEW_STATUS)
        self.Bind(wx.EVT_MENU, self.onimagetype, id=RGB)
        self.Bind(wx.EVT_MENU, self.onimagetype, id=SRGB)

    def onQuit(self, event):
        print('Выход из программы.')
        self.Close()

    def onstatus(self, event):
        if self.vstatus.IsChecked():
            print("Статусная строка активирована.")
        else:
            print("Статусная строка деактивирована.")

    def onimagetype(self, event):
        if self.vRGB.IsChecked():
            print('Режим RGB активирован.')
        elif self.vsRGB.IsChecked():
            print('Режим sRGB активирован.')


app = wx.App()

frame = MyFrame(None, title='Main Window')
frame.Show()

app.MainLoop()


# Для создания меню используется 3 класса:
#       MenuBar - для создания панели меню;
#       Menu - для создания вкладки меню (по аналогии - File);
#       MenuItem - для создания отдельного пункта меню.
