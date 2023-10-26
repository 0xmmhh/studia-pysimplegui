import PySimpleGUI as sg

layout = [
    [sg.Text("Najmniejsza lub największa ilość w liście")],
    [sg.InputText(key="-INPUT-"), sg.Button("Dodaj do listy", key="-ADD-")],
    [sg.Button("Wyświetl największą wartość", key="-SHOW_MAX-"), sg.Button("Wyświetl najmniejszą wartość", key="-SHOW_MIN-")],
    [sg.Text("", key="-MAX-"), sg.Text("", key="-MIN-")],  # Zmieniony klucz na -MAX- i -MIN-
    [sg.Button("Zamknij program", key="-EXIT-"), sg.Button("Wyczyść listę", key="-CLEAR-")],
]

window = sg.Window("Najmniejsza i największa wartość", layout)

lista = []

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "-EXIT-"):
        break
    elif event == "-ADD-":
        wpisane = values["-INPUT-"]
        lista.append(wpisane)
        window["-INPUT-"].update(" ")
    elif event == "-SHOW_MAX-":
        if lista:
            max_val = str(max(lista))
            window["-MAX-"].update(f"Największa wartość w liście to: {max_val}")
        else:
            window["-MAX-"].update("Lista jest pusta")  # Zaktualizowany klucz na -MAX-
    elif event == "-SHOW_MIN-":
        if lista:
            min_val = str(min(lista))
            window["-MIN-"].update(f"Najmniejsza wartość w liście to: {min_val}")
        else:
            window["-MIN-"].update("Lista jest pusta")  # Zaktualizowany klucz na -MIN-
    elif event == "-CLEAR-":
        lista.clear()

window.close()
