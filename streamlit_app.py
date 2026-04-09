import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Text Wizard", layout="centered")

API_KEY = "ТВОЙ_КЛЮЧ_ТУТ"
genai.configure(api_key=API_KEY)

st.title("AI Text Wizard")
st.write("Редактор текстов")

user_input = st.text_area("Текст:", height=150)

tone = st.selectbox(
    "Стиль:",
    ["Профессиональный", "Дружелюбный", "Краткий", "Креативный"]
)

if st.button("Сгенерировать"):
    if not user_input:
        st.warning("Введи текст")
    else:
        try:
            model = genai.GenerativeModel("gemini-1.0-pro")

            prompt = f"""
Перепиши текст в стиле: {tone}.
Сделай его понятным и интересным.

{user_input}
"""

            with st.spinner("Генерация..."):
                response = model.generate_content(prompt)

            result = getattr(response, "text", None)

            if not result and hasattr(response, "candidates"):
                result = response.candidates[0].content.parts[0].text

            if result:
                st.write(result)
            else:
                st.error("Нет ответа")

        except Exception as e:
            st.error(f"Ошибка: {e}")
