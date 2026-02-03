import streamlit as st

st.set_page_config(
    page_title="Projects",
    page_icon="🚀",
    layout="wide"
)

# ===============================
# Session State
# ===============================
if "active_project" not in st.session_state:
    st.session_state.active_project = None


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
st.title("🚀 Projects")
st.markdown("Selected research and development projects.")
st.markdown("---")


# ===============================
# Project Cards
# ===============================
col1, col2 = st.columns(2)

with col1:
    st.subheader("🛰️ AIRBENDER (Navi)")
    st.caption("NASA TEMPO-based Air Quality Forecasting System")
    if st.button("View Details", key="airbender"):
        st.session_state.active_project = "airbender"

    st.subheader("🎯 FocusAI")
    st.caption("Vision-Based Real-Time Concentration Analysis System")
    if st.button("View Details", key="focusai"):
        st.session_state.active_project = "focusai"

with col2:
    st.subheader("🤖 Distribot")
    st.caption("Multi-User LLM-Based Interview Simulation System")
    if st.button("View Details", key="distribot"):
        st.session_state.active_project = "distribot"

    st.subheader("🚗 FocusDrive")
    st.caption("Real-Time Driver Drowsiness Detection System")
    if st.button("View Details", key="focusdrive"):
        st.session_state.active_project = "focusdrive"


# ===============================
# Popup-like Detail Area
# ===============================
if st.session_state.active_project:
    st.markdown("---")
    with st.container(border=True):

        # ===== AIRBENDER =====
        if st.session_state.active_project == "airbender":
            st.header("🛰️ AIRBENDER | Navi")

            st.image(
                "assets/projects/airbender.png",
                use_container_width=True
            )

            st.markdown("""
            **AIRBENDER** is an AI-powered air quality forecasting system leveraging
            **NASA TEMPO satellite data** to predict ozone levels and provide
            personalized health recommendations.
            """)

            st.markdown("""
            - Satellite & meteorological data fusion  
            - Vertex AI-based ozone forecasting  
            - LLM-driven personalized alerts
            """)

            st.video("https://www.youtube.com/watch?v=VvfAQruD_C0")

        # ===== FocusAI (2 images) =====
        elif st.session_state.active_project == "focusai":
            st.header("🎯 FocusAI")

            img1, img2 = st.columns(2)
            with img1:
                st.image("assets/projects/focusai_1.png", use_container_width=True)
            with img2:
                st.image("assets/projects/focusai_2.png", use_container_width=True)

            st.markdown("""
            **FocusAI** analyzes learner concentration in real time by detecting
            facial expressions and behaviors in intelligent learning environments.
            """)

            st.markdown("""
            - Eye closure, yawning, head movement detection  
            - Focus score calculation  
            - Learning time analysis
            """)

        # ===== Distribot (4 images) =====
        elif st.session_state.active_project == "distribot":
            st.header("🤖 Distribot")

            r1c1, r1c2 = st.columns(2)
            r2c1, r2c2 = st.columns(2)

            with r1c1:
                st.image("assets/projects/distribot_1.png", use_container_width=True)
            with r1c2:
                st.image("assets/projects/distribot_2.png", use_container_width=True)
            with r2c1:
                st.image("assets/projects/distribot_3.png", use_container_width=True)
            with r2c2:
                st.image("assets/projects/distribot_4.png", use_container_width=True)

            st.markdown("""
            **Distribot** is a scalable, multi-user interview simulation system
            powered by large language models.
            """)

            st.markdown("""
            - Real-time multi-user interview sessions  
            - LLM-based interviewer  
            - Session & time management
            """)

        # ===== FocusDrive (2 images) =====
        elif st.session_state.active_project == "focusdrive":
            st.header("🚗 FocusDrive")

            img1, img2 = st.columns(2)
            with img1:
                st.image("assets/projects/focusdrive_1.png", use_container_width=True)
            with img2:
                st.image("assets/projects/focusdrive_2.png", use_container_width=True)

            st.markdown("""
            **FocusDrive** detects driver drowsiness in real time using webcam input
            and triggers immediate alerts.
            """)

            st.markdown("""
            - OpenCV-based real-time frame capture  
            - Vertex AI AutoML Vision classification  
            - Immediate audio alert
            """)

            st.video("https://youtu.be/XolHcfSMTRQ")

        st.button("❌ Close", on_click=lambda: setattr(st.session_state, "active_project", None))


st.markdown("---")
st.caption("© 2026 Jihoon Jeong · Streamlit Portfolio")