#GCP(project) --> API有効化 --> google drive API, google sheets API --> APIサービスアカウント-認証情報
#サービスアカウントから秘密鍵作成json 
# 
from bs4 import BeautifulSoup  # HTML を持ってきて成形するライブラリ
import requests                # HTML をとってくるライブラリ
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe
import datetime

#Udemy
def get_data_udemy():
    url = 'https://scraping-for-beginner.herokuapp.com/udemy'  #HTMLページ
    res = requests.get(url) #res.text にHTML をコードを取得する
    soup = BeautifulSoup(res.text, 'html.parser')  # きれいに並べる
    # 要素の抽出の仕方は覚える
    # (あらかじめ取りたい情報のタグやクラスなどを開発者ツールで確認する)
    #find_allで全てとる--> 情報を絞る-->１つになったらfindに直して取得する  classの時
    n_subscriber = soup.find('p', {'class':'subscribers'}).text 
    n_subscriber = int(n_subscriber.split('：')[1])

    n_review = soup.find('p', {'class':'reviews'}).text 
    n_review = int(n_review.split('：')[1])
    return {
        'n_subscriber': n_subscriber,
        'n_review': n_review
    }

def main():
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    credentials = Credentials.from_service_account_file(
        'service_account.json',
        scopes=scopes
    )
    gc = gspread.authorize(credentials)

    SP_SHEET_KEY = '' # spreadsheet の URL の d/ の後ろ
    sh = gc.open_by_key(SP_SHEET_KEY)

    SP_SHEET = 'db'  # spreadsheetの名前
    worksheet = sh.worksheet(SP_SHEET)

    data = worksheet.get_all_values()
    df = pd.DataFrame(data[1:], columns=data[0])

    data_udemy = get_data_udemy()

    today = datetime.date.today().strftime('%Y/%m/%d')
    data_udemy['date'] = today
    df = df.append(data_udemy, ignore_index=True)

    set_with_dataframe(worksheet, df, row=1, col=1)

if __name__ == '__main__':
    main()