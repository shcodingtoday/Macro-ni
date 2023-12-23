from pynput import keyboard
import json
import subprocess

def callUserHotkey(key, commandString):
    print("Pressed:    " + key + "\nExecuting:  "+commandString)
    commandArray = commandString.split(" ")
    subprocess.run(commandArray)

def loadHotkeys():
    f = open("/Users/sh/DEV/macroni/hotkeys.json", "rt")
    hotkey_string_commands = json.loads(f.read())
    hotkeys = {}
    for key, value in hotkey_string_commands.items():
        hotkeys[key] = lambda key=key,value=value: callUserHotkey(key,value)
    f.close()
    return hotkeys

with keyboard.GlobalHotKeys(loadHotkeys()) as h: h.join()