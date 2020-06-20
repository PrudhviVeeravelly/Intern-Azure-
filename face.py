import cv2
detector=cv2.CascadeClassifier('C://Users//admin//Desktop//ML//data//haarcascades_GPU//haarcascade_eye_tree_eyeglasses.xml')
cap=cv2.VideoCapture(0)
while(True):
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    eye=detector.detectMultiScale(gray,1.5,5)
    for(x,y,w,h) in eye:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        cv2.imshow('frame',img)
        cv2.imwrite('pipz.jpg',img)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()