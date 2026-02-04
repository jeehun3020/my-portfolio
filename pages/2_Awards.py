import streamlit as st

st.set_page_config(
    page_title="Awards",
    page_icon="🏆",
    layout="wide"
)

# ===== Sidebar =====
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
            label="📄 Download CV",
            data=pdf_file,
            file_name="Jihoon_Jeong_CV.pdf",
            mime="application/pdf"
        )

# ===== Main =====
st.title("AWARDS")
st.markdown("---")

def award_item(title, org, date, image_path, note=None):
    with st.expander(f"🏅 {title}"):
        st.markdown(f"**{org}**  \n{date}")
        if note:
            st.markdown(f"*{note}*")
        st.image(image_path, use_container_width=True)

award_item(
    "2025 SW중심대학 연합 SW FESTIVAL 대상",
    "SW중심대학연합, Korea",
    "Nov. 2025",
    "assets/awards/sw_festival_2025.jpg"
)

award_item(
    "2025 NASA International Space Apps Challenge – GALACTIC PROBLEM SOLVER",
    "NASA, Korea",
    "Oct. 2025",
    "assets/awards/nasa_space_apps_2025.png"
)

award_item(
    "2025 캡스톤 디자인 및 AI 해커톤 경진대회 장려상",
    "Korea Association of Computer Education, Korea",
    "Oct. 2025",
    "assets/awards/capstone_ai_hackathon_2025.png"
)

award_item(
    "국가우수장학금(이공계)",
    "Ministry of Science and ICT (MSIT), Korea Scholarship Foundation",
    "Oct. 2025",
    "assets/awards/scholarship_msit.png",
    note="Full tuition scholarship for junior and senior years"
)

award_item(
    "2025 한국정보기술학회 하계 종합학술대회 우수논문상(금상)",
    "Korea Institute of Information Technology, Korea",
    "Jun. 2025",
    "assets/awards/kiit_best_paper_2025.png"
)

award_item(
    "[교내] 2025 AI-Powered SW상상기업 경진대회 우수상",
    "Kyonggi University",
    "Oct. 2025",
    "assets/awards/sw_startup_award_2025.png"
)

award_item(
    "[교내] 2025 산학협력 캡스톤디자인 경진대회 은상",
    "Kyonggi University",
    "Jul. 2025",
    "assets/awards/capstone_industry_2025.png"
)
