# =============================================================
# ТИПОВАЯ ЗАГОТОВКА ДЛЯ СОЗДАНИЯ ТИПОВОГО ОКНА.
# =============================================================
import wx

# App() - класс общего функционала приложения.
# Создаем экземпляр app - производим инициализацию приложения
app = wx.App()

# Frame - класс для создания стандартного окна (их может быть несколько
# Конструктор Frame() - структура:
# wx.Frame(parent, id=-1, title='', pos=wx.DefaultPosition,
#   size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE,
#   name='frame'),
# где:
# - parent - ссылка на родительское окно, с которым связан
#   данный frame. Если это первое окно, то значение None;
# - id - (id при необходимости);
# - title='' - заголовок в полоске окна сверху;
# - pos=wx.DefaultPosition - позиция окна;
# - size = wx.DefaultSize - размер окна;
# - style=wx.DEFAULT_FRAME_STYLE - стиль окна по умолчанию;
# - name='frame' - имя окна.

# Стиль окна:
# DEFAULT_FRAME_STYLE=wx.MINIMIZE_BOX |
#   wx.MAXIMIZE_BOX | wx.RESIZE_BORDER |
#   wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX |
#   wx.CLIP_CHILDREN
# Стиль окна состоит из:
# - wx.MINIMIZE_BOX - кнопка для свертывания окна;
# - wx.MAXIMIZE_BOX - кнопка для полного развертывания окна;
# - wx.RESIZE_BORDER - кнопка для закрытия окна;
# - wx.SYSTEM_MENU - разрешение для системного меню;
# - wx.CAPTION - разрешение полосы с заголовком окна;
# - wx.CLOSE_BOX - кнопка для закрытия окна;
# - wx.CLIP_CHILDREN - кнопка для

# С помощью класса Frame() создаем окно (экз.класса - frame).
frame1 = wx.Frame(None, title='Frame 1', pos=(100, 100),
                  size=(1200, 600), style=wx.MINIMIZE_BOX |
                                          wx.MAXIMIZE_BOX |
                                          wx.RESIZE_BORDER |
                                          wx.SYSTEM_MENU |
                                          wx.CAPTION |
                                          wx.CLOSE_BOX |
                                          wx.CLIP_CHILDREN,
                  name='AAAAAA')

frame2 = wx.Frame(frame1, title='Frame 2 (parent = frame 1)', pos=(120, 120),
                  size=(600, 500), style=wx.MINIMIZE_BOX |
                                         wx.MAXIMIZE_BOX |
                                         wx.RESIZE_BORDER |
                                         wx.SYSTEM_MENU |
                                         wx.CAPTION |
                                         wx.CLOSE_BOX |
                                         wx.CLIP_CHILDREN,
                  name='AAAAAA')
# МЕТОДЫ класса Frame() (некоторые):
# frame.Center()  # метод для размещения окна в центре экрана;
# frame.Close()  # закрывает окно;
# frame.Maximize()  # распахивает окно на весь экран;
# frame.Move(300, 400)  # располагает окно со смещением х, у;
# frame.SetPosition( pt: wx.Point(100, 200))  # помещает окно
#   с начальной точкой pt, например:
# frame.SetPosition(wx.Point(0, 0))
# frame.SetSize(x, y, wight, height)  # положение и размер окна.

# С помощью класса Show() отображаем окно frame
frame1.Show()
frame2.Show()

# Метод MainLoop() реализует обработку всех событий.
# Запускаем главный цикл обработки событий.
app.MainLoop()
