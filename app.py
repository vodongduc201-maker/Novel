import streamlit as st
import subprocess

st.title("🧙‍♂️ AI Novel Generator")

# Ô nhập thông tin ý tưởng truyện
genre = st.selectbox("Thể loại:", ["Tiên hiệp", "Kiếm hiệp", "Khoa huyễn", "Đô thị"])
prompt = st.text_area("Ý tưởng/Tóm tắt cốt truyện:")

if st.button("Bắt đầu sáng tác"):
    with st.spinner("Các Agent AI đang thảo luận và viết truyện..."):
        # Gọi lệnh CLI chạy ngầm bằng Python subprocess
        # (Ví dụ: node dist/index.js --prompt "...")
        cmd = ["node", "dist/index.js", "--genre", genre, "--prompt", prompt]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        
        if result.returncode == 0:
            st.success("Đã viết xong!")
            st.markdown(result.stdout) # Hiển thị nội dung truyện ra web
        else:
            st.error("Có lỗi xảy ra khi chạy CLI:")
            st.code(result.stderr)
