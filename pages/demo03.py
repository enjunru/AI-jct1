'''
基于历史对话的聊天模型
'''

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain

#构建一个大模型对象
model = ChatOpenAI(
    temperature=0.8,#创新性
    model = "glm-4-plus",#大模型名字
    base_url = "https://open.bigmodel.cn/api/paas/v4/",
    api_key = "2e01180b076dc528afb3042fae705d6d.7FB1hUGKJIp80itG",#账号信息
)
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="history")

#提示词对象
prompt = PromptTemplate.from_template("你的名字叫檀健次，你现在要扮演一个男朋友的角色，你的性格是活泼开朗的，你现在要和你的女朋友进行对话，你只需要回应的女朋友的话,你女朋友说的话是{input}，你和你女朋友的历史对话为{history}")
chain = LLMChain(
    llm=model,
    prompt=prompt,
    memory=st.session_state.memory
)

st.title("邻家有个霸道总裁叫檀健次")
if "cache1" not in st.session_state:
    st.session_state.cache1 = []
else:
    #需要从缓存中获取信息在界面上渲染
    for message in st.session_state.cache1:
        with st.chat_message(message['role']):
            st.write(message["content"])

#创建聊天输入框
problem = st.chat_input("你的男朋友檀健次正在等待你的回答")
#判断是用来确定用户有没有输入问题 如果输入了问题
if problem:
    #1.将用户的问题输入到界面上
    with st.chat_message("user"):
        st.write(problem)
    st.session_state.cache1.append({"role":"user","content":problem})
    result = chain.invoke({"input": problem})
#调用大模型回答问题

#将大模型回答的问题输入到界面上

    with st.chat_message("assistant"):
        st.write(result['text'])
    st.session_state.cache1.append({"role": "assistant", "content":result['text']})