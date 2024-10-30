#制作聊天界面
import streamlit as st
from  langchain_openai import ChatOpenAI


#构建一个大模型
model = ChatOpenAI(
    temperature=0.8,#创新性
    model = "glm-4-plus",#大模型名字
    base_url = "https://open.bigmodel.cn/api/paas/v4/",
    api_key = "2e01180b076dc528afb3042fae705d6d.7FB1hUGKJIp80itG",#账号信息
)
st.title("AI demo小程序")
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    #需要从缓存中获取信息在界面上渲染
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])

#创建聊天输入框
problem = st.chat_input("请输入你的问题")
#判断是用来确定用户有没有输入问题 如果输入了问题
if problem:
    #1.将用户的问题输入到界面上
    with st.chat_message("user"):
        st.write(problem)
    st.session_state.cache.append({"role":"user","content":problem})
#调用大模型回答问题
    result = model.invoke(problem)
#将大模型回答的问题输入到界面上

    with st.chat_message("assistant"):
        st.write(result.content)
    st.session_state.cache.append({"role": "assistant", "content":result.content})