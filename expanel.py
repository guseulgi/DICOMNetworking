import wx


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(350, 400))

        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('#ccc')
        vBoxP = wx.BoxSizer(wx.VERTICAL)

        topP = wx.Panel(panel, -1)
        topP.SetBackgroundColour('#666')

        midP = wx.Panel(panel, -1)
        bottomP = wx.Panel(panel, -1)

        vBoxP.Add(topP, 1, wx.EXPAND | wx.ALL, 5)
        vBoxP.Add(midP, 1, wx.EXPAND | wx.ALL, 5)
        vBoxP.Add(bottomP, 1, wx.EXPAND | wx.ALL, 5)

        menu_bar = wx.MenuBar()
        file = wx.Menu()
        edit = wx.Menu()
        help = wx.Menu()
        menu_bar.Append(file, '&File')
        menu_bar.Append(edit, '&Edit')
        menu_bar.Append(help, '&help')
        self.SetMenuBar(menu_bar)

        file.Append(101, 'Example menu')
        file.Append(102, 'Exit')
        help.Append(301, 'Info')

        panel.SetSizer(vBoxP)
        self.Centre()


def openFrame():
    app = wx.App()
    frame = MainFrame(None, -1, 'Example Framess')

    frame.Show()
    app.MainLoop()


openFrame()
