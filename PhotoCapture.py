import time
from naoqi import ALProxy

IP = "192.168.199.79"
PORT = 9559

try:
	photoCaptureProxy = ALProxy("ALPhotoCapture", IP, PORT)
except Exception, e:
	print "Error when creating ALPhotoCapture proxy:"
	print str(e)
	exit(1)
while i < 10:
	t1 = time.time()
	ptint t1
	photoCaptureProxy.setResolution(1)  #kQVGA,Image of 320*240px
	photoCaptureProxy.setPictureFormat("jpg")
	photoCaptureProxy.takePictures(3, "/home/nao/recordings/cameras/", "image"+i)
	time.sleep(2)
	i = i + 1
