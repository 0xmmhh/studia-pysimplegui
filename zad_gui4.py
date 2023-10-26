import PySimpleGUI as sg
import sys

layout = [
    [sg.Text("Liczby podzielne przez 7 ale niepodzielne przez 5 od 0 do 100")],
    [sg.Button("Oblicz", key="-BUTTON1-")],
    [sg.Output(size=(45, 20))],
    [sg.Button("Zamknij program", key="-BUTTON2-")]
]

window = sg.Window("Parzyste", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "-BUTTON2-"):
        break
    elif event == "-BUTTON1-":
        for i in range(101):
            if i % 7 == 0 and i % 5 != 0:
                print(i)
        sys.stdout.flush()

window.close()
