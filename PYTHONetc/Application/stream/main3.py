# 物体検知(未完成)
# Azure に登録　(基本無料だが、クレカの登録が必要)
# Computer Vision API + Document
# ドキュメントからリソースを作成
# microsoft azure --> keys and endpoint を取得
# 基本公式ドキュメントからのコピーで作る
# jsonファイルとimgディレクトリを作成しておく


# 必要モジュールは公式のクイックスタートからコピー

# keyとendpoint をjsonにかいて読み込む
import json
with open('secret.json') as f:
    secret = json.load(f)
KEY = secret['KEY']
ENDPOINT = secret['ENDPOINT']

# サブスクリプションキーの作成
computervision_client = 1 # ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# 関数
def get_tags(filepath):                     # 画像タグ取得関数
    local_image = open(filepath, "rb")
    tags_result = computervision_client.tag_image_in_stream(local_image) 
    # tags_result_remote = computervision_client.tag_image(remote_image_url) # リモートファイルの場合
    tags = tags_result.tags                 # タグを取ってくる。詳細はドキュメント
    tags_name = []
    for tag in tags:
        tags_name.append(tag.name)          # tagのなかにname, confidence がある
    return tags_name

def detect_objects(filepath):             # 物体情報取得関数
    local_image = open(filepath, "rb")
    detect_objects_results = computervision_client.detect_objects_in_stream(local_image)
    objects = detect_objects_results.objects
    return objects



# streamlit の形を作る
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.title('物体検出アプリ')

uploaded_file = st.file_uploader('Choose an image ...', type=['jpg', 'png'])

if uploaded_file is not None:
    img = Image.open(uploaded_file) # 読み込み
    img_path = f'img/{uploaded_file.name}'  # 画像からパスを作る、imgディレクトリ作る
    img.save(img_path)                      # 保存
    objects = detect_objects(img_path)

    # 描画
    draw = ImageDraw.Draw(img)
    for object in objects:
        x = object.rectangle.x
        y = object.rectangle.y
        w = object.rectangle.w
        h = object.rectangle.h
        caption = object.object_property

        font = ImageFont.truetype(font='./fontfilepath', size=50)
        text_w, text_h = draw.textsize(caption, font=font)
        draw.rectangle([(x, y), (x+w, y+h)], fill=None, outline='green', width=5)
        draw.rectangle([(x, y), (x+text_w, y+text_h)], fill='green')
        draw.text((x, y), caption, fill='white', fomt=font)
    st.image(img)                   # 表示

    # コンテンツタグ取得
    tags_name = get_tags(img_path)
    tags_name = ', '.join(tags_name) # 各要素を, でつなげる
    st.markdown('**認識されたコンテンツタグ**')
    st.markdown(f'> {tags_name}')
