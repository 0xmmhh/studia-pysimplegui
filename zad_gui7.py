import PySimpleGUI as sg 
import random
layout = [
    [sg.Text("Zagrajmy w grę. Spróbujesz odgadnąć cyfrę w zakresie od 1 do 10 w 5 próbach?")],
    [sg.InputText(size=(4,1), key="-INPUT-"), sg.Button("Sprawdz", key="-CHECK-"), sg.Text(key="-ANSWER-")],
    [sg.Button("Zamknij program", key="-EXIT-")]
]

window = sg.Window("Zgadywanka", layout)

tajemnicza = random.randint(1,10)

num_of_attempts = 0

while True:
    event, values = window.read()
    if event in ("-EXIT-", sg.WIN_CLOSED):
        break
    elif event == "-CHECK-":
        num_of_attempts += 1
        guess = int(values["-INPUT-"])
        if num_of_attempts >= 5:
            window["-CHECK-"].update(disabled=True)
            window["-ANSWER-"].update("Wykorzystałeś juz 5 prób")
        if guess == tajemnicza:
            window["-ANSWER-"].update(f"Gratulacje, udało ci się zgadnąć liczbę w {num_of_attempts} próbach")
        elif guess > tajemnicza:
            window["-ANSWER-"].update("Spróbuj mniejszą liczbę")
        elif guess < tajemnicza:
            window["-ANSWER-"].update("Spróbuj większą liczbę")

window.close()

