from importlib.resources import path
from pathlib import Path
import PySimpleGUI as sg

symbols = ["$", "%", "@"]

menu_layout = [
    ["File", ["Open", "Save", "---", "Exit"]],
    ["Tools", ["Word Count"]],
    ["Symbols", symbols],
]
sg.theme("GreenMono")
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text("Untitled", key="-docname-")],
    [sg.Multiline(size=(40, 30), key="-textbox-", no_scrollbar=True)],
]

window = sg.Window("App", layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    elif event == "Open":
        file_path = sg.PopupGetFile(
            "Open", no_window=True
        )  # generates the window using it we can open or save
        if file_path:
            file = Path(file_path)
            window["-textbox-"].update(file.read_text())
            window["-docname-"].update(file_path.split("/")[-1])

    elif event == "Save":
        file_path = sg.popup_get_file("Save as", no_window=True, save_as=True) + ".txt"
        file = Path(file_path)  # now file got created in directory
        file.write_text(values["-textbox-"])
        window["-docname-"].update(file_path.split("/")[-1])
        
    elif event == "Word Count":
        words_list = (values["-textbox-"].replace('\n', ' ').split(' '))
        word_count = len(words_list)
        total_chars = len(''.join(words_list))
        sg.popup(f'Total Words: {word_count}\nTotal Chars: {total_chars}')
        
    elif event in symbols: # not ==, because symbols is a list here
        window["-textbox-"].update(values['-textbox-']+" "+event)

window.close()
