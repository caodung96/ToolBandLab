import keyboard,time,pywinauto,pyautogui,subprocess 

def importfile(window,name):
    window.child_window(title="File", control_type="MenuItem").click_input()
    window.child_window(title="Import", control_type="MenuItem").click_input()
    window.child_window(title="Audio...", auto_id="32892", control_type="MenuItem").click_input()
    window.child_window(title="This PC", control_type="Button").click_input()
    window.child_window(title="Local Disk (D:)", control_type="ListItem").click_input(button='left', double=True)
    window.child_window(title="1.Tool", control_type="Edit").click_input(button='left', double=True)
    window[name].click_input(button='left', double=True)


def exportfile(window,pwa_app):
    window.child_window(title="File", control_type="MenuItem").click_input()
    window.child_window(title="Export", control_type="MenuItem").click_input()
    window["Audio..."].click_input()
    pyautogui.press("R")    
    pyautogui.press("e")    
    pyautogui.press("s")    
    pyautogui.press("u")    
    pyautogui.press("l")    
    pyautogui.press("t")    
    handles = pywinauto.findwindows.find_windows()
    for w_handle in handles:
        wind = pwa_app.window_(handle=w_handle)
        if "Export Audio" in wind.window_text():
            wind.print_control_identifiers()
def sendto():
    start = pyautogui.locateCenterOnScreen('start.png')
    print(start)
    pyautogui.doubleClick(start)


def main():
    pig = subprocess.Popen(["C:\Program Files\Cakewalk\Cakewalk Core\Cakewalk.exe"], stdin=subprocess.PIPE) 
    time.sleep(2.0)
    pwa_app = pywinauto.application.Application(backend="uia")
    pwa_app.connect( path=r"C:\\Program Files\\Cakewalk\\Cakewalk Core\\Cakewalk.exe")
    time.sleep(5)
    New = pyautogui.locateCenterOnScreen('Click1.png')
    print(New)
    pyautogui.doubleClick(New)
    time.sleep(5)
    w_handle = pywinauto.findwindows.find_windows(title=u'Cakewalk - [Untitled Project1]')[0] 
    window = pwa_app.window_(handle=w_handle)
    importfile(window,'beat.*')
    time.sleep(5)
    #window['Input Echo on Track 1'].click_input()
    window.child_window(title=" on Track 2", auto_id="100549", control_type="Button").click_input()
    window.child_window(title=" on Track 2", auto_id="100549", control_type="Button").click_input()
    importfile(window,'Vocal.*')
    time.sleep(5)
    Autokey = pyautogui.locateCenterOnScreen('Click2.png')
    print(Autokey)
    pyautogui.doubleClick(Autokey)
    pyautogui.press("SPACE")
    time.sleep(10)
    sendto()
    pywinauto.keyboard.send_keys('^a')
    #window.child_window(title="File", control_type="MenuItem").click_input()
    #window.print_control_identifiers()
    
    handles = pywinauto.findwindows.find_windows()
    for w_handle in handles:
        wind = pwa_app.window_(handle=w_handle)
        if "Auto-Key" in wind.window_text():
            #wind.print_control_identifiers()
            wind.child_window(title="Close", control_type="Button").click()
    
    pyautogui.press("SPACE")
    exportfile(window,pwa_app)
    time.sleep(200)

main()

