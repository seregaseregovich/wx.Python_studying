import wx

# App - класс общего функционала приложения
app = wx.App()

# Frame - класс отдельного окна (их может быть несколько
# Конструктор Frame():
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
frame = wx.Frame(None, title='Helloy', pos=(100, 100),
                 size=(800, 600), style=wx.MINIMIZE_BOX |
                                        wx.MAXIMIZE_BOX |
                                        wx.RESIZE_BORDER |
                                        wx.SYSTEM_MENU |
                                        wx.CAPTION |
                                        wx.CLOSE_BOX |
                                        wx.CLIP_CHILDREN,
                 name='AAAAAA')
# МЕТОДЫ (некоторые):
# frame.Center()  # метод для размещения окна в центре экрана;
# frame.Close()  # закрывает окно;
# frame.Maximize()  # распахивает окно на весь экран;
# frame.Move(300, 400)  # располагает окно со смещением х, у;
# frame.SetPosition( pt: wx.Point(100, 200))  # помещает окно
#   с начальной точкой pt, например:
# frame.SetPosition(wx.Point(0, 0))
# frame.SetSize(x, y, wight, height)  # положение и размер окна.
frame.Show()


# Метод реализует обработку всех событий
app.MainLoop()
