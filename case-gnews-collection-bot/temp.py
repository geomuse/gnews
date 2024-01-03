import streamlit as st

# 标题
st.title("Streamlit 排版示例")

# 段落文本
st.write("这是一个简单的 Streamlit 应用，演示文本排版。")

# Markdown
st.markdown("## 这是一个 Markdown 标题")
st.markdown("可以使用 *斜体* 和 **粗体**。")

# HTML
st.markdown("<p style='color: blue;'>这是一个带有样式的段落。</p>", unsafe_allow_html=True)

# 列表
st.markdown("### 列表示例")
st.markdown("- 项目 1")
st.markdown("- 项目 2")
st.markdown("- 项目 3")

# 表格
st.markdown("### 表格示例")
st.table({"列1": [1, 2, 3], "列2": ["A", "B", "C"]})
