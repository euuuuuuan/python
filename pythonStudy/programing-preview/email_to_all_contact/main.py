import yagmail

email = "???"
name = "기쁨"
subject = f"{name}님 수료를 축하해요!"
body = f"{name}님 본문"

yag = yagmail.SMTP(
    user="???",  # 0000@gmail.com 내 이메일
    password="xxxxx"  # 메일 비밀번호
)
yag.send(  # 보낼 이메일 관련 정보
    to=email,
    subject=subject,
    contents=body,
)