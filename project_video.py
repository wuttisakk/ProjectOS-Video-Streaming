from flask import Flask, render_template, Response
import cv2
import PySimpleGUI as sg

app = Flask(__name__)
sg.theme('Reddit')
layout = [[sg.Text("Your Video", size=(25,1),justification='right'),sg.InputText('Defalut Folder'), sg.FileBrowse(), sg.OK()],
          [sg.Text("",size=(83,1)),sg.Button("Exit", button_color=('white', 'red'), size=(4, 1), font=("Helvetica", 8))]
          ]
window = sg.Window("Select Video", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
       break
   # print("This is : ", values[0])

print("This is : ", values[0])        
cap = cv2.VideoCapture(values[0])

def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# Web Streaming With Flask
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
