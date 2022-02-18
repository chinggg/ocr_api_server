import requests
import ddddocr


CAPTCHA_URL = 'https://passport.bilibili.com/web/captcha/img'
HOST = "http://127.0.0.1:9898"

img_bytes = requests.get(CAPTCHA_URL).content
with open('captcha.png', 'wb') as f:
    f.write(img_bytes)

ocr = ddddocr.DdddOcr(show_ad=False)
ans1 = ocr.classification(img_bytes)
ans2 = requests.post(f"{HOST}/ocr/file", files={'image': img_bytes}).text
print(ans1, ans2)