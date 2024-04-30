import cv2

detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

foto = cv2.imread("bey.jpg")
foto_cinza = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
faces_detectadas = detector.detectMultiScale(foto_cinza, scaleFactor=1.02, minSize=(52, 52))
print("pessoas detectadas", len(faces_detectadas))
for x, y, l, a in faces_detectadas:
    #arquivo_img, ponto_inicial, ponto_final, cor
    foto = cv2.rectangle(foto, (x,y), (x+l, y+a), (0,0,255))

cv2.imshow("umas pessoas aleatorias", foto)
cv2.waitKey()

