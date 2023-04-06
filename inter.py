import PySimpleGUI as sg

layout = [[sg.Button(f'{row}, {col}') for col in range(15)] for row in range(9)]

event, values = sg.Window('10JO', layout).read(close=True)