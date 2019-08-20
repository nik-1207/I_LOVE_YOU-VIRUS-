import os
from pynput.keyboard import Key, Controller
import time
def hang():
    M = Controller()
    time.sleep(0.5)

    M.press(Key.cmd)
    M.release(Key.cmd)

    M.press(Key.caps_lock)
    M.release(Key.caps_lock)

    M.press(Key.backspace)
    M.release(Key.backspace)

    M.press(Key.up)
    M.release(Key.up)
    M.press(Key.enter)
    M.release(Key.enter)

    M.press(Key.down)
    M.release(Key.down)
    M.press(Key.enter)
    M.release(Key.enter)

    M.press(Key.left)
    M.release(Key.left)
    M.press(Key.enter)
    M.release(Key.enter)

    M.press(Key.right)
    M.release(Key.right)
    M.press(Key.enter)
    M.release(Key.enter)

    M.press(Key.num_lock)
    M.release(Key.num_lock)

    M.press(Key.scroll_lock)
    M.release(Key.scroll_lock)

    M.press(Key.pause)
    M.release(Key.pause)

    M.press(Key.ctrl_l)
    M.press(Key.alt)
    for i in (Key.up, Key.down, Key.left, Key.right, Key.up):
        M.press(i)
        M.release(i)
    M.release(Key.ctrl_l)
    M.press(Key.alt)
    return None
def m_c():
    from pynput.mouse import Button,Controller
    mouse=Controller()
    for i in range(0,1365):
        for j in range(0,767):
            mouse.move(i,j)
            return None
def i_love_you():
    from gtts import gTTS
    speech=gTTS("I love you",'en','slow')
    speech.save("sample.mp3")
    return None
def play():
    os.system("path for sample.m3 file")
    return None
i_love_you()
while(1):
    m=Controller()
    hang()
    m_c()
    play()
    time.sleep(0.45)
    m.press(Key.alt)
    m.press(Key.f4)
    m.release(Key.alt)
    m.release(Key.f4)




