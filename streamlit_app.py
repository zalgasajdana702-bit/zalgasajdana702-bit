import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Helper")

with st.sidebar:
    st.title("Настройки")
    api_key = st.text_input("Gemini API Key", type="password")

st.title("🧙‍♂️ AI Мастер")

user_input = st.text_area("Что сделать?", placeholder="Напиши что-нибудь...")

if st.button("Запустить"):
    if not api_key:
        st.error("Вставь API ключ в боковое меню!")
    else:
        try:
            genai.configure(api_key=api_key)
            # Используем flash-latest — она самая «живая» сейчас
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            
            with st.spinner('Магия в процессе...'):
                response = model.generate_content(user_input)
                st.success("Готово:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Ошибка: {str(e)}")
            st.info("Если видишь 404, проверь, не заблокирован ли Gemini в твоем регионе (иногда нужен VPN для работы API).")
