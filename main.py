import cv2
import easyocr

numberPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
reader = easyocr.Reader(['en'])

windowWidth = 600
windowHeight = 600

color = (255, 0, 255)

webcam = cv2.VideoCapture(0)
webcam.set(3, windowWidth)
webcam.set(4, windowHeight)

counter = 0

while True:
    success, image = webcam.read()
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    numberPlates = numberPlateCascade.detectMultiScale(imageGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        cv2.rectangle(image, (x,y), (x+w, y+h), color, 2)
        cv2.putText(image, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)
        imageNumberPlate = image[y:y+h, :x+w]
        cv2.imshow("Number Plate", imageNumberPlate)

    cv2.imshow("Output", image)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        textOutput = reader.readtext(imageNumberPlate)
        print(textOutput[-1][1])
        cv2.imwrite("Resources/Scanned/NumberPlate_" + str(counter) + ".jpg", imageNumberPlate)
        print("Image Saved")
        counter += 1

