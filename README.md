# Macro-ni
Macro-ni is an open source global hotkey script.  
A specified key combination runs a terminal command.  
It is flexible, use a hotkey to run any code in any language.  

# Exiting the program
Use a keyboard interrupt in the terminal this is running in. (`<ctrl>+c` usually)

Examples:   
`"<ctrl>+<shift>+h": "echo Hello World"`  
`"g+l+o+w+i+e": "/Users/Terry/WeNeedToGTFOofHere.out"`
`"<space>": "python3 /Users/DrEvil/BigRedButton.py"`


## Create a hotkey
1. Open up hotkeys.json
2. Choose a key combo.
<details>
<summary>What keys mean what<a href="https://pynput.readthedocs.io/en/latest/keyboard.html">???</a></summary>


```
class pynput.keyboard.Key[source]
A class representing various buttons that may not correspond to letters. This includes modifier keys and function keys.

The actual values for these items differ between platforms. Some platforms may have additional buttons, but these are guaranteed to be present everywhere.

alt = <0>
A generic Alt key. This is a modifier.

alt_gr = <0>
The AltGr key. This is a modifier.

alt_l = <0>
The left Alt key. This is a modifier.

alt_r = <0>
The right Alt key. This is a modifier.

backspace = <0>
The Backspace key.

caps_lock = <0>
The CapsLock key.

cmd = <0>
A generic command button. On PC platforms, this corresponds to the Super key or Windows key, and on Mac it corresponds to the Command key. This may be a modifier.

cmd_l = <0>
The left command button. On PC platforms, this corresponds to the Super key or Windows key, and on Mac it corresponds to the Command key. This may be a modifier.

cmd_r = <0>
The right command button. On PC platforms, this corresponds to the Super key or Windows key, and on Mac it corresponds to the Command key. This may be a modifier.

ctrl = <0>
A generic Ctrl key. This is a modifier.

ctrl_l = <0>
The left Ctrl key. This is a modifier.

ctrl_r = <0>
The right Ctrl key. This is a modifier.

delete = <0>
The Delete key.

down = <0>
A down arrow key.

end = <0>
The End key.

enter = <0>
The Enter or Return key.

esc = <0>
The Esc key.

f1 = <0>
The function keys. F1 to F20 are defined.

home = <0>
The Home key.

insert = <0>
The Insert key. This may be undefined for some platforms.

left = <0>
A left arrow key.

media_next = <0>
The next track button.

media_play_pause = <0>
The play/pause toggle.

media_previous = <0>
The previous track button.

media_volume_down = <0>
The volume down button.

media_volume_mute = <0>
The volume mute button.

media_volume_up = <0>
The volume up button.

menu = <0>
The Menu key. This may be undefined for some platforms.

num_lock = <0>
The NumLock key. This may be undefined for some platforms.

page_down = <0>
The PageDown key.

page_up = <0>
The PageUp key.

pause = <0>
The Pause/Break key. This may be undefined for some platforms.

print_screen = <0>
The PrintScreen key. This may be undefined for some platforms.

right = <0>
A right arrow key.

scroll_lock = <0>
The ScrollLock key. This may be undefined for some platforms.

shift = <0>
A generic Shift key. This is a modifier.

shift_l = <0>
The left Shift key. This is a modifier.

shift_r = <0>
The right Shift key. This is a modifier.

space = <0>
The Space key.

tab = <0>
The Tab key.

up = <0>
An up arrow key.
```

</details>
3. The value corresponding to the key press should be a terminal command.  
   This can be used to execute other scripts.

# Future additions to add
1. macro to exit the program
2. Add info on how to bundle project into .exe or .dmg etc and how to run on launch
