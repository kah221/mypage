#230410_1812~
#streamlitを使用するため
import streamlit as st
from PIL import Image
#年齢や日付を表示するため
from datetime import date
import time
#現在時刻を得るため？
from datetime import datetime
#乱数を生成するため
import random

#タイトル部start------------------------------------------------------------
#st.title('響@kah_7221 のプロフィール')
st.title('マイページ')
st.text('響　@kah_7221　　閲覧ありがとうございます!(^^)!')
#st.text('~~~~~~閲覧ありがとうございます!(^^)!~~~~~~')
#日付と現在時刻
today = date.today()
t = datetime.now()
#曜日
youbi = today.weekday()
youbi_list = ['月', '火', '水', '木', '金', '土', '日']
for x in range(6):
    if x == youbi:  #今日の曜日番号とリストの番号が一致したときにリストの要素を本日の曜日に。
        youbi_str = youbi_list[x]

st.caption(f'～ ただいまの時刻... {today.year}年{today.month}月{today.day}日（{youbi_str}）{t.hour}時{t.minute}分{t.second}秒 ～')

image = Image.open('./data/icon230410.jpg')
st.image(image, width=220)
#タイトル部end------------------------------------------------------------

#変数定義部start------------------------------------------------------------
#年齢を求める
myBirthDay = date(2003, 7, 22)
#today = date.today()
age = today.year - myBirthDay.year -1   #満年齢が出てしまうので、1引いておく。
if 7 <= today.month and 22 <= today.day:    #7/22以降ならば。
    age += 1
#誕生日までの日にちdiffを求める
if 7 <= today.month and 22 <= today.day:    #その年でもう誕生日を迎えている場合
    nextBirthDay = date(today.year + 1, 7, 22)    
else:   #まだその年で誕生日を迎えていない場合
    nextBirthDay = date(today.year, 7, 22)
diff = nextBirthDay - today

#変数定義部end------------------------------------------------------------

#基本情報部start------------------------------------------------------------
st.subheader('Profile')
st.text(f'生まれ ： 広島\n誕生日 ： 2003年7月22日\n年　齢 ： {age}      （次の誕生日まであと {diff.days} 日！！）\n好きな食べ物 ： 寿司, ﾁｰｽﾞを含むもの\n趣味 ： 工作, ピアノ')

st.text('ここにコメントを書く')

st.text('')
st.subheader('Platforms')
st.text('Twitter（本垢） ： @kah_7221\nTwitter（スタプラ） ： @KH257411\nYouTube ： @\nGitHub ： kah_221')
#基本情報部end------------------------------------------------------------

#ランダム発生部start------------------------------------------------------------
rand = random.randint(0, 9)
#st.text(f'{rand}')
if rand == 0:
    st.text('((/・ω・)/    ←10%の確率で発生中')
#ランダム発生部end------------------------------------------------------------