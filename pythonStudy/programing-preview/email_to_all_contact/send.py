import pandas as pd
import yagmail
from time import sleep

yag = yagmail.SMTP(
    user="xxxxxx",
    password="xxxxxx"
)

contacts_df = pd.read_csv('./contacts.csv')
print(contacts_df.head())

for index, contact in contacts_df.iterrows():
    name = contact["Given Name"]
    email = contact["E-mail 1 - Value"]
    subject = f'{name}님 수료를 축하드려요!'
    body = (
        f'{name}님 안녕하세요.\n'
        f'캠프 매니저 김우주입니다.\n'
        f'\n'
        f'코딩 첫걸음 캠프 수료 축하드려요!\n'
        f'수료증은 다음 주 중에 우편으로 발송될 예정입니다 :)\n'
        f'\n'
        f'좋은 하루되세요.\n'
        f'감사합니다.\n'
        f'\n'
        f'김우주 드림\n'
    )
    yag.send(
        to=email,
        subject=subject,
        contents=body,
    )
    print(f'{name}님 전송 완료')
    sleep(30)  # 이메일 수신 정책 관련 term을 줘서 송수신해야 한다.