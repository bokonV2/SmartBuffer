from keyboard import on_release_key, send, write, wait, remove_hotkey, add_hotkey, remap_hotkey, unhook_all_hotkeys
import time
import win32com.client
shell = win32com.client.Dispatch('WScript.Shell')
import pynput


class Buff():

    def __init__(self):
        self.buff0 = ""
        self.buff1 = ""
        self.buff2 = ""
        self.hotkey = "ctrl + b"
        self.hotkey2 = "ctrl + n"
        self.hotkey3 = "ctrl + m"
        self.hotkey4 = "space"
        self.i = 0
        self.whait = 0.5
        self.listHotkey = [[self.hotkey,self.pastBuff0], [self.hotkey2,self.pastBuff1],[self.hotkey3,self.pressMouse], [self.hotkey4, self.pastLine]]


    def pastBuff0(self):
        print("Buff0")
        write(self.buff0, delay=0.001)
        send('enter')

    def pastBuff1(self):
        print("Buff1")
        write(self.buff1, delay=0.001)
        send('enter')

    def pastLine(self):
        print(self.buff2.split())
        line = self.buff2.split()

        if self.i == 0:
            self.i = len(line)

        write(line[len(line)-self.i], delay=0.001)
        send('enter')
        self.i-=1



    def AddHotKey(self):
        print("Запуск скрипта\n",self.listHotkey)
        self.liveWork = True
        for i in self.listHotkey:
            add_hotkey(i[0], i[-1])

    def RemapHotKey(self, hotkey = None, hotkey2 = None, hotkey3 = None, hotkey4 = None):
        try:
            self.RemoveHotKey()
        except:
            pass

        if hotkey != None: self.hotkey = hotkey

        if hotkey2 != None: self.hotkey2 = hotkey2

        if hotkey3 != None: self.hotkey3 = hotkey3

        if hotkey4 != None: self.hotkey4 = hotkey4

        self.listHotkey = [[self.hotkey,self.pastBuff0], [self.hotkey2,self.pastBuff1],[self.hotkey3,self.pressMouse], [self.hotkey4, self.pastLine]]

        if len(self.hotkey) == 1: self.RemapKey(self.hotkey)
        if len(self.hotkey2) == 1: self.RemapKey(self.hotkey2)
        if len(self.hotkey3) == 1: self.RemapKey(self.hotkey3)
        if len(self.hotkey4) == 1 or self.hotkey4 == "space": self.RemapKey(self.hotkey4); print("remap space")


    def RemapKey(self,key):
        print("RemapKey "+key)
        remap_hotkey(key, 'ctrl+{}'.format(key))

    def RemoveHotKey(self):
        for i in self.listHotkey:
            remove_hotkey(i[0])
        print("Остановка скрипта")
        unhook_all_hotkeys()

    def Wait(self):
        wait("Ctrl + q")
        print(self.x)
        print(self.y)

    def on_click(self, x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
        self.x = x
        self.y = y
        if not pressed:
            return False

    def Mouse(self):
        print("mouse!")
        with pynput.mouse.Listener(on_click=self.on_click) as listener:
            listener.join()

    def pressMouse(self):
        print("mouse!2")
        controller = pynput.mouse.Controller()
        controller.position = (self.x, self.y)
        controller.click(pynput.mouse.Button.left, 1)
