import streamlit as st
import base64

st.set_page_config(
    page_title="Home | Jihoon Jeong",
    layout="wide"
)

# ==============================
# Global CSS (Dark mode support)
# ==============================
st.markdown(
    """
    <style>
    :root {
        --accent: #4F46E5;
        --card-bg-light: #ffffff;
        --card-bg-dark: #1f2937;
        --border-light: #e5e7eb;
        --border-dark: #374151;
        --tag-light: #eef2ff;
        --tag-dark: #312e81;
    }

    @media (prefers-color-scheme: dark) {
        .card {
            background-color: var(--card-bg-dark);
            border: 1px solid var(--border-dark);
        }
        .tag {
            background-color: var(--tag-dark);
            color: #e0e7ff;
        }
    }

    @media (prefers-color-scheme: light) {
        .card {
            background-color: var(--card-bg-light);
            border: 1px solid var(--border-light);
        }
        .tag {
            background-color: var(--tag-light);
            color: #1e1b4b;
        }
    }

    .card {
        padding: 22px;
        border-radius: 16px;
        margin-bottom: 12px;
    }

    .accent {
        color: var(--accent);
    }

    .tag {
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 0.85rem;
        white-space: nowrap;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# Helper: PDF Viewer
# ==============================
def show_pdf(file_path: str):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    st.markdown(
        f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}"
                width="100%" height="850px" style="border:none;"></iframe>
        """,
        unsafe_allow_html=True
    )


# ==============================
# Sidebar — Profile & Contact
# ==============================
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

    if st.button("👀 View CV"):
        st.session_state["show_cv"] = True

    with open("assets/Jihoon_Jeong_CV.pdf", "rb") as pdf_file:
        st.download_button(
            "📄 Download CV",
            pdf_file,
            file_name="Jihoon_Jeong_CV.pdf",
            mime="application/pdf"
        )


# ==============================
# CV Viewer
# ==============================
if st.session_state.get("show_cv", False):
    st.markdown("## 📄 Curriculum Vitae")
    show_pdf("assets/Jihoon_Jeong_CV.pdf")
    st.markdown("---")


# ==============================
# Research Focus
# ==============================
st.markdown(
    """
    <div class="card">
        <b>Research Focus</b><br>
        Building efficient computer vision systems that bridge
        <b>theoretical robustness</b> and <b>real-world deployment</b>.
    </div>
    """,
    unsafe_allow_html=True
)

# ==============================
# About Me
# ==============================
st.markdown("## 👤 About Me")
st.write(
    "I am a Bachelor student in AI Computer Engineering at Kyonggi University "
    "with research interests in Computer Vision, Image Segmentation, and "
    "Efficient Deep Learning. I aim to design AI systems that are both "
    "theoretically grounded and practically deployable."
)

st.markdown("---")


# ==============================
# Skills & Education
# ==============================
left, right = st.columns(2)

with left:
    st.markdown("## 🛠 Technical Skills")
    st.markdown("""
    **Languages**  
    Python · R · SQL  

    **Frameworks**  
    PyTorch · TensorFlow · Keras
    """)

    st.markdown("**Research Interests**")
    st.markdown(
        """
        <div style="display:flex; flex-wrap:wrap; gap:8px;">
            <span class="tag">Computer Vision</span>
            <span class="tag">Image & Semantic Segmentation</span>
            <span class="tag">Vision-Language Multimodal Learning</span>
            <span class="tag">Efficient / On-Device AI</span>
        </div>
        """,
        unsafe_allow_html=True
    )

with right:
    st.markdown("## 🎓 Education")
    st.markdown("""
    **Kyonggi University**  
    Department of AI Computer Engineering  

    - Bachelor Student (Mar. 2021 – Present)  
    - GPA: **4.49 / 4.5**
    """)

st.markdown("---")


# ==============================
# Featured Project
# ==============================
st.markdown("## ⭐ Featured Project")

st.markdown(
    """
    <div class="card">
        <h3 class="accent">🎯 FocusAI — Intelligent Study Room System</h3>
        Vision-based learning concentration analysis system using
        facial expression and behavior recognition.  
        Designed for real-world deployment in intelligent study environments.
    </div>
    """,
    unsafe_allow_html=True
)
st.page_link("pages/1_Projects.py", label="View Project Details →")

st.markdown("---")


# ==============================
# Explore
# ==============================
st.markdown("## 🔗 Explore")

def explore_card(title, desc, link):
    st.markdown(
        f"""
        <div class="card">
            <h3 class="accent">{title}</h3>
            <p>{desc}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.page_link(link, label="View →")

c1, c2 = st.columns(2)
c3, c4 = st.columns(2)

with c1:
    explore_card("🚀 Projects", "Research and AI system development projects.", "pages/1_Projects.py")

with c2:
    explore_card("🎓 Programs", "International programs and mentorship experiences.", "pages/3_Programs.py")

with c3:
    explore_card("🏆 Awards", "Academic awards, competitions, and scholarships.", "pages/2_Awards.py")

with c4:
    explore_card("📄 Publications", "Peer-reviewed conference papers and publications.", "pages/5_Publications.py")

st.markdown("---")
st.caption("© 2026 Jihoon Jeong · Streamlit Portfolio")