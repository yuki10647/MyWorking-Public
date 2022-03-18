# 基本
# streamlit run main.py
# API reference にいろいろ書いてある　 TEXもかける
# streamlit hello でドキュメントを見ることができる
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit入門')

# DataFrame の表示
# st.write('DataFrame')
# df = pd.DataFrame({
#     '1列目' : [1, 2, 3, 4],
#     '2列目' : [10, 20, 30, 40]
# })
# st.DataFrame(df.style.highlight_max(axis=0))   # width height を設定できる
# st.table(df.style.highlight_max(axis=0))  # 静的


# markdown 記法
"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

# グラフの描画
# df2 = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns = ['a', 'b', 'c']
# )
# st.line_chart(df2)  # area_chart は塗りつぶし, bar_chart は積み立て

# マップの表示
# df3 = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns = ['lat', 'lon']
# )
# st.map(df3)

# 画像の表示
# st.write('displayImage')
# img = Image.open('sample.jpg')
# st.image(img, caption='screen', use_column_width=True)


# インタラクティブなウィジェット
# if st.checkbox('Show Image'):
#     img = Image.open('../app/shot/image2.png')
#     st.image(img, caption='screen', use_column_width=True)


# option = st.selectbox(
#     'あなたの好きな数字を入れてください',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は', option, 'です'


# option2 = st.text_input('あなたの趣味は何ですか')
# 'あなたの趣味は', option2


# condition = st.slider('あなたの今の調子は', 0, 100, 50)
# 'コンディション', condition


# サイドバー 上記のものに対してほとんど使える
# condition2 = st.sidebar.slider('あなたの気分は', 0, 50, 30)
# 'コンディション', condition2

# 2カラムレイアウト
# left_column, right_column = st.columns(2)
# button = left_column.button('ボタン')
# if button:
#     right_column.write('右カラム')

# エクスパンダ―
# expandar = st.expander('問い合わせ')  # 質問解答や選択
# expandar.write('naiyou')
# expandar.write('naiyou')
# expandar.write('naiyou')
# expandar.write('naiyou')


# プログレスバー
latest_iteration = st.empty()  # これより下のコードは、この操作が終わるまで表示されない
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!!!!!'


# 公開
# streamlit sharing 登録   公式ページ
# git を使う githubのメアドを使う  ->  3日後に通知が来る
# git init -> git remote add origin URL 
# add   commit   push origin master
# Deploy で repositry 選択













