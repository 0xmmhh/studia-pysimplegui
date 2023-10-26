import sys
import PySimpleGUI as sg


def ocena2():
    sg.popup('Oceniłeś na 2 gwiazdki, aż tak źle?')
    print('Oceniłeś na 2 gwiazdki')


def ocena3():
    sg.popup('Oceniłeś na 3 gwiazdki, dlaczego tak mało?')
    print('Oceniłeś na 3 gwiazdki')

def ocena4():
    sg.popup('Oceniłeś na 4 gwiazdki, coś możemy poprawić?')
    print('Oceniłeś na 4 gwiazdki')
def ocena5():
    sg.popup('Oceniłeś na 5 gwiazdki, dziękujemy!')


layout = [[sg.T('Jak oceniasz ta aplikacje?')],
          [sg.B('2 gwiazdki', key="OCENA2"), sg.B('3 gwiazdki', key="OCENA3"), sg.Button('3 gwiazdki', key="OCENA3"), sg.Button('4 gwiazdki', key="OCENA4"), sg.B('5 gwiazdek', key="OCENA5")]]

window = sg.Window('Oceny', layout)

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'OCENA2':
        ocena2()
    elif event == 'OCENA3':
        ocena3()
    elif event == 'OCENA4':
        ocena4()
    elif event == 'OCENA5':
        ocena5()

window.close()
