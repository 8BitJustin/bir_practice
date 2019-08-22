import cv2
import glob

# creates list of files with .jpg extension
images = glob.glob("*.jpg")

# runs for loop for items within images list
for i in images:
    # reads the image as color
    img = cv2.imread(i, 1)
    # resizes each 'img' to 100x100
    res = cv2.resize(img, (100, 100))
    # shows image
    cv2.imshow("Batch Image", res)
    # shows for 1 second, ideally looping through the list
    cv2.waitKey(1000)
    # closes after all are shown
    cv2.destroyAllWindows()
    # writes/creates new image file with updated resolution
    cv2.imwrite("resized-" + i, res)