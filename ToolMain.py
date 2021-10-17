import keyboard,time,pywinauto,pyautogui,subprocess 

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
    # Autokey = pyautogui.locateCenterOnScreen('Click2.png')
    # print(Autokey)
    # pyautogui.doubleClick(Autokey)

    w_handle = pywinauto.findwindows.find_windows(title=u'Cakewalk - [Untitled Project1]')[0] 
    window = pwa_app.window_(handle=w_handle)
    window['Input Echo on Track 1'].click_input()
    window.print_control_identifiers()

    time.sleep(200)

main()

