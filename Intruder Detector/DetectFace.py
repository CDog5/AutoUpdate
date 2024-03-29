import cv2
import sys
import gtts,pygame
from playsound import playsound
##tts = gtts.gTTS("Intruder detected!")
##tts.save("intruder.mp3")

pygame.mixer.init() 
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
intruder = False
video_capture = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        if not intruder:
            pygame.mixer.music.load("intruder.mp3")
            pygame.mixer.music.play()
            intruder = True
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
