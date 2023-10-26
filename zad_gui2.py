import PySimpleGUI as sg

layout = [
    [sg.Text("Twoja lista: [1, 2, 'ananas', (2,4,5), 'butelka', 2.5837]")],
    [sg.Button("Wyświetl elementy liczbowe", key="-BUTTON-"), sg.Text(key="-OUTPUT-")],
    [sg.Button("Zamknij program", key="-EXIT-")]
]
window = sg.Window("Lista", layout)
nowa = []
while True:
    event, values = window.read()
    if event in ("-EXIT-", sg.WIN_CLOSED):
        break
    elif event == "-BUTTON-":
        x = [1, 2, "ananas", (2,4,5), "butelka", 2.5837]
        for element in x:
            if isinstance(element, (int, float)):
                nowa.append(element)
                window["-OUTPUT-"].update(f"Elementy liczbowe tej listy to: {nowa}")

window.close()