import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time
import pandas as pd
## Make canvas and set the color
#img = np.zeros((200, 400, 3), np.uint8)
def start_write():
    path = r'D:\CODE\python\app\data\test.jpg'
    # Using cv2.imread() method
    img = cv2.imread(path)
    b, g, r, a = 0, 255, 0, 0
    import pandas as pd
    df = pd.read_csv('final.csv')
    fontpath = "font/RobotoSlab-VariableFont_wght.ttf"
    font = ImageFont.truetype(fontpath, 16)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)

    for i in range(df.shape[0]):
        draw.text((df.iloc[i][0] * 0.97, df.iloc[i][1] * 0.97), df.iloc[i][9], font=font, fill=(b, g, r, a))
        img = np.array(img_pil)
    cv2.imwrite("after_trans/result.png", img)
    cv2.imwrite("static/result.png", img)
'''    topLeft = (df.iloc[i][0],df.iloc[i][1])
    bottomRight = (df.iloc[i][4], df.iloc[i][5])
    x, y = topLeft[0], topLeft[1]
    w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]
    # Grab ROI with Numpy slicing and blur
    ROI = img[y:y + h, x:x + w]
    blur = cv2.GaussianBlur(ROI, (51, 51), 0)
    # Insert ROI back into image
    img[y:y + h, x:x + w] = blur'''


'''text = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime())
cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (b, g, r), 1, cv2.LINE_AA)


fontpath = "font/RobotoSlab-VariableFont_wght.ttf"
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((50, 80), "cậu ơi tớ hỏi chút", font=font, fill=(b, g, r, a))
img = np.array(img_pil)

cv2.putText(img, "--- by Silencer", (200, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (b, g, r), 1, cv2.LINE_AA)

## Display
cv2.imshow("res", img);
cv2.waitKey();
cv2.destroyAllWindows()'''

