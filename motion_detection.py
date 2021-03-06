import cv2 ,time, pandas
from datetime import datetime 
first_frame=None
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["start","end"])


video=cv2.VideoCapture(0,cv2.CAP_DSHOW)#zero here is the number or webcam in pc

while True:#this loop will iterate through the frames and display window
    
    check,frame = video.read()#check is the bool it returns true if it can read VideoCapture object while Frame is the numpy array of first captured image of video
    status=0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame, gray)
    thresh_delta=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta=cv2.dilate(thresh_delta, None, iterations=3)
    cnts, _ =cv2.findContours(thresh_delta.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (234,113,46),3)
    status_list.append(status)
    status_list=status_list[-2:]
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())
    
    cv2.imshow("frame",frame)
    cv2.imshow("Capturing",gray)
    cv2.imshow("delta",delta_frame)
    cv2.imshow("thresh",thresh_delta)
    key=cv2.waitKey(1)#this will generate a frame in every 1 milisecond
    if key==ord('q'):# when we will press q from keyboard window will distroy
        break
print(a)#this will print number of frames
print(status_list)
print(times)
for i in range(0,len(times),2):
    df=df.append({"start":times[i],"end":times[i+1]},ignore_index=True)
df.to_csv("times.csv")    
video.release()
cv2.destroyAllWindows()
