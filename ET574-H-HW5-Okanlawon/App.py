import wx

class StudentVisualizer(wx.Frame):

    def __init__(self):

        super().__init__(
            parent=None,
            title="Student Performance Visualizer",
            size=(700, 500)
        )

        panel = wx.Panel(self)

        self.Show()

app = wx.App()
frame = StudentVisualizer()
app.MainLoop()