import wx

app = wx.App()

frame = wx.Frame(
    parent=None,
    title="Student Performance Visualizer"
)

frame.Show()

app.MainLoop()