import imutils
import cv2

redLower = (100,24,73)
redUpper = (179,113,134)

camera = cv2.VideoCapture(0)

while True:

    (grabbed, frame) = camera.read() #read the camera img and garbbed pathila _ podalam

    frame = imutils.resize(frame, width=500) #resize frame of camera shoe to me

    blurred = cv2.GaussianBlur(frame, (11,11),0)  

    hsv = cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV) #hsv format change

    mask = cv2.inRange(hsv, redLower,redUpper)  #blue color thedum mela ulla step la hsv la 
    mask = cv2.erode(mask, None ,iterations=2)    #athachum blue colr la shade or light shade erutha atha remove panum  namaku result tharaum
    mask = cv2.dilate(mask, None ,iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,   
                            cv2.CHAIN_APPROX_SIMPLE)[-2]   #frame size

    center = None
    if len(cnts) > 0:  #count agum len  means
        c  =  max(cnts,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M=cv2.moments(c)                        #formula
        center=(int(M["m10"] / M["m00"]) , int(M["m01"] / M["m00"]))

        if radius > 10:   #mosquito no detect athu mari eruka object katathu
            cv2.circle(frame,(int(x),int(y)),int(radius),  #apdi eruutha circle podum
                              (0,255,255),2)
            cv2.circle(frame,center,5,(0,0,255), -1)  # dot podum
##            print(center,radius)

            if radius > 250:
                print("Stop")
            else:
                if(center[0]<150):
                    print("Right")
                elif(center[0]>450):
                    print("Left")
                elif(radius<250):
                    print("Front")
                else:
                    print("Stop")
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key== ord("q"):
         break
camera.release()
cv2.destroyAllWindows()
        
                    

            
    
    
