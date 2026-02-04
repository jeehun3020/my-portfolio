import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="Programs",
    page_icon="🎓",
    layout="wide"
)

# ===============================
# Session State
# ===============================
if "active_program" not in st.session_state:
    st.session_state.active_program = None


# ===============================
# Image Loader (robust)
# ===============================
SUPPORTED_EXTS = [".png", ".jpg", ".jpeg", ".JPG", ".JPEG"]

def load_images(folder, prefix=None):
    images = []
    if not os.path.exists(folder):
        return images

    for file in sorted(os.listdir(folder)):
        name, ext = os.path.splitext(file)
        if ext in SUPPORTED_EXTS:
            if prefix is None or name.startswith(prefix):
                try:
                    img = Image.open(os.path.join(folder, file)).convert("RGB")
                    images.append(img)
                except Exception:
                    pass
    return images


# ===============================
# Sidebar (Always Visible)
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
st.title("🎓 Programs")
st.markdown(
    "Selected international programs, training courses, and mentorship experiences."
)
st.markdown("---")


# ===============================
# Program Cards
# ===============================
col1, col2 = st.columns(2)

with col1:
    st.subheader("🇺🇸 Qualcomm AI Entrepreneurship Program")
    st.caption("UC San Diego · Qualcomm Institute (Jul. 2025)")
    if st.button("View Details", key="qualcomm"):
        st.session_state.active_program = "qualcomm"

    st.subheader("🇸🇬 Singapore Secure Coding Program")
    st.caption("Uppsala Security (Aug. 2024)")
    if st.button("View Details", key="singapore"):
        st.session_state.active_program = "singapore"

with col2:
    st.subheader("🌎 CES 2025 Software Mentoring Program")
    st.caption("Las Vegas & San Francisco (Jan. 2025)")
    if st.button("View Details", key="ces"):
        st.session_state.active_program = "ces"

    st.subheader("🇰🇷 Naver Boostcourse AI Program")
    st.caption("AI Basic Coaching Study (Jan–Feb. 2022)")
    if st.button("View Details", key="naver"):
        st.session_state.active_program = "naver"


# ===============================
# Popup-like Detail Area
# ===============================
if st.session_state.active_program:
    st.markdown("---")
    with st.container(border=True):

        # ===== Qualcomm =====
        if st.session_state.active_program == "qualcomm":
            st.header("Qualcomm Institute AI Entrepreneurship Program")

            st.markdown(
                """
                **Program Overview**  
                Participated in an intensive entrepreneurship program focused on  
                **AI-driven technology commercialization**.  
                Worked on team-based projects covering problem definition, technical validation,  
                business modeling, and pitching with mentorship from researchers and industry experts.
                """
            )

            st.markdown("---")

            photos = load_images("assets/programs/qualcomm", prefix="photo")
            if photos:
                cols = st.columns(min(5, len(photos)))
                for col, img in zip(cols, photos):
                    col.image(img, width=260)

            certs = load_images("assets/programs/qualcomm", prefix="certificate")
            if certs:
                st.subheader("📜 Certificates")
                c1, c2 = st.columns(min(2, len(certs)))
                for col, cert in zip([c1, c2], certs):
                    col.image(cert, width=420)

            st.markdown("📍 San Diego, United States  \n🗓 Jul. 5 – Jul. 27, 2025")

        # ===== CES =====
        elif st.session_state.active_program == "ces":
            st.header("CES 2025 Emerging Software Technology Program")

            st.markdown(
                """
                **Program Overview**  
                Explored emerging software technologies and global AI trends at **CES 2025**.  
                Participated in mentoring sessions and gained insights into how  
                cutting-edge research is translated into real-world products and services.
                """
            )

            st.markdown("---")

            photos = load_images("assets/programs/ces", prefix="photo")
            if photos:
                cols = st.columns(min(5, len(photos)))
                for col, img in zip(cols, photos):
                    col.image(img, width=260)

            certs = load_images("assets/programs/ces", prefix="certificate")
            if certs:
                st.subheader("📜 Certificate")
                for cert in certs:
                    st.image(cert, width=500)

            st.markdown("📍 Las Vegas & San Francisco, United States  \n🗓 Jan. 5 – Jan. 13, 2025")

        # ===== Singapore =====
        elif st.session_state.active_program == "singapore":
            st.header("Singapore Summer Secure Coding Program")

            st.markdown(
                """
                **Program Overview**  
                Completed an intensive training program focused on  
                **secure coding practices and software vulnerability analysis**.  
                Gained hands-on experience in identifying common security flaws  
                and understanding secure system design in real-world software systems.
                """
            )

            st.markdown("---")

            photos = load_images("assets/programs/singapore", prefix="photo")
            if photos:
                cols = st.columns(min(5, len(photos)))
                for col, img in zip(cols, photos):
                    col.image(img, width=260)

            certs = load_images("assets/programs/singapore", prefix="certificate")
            if certs:
                st.subheader("📜 Certificate")
                for cert in certs:
                    st.image(cert, width=500)

            st.markdown("📍 Singapore  \n🗓 Aug. 13 – Aug. 22, 2024")

        # ===== Naver =====
        elif st.session_state.active_program == "naver":
            st.header("Naver Boostcourse AI Basic Coaching Study Program")

            st.markdown(
                """
                **Program Overview**  
                Completed a foundational AI study program covering  
                machine learning concepts, model implementation, and  
                collaborative problem-solving through guided coaching sessions.
                """
            )

            st.markdown("---")

            certs = load_images("assets/programs/naver", prefix="certificate")
            for cert in certs:
                st.image(cert, width=500)

            st.markdown("📍 Korea  \n🗓 Jan. 13 – Feb. 24, 2022")

        st.button("❌ Close", on_click=lambda: setattr(st.session_state, "active_program", None))


st.markdown("---")
st.caption("© 2026 Jihoon Jeong · Streamlit Portfolio")
