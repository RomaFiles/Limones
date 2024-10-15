import cv2

ip = 'rtsp://admin:Arturit0.@192.168.1.103:554/cam/realmonitor?channel=1&subtype=0'
cap = cv2.VideoCapture(ip)  
if not cap.isOpened():
    print("Error: No se puede abrir la cámara")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se puede recibir frame (el stream se ha terminado?). Saliendo ...")
        break
    cv2.imshow('Frame Original', frame)