import keyboard,time,pywinauto,pyautogui

def sendto():
    start = pyautogui.locateCenterOnScreen('start.png')
    print(start)
    pyautogui.doubleClick(start)
    #app = pywinauto.application.Application(backend="uia")
    #app.connect( path=r"C:\\Program Files\\Cakewalk\\Cakewalk Core\\Cakewalk.exe")
    #handles = pywinauto.findwindows.find_windows()
    #for w_handle in handles:
        #wind = app.window_(handle=w_handle)
        #if "Auto-Key" in wind.window_text():
            #wind.click_input(coords=(270, 220))

def start():
    while True:
        if keyboard.read_key() == "space":
            time.sleep(5)
            sendto()    
            break
while True:
    if keyboard.read_key() == "space":
        time.sleep(20)
        sendto()
        break

