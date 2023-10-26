import PySimpleGUI as sg
import sys

layout = [
    [sg.Text("Wpisz slowo, po kliknieciu przycisku zostanie one odwrocone"), sg.Button("Kliknij", key="-BUTTON1-")],
    [sg.InputText(key="-INPUT-")],
    [sg.Output(size=(45, 20))],
    [sg.Button("Zamknij program", key="-BUTTON2-")]
]

window = sg.Window("Odwrocony string", layout)

while True:
    event, values = window.read()
    if event == "-BUTTON2-" or event == sg.WIN_CLOSED:
        break
    elif event == "-BUTTON1-":
        zdanie = str(values["-INPUT-"])
        if zdanie:
            print(zdanie[::-1])
            sys.stdout.flush()

window.close()