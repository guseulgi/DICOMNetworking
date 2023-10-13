import wx


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(350, 400))

        vBoxP = wx.BoxSizer(wx.VERTICAL)

        # Top Section
        topP = wx.Panel(self, -1, size=(350, 80))
        topP.SetBackgroundColour('#fff')

        grid_top = wx.GridSizer(1, 5, 0, 0)

        self.title_label = wx.StaticText(topP, label="Example\nFrame!")
        self.title_label.SetFont(wx.Font(17,  wx.DEFAULT, wx.NORMAL, wx.BOLD))

        bitmap = wx.Bitmap('./sources/logo.png')
        image = bitmap.ConvertToImage()
        image = image.Scale(32, 32, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        control = wx.StaticBitmap(topP, -1, result)

        grid_top.AddMany([
            (wx.Panel(topP, size=(10, 0)), 1, wx.EXPAND | wx.ALL, 5),
            (self.title_label, 1, wx.EXPAND | wx.ALL, 5),
            (wx.Panel(topP, size=(30, 0)), 1, wx.EXPAND | wx.ALL, 5),
            (control, 1, wx.EXPAND | wx.ALL, 5),
            (wx.Panel(topP, size=(10, 0)), 1, wx.EXPAND | wx.ALL, 5),
        ])

        topP.SetSizer(grid_top)

        # mid Section
        midP = wx.Panel(self, -1)
        bottomP = wx.Panel(self, -1)

        vBoxP.Add(topP, 1, wx.EXPAND | wx.ALL, 5)
        vBoxP.Add(midP, 1, wx.EXPAND | wx.ALL, 5)
        vBoxP.Add(bottomP, 1, wx.EXPAND | wx.ALL, 5)

        # 메뉴바
        menu_bar = wx.MenuBar()
        file = wx.Menu()
        edit = wx.Menu()
        view = wx.Menu()
        help = wx.Menu()
        menu_bar.Append(file, '&File')
        menu_bar.Append(edit, '&Edit')
        menu_bar.Append(view, '&View')
        menu_bar.Append(help, '&help')
        self.SetMenuBar(menu_bar)

        file.Append(101, 'Example menu')
        file.Append(102, 'Exit')
        help.Append(301, 'Info')

        self.SetSizer(vBoxP)

        self.Centre()


def openFrame():
    app = wx.App()
    frame = MainFrame(None, -1, 'Example Framess')

    frame.Show()
    app.MainLoop()
