import cv2
import cvzone
from cvzone.PoseModule import PoseDetector

detector = PoseDetector()
cap = cv2.VideoCapture("5.mp4")

while True :
    ret ,img = cap.read()
    image = detector.findPose(img)
    lms , bboxInfo = detector.findPosition(image,bboxWithHands=False)
    if bboxInfo:
        center = bboxInfo["center"]
        cv2.circle(image, center, 5, (255, 0, 255), cv2.FILLED)
    cv2.imshow("Image",image)
    if cv2.waitKey(1) & 0xFF == ord("Y"):
        break
cap.release()
cv2.destroyAllWindows()