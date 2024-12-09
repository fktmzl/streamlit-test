import streamlit as st
st.title("st.form")
# 'with' 표기법을 사용한 전체 예시
st.header('1. with 표기법 사용 예시')
st.subheader('게임 접속하기')
with st.form('my_form'):
    st.subheader('**게임 캐릭터 생성하기**')
    #입력 위젯
    new_Character = st.selectbox('성별', ['남자', '여자'])
    Character_Haircolor = st.selectbox('머리색', ['검정색', '하얀색', '빨강색'])
    Character_build = st.selectbox('체구', ['뚱뚱함', '마름', '평범'])
    Character_Occupation = st.selectbox('직업', ['기사', '도적', '마법사'])
   
    submitted = st.form_submit_button('생성하기') #모든 양식은 제출 버튼을 가져야 함
if submitted:
    st.markdown(f'''
            주문하신 내용:
        - 성별: '{new_Character}'
        - 머리색: '{Character_Haircolor}'
        - 체구: '{Character_build}'
        - 직업: '{Character_Occupation}' 
           
        ''')
else:
    st.write(' 주문하세요!')


# 객체 표기법을 사용한 짧은 예시
st.header('2. 객체 표기법 예시')

form = st.form('my_form_2')
selected_val = form.slider('값 선택')
form.form_submit_button('제출') #모든 양식은 st.form_submit_button을 포함해야 함.
#st.button과 st.download_button은 양식에 추가할 수 없습니다.
st.write('선택된 값: ', selected_val)
