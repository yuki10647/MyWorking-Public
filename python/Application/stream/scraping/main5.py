# スクレイピング(未完成)
from bs4 import BeautifulSoup  # HTML を持ってきて成形するライブラリ
import requests                # HTML をとってくるライブラリ
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import altair as alt
#from gspread_dataframe import set_with_dataframe
#import datetime


def get_df_ec():
    url_ec = 'https://scraping.official.ec/'    # ECサイト
    res = requests.get(url_ec) 
    soup = BeautifulSoup(res.text, 'html.parser') 
    # idは一つとわかっているので、find_allとしなくてよい
    item_list = soup.find('ul', {'id', 'itemlist'})
    items = item_list.find_all('li')

    data_ec = []
    for item in items:      # まず１つ取り出してする
        datum_ec = {}       # 辞書を作成する
        datum_ec['title'] = item.find('p', {'class': 'items-grid_itemTitleText_b58666da'}).text 
        price = item.find('p', {'class': 'items-grid_price_b58666da'}).text
        datum_ec['price'] = int(price.replace('¥ ', '').replace(',', ''))  # いらない部分を取る
        datum_ec['link'] = item.find('a')['href'] # aタグが１つなのを確認する
        is_stock = item.find('p', {'class':'items-grid_soldOut_b58666da'}) == None
        datum_ec['is_stock'] = '在庫あり' if is_stock == True else '在庫なし'

        data_ec.append(datum_ec) # 辞書のリストを作る

        df_ec = pd.DataFrame(data_ec)
    return df_ec

def get_worksheet():
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
    return worksheet


def get_chart():
    worksheet = get_worksheet()
    data = worksheet.get_all_values()
    df_udemy = pd.DataFrame(data[1:], columns=data[0])
    df_udemy = df_udemy.astype({
        'n_subscriber': int,
        'n_review': int
    })

    ymin1 = df_udemy['n_subscriber'].min - 10
    ymax1 = df_udemy['n_subscriber'].max + 10
    ymin2 = df_udemy['n_review'].min - 10
    ymax2 = df_udemy['n_review'].max + 10

    base = alt.Chart(df_udemy).encode(
        alt.X('data:T', axis=alt.Axis(title=None))
    )
    line1 = base.mark_line(opacity=0.3, color='#57A44C').encode(
        alt.Y('n_subscriber',
            axis=alt.Axis(title='受講生数', titleColor='#57A44C'),
            scale=alt.Scale(domain=[ymin1, ymax1])
        )
    )
    line2 = base.mark_line(stroke='#5276A7', interpolate='monotone').encode(
        alt.Y('n_review',
            axis=alt.Axis(title='レビュー数', titleColor='#5276A7'),
            scale=alt.Scale(domain=[ymin2, ymax2])
        )
    )
    chart = alt.layer(line1, line2).resolve_scale(
        y = 'independent'
    )
    return chart

df_ec = get_df_ec()
chart = get_chart()


import streamlit as st

st.title('Webスクレイピング活用アプリ')

st.write('## Udemy情報')
st.altair_chart(chart, use_container_width=True)

st.write('## EC在庫情報', df_ec)

# Heroku新規登録
# Heroku CLI インストール
# その前にgit の環境構築
# https://github.com/MaartenGr/streamlit_guide
# streamlit sharing