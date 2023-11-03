from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path
from datetime import datetime


def frontdoor_warningemail():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    content = MIMEMultipart()       # 建立MIMEMultipart物件
    content["subject"] = now + " 你的前門CCTV有偵測到移動物體"      # 郵件標題
    content["from"] = "p0933396228@gmail.com"  # 寄件者
    content["to"] = "p88552@gmail.com"  # 收件者
    # content.attach(MIMEText("文字內容"))  # 郵件純文字內容
    content.attach(MIMEImage(Path(r"C:\Users\p0933\Desktop\Python\New\Capture\output_0001.jpg".format()).read_bytes()))  # 郵件圖片內容

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("p0933396228@gmail.com", "psqr wbep sqsf epbt")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("寄送成功!")
        except Exception as e:
            print("Error message: ", e)
    return None
