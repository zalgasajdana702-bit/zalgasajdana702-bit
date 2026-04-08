import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Text Wizard", layout="centered")

with st.sidebar:
    st.title("Настройки")
    api_key = st.text_input("Gemini API Key", type="password")

st.title("AI Text Wizard")
st.write("Улучшу твой текст или идею")

user_input = st.text_area("Текст:", height=150)

tone = st.selectbox(
    "Стиль:",
    ["Профессиональный", "Дружелюбный", "Краткий", "Креативный"]
)

if st.button("Сгенерировать"):
    if not api_key or not user_input:
        st.warning("Заполни все поля")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-pro")

            prompt = f"""
            Улучши текст в стиле: {tone}.
            Сделай его понятным, грамотным и интересным.

            Текст:
            {user_input}
            """

            with st.spinner("Генерация..."):
                response = model.generate_content(prompt)

            result = getattr(response, "text", None)

            if not result and hasattr(response, "candidates"):
                result = response.candidates[0].content.parts[0].text

            if result:
                st.success("Готово")
                st.write(result)
            else:
                st.error("Не удалось получить ответ от модели")

        except Exception as e:
            st.error(f"Ошибка: {e}")
