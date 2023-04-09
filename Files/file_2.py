import wx

# класс MDIParentFrame() создает многооконный интерфейс.
# С ним связан класс MDIChildFrame(), который
# создает дочерний класс (окно) внутри класса MDIParentFrame.
class MyFrame(wx.MDIParentFrame):
    def __init__(self, parent, title):  # конструктор для инициализации
        super().__init__(parent, title=title)

        # Метод MenuBar() создает панель, где можно создать
        #  меню. Без этого метода класс MDIParentFrame() не работает.
        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)

        # С помощью класса MDIChildFrame() создаются дочерние окна.
        win1 = wx.MDIChildFrame(self, -1, 'Child Window1', size=(100, 150))
        win1.Show()

        win2 = wx.MDIChildFrame(self, -2, 'Child Window2', size=(100, 150))
        win2.Show()


app = wx.App()

frame = MyFrame(None, title='Parent Window')
frame.Show()

app.MainLoop()
