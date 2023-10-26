import PySimpleGUI as sg
import sys

layout = [
    [sg.Text("Wpisz zdanie, a zostanie wypisana ilosc spacji"), sg.Button("Oblicz",key="-BUTTON1-")],
    [sg.InputText(key="-INPUT-")],
    [sg.Output(size=(45, 20))],
    [sg.Button("Zamknij program", key="-BUTTON2-")]
]

window = sg.Window("Liczenie spacji", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "-BUTTON2-"):
        break
    elif event == "-BUTTON1-":
        wpisane_zdanie = str(values["-INPUT-"])
        if wpisane_zdanie:
            ilosc = wpisane_zdanie.count(" ")
            print(f"Twoje zdanie posiada {ilosc} spacji")
        sys.stdout.flush()
window.close()