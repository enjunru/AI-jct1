import  streamlit as st
st.title("AI 大模型产品数据")
col,col1,col2 = st.columns(3)
with col:
    st.image("https://img1.baidu.com/it/u=4210670833,2619333922&fm=253&fmt=auto&app=120&f=GIF?w=380&h=380",width=225)
    flag = st.button("JC-T绘言",use_container_width=True)
    if flag:
        st.switch_page("pages/demo03.py")
with col1:
    st.image("https://img1.baidu.com/it/u=1911613735,2891783689&fm=253&fmt=auto&app=120&f=GIF?w=380&h=380", width=225)
    flag1 = st.button("JC-T绘图",use_container_width=True)
    if flag1:
        st.switch_page("pages/textToimage.py")
with col2:
    st.image("https://img1.baidu.com/it/u=4210670833,2619333922&fm=253&fmt=auto&app=120&f=GIF?w=380&h=380", width=225)
    flag2 = st.button("JC-T智能回复",use_container_width=True)
    if flag2:
        st.switch_page("pages/job-ai.py")
# c1,c2,c3,c4,c5 = st.columns(5)
# with c1:
#     flag = st.button("基础版")
#     if flag:
#         st.switch_page("pages/demo.py")
# with c2:
#     flag1 = st.button("进阶版1")
#     if flag1:
#         st.switch_page("pages/demo01.py")
# with c3:
#     flag2 = st.button("进阶版2")
#     if flag2:
#         st.switch_page("pages/demo02.py")
# with c4:
#     flag3 = st.button("最终版")
#     if flag3:
#         st.switch_page("pages/demo03.py")
# with c5:
#     flag4 = st.button("文生图")
#     if flag4:
#         st.switch_page("pages/textToimage.py")