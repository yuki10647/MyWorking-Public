# 米国株価表示アプリ
import pandas as pd
import yfinance as yf
import altair as alt # matpltlibの代わり
import streamlit as st

# yfinanceについて
# aapl = yf.Ticker('AAPL')
# aapl.history() 株価の推移
# aapl.info 会社情報
# aapl.actions 配当金と株式分割   aapl.actions['dividends'].plot()

# title
st.title('米国株価可視化アプリ')

# sidebar
st.sidebar.write("""
# GAFA株価
コチラは株価可視化ツールです。以下のオプションから表示日数を指定してください
""")
# 変数にサイドバーを利用できる
st.sidebar.write("""
## 表示日数
""")
days = st.sidebar.slider('日数', 1, 50, 20)

st.sidebar.write("""
## 株価の範囲指定
""")
ymin, ymax = st.sidebar.slider(
    '範囲を指定してください',
    0.0, 3500.0, (0.0, 3500.0)
)


# main
st.write(f"""
### 過去 **{days}日間** のGAFA株価
""")

@st.cache
def get_data(days, tickers):#関数化する
    df = pd.DataFrame()  # 空のデータフレームを用意
    for company in tickers.keys():  # company="apple"
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d') # 株価の期間をきめて取り出す
        hist.index = hist.index.strftime('%d %B %Y') # 表記の仕方の変更
        hist = hist[['Close']] # 終値のみ取ってくる
        hist.columns = [company]  # カラム名変更
        hist = hist.T # 転置
        hist.index.name = 'Name' # インデックス名を作る
        df = pd.concat([df, hist]) # 結合
    return df

tickers = {                # ティッカーシンボルで調べられる
    'apple' : 'AAPL',
    'facebook' : 'FB',
    'google' : 'GOOGL',
    'microsoft' : 'MSFT',
    'netflix' : 'NFLX',
    'amazon' : 'AMZN'
}
df = get_data(days, tickers) # 変数をちゃんと設定しているか確認する


companies = st.multiselect(  # どの株価を表示するか選ぶ枠を作る
    '会社名を選択してください',
    list(df.index),             # 一つ一つ書いてもいいが、このほうが楽
    ['google', 'amazon', 'facebook', 'apple']  # 初期値
)
if not companies:
    st.error('少なくとも一社は選んでください')
else:
    # データフレーム
    data = df.loc[companies]   # 条件に合うようにデータフレームを削る
    st.write("### 株価(USD)", data.sort_index())
    # グラフの可視化
    data = data.T.reset_index()  # 縦のデータフレームにする
    data = pd.melt(data, id_vars=['Date']).rename(    # これは技術として覚えとく
        columns = {'value' : 'Stock Prices(USD)'}
    )
    chart = (                    # altair の記法
        alt.Chart(data)
        .mark_line(opacity=0.8, clip=True)  # opacity 透明度　　clip 枠内のみ表示
        .encode(
            x = "Date:T",  # オプション設定の場合は y のようにする
            y = alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
            color = 'Name:N'
        )
    )
    st.altair_chart(chart, use_container_width=True)  # streamlitに表示
