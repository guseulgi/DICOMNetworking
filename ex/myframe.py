import wx

# ### 최상위 윈도우
# Frame, Dialog 같은 윈도우들로 다른 컨테이너에 포함 될 수 없다.
# 비주얼 윈도우의 최상위 계층


class MyFrame(wx.Frame):
    def __init__(self, parent, title=''):
        super(MyFrame, self).__init__(parent, title=title)

        self.SetIcon(wx.Icon("./sources/logo.png"))

        self.panel = MyPanel(self)

# ### 일반적인 컨테이너
# Panel, Notebook, ....
# 컨트롤을 그룹으로 묶거나 배치를 할 때 사용
# 다른 컨테니어나 컨트롤을 가질 수 있다.


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        font1 = wx.Font(10, wx.DEFAULT, wx.ITALIC, wx.NORMAL)
        s = wx.StaticText(self, -1, '폰트', (20, 30), style=wx.ALIGN_CENTER)
        s.SetFont(font1)

        self.button = wx.Button(self, label='Push me')

        # self.SetCursor(wx.CURSOR_HAND)


# ### 컨트롤
# Button, CheckBox, ComboBox, ....
# 다른 컨트롤을 포함할 수 없는 컨트롤
# 트리의 최하 레벨


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title='Main Frame')
        self.frame.Show()
        return super().OnInit()


if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
