import PySimpleGUI as sg

layout = [
    [sg.Text("Wpisz liczbe a zostana wypisane liczby parzyste od 0 do twojej liczby")],
    [sg.InputText(key="-INPUT-"), sg.Button("Oblicz", key="-BUTTON1-")],
    [sg.Button("Zamknij program", key="-BUTTON2-")]
]

window = sg.Window("Parzyste", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "-BUTTON2-"):
        break
    elif event == "-BUTTON1-":
        input_number = int(values["-INPUT-"])
        if input_number:
            for i in range(input_number + 1):
                if i % 2 == 0:
                    sg.Print(i)

window.close()
