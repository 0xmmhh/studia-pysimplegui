import PySimpleGUI as sg

layout = [
    [sg.Text("Czy twoje słowo jest palindromem?")],
    [sg.InputText(key="-INPUT-"), sg.Button("Sprawdz", key="-CHECK-")],
    [sg.Text("Obok wyświetli się wynik:") ,sg.Text("", key="-RESULT-")],
    [sg.Button("Zamknij program", key="-EXIT-")]
]

window = sg.Window("Palindrom", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "-EXIT-"):
        break
    elif event == "-CHECK-":
        slowo = str(values["-INPUT-"])
        if slowo:
            if slowo == slowo[::-1]:
                window["-RESULT-"].update(f"Slowo {slowo} jest palindromem")
            else:
                window["-RESULT-"].update(f"Twoje nie slowo jest palindromem")
            
window.close()
