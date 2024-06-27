import streamlit as st

# 웹 페이지 타이틀 설정
st.title('AI 디자이너 | 언리밋')

# 명함 이미지 파일 경로
business_card_image_path = 'business_card.png'  # QR code card 폴더 안에 있는 이미지 파일

# 명함 이미지 표시
st.image(business_card_image_path, use_column_width=True)

# 버튼들 배치
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <a href="https://litt.ly/unlimit" target="_blank">
            <button style="background-color:#4CAF50; border:none; color:white; padding:15px 32px; text-align:center; text-decoration:none; display:inline-block; font-size:16px; margin:4px 2px; cursor:pointer; border-radius:4px;">
                프로필 이동
            </button>
        </a>
        """, unsafe_allow_html=True
    )

with col2:
    with open(business_card_image_path, "rb") as file:
        st.download_button(
            label="Download Business Card",
            data=file,
            file_name="BusinessCard.png",
            mime="image/png"
        )
