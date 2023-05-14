# ==============================================================
# ПРИМЕР СОЗДАНИЯ ОКНА С ТРЕМЯ ДОЧЕРНИМИ ОКНАМИ ВНУТРИ
# ==============================================================
import wx


class MyFrame(wx.MDIParentFrame):
    def __init__(self, parent, title):  # конструктор для инициализации
        super().__init__(parent, title=title)

        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)

        win1 = wx.MDIChildFrame(self, -1, 'Child Window1', size=(100, 150))
        win1.Show()

        win2 = wx.MDIChildFrame(self, -2, 'Child Window2', size=(100, 150))
        win2.Show()

        win3 = wx.MDIChildFrame(self, -2, 'Child Window3', size=(100, 150))
        win3.Show()


app = wx.App()

frame = MyFrame(None, title='Parent Window')
frame.Show()

app.MainLoop()


# MDIParentFrame() - родительский класс для создания основоного окна
#       многооконного интерфейса. С ним связан класс MDIChildFrame(),
#       с помощью экземпляров которого можно создать окно или
#       несколько окон внутри класса MDIParentFrame.
# Метод MenuBar() класса MDIParentFrame() создает панель, где можно
#       создать меню. Без этого метода класс MDIParentFrame() не работает.
# MDIChildFrame() - с помощью этого класса создаются дочерние окна
#       внутри класса MDIParentFrame().

# Также существуют следующие классы:
# PopupWindow() - специальный оконный класс для
#       создания popup-меню, списков combobox и других вспомогательных
#       виджетов подобного рода.
# ScrolledWindow() - используется для создания окна с
#       прокручиваемым содержимым.
# Frame() - класс для создания стандартного окна (смотри file_1.py).
# Dialog() - класс для создания диалоговых окон.
# ScrolledWindow() - класс (контейнер) с прокручиваемым содержимым.
# SplitterWindow() - класс (контейнер) с разделительной полосой,
#       которую можно перемещать, изменяя размеры соответствующих
#       содержимых.
# Notebook() - класс для создания tab-интерфейса (панель со вкладками).

# ВИДЖЕТЫ:
# Для динамических виджетов:
#   Button - обычная кнопка
#   BitmapButton -
#   ToggleButton -
#   SpinButton -
#   RadioButton -
#   CheckBox -
#
