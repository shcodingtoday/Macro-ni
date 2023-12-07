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
    raise ValueError('You pressed <ctrl>+<alt>+<cmd> which ended the application')

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


hotkeys = {
    '<ctrl>+<alt>+<cmd>+<esc>': on_interrupt,
    # To Maybe implement later
    '<ctrl>+<alt>+<cmd>+<space>': newHotkey, 
    '<ctrl>+<alt>+<cmd>+l': listHotkeys,
    '<ctrl>+<alt>+<cmd>+<backspace>': deleteHotkey,
    '<ctrl>+<alt>+<cmd>+h': helpHotkey
}

def loadHotkeys():
    print("load hotkeys")
    f = open("userHotkeys.json", "rt")
    userHotkeysJSON = json.loads(f.read())
    for key, value in userHotkeysJSON.items():
        hotkeys[key] = lambda: callUserHotkey(value)
    print(hotkeys)
    f.close()

loadHotkeys()

with keyboard.GlobalHotKeys(hotkeys) as h:
    h.join()