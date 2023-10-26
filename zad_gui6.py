import PySimpleGUI as sg

layout = [
    [sg.Text("Wprowadz dane: ")],
    [sg.InputText("", key="-INPUT-"), sg.Button("Dodaj do listy", key="-ADD-")],
    [sg.Button("Oblicz", key="-BUTTON-")],
    [sg.Text("Kwadrat podanych liczb w liście:"), sg.Text("", key="-RESULT-")],
    [sg.Button("Zamknij program", key="-EXIT-")]
]
window = sg.Window("Kwadrat", layout)

elementy = []
kwadrat = []
while True:
    try:
        event, values = window.read()
        if event == "-EXIT-" or event == sg.WIN_CLOSED:
            break
        elif event == "-ADD-":
            dane = int(values["-INPUT-"])
            if dane:
                elementy.append(int(dane))
                window["-INPUT-"].update('')
        elif event == "-BUTTON-":
            if dane: 
                for i in elementy:
                    nowy = i ** 2
                    kwadrat.append(nowy)
                    window["-RESULT-"].update(f"Kwadraty podanych liczb w liście: {kwadrat})")
    except ValueError:
        print("Wpisz liczbe")