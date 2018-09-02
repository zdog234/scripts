from subprocess import Popen, PIPE, STDOUT
from pathlib import Path
import wx


def get_input():
    app = wx.App()
    frame = wx.Frame(None, -1, 'Hello World')
    frame.add(wx.TextCtrl())
    frame.Show()
    app.MainLoop()


def create_note():
    Popen("C:\\Program Files (x86)\\Evernote\\Evernote\\ENScript.exe")


if __name__ == '__main__':
    get_input()
