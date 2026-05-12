import wx
import pandas as pd
import matplotlib.pyplot as plt

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

        button.Bind(wx.EVT_BUTTON, self.load_data)

        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.AddStretchSpacer()
        sizer.Add(button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer.AddStretchSpacer()

        panel.SetSizer(sizer)

        self.Show()

    def load_data(self, event):

        df = pd.read_csv(
            "student_data.csv",
            sep=";"
        )

        plt.figure(figsize=(8,5))

        plt.scatter(
            df["studytime"],
            df["G3"]
        )

        plt.title("Study Time vs Final Grade")

        plt.xlabel("Study Time")
        plt.ylabel("Final Grade")

        plt.grid(True)

        plt.show()

app = wx.App()
frame = StudentVisualizer()
app.MainLoop()