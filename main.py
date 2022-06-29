import streamlit as st
from PIL import Image
import time

st.title('Streamlit使ってみた')

st.write('お試し～')
'Start!!'

if st.checkbox('ようこそ！'):
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):                                #チェックボックス入力後にNowLoadingを表示
        latest_iteration.text(f'NowLoading {i+1}')
        bar.progress(i + 1)
        time.sleep(0.01)

    img = Image.open('C:/Users/Wolira/Desktop/streamlit/sample.jpg')    #NowLoadingが終了後画像表示
    st.image(img, caption='taco', use_column_width=True)

    'Done!!'

# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#    right_column.write('ここは右カラムです')

# expander1 = st.expander('問い合わせ1')
# expander1.write('問い合わせ1の回答')
# expander2 = st.expander('問い合わせ2')
# expander2.write('問い合わせ2の回答')
# expander3 = st.expander('問い合わせ3')
# expander3.write('問い合わせ3の回答')



#option = st.selectbox(
#    'あたなが好きな数字を教えてください。',
#    list(range(1, 11))
#)

#'あなたの好きな数字は、', option, 'です。'


# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：', text

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition
