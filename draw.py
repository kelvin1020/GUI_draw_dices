import random
import time

t0 = 1 
t1 = 100
d = 1

a = [str(x) for x in range(t0,t1 + 1, d)]# a 为列表
b = []
nn = [0]
def choice(event):
	time.sleep(1)
	rm = random.choice(a)
	a.remove(rm)#无放回抽签
	b.append(rm)

	if ((len(b)-nn[0])%10 == 0):
		b.append('\n')
		nn[0] += 1 
	bstr = ', '.join(b)
#随机输出数字
	ctn = wx.TextCtrl(win,-1,str(rm),pos = (95,225),size = (240, 160),style = (wx.TE_CENTER |wx.TE_READONLY))
	font = wx.Font(100,wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
	ctn.SetFont(font)

#已输出的
	dtn = wx.TextCtrl(win,-1,bstr,pos = (95,85),size = (240, 120),style = (wx.TE_LEFT |wx.TE_READONLY))
	font = wx.Font(15,wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
	dtn.SetFont(font)


#mac
#conda install python.app
#pythonw *.py

#linux
#conda install wxpython
#python *.py

import wx
app = wx.App()
win = wx.Frame(None, title = '抽奖器',size = (450,500))


win.Show()

btn = wx.Button(win, label = '抽奖', pos = (165,45), size = (80, 25))
btn.Bind(wx.EVT_BUTTON, choice)

codes = 'ctn = wx.TextCtrl(win,-1,"",pos = (95,225),size = (240, 160),style = (wx.TE_CENTER |wx.TE_READONLY));font = wx.Font(100,wx.DECORATIVE, wx.ITALIC, wx.NORMAL);ctn.SetFont(font)'
exec(codes)

codes = 'dtn = wx.TextCtrl(win,-1,"",pos = (95,85),size = (240, 120),style = (wx.TE_LEFT |wx.TE_READONLY));font = wx.Font(15,wx.DECORATIVE, wx.ITALIC, wx.NORMAL);dtn.SetFont(font)'
exec(codes)

app.MainLoop()
