from cgitb import text
from multiprocessing.sharedctypes import Value
from optparse import Values
from tokenize import Triple
import PySimpleGUI as sg

sg.theme('DarkBlue4')
sg.popup('Aplicativo para saber a Média de notas')

layout = [
    [sg.Text("Redação")],
    [sg.Input("", key='reda')],
    [sg.Text("Ciências da Natureza")],
    [sg.Input("", key='ciencia_na')],
    [sg.Text("Ciências Humanas")],
    [sg.Input("", key='ciencia_hu')],
    [sg.Text("Linguagens")],
    [sg.Input("", key='lingua')],
    [sg.Text("Matemática")],
    [sg.Input('', key='mate')],
    [sg.Text("", key='medio'), sg.Text("", key='nota_final')],
    [sg.Text("", key='media_para_passar')],
    [sg.Button("CALCULAR")]
]

janela = sg.Window("Media de nota", layout=layout, finalize=True)

while True:
    try:
        event, values = janela.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif (values['reda']) == '':
            janela["medio"].update(f"Preencha o campo Redação!")
        elif values['ciencia_na'] == '':
            janela["medio"].update(f"Preencha o campo Ciências da Natureza")
        elif values['ciencia_hu'] == '':
            janela["medio"].update(f"Preencha o campo Ciências Humanas!")
        elif values['lingua'] == '':
            janela["medio"].update(f"Preencha o campo Linguagens!")
        elif values['mate'] == '':
            janela["medio"].update(f"Preencha o campo Matemática!")
        elif event == "CALCULAR":
            valores = int(values["reda"]) + int(values["ciencia_na"]) + int(values["ciencia_hu"]) + int(values["lingua"]) + int(values["mate"])
            media = valores / 5
            janela["medio"].update(f"Sua média foi de {media}")
            janela["nota_final"].update(f"Sua nota final foi de {valores}")

    except:
        janela["medio"].update(f"Coloque apenas numeros")
