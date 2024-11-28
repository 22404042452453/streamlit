import streamlit as st

st.title("Расчет индекса массы тела")

selected_sex = st.radio("Выбирите ваш пол:", ["Мужчина", "Женщина"], index=False)

selected_age = st.slider("Ваш возраст:", min_value=0, max_value=100)

selected_weight = st.slider("Ваша масса в кг:", min_value=0, max_value=180)

selected_height = st.slider("Ваша рост в см:", min_value=0, max_value=300)


@st.dialog("Ваш BMI")
def research_bmi():


    global selected_weight
    global selected_height
    try:

        bmi = round(selected_weight/(selected_height/100)**2, 1)


        if bmi <= 18.5:
            st.write('Ваш BMI', bmi,'а это значит, что у вас недостаточный вес!!!')

        elif bmi > 18.5 and bmi < 25:
            st.write('Ваш BMI', bmi,'а это значит, что ты нормальный.')

        elif bmi > 25 and bmi < 30:
            st.write('Ваш BMI', bmi,'а это значит, что у вас избыточный вес!')

        elif bmi > 30:
            st.write('Ваш BMI', bmi,'а это значит, что вы страдаете ожирением!!!')

    except Exception as ex:
        st.write('Ошибка')
        st.write('Пожалуйста проверьте данные которые вы ввели')



    st.snow()





st.button("Расчитать индекс массы тела", on_click = research_bmi)







