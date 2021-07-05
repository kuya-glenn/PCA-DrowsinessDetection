import dlib
import cv2
import Name_Find
import glob
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
import imutils

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("68_Landmarks.dat")

cam = cv2.VideoCapture(0)

color_green = (0,255,0)
line_width = 3
count = 0
ID = Name_Find.Add_Name()

cond = False
while count <10:
    ret_val, img = cam.read()
    Gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = detector(Gray_image)
    fa = FaceAligner(predictor, desiredFaceWidth=256)
    cv2.imshow("G!", img)
    
    for det in dets:
        
        
        
        F = cv2.imwrite("dataSet/User."  + "." + str(count)  + str(ID) + ".jpg",Gray_image)
        cv2.waitKey(300)
        cv2.imshow("CAPTURED PHOTO", Gray_image) 
        count +=1

    if cv2.waitKey(1) == 27:
        break  # esc to quit
    if count > 10:
        cond = True


cv2.destroyAllWindows()

count = 0
while count <10:
    images = glob.glob("dataSet/*.jpg")
    for image in images:
        img = cv2.imread(image, 1)


        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_alt2.xml')
            
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), 
                            (0, 0, 255), 2)
                
            faces = img[y:y + h, x:x + w]
            cv2.imshow("face",faces)
                
            cv2.imwrite('dataSet/Face_Extracted/face' + str(count) + '.jpg', faces)
            count +=1 

        for rect in dets:
    
	        (x, y, w, h) = rect_to_bb(rect)
	        faceOrig = imutils.resize(img[y:y + h, x:x + w], width=256)
	        faceAligned = fa.align(img, Gray_image, rect)

	        import uuid
	        f = str(uuid.uuid4())
	        cv2.imwrite('dataSet/Face_Extracted/faceAligned' + str(count) + '.jpg', faceAligned)




