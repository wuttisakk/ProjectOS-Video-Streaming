import sys
import subprocess
import PySimpleGUI as sg
import webbrowser


sg.set_options()
sg.theme('Reddit')
layout = [[sg.Text("  Video Streaming  ",
                   text_color=('red'),
                   size=(20, 1),
                   justification='center',
                   font=("Helvetica", 48),
                   relief=sg.RELIEF_RIDGE)],
          [sg.Text("")],
          [sg.Text("")],
          [sg.Frame('',[
             [sg.Text("Streaming")],
             [sg.Text("Streaming ",
                      size=(32, 1),
                      text_color=('blue'),
                      font=("Helvetica", 24)),
              sg.Button("stream",
                        button_color=('white', 'blue'),
                        size=(6, 1),
                        font=("Helvetica", 20))],
             [sg.Text("Record Video",
                      size=(32, 1),
                      text_color=('blue'),
                      font=("Helvetica", 24)),
              sg.Button("record",
                        button_color=('white', 'blue'),
                        size=(6, 1),
                        font=("Helvetica", 20))],
             [sg.Text("")],
          ])],
          [sg.Frame('Live Video',[
             [sg.Text("")],
             [sg.Text("Live Video",
                      size=(25, 1),
                      text_color=('blue'),
                      font=("Helvetica", 24)),
              sg.Text('Select Video',
                      font=("Helvetica", 16)),
              sg.Button("Select",
                        button_color=('white', 'blue'),
                        size=(10, 1),
                        font=("Helvetica", 12))],
             [sg.Text("", size=(25, 1),
                      text_color=('blue'),
                      font=("Helvetica", 24)),
              sg.Text('Start Stream',
                      font=("Helvetica", 16)),
              sg.Button("LIVE",
                        button_color=('white', 'blue'),
                        size=(10, 1),
                        font=("Helvetica", 12))],
             [sg.Text("")],
          ])],
          [sg.Text("")],
          [sg.Text("")],
          [sg.Text("Exit From Video Streaming",
                   size=(32, 1),
                   text_color=('blue'),
                   font=("Helvetica", 24)),
           sg.Button("EXIT",
                     button_color=('white', 'red'),
                     size=(6, 1),
                     font=("Helvetica", 20))],

         ]
window = sg.Window("Video Streaming", layout)
while True:
    event, values = window.read()
    if event == "stream":
       subprocess.Popen('python /home/pi/ProjectOS-Video-Streaming/project.py', shell=True)
       webbrowser.open('http://10.0.2.15/', new=2)
       continue
    if event == "record":
        subprocess.Popen('python /home/pi/ProjectOS-Video-Streaming/videoRec.py', shell=True)
    if event == "Select":
        subprocess.Popen('python /home/pi/ProjectOS-Video-Streaming/project_video.py', shell=True)
    if event == "LIVE":
       webbrowser.open('http://10.0.2.15/', new=2)
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()