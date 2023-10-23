import wx
import os
from wx.adv import DatePickerCtrl

# import utils

# ### 최상위 윈도우
# Frame, Dialog 같은 윈도우들로 다른 컨테이너에 포함 될 수 없다.
# 비주얼 윈도우의 최상위 계층

# wx.Frame 생성자 는 여러 스타일 플래그를 제공한다.
# wx.DEFAULT_FRAME_STYLE  다음에 열거하는 모든 마스크 포함하는 bit mask
# wx.MINIMIZE_BOX 타이틀바에 최소화 버튼 표시
# wx.MAXIMIZE_BOX
# wx.RESIZE_BORDER  사용자가 윈도우 크기 조정가능
# wx.CAPTION  프레임의 타이틀바에 타이틀 설명 표시
# wx.CLOSE_BOX 닫기 버튼 표시
# wx.SYSTEM_MENU  시스템 메뉴 표시
# wx.CLIP_CHILDREN  백그라운드에서 다시 그릴 때 발생하는 깜빡임 제거(windows의 경우에만)


class MyFrame(wx.Frame):
    def __init__(self, parent, title=''):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))

        self.SetIcon(wx.Icon("../sources/logo.png"))

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.panel_1 = MyPanel(self)
        self.panel_2 = CheckboxPanel(self)
        self.panel_3 = ImagePanel(self)
        self.panel_4 = MyDropPanel(self)

        self.panel_5 = MyRadioPanel(self)

        vbox.AddMany([
            (self.panel_1, wx.EXPAND | wx.ALL),
            (self.panel_2, wx.EXPAND | wx.ALL),
            (self.panel_3, wx.EXPAND | wx.ALL),
            (self.panel_4, wx.EXPAND | wx.ALL),
            (self.panel_5, wx.EXPAND | wx.ALL),
        ])
        self.SetSizer(vbox)

        self.statusbar = self.CreateStatusBar(2)
        self.statusbar.SetStatusText('Statusbar!')


# ### 일반적인 컨테이너
# Panel, Notebook, ....
# 컨트롤을 그룹으로 묶거나 배치를 할 때 사용
# 다른 컨테니어나 컨트롤을 가질 수 있다.

class MyDropPanel(wx.Panel):
    def __init__(self, parent):
        super(MyDropPanel, self).__init__(parent)

        self.text = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.text.AppendText("Drag and Drop files")
        dropTarget = MyFileDropTarget(self.text)
        self.text = self.SetDropTarget(dropTarget)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        font1 = wx.Font(10, wx.DEFAULT, wx.ITALIC, wx.NORMAL)
        s = wx.StaticText(self, -1, '폰트', (20, 30), style=wx.ALIGN_CENTER)
        s.SetFont(font1)

        self.button_copy = wx.Button(self, label='Copy')
        self.button_paste = wx.Button(self, label='Paste')

        now = wx.DateTime.Now()
        self._dp = DatePicker(
            self, now, wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)

        vbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox.AddMany([
            (self.button_copy, wx.EXPAND | wx.ALL, 0),
            (self.button_paste, wx.EXPAND | wx.ALL, 0),
            (self._dp, wx.EXPAND | wx.ALL, 0),
        ])

        self.Bind(wx.EVT_BUTTON, self.OnButton)

        self.SetSizer(vbox)

    def OnButton(self, event):
        button = event.EventObject
        if button is self.button_copy:
            txt = GetClipboardText()
            print(txt)
        elif button is self.button_paste:
            SetClipboardText('test for clipboard')
            print("set")


class MyRadioPanel(wx.Panel):
    def __init__(self, parent):
        super(MyRadioPanel, self).__init__(parent)

        self.rb1 = wx.RadioButton(
            self, 11, label='Radio A', pos=(10, 10), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(self, 22, label='Radio B', pos=(10, 40))
        self.rb3 = wx.RadioButton(self, 33, label='Radio C', pos=(10, 70))

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.AddMany([
            (self.rb1, wx.EXPAND | wx.ALL | 0),
            (self.rb2, wx.EXPAND | wx.ALL | 0),
            (self.rb3, wx.EXPAND | wx.ALL | 0),
        ])

        self.SetSizer(self.vbox)


class CheckboxPanel(wx.Panel):
    def __init__(self, parent):
        super(CheckboxPanel, self).__init__(parent)

        vsizer = wx.BoxSizer(wx.VERTICAL)
        self.cbAll = wx.CheckBox(self, label='모두 선택', style=wx.CHK_3STATE)
        vsizer.Add(self.cbAll)
        self.option1 = wx.CheckBox(self, label='옵션 1')
        vsizer.Add(self.option1, flag=wx.LEFT, border=10)
        self.option2 = wx.CheckBox(self, label="옵션 2")
        vsizer.Add(self.option2, flag=wx.LEFT, border=10)

        self.SetSizer(vsizer)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)

    def OnCheckBox(self, event):
        check = event.EventObject
        if check is self.cbAll:
            self.option1.Value = check.Value
            self.option2.Value = check.Value
        else:
            values = [self.option1.Value, self.option2.Value]

        if all(values):
            self.cbAll.Set3StateValue(wx.CHK_CHECKED)
        elif any(values):
            self.cbAll.Set3StateValue(wx.CHK_UNDETERMINED)
        else:
            self.cbAll.Set3StateValue(wx.CHK_UNCHECKED)


def GetClipboardText():
    text_obj = wx.TextDataObject()
    rtext = ""
    if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
        if wx.TheClipboard.GetData(text_obj):
            rtext = text_obj.GetText()
            wx.TheClipboard.Close()
            return rtext


def SetClipboardText(text):
    data_o = wx.TextDataObject()
    data_o.SetText(text)
    if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
        wx.TheClipboard.SetData(data_o)
        wx.TheClipboard.Close()


class ImagePanel(wx.Panel):
    def __init__(self, parent):
        super(ImagePanel, self).__init__(parent)

        theBitmap = wx.Bitmap('../sources/logo.png')
        self.bitmap = wx.StaticBitmap(self, bitmap=theBitmap)
        self.bitmap.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDownThumbImage)

    def OnRightDownThumbImage(self, e):
        mpos = wx.GetMousePosition()
        pos = self.ScreenToClient(mpos)
        self.PopupMenu(PopMenu(self), pos)


# ### 컨트롤
# Button, CheckBox, ComboBox, ....
# 다른 컨트롤을 포함할 수 없는 컨트롤
# 트리의 최하 레벨

class PopMenu(wx.Menu):
    def __init__(self, parent):
        super(PopMenu, self).__init__()

        self.parent = parent

        pmnuOpenFolder = wx.MenuItem(self, wx.ID_ANY, '폴더열기')
        self.Append(pmnuOpenFolder)
        pmnuSaveAs = wx.MenuItem(self, wx.ID_ANY, '다른이름으로 저장')
        self.Append(pmnuSaveAs)
        pmnuDelete = wx.MenuItem(self, wx.ID_ANY, '삭제')
        self.Append(pmnuDelete)

        self.Bind(wx.EVT_MENU, self.OnOpenFolder, pmnuOpenFolder)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, pmnuSaveAs)
        self.Bind(wx.EVT_MENU, self.OnDelete, pmnuDelete)

    def OnOpenFolder(self, e):
        print("folder name: ", self.parent.fn)
        pass

    def OnSaveAs(self, e):
        pass

    def OnDelete(self, e):
        fn = self.parent.fn
        if os.path.exists(fn):
            os.remove(fn)

        pass


class DatePicker(wx.adv.DatePickerCtrl):
    def __init__(self, parent, dt, style=wx.adv.DP_DEFAULT):
        super(DatePicker, self).__init__(parent, dt=dt, style=style)
        self.SetInitialSize((120, -1))


class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, target):
        super(MyFileDropTarget, self).__init__()
        self.target = target

    def OnDropFiles(self, x, y, filenames):
        for fname in filenames:
            self.target.AppendText(fname)


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title='Main APP')

        self.frame.Bind(wx.EVT_SHOW, self.OnFrameShow)  # 프레임이 보일 떄 실행되는 이벤트
        self.frame.Bind(wx.EVT_CLOSE, self.OnFrameClose)  # 프레임이 닫힐 때
        self.frame.Bind(wx.adv.EVT_DATE_CHANGED, self.OnDateChange)

        self.frame.Show()

        return super().OnInit()

    def OnFrameShow(self, event):
        theFrame = event.EventObject
        print("Frame (%s) shown !" % theFrame.Title)
        event.Skip()

    def OnFrameClose(self, event):
        theFrame = event.EventObject
        print("Frame (%s) closing !" % theFrame.Title)
        event.Skip()

    def OnDateChange(self, evt):
        date = evt.GetDate()
        self.Title = date.Format()


if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
