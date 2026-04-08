import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Text Wizard", layout="centered")

with st.sidebar:
    st.title("Настройки")
    api_key = st.text_input("OpenAI API Key", type="password")

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
            client = OpenAI(api_key=api_key)

            prompt = f"""
Улучши текст в стиле: {tone}.
Сделай его понятным, грамотным и интересным.

Текст:
{user_input}
"""

            with st.spinner("Генерация..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Ты помогаешь улучшать тексты."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )

            result = response.choices[0].message.content

            st.success("Готово")
            st.write(result)

        except Exception as e:
            st.error(f"Ошибка: {e}")
