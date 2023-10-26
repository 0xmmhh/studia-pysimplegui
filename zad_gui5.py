import PySimpleGUI as sg

layout = [
    [sg.Text("Wprowadz dane: ")],
    [sg.InputText("", key="-INPUT-"), sg.Button("Dodaj do listy", key="-ADD-")],
    [sg.Button("Oblicz sume", key="-BUTTON-")],
    [sg.Text("Wynik sumy dodanych wszystkich elementow:"), sg.Text("", key="-RESULT-")],
    [sg.Button("Zamknij program", key="-EXIT-")]
]
window = sg.Window("Suma", layout)

elementy = []

while True:
    event, values = window.read()
    if event == "-EXIT-" or event == sg.WIN_CLOSED:
        break
    elif event == "-ADD-":
        dane = int(values["-INPUT-"])
        elementy.append(dane)
    elif event == "-BUTTON-":
        if dane: 
            window["-RESULT-"].update(f"Suma elementów w liście: {sum(elementy)}")
