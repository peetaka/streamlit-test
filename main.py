import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門') #タイトルの追加

st.write('DataFrame') #テキストの追加

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=['lat','lon']
)

# st.write(df)#テーブルの作成_1

# st.dataframe(df.style.highlight_max(axis=0), width=300 ,height=300) #テーブルの作成_2

# st.table(df.style.highlight_max(axis=0)) #テーブルの作成_3（ソートできないテーブル）https://docs.streamlit.io/library/api-reference/data/st.dataframe

#プログレスバー
'start'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'イテレーション{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'done'

# マジックコマンドの利用
"""
# 1章
## 1節
### 1項
```
import streamlit as st
import numpy as np
import pandas as pd
```
"""
# chartプロット
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# mapプロット
# st.map(df)

st.write('DisplayImage') #テキストの追加

left_column, right_column = st.columns(2)

# if st.checkbox('show image'):
#     img = Image.open('00.jpg')
#     st.image(img, caption='Gorilla', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字は？',
    list(range(1,11))
)

'あなたの好きな数字は', option, 'です'


option2 = st.sidebar.text_input('あなたの趣味は？')
'あなたの好きな趣味は', option2, 'です'

option3 = st.sidebar.slider('あなたの調子は？', 0,100,50)
'あなたの好きな調子は', option3, 'です'

btn = left_column.button('ボタン')
if btn:
    right_column.write('ヘイ')

expander = st.expander('問い合わせ')
expander.write('問い合わせないよ床く')

