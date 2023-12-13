from pynput import keyboard
import json
import subprocess

# https://docs.python.org/3/library/subprocess.html
# https://pynput.readthedocs.io/en/latest/keyboard.html
# https://pypi.org/project/pynput/

# keys = []
# combos = [
#     {
#         "keys": ["a", "b", "c"],
#         "pathToScript": "hello"
#     }
# ]

# def checkAddKey(_key):
#     if _key not in keys:
#         keys.append(_key)
#     print(keys)

# def checkRemoveKey(_key):
#     for key in keys:
#         if key == _key:
#             keys.remove(_key)
#     print(keys)

# def checkCombo(releasedKey):
#     print("keys: "+str(keys))
#     foundCombo = False
#     for combo in combos:
#         # print(str(releasedKey) + " released")

#         # print(combo["keys"])
#         # print(str(releasedKey) in combo["keys"])

#         # print(type(combo["keys"][0]))
#         # print(type(str(releasedKey)))
#         print(str(releasedKey))
#         print(combo["keys"][0])
#         print(releasedKey)

#         print(releasedKey == combo["keys"][0])



#         if (str(releasedKey) in combo["keys"]):
#             print("found released key in combo")
#             for key in keys:
                
#                 print("checking key " + str(key))
#                 if (str(key) in combo["keys"]):
#                     print("found key in combo")
#                 else: 
#                     print (str(key) + " not in " + combo["keys"])
#                     break
#         else:
#             continue
#     if (not foundCombo):
#         print("no combo found")


# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#         checkAddKey(key.char)
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))
#         checkAddKey(key)

# def on_release(key):
#     # print('{0} released'.format(
#     #     key))
#     # checkCombo(key)
#     print("release "+str(key))
#     checkRemoveKey(key)
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# # pynput.keyboard.Listener.stop()


# def 

def on_interrupt():
    raise ValueError('You pressed <ctrl>+<alt>+<cmd>+b which ended the application')

# To Maybe implement later ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def newHotkey():
    print("new hotkey")

def listHotkeys():
    print("list hotkeys")

def deleteHotkey():
    print("delete hotkey")

def helpHotkey():
    print("help")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def callUserHotkey(commandString):
    # print("call user hotkey")
    print("Executing: "+commandString)
    # split command string into array 
    commandArray = commandString.split(" ")
    subprocess.run(commandArray)

# def openUserHotkeyJSON():
#     # print("open user hotkey json")
#     subprocess.run(["code", "/Users/sh/DEV/macroni/hotkeys.json"])


# hotkeys = {
#     # '<ctrl>+<alt>+<cmd>+b': on_interrupt,
#     # '<ctrl>+<alt>+<cmd>+r': loadHotkeys,
#     # '<ctrl>+<alt>+<cmd>+o': openUserHotkeyJSON,
#     # To Maybe implement later
#     '<ctrl>+<alt>+<cmd>+<space>': newHotkey, 
#     '<ctrl>+<alt>+<cmd>+l': listHotkeys,
#     # '<ctrl>+<alt>+<cmd>+<backspace>': deleteHotkey,
#     '<ctrl>+<alt>+<cmd>+h': helpHotkey
# }

def loadHotkeys():
    print("load hotkeys")
    f = open("/Users/sh/DEV/macroni/hotkeys.json", "rt")
    hotkey_string_commands = json.loads(f.read())
    hotkeys = {}
    for key, value in hotkey_string_commands.items():
        print(key)
        print(value)
        # temp = hotkey_string_commands[key]
        # hotkeys[key] = lambda: callUserHotkey(temp)
        hotkeys[key] = lambda value=value: callUserHotkey(value)
    # print(hotkeys)
    f.close()
    print(hotkeys)
    return hotkeys



# hhh = loadHotkeys()
# hhh["<ctrl>+<alt>+p"]()
# print(hhh)
def addHotkeys(hotkeyDict):

    with keyboard.GlobalHotKeys(
    #     {
    #     "<ctrl>+<alt>+p": lambda: callUserHotkey("python3 /Users/sh/DEV/password-generator/generate-password.py"),
        
    #     "<ctrl>+<alt>+<cmd>+o": lambda: callUserHotkey("python3 /Users/sh/DEV/macroni/scripts/reload.py")
    # }
    hotkeyDict
    ) as h:
        h.join()

addHotkeys(loadHotkeys())
# Attempting to initialise multiple global hotkeys with small dict to fix lamda dict issue
# does not work, only the first executes
def initHotkeys():
    f = open("/Users/sh/DEV/macroni/hotkeys.json", "rt")
    hotkey_string_commands = json.loads(f.read())
    # hotkeys = {}
    for key, value in hotkey_string_commands.items():

        addHotkeys({key: lambda: callUserHotkey(hotkey_string_commands[key])})
    # print(hotkeys)
    f.close()
    # print(hotkeys)
    # return hotkeys
# initHotkeys()