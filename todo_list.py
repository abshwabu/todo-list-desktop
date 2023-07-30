#!/bin/python3

import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('task')],
            [sg.Text('new task'), sg.InputText()],
            [sg.Button('Add'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Todo app', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
