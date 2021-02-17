import webbrowser
import sys
import subprocess
import PySimpleGUI as sg

sg.set_options()
sg.theme('Reddit')
layout = [[sg.Text("  Video Streaming  ", text_color=('red'), size=(28, 1), justification='center', font=("Helvetica", 48), relief=sg.RELIEF_RIDGE)],
          [sg.Text("")],
          [sg.Text("")],
          [sg.Text("")],
          [sg.Frame('',[
             [sg.Text("")],
             [sg.Text("Streaming Video ",
                      size=(50, 1),
                      text_color=('blue'),
                      font=("Helvetica", 24)),
              sg.Button("Streaming",
                        button_color=('white', 'blue'),
                        size=(8, 1),
                        font=("Helvetica", 20))],
             [sg.Text("Record Video",
                      size=(50, 1),
                      text_color=('blue'),
                      font=("Helvetica", 24)),
              sg.Button("Record",
                        button_color=('white', 'blue'),
                        size=(8, 1),
                        font=("Helvetica", 20))],
             [sg.Text("")],
          ])],
          [sg.Text("")],
          [sg.Text("")],
          [sg.Text("")],
          [sg.Text("")],
          [sg.Text("Exit From Video Streaming",
                   size=(50, 1), text_color=('blue'),
                   font=("Helvetica", 24)),
           sg.Button("Exit",
                     button_color=('white', 'red'),
                     size=(6, 1),
                     font=("Helvetica", 20))],

         ]

window = sg.Window("Video Streaming", layout)

while True:
    event, values = window.read()
    if event == "Record":
       subprocess.Popen('python record.py', shell=True)

    if event == "Streaming":
       subprocess.Popen('python project.py', shell=True)
       webbrowser.open('http://127.0.0.1:5000/')

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()