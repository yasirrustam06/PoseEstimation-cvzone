import cvzone
import cv2

from cvzone.PoseModule import PoseDetector
pose_detector =PoseDetector(detectionCon=0.5,trackCon=0.5)

img = cv2.imread("image.jpeg")

image = pose_detector.findPose(img)
lmList, bboxInfo = pose_detector.findPosition(image, bboxWithHands=False)
if bboxInfo:
    center = bboxInfo["center"]
    cv2.circle(image, center, 5, (255, 0, 255), cv2.FILLED)

cv2.imwrite("ppgfose.jpg",image)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()































