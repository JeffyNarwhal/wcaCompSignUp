import keyboard, pyautogui, os, sys, time

file = open(os.path.join(sys.path[0], "registration_info.txt"), "r")
x = file.read()
y = x.split("\n")

for i in y:
    while True:
        if keyboard.is_pressed("x"):
            pyautogui.typewrite(i)
            break
    time.sleep(0.05)

