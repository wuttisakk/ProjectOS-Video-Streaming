from flask import Flask, render_template, Response
import cv2
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

app = Flask(__name__)

def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors,minSize=(55, 55))
        coords=[]
        for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
                cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
                cv2.putText(img,"Amount : "+str(features.shape[0]),(0,25),cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),1)
                coords=[x,y,w,h]
        return img,coords 
        
def detect(img,faceCascade):
        img,coords=draw_boundary(img,faceCascade,1.1,10,(0,255,0),"Face")
        return img

        
camera = cv2.VideoCapture(0)

                
def gen_frames():
    while True:
        success, frame = camera.read()
        frame=detect(frame,faceCascade)
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
