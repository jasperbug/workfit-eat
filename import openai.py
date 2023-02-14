import openai
import streamlit as st

# 設置OpenAI API密鑰
openai.api_key = "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"

# 定義生成建議的函數
def generate_diet_suggestion(age, gender, height, weight):
    prompt = f"根據以下信息生成一份飲食建議：\n年齡：{age}\n性別：{gender}\n身高：{height}\n體重：{weight}\n請生成一份飲食建議。"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        n=1,
        stop=None,
        timeout=10,
    )
    suggestion = response.choices[0].text.strip()
    return suggestion

# 定義Streamlit應用程序
def app():
    # 設置頁面標題和說明
    st.title("飲食建議生成器")
    st.write("請輸入您的個人信息以獲得一份飲食建議。")

    # 設置用戶輸入表單
    age = st.number_input("年齡", min_value=0, max_value=120, value=30)
    gender = st.selectbox("性別", ["男", "女"])
    height = st.number_input("身高（cm）", min_value=0, max_value=300, value=170)
    weight = st.number_input("體重（kg）", min_value=0, max_value=500, value=70)

    # 設置生成建議的按鈕
    if st.button("生成飲食建議"):
        suggestion = generate_diet_suggestion(age, gender, height, weight)
        st.write("您的飲食建議是：")
        st.write(suggestion)

# 運行Streamlit應用程序
if __name__ == "__main__":
    app()
