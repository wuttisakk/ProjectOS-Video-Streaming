# ProjectOS-Video-Streaming
โดย OpenCV , Flask และ Nginx

### Virtualbox ให้ใช้กล้องได้
[Click to download addition](http://download.virtualbox.org/virtualbox/6.1.0_RC1/Oracle_VM_VirtualBox_Extension_Pack-6.1.0_RC1.vbox-extpack)

1. เปิด “Oracle VirtualBox Manager” กดที่ “File” -> “Preferences” <br>
2. คลิ๊กแท็บ ‘Extensions’ <br>
3. กดปุ่มรูปบวกทางขวา <br>
4. เลือก package ที่ดาวน์โหลดมา <br>
5. เปิด Raspbian ใน Virtualbox <br>
6. เปิด cmd ใน Windows <br>
```
cd c:\Program Files\Oracle\VirtualBox
VBoxManage list webcams
VboxManage controlvm "Raspbian" webcam attach .1
```
7. ใน Raspbian เปิด Terminal (Ctrl+Alt+T)
8. ตรงแท็บด้านบน Raspbian กดที่ Devices ---> Webcam เลือกกล้อง 
```
sudo apt update
sudo apt upgrade
sudo apt-get install cheese
cheese
```

### OpenCV
เปลี่ยนเวอร์ชัน python ให้เป็นเวอร์ชัน 3
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
```
ติดตั้ง openCV
```
sudo pip install opencv-python
```

### Flask
```
sudo pip install flask
```

### Clone ProjectOS และการรันโปรแกรม
```
git clone https://github.com/wuttisakk/ProjectOS-Video-Streaming.git
cd ProjectOS-Video-Streaming
python3 project.py (รันโปรแกรม)
```
#### กรณี Error
น่าจะเกิดจากการที่หากล้องไม่เจอ แก้ไฟล์ project.py <br>
หาบรรทัด camera = cv2.VideoCapture(0)
เลขในวงเล็บคือ index ของกล้อง ถ้ามีกล้องตัวเดียวก็เป็น 0 ถ้ามีกล้องหลายตัว ลองเปลี่ยนเป็น 1 2 3 ไปเรื่อยๆ

### NGINX
ติดตั้ง NGINX
```
sudo apt-get update
sudo apt-get install nginx
```
สร้างไฟล์
```
sudo nano /etc/nginx/sites-available/project
```
เปิด server block และเซ็ตให้ Nginx listen ที่ port 80 และระบุ domain name หรือ IP ของเครื่อง server <br>
วางโค้ด ( ip เครื่องน่าจะเลขเดียวกันทุกคนแหละ)
```
server {
    listen 80;
    server_name 10.0.2.15;

    location / {
        proxy_pass http://127.0.0.1:5000;
    }
}
```
เสร็จแล้ว enable NGINX server block ที่เราสร้างด้านบน ด้วยคำสั่ง
```
sudo ln -s /etc/nginx/sites-available/project /etc/nginx/sites-enabled
```
ลองทดสอบ syntax ของ file ว่ามี error หรือไม่ ด้วยคำสั่ง
```
sudo nginx -t
```
ถ้าไม่มี error (มีคำว่า Success) ก็ start NGINX ได้เลย
```
sudo systemctl start nginx (ใช้ start NGINX)
```
เข้าเว็บด้วย IP พิมพ์ 10.0.2.15 ในบราวน์เซอร์ได้เลย

--------- End ----------

คำสั่งเพิ่มเติม
```
sudo systemctl stop nginx (ใช้ stop NGINX)
sudo systemctl restart nginx หรือ sudo systemctl restart nginx (ใช้ restart NGINX หลังแก้โค้ด NGINX ทุกครั้ง)
```
