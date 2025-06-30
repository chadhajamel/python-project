import time

import streamlit as st
import pandas as pd
st.title('Sales Report')
st.header('Q1 Result')
q1_sales ={
    'january':100,
    'february':110,
    'march':115,
}
st.write('january was the start of the year')
st.write(q1_sales)
st.write('Q2 Results')

q2_sales ={
    'April':150,
    'May':200,
    'June':250,
}
'Q2 had better results:smile:'
q2_df=pd.DataFrame(q2_sales.items(),columns=['Month','Amount']    )
st.table(q2_df)
st.dataframe(q2_df)
st.line_chart(q2_df)
st.area_chart(q2_df)
st.bar_chart([q1_sales.values(),q2_sales.values()])

'button'
if st.button('Show q2 Data'):
     st.table(q2_df)
else:
    st.table(q1_sales)
'checkbox'
if st.checkbox('Show q1 Data'):
    st.table(q2_sales)
else:
    st.table(q1_sales)
'radio'
quarter= st.radio('which quarter?',('Q1','Q2'))
if quarter=='Q1':
    st.line_chart(q1_sales)
elif quarter=='Q2':
    st.line_chart(q2_sales)
'select box'
selected_quarter=st.selectbox('Which quarter?',('Q1','Q2'))
if selected_quarter=='Q1':
    st.line_chart(q1_sales)
elif selected_quarter=='Q2':
    st.line_chart(q2_sales)
'slider'
st.write(st.slider('which quarters?',1,4,(1,2)))
'multiselect'
st.write(st.multiselect('Which quarter?',['Q1','Q2','Q3','Q4']))
#sidebar
section=st.sidebar.radio('which section ?', ('Text','Charts','Widgets','More widgets'))
if section=='Text':
  st.write('January was the start of the year')
  st.write(q1_sales)
  st.header('Q2 Results')
  'Q2 had better results:smile:'
  st.table(q2_sales)
  st.dataframe(q2_sales)

elif section=='Charts':
    st.line_chart(q2_sales)
    st.area_chart(q2_sales)
    st.bar_chart([q1_sales.values(),q2_sales.values()])
elif section=='Widgets':
    if st.button('show Q2 Data'): st.table(q2_df)
    else:
         st.table(q1_sales)
    if st.checkbox('Show Q1 Data'): st.table(q1_sales)
    else: st.table(q2_sales)
elif section=='More widgets':
    st.write(st.slider('Which quarter?',1,4,(1,2)))
    st.write(st.multiselect('choose quarters',['Q1','Q2','Q3','Q4']))
    st.write(st.number_input('Which quarter?',1,4,(1,2)))
#cahcing
def download_data(quarter):
    sales=[100,200,300,400]
    time.sleep(3)
    return sales [quarter-1]

