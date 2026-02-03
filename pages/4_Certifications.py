import streamlit as st

st.set_page_config(
    page_title="Certifications",
    page_icon="📜",
    layout="wide"
)

# ===============================
# Session State
# ===============================
if "active_cert" not in st.session_state:
    st.session_state.active_cert = None


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
st.title("📜 Certifications")
st.markdown("Professional certifications and technical qualifications.")
st.markdown("---")


# ===============================
# Certification Cards
# ===============================
col1, col2 = st.columns(2)

with col1:
    st.subheader("☁️ Google Cloud Professional ML Engineer")
    st.caption("Google Cloud Platform · Jul. 2025")
    if st.button("View Details", key="gcp_ml"):
        st.session_state.active_cert = "gcp_ml"

    st.subheader("🧪 CSTS")
    st.caption("Certified Software Test Specialist · May 2025")
    if st.button("View Details", key="csts"):
        st.session_state.active_cert = "csts"

    st.subheader("📊 TOPCIT")
    st.caption("Test of Practical Competency in IT · Score: 639 · May 2025")
    if st.button("View Details", key="topcit"):
        st.session_state.active_cert = "topcit"

with col2:
    st.subheader("📈 ADsP")
    st.caption("Advanced Data Analytics Semi-Professional · Mar. 2025")
    if st.button("View Details", key="adsp"):
        st.session_state.active_cert = "adsp"

    st.subheader("🗄 SQLD")
    st.caption("SQL Developer · Dec. 2024")
    if st.button("View Details", key="sqld"):
        st.session_state.active_cert = "sqld"

    st.subheader("🖥 MOS Master")
    st.caption("Microsoft Office Specialist Master · Jul. 2021")
    if st.button("View Details", key="mos"):
        st.session_state.active_cert = "mos"


# ===============================
# Popup-like Detail Area
# ===============================
if st.session_state.active_cert:
    st.markdown("---")
    with st.container(border=True):

        # ===== GCP ML Engineer =====
        if st.session_state.active_cert == "gcp_ml":
            st.header("Google Cloud Professional Machine Learning Engineer")

            st.markdown("""
            A professional-level certification validating the ability to design,
            build, and productionize machine learning models on **Google Cloud Platform**.
            """)

            st.markdown("""
            **Key Competencies**
            - End-to-end ML system design on GCP  
            - Vertex AI model training, deployment, and monitoring  
            - Feature engineering & data pipelines  
            - Responsible AI and MLOps practices
            """)

            st.markdown("🗓 **Issued**: Jul. 2025")

        # ===== CSTS =====
        elif st.session_state.active_cert == "csts":
            st.header("CSTS (Certified Software Test Specialist)")

            st.markdown("""
            A professional certification focused on software testing theory,
            test design techniques, and quality assurance processes.
            """)

            st.markdown("""
            **Coverage**
            - Software testing life cycle  
            - Black-box & white-box testing  
            - Test case design and defect management
            """)

            st.markdown("🗓 **Issued**: May 2025")

        # ===== TOPCIT =====
        elif st.session_state.active_cert == "topcit":
            st.header("TOPCIT (Test Of Practical Competency in IT)")

            st.markdown("""
            A nationally recognized IT competency assessment measuring
            problem-solving ability and practical engineering skills.
            """)

            st.markdown("""
            **Highlights**
            - Software development & data analysis  
            - System architecture understanding  
            - Practical problem-solving assessment
            """)

            st.markdown("🏆 **Score**: 639  \n🗓 **Issued**: May 2025")

        # ===== ADsP =====
        elif st.session_state.active_cert == "adsp":
            st.header("ADsP (Advanced Data Analytics Semi-Professional)")

            st.markdown("""
            A data analytics certification issued by the **Korea Data Agency**,
            validating foundational knowledge in data analysis and statistics.
            """)

            st.markdown("""
            **Coverage**
            - Data preprocessing & EDA  
            - Statistical analysis  
            - Data-driven decision making
            """)

            st.markdown("🗓 **Issued**: Mar. 2025")

        # ===== SQLD =====
        elif st.session_state.active_cert == "sqld":
            st.header("SQLD (SQL Developer)")

            st.markdown("""
            A certification verifying proficiency in SQL-based data modeling,
            querying, and database management.
            """)

            st.markdown("""
            **Coverage**
            - Relational data modeling  
            - Advanced SQL queries  
            - Database integrity and optimization
            """)

            st.markdown("🗓 **Issued**: Dec. 2024")

        # ===== MOS =====
        elif st.session_state.active_cert == "mos":
            st.header("MOS Master (Microsoft Office Specialist Master)")

            st.markdown("""
            A master-level certification demonstrating advanced proficiency
            across multiple Microsoft Office applications.
            """)

            st.markdown("""
            **Included Applications**
            - Word, Excel, PowerPoint, Outlook  
            - Advanced document and data handling
            """)

            st.markdown("🗓 **Issued**: Jul. 2021")

        st.button("❌ Close", on_click=lambda: setattr(st.session_state, "active_cert", None))


st.markdown("---")
st.caption("© 2026 Jihoon Jeong · Streamlit Portfolio")