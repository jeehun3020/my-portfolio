import streamlit as st

st.set_page_config(
    page_title="Publications",
    page_icon="📄",
    layout="wide"
)

# ===============================
# Session State
# ===============================
if "active_paper" not in st.session_state:
    st.session_state.active_paper = None


# ===============================
# Sidebar (항상 유지)
# ===============================
with st.sidebar:
    st.image("assets/profile.jpg", width=160)
    st.markdown("## Jihoon Jeong")
    st.caption("Undergraduate Researcher · Computer Vision & AI")

    st.markdown("📞 **Phone**: +82-10-9260-6744")
    st.markdown("🎂 **Date of Birth**: 2001.03.02")
    st.markdown("✉️ **Email**: jeehun3020@gmail.com")
    st.markdown("[GitHub](https://github.com/jeehun3020)")

    st.info(
        "I am interested in building efficient AI systems that transform "
        "complex visual data into practical value."
    )

    st.markdown("---")
    st.markdown("### Curriculum Vitae")
    with open("assets/Jihoon_Jeong_CV.pdf", "rb") as pdf_file:
        st.download_button(
            "📄 Download CV",
            data=pdf_file,
            file_name="Jihoon_Jeong_CV.pdf",
            mime="application/pdf"
        )


# ===============================
# Main Page
# ===============================
st.title("📄 Publications")
st.markdown("Peer-reviewed conference papers and academic publications.")
st.markdown("---")


# ===============================
# Publication Cards
# ===============================
st.subheader("📌 Conference Papers")

paper_col1, paper_col2 = st.columns(2)

with paper_col1:
    st.markdown("### 지능형 독서실에서 얼굴 및 행동 분석 기반 학습 집중도 시스템")
    st.caption("한국정보기술학회 하계 종합학술대회 · 2025")
    if st.button("View Details", key="paper_focus"):
        st.session_state.active_paper = "focus"

with paper_col2:
    st.markdown("### 객체 인식 기반 딥러닝을 활용한 노인 낙상 및 위험 상황 감지 시스템")
    st.caption("한국인터넷정보학회 추계학술발표대회 · 2024")
    if st.button("View Details", key="paper_fall"):
        st.session_state.active_paper = "fall"


# ===============================
# Popup-like Detail Area
# ===============================
if st.session_state.active_paper:
    st.markdown("---")
    with st.container(border=True):

        # ===== Paper 1 =====
        if st.session_state.active_paper == "focus":
            st.header("지능형 독서실에서 얼굴 및 행동 분석 기반 학습 집중도 시스템")

            st.markdown("""
            **Authors**  
            Jihoon Jeong, Sieun Kim, Yeeun Kim, Eunseo Park,  
            Seunga Seo, Seoryeong Jang, Kiyeon Ham
            """)

            st.markdown("""
            **Conference**  
            한국정보기술학회 하계 종합학술대회 논문집
            """)

            st.markdown("""
            **Year**  
            2025
            """)

            st.markdown("""
            **Abstract**  
            This paper presents a vision-based learning concentration analysis system
            for intelligent study environments. The proposed system analyzes facial
            expressions and behavioral cues such as eye closure, yawning, head movement,
            and seat departure to quantitatively evaluate learner focus levels.
            """)

        # ===== Paper 2 =====
        elif st.session_state.active_paper == "fall":
            st.header("객체 인식 기반 딥러닝을 활용한 노인 낙상 및 위험 상황 감지 시스템")

            st.markdown("""
            **Authors**  
            Bo-Gyeong Ko, Jeong-Yeon Park, Youn-A Lee, Seung-Jae Kim,  
            Jihoon Jeong, Chae-Won Lee, Sieun Kim, Yeeun Kim, Seunga Seo
            """)

            st.markdown("""
            **Conference**  
            한국인터넷정보학회 추계학술발표대회 논문집
            """)

            st.markdown("""
            **Year**  
            2024
            """)

            st.markdown("""
            **Abstract**  
            This study proposes a deep learning-based elderly fall and risk situation
            detection system using object recognition techniques. The system aims to
            improve safety monitoring by accurately detecting falls and hazardous
            situations in indoor environments.
            """)

        st.button("❌ Close", on_click=lambda: setattr(st.session_state, "active_paper", None))


st.markdown("---")
st.caption("© 2026 Jihoon Jeong · Streamlit Portfolio")