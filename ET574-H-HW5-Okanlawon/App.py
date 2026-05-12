import wx
import pandas as pd

class StudentVisualizer(wx.Frame):

    def __init__(self):

        super().__init__(
            parent=None,
            title="Student Performance Visualizer",
            size=(700, 500)
        )

        panel = wx.Panel(self)

        button = wx.Button(
            panel,
            label="Open Student Dataset"
        )

        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.AddStretchSpacer()
        sizer.Add(button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer.AddStretchSpacer()

        panel.SetSizer(sizer)

        self.Show()

app = wx.App()
frame = StudentVisualizer()
app.MainLoop()