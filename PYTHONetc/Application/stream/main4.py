# 音声生成アプリ(未完成)
# google cloud platform登録 --> project作成 --> APIを有効化する(APIとサービス) --> texttospeech
# --> APIとサービス --> 認証情報 --> サービスアカウントの作成 --> jsonの秘密鍵作成
# YoutubeDataAPI は時間が見つかったらやる

# pip install --upgrade google-cloud-texttospeech むりなら cloudSDKで初期化
import os
import io
from google.cloud import texttosppech
import streamlit as st

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret.json'

def synthesize_speech(text, lang='日本語', gender='default'):  # defalut
    gender_type = {   # github読む
        'default': texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
        'male': texttospeech.SsmlVoiceGender.MALE,
        'female' : texttospeech.SsmlVoiceGender.FEMALE,
        'neutral' : texttospeech.SsmlVoiceGender.NEUTRAL
    }
    lang_code = {
        '英語' : 'en-US',
        '日本語' : 'ja-JP'
    }

    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttosppech.VoiceSelectionParams(
        language_code=lang_code[lang], ssml_gender=gender_type[gender]
    )

    audio_config = texttosppech.AudioConfig(
        audio_encoding = texttosppech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input = synthesis_input, voice=voice, audio_config=audio_config
    )
    return response

# from Ipython.display import Audio
# Audio(response.audio_content)

# streamlit の形を作る
st.title('音声生成アプリ')
st.markdown('### データ準備')

input_option = st.selectbox(
    '入力データの選択',
    ('直接入力', 'テキストファイル')
)
input_data = None

if input_option == '直接入力':
    input_data = st.text_area('テキストを入力してください', 'サンプル文になります')
else:
    uploaded_file = st.file_uploader('テキストファイルを入れてください', ['txt'])
    if uploaded_file is not None:
        content = uploaded_file.read()
        input_data = content.decode()

if input_data is not None:
    st.write('入力データ')
    st.write(input_data)
    st.markdown('### パラメータ設定')
    st.subheader('言語と話者の性別選択')

    lang = st.selectbox(
        '言語を選択してください',
        ('日本語', '英語')
    )

    gender = st.selectbox(
        '話者の性別を選択してください',
        ('default', 'male', 'female', 'neutral')
    )

    st.markdown('### 音声生成')
    st.write('コチラの文章で音声ファイルの生成を行いますか')
    if st.button('開始'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang=lang, gender=gender) 
        st.audio(response.audio_content)
        comment.write('完了しました。')