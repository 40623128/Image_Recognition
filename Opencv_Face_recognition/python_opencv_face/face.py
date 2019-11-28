import cv2

# 載入分類器
face_cascade = cv2.CascadeClassifier('..\haarcascades\haarcascade_frontalface_default.xml')
# 讀取圖片
img = cv2.imread('..\img\onshape.jpg')
# 轉成灰階圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測臉部
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=4,
    minSize=(16, 16),
    maxSize=(64, 64)
)
# 繪製人臉部份的方框
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)    
# 顯示成果
print(len(faces))
cv2.namedWindow('img', cv2.WINDOW_NORMAL)  #正常視窗大小
cv2.imshow('img', img)                     #秀出圖片
cv2.imwrite( "result.jpg", img)           #保存圖片
cv2.waitKey(0)                             #等待按下任一按鍵
cv2.destroyAllWindows()                    #關閉視窗
