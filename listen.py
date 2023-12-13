from pynput import keyboard
import json
import subprocess

def callUserHotkey(commandString):
    # print("call user hotkey")
    print("Executing: "+commandString)
    # split command string into array 
    commandArray = commandString.split(" ")
    subprocess.run(commandArray)

def loadHotkeys():
    print("load hotkeys")
    f = open("/Users/sh/DEV/macroni/hotkeys.json", "rt")
    hotkey_string_commands = json.loads(f.read())
    hotkeys = {}
    for key, value in hotkey_string_commands.items():
        # print(key)
        # print(value)
        hotkeys[key] = lambda value=value: callUserHotkey(value)
    f.close()
    # print(hotkeys)
    return hotkeys

with keyboard.GlobalHotKeys(loadHotkeys()) as h: h.join()