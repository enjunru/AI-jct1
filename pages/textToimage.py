import streamlit as st
from zhipuai import ZhipuAI
model = ZhipuAI(api_key="2e01180b076dc528afb3042fae705d6d.7FB1hUGKJIp80itG")
st.title("设计")

if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    #需要从缓存中获取信息在界面上渲染
    for message in st.session_state.cache:
        if message['role']=='user':
            with st.chat_message(message['role']):
                st.write(message['content'])
        else:
            with st.chat_message(message['role']):
                st.image(message["content"], width=400)



desc = st.chat_input("请输入图片的描述")
if desc:
    with st.chat_message("user"):
        st.write(desc)
        st.session_state.cache.append(({"role":"user","content":desc}))
    response = model.images.generations(
            model="cogview-3-plus",  # 填写需要调用的模型编码
            prompt=desc,
        )
    with st.chat_message("assistant"):
        st.image(response.data[0].url,width=400)
        st.session_state.cache.append(({"role": "assistant", "content": response.data[0].url}))
