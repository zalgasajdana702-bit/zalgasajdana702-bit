import streamlit as st
import google.generativeai as genai

# Настройка страницы
st.set_page_config(page_title="AI Text Wizard", layout="centered")

# Боковое меню (Sidebar)
with st.sidebar:
    st.title("⚙️ Настройки")
    api_key = st.text_input("Введите Gemini API Key:", type="password")
    st.info("Получите ключ в Google AI Studio")

# Основной интерфейс
st.title("🧙‍♂️ AI Text Wizard")
st.subheader("Превращу твои мысли в идеальный пост")

# Поле ввода
user_input = st.text_area("Введите текст или идею:", placeholder="Например: Напиши пост про пользу сна для студентов")

# Кнопка запуска
if st.button("Сгенерировать магию ✨"):
    if not api_key:
        st.error("Сначала введи API ключ в боковом меню!")
    elif not user_input:
        st.warning("Напиши хоть что-нибудь!")
    else:
        try:
            # Настройка AI
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            
            with st.spinner('AI думает...'):
                response = model.generate_content(f"Сделай этот текст лучше и профессиональнее: {user_input}")
                
            # Отображение результата
            st.success("Готово!")
            st.write(response.text)
        except Exception as e:
            st.error(f"Ошибка: {e}")
