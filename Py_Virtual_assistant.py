import wx
import wikipedia
import wolframalpha

class MyFrame(wx.Frame):
    
    def onButton(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            #wolframalpha
            app_id = "YKTE2W-HRKGEVQRTP"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print (answer)
        except:
            #wikipedia
            print (wikipedia.summary(input))
            
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos= wx.DefaultPosition, size=wx.Size(450, 200),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am PyDA the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        #self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        button = wx.Button(panel, wx.ID_ANY, 'Answer', (150, 100))
        button.Bind(wx.EVT_BUTTON, self.onButton)

        self.Show()
    
    

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()