import streamlit as st
import base64
import os

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Raja Roy | AI & Data Science Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# HELPERS
# ---------------------------
def get_file_bytes(filename: str) -> bytes | None:
    """Read file bytes from app directory (or relative path)."""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        path1 = os.path.join(script_dir, filename)
        if os.path.exists(path1):
            with open(path1, "rb") as f:
                return f.read()

        if os.path.exists(filename):
            with open(filename, "rb") as f:
                return f.read()

        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def get_image_base64(image_filename: str) -> str | None:
    """Convert image to base64 for embedding."""
    data = get_file_bytes(image_filename)
    if not data:
        return None
    return base64.b64encode(data).decode()


# ---------------------------
# THEME TOGGLE (Light/Dark)
# ---------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

with st.sidebar:
    st.markdown("### 🎨 Theme")
    theme_choice = st.radio(
        "Select theme",
        ["Light", "Dark"],
        index=0 if st.session_state.theme == "light" else 1,
        label_visibility="collapsed"
    )
    st.session_state.theme = "light" if theme_choice == "Light" else "dark"


# ---------------------------
# CSS (Variables for Light/Dark + Sidebar Width + Mobile Fixes)
# ---------------------------
# You can tweak these widths:
# Desktop sidebar width: 300px
# Mobile sidebar width: 260px

theme = st.session_state.theme

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

* {{
  font-family: 'Poppins', sans-serif;
}}

/* ---------------------------
   THEME VARIABLES
--------------------------- */
:root {{
  --bg1: #667eea;
  --bg2: #764ba2;

  --panel: rgba(255,255,255,0.95);
  --panel2: rgba(255,255,255,0.10);

  --text: #111827;
  --muted: #6B7280;

  --shadow: 0 8px 24px rgba(0,0,0,0.10);
  --shadow2: 0 16px 48px rgba(0,0,0,0.20);

  --accent1: #667eea;
  --accent2: #764ba2;
}}

{"/* DARK THEME OVERRIDES */" if theme == "dark" else ""}
{"\
:root {\
  --panel: rgba(17,24,39,0.92);\
  --panel2: rgba(255,255,255,0.08);\
  --text: #F9FAFB;\
  --muted: #D1D5DB;\
  --shadow: 0 8px 24px rgba(0,0,0,0.35);\
  --shadow2: 0 16px 48px rgba(0,0,0,0.55);\
}\
" if theme == "dark" else ""}

/* ---------------------------
   BACKGROUND
--------------------------- */
.stApp {{
  background: linear-gradient(135deg, var(--bg1) 0%, var(--bg2) 100%);
  background-attachment: fixed;
}}

/* Give space so header toggle isn't overlapped */
.block-container {{
  padding-top: 2.5rem !important;
}}

/* Hide menu/footer only */
#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}

/* Sidebar toggle safe */
[data-testid="collapsedControl"],
[data-testid="stSidebarCollapsedControl"] {{
  z-index: 9999 !important;
  border-radius: 999px !important;
  background: rgba(255,255,255,0.92) !important;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
}}
{"\
[data-testid='collapsedControl'],\
[data-testid='stSidebarCollapsedControl'] {\
  background: rgba(17,24,39,0.85) !important;\
}\
" if theme == "dark" else ""}

/* ---------------------------
   SIDEBAR WIDTH (NARROW)
--------------------------- */
/* Sidebar container */
[data-testid="stSidebar"] {{
  background: var(--panel);
  backdrop-filter: blur(10px);
  border-right: 1px solid rgba(255,255,255,0.20);
  box-shadow: 4px 0 24px rgba(0,0,0,0.10);
  width: 300px !important;
}}
/* Inner sidebar */
[data-testid="stSidebar"] > div:first-child {{
  padding-top: 1.25rem;
  width: 300px !important;
}}

/* ---------------------------
   COMPONENTS
--------------------------- */
.glass-card {{
  background: var(--panel);
  backdrop-filter: blur(10px);
  border-radius: 24px;
  padding: 2.5rem;
  border: 1px solid rgba(255,255,255,0.25);
  box-shadow: var(--shadow);
  margin-bottom: 2rem;
  transition: all 0.3s ease;
  color: var(--text);
}}

.glass-card:hover {{
  transform: translateY(-8px);
  box-shadow: var(--shadow2);
}}

.hero-glass {{
  background: var(--panel2);
  backdrop-filter: blur(20px);
  border-radius: 32px;
  padding: 4rem;
  border: 1px solid rgba(255,255,255,0.20);
  box-shadow: 0 8px 32px rgba(0,0,0,0.20);
  margin-bottom: 3rem;
  color: white;
}}

.profile-container {{
  text-align: center;
  margin-bottom: 1.25rem;
}}

.profile-img {{
  border-radius: 50%;
  width: 170px;
  height: 170px;
  object-fit: cover;
  border: 5px solid rgba(255,255,255,0.85);
  box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
  margin: 0 auto;
  display: block;
  transition: all 0.3s ease;
}}

.profile-img:hover {{
  transform: scale(1.05);
}}

.skill-badge {{
  display: inline-block;
  padding: 8px 16px;
  margin: 5px;
  background: linear-gradient(135deg, var(--accent1) 0%, var(--accent2) 100%);
  color: white;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
  transition: all 0.3s ease;
}}
.skill-badge:hover {{
  transform: translateY(-2px);
}}

.stat-box {{
  background: var(--panel);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 2rem;
  text-align: center;
  border: 1px solid rgba(255,255,255,0.25);
  box-shadow: var(--shadow);
  transition: all 0.3s ease;
  color: var(--text);
}}
.stat-box:hover {{
  transform: translateY(-5px);
}}

.stat-number {{
  font-size: 3rem;
  font-weight: 900;
  background: linear-gradient(135deg, var(--accent1) 0%, var(--accent2) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
  margin-bottom: 0.5rem;
}}
.stat-label {{
  font-size: 0.85rem;
  color: var(--muted);
  font-weight: 600;
  letter-spacing: 0.05em;
}}

.timeline-card {{
  background: var(--panel);
  backdrop-filter: blur(10px);
  border-left: 4px solid var(--accent1);
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  transition: all 0.3s ease;
  color: var(--text);
}}
.timeline-card:hover {{
  transform: translateX(8px);
  border-left-color: var(--accent2);
}}

.gradient-text {{
  background: linear-gradient(135deg, var(--accent1) 0%, var(--accent2) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 800;
}}

.contact-item {{
  padding: 0.75rem;
  margin: 0.5rem 0;
  background: rgba(102, 126, 234, 0.12);
  border-radius: 12px;
  border-left: 3px solid var(--accent1);
  transition: all 0.3s ease;
  color: var(--text);
}}
.contact-item:hover {{
  background: rgba(102, 126, 234, 0.20);
  transform: translateX(5px);
}}

.project-card {{
  background: var(--panel);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 2rem;
  border: 1px solid rgba(255,255,255,0.25);
  box-shadow: var(--shadow);
  height: 100%;
  transition: all 0.3s ease;
  color: var(--text);
}}
.project-card:hover {{
  transform: translateY(-8px);
}}

.featured-project {{
  background: linear-gradient(135deg, var(--accent1) 0%, var(--accent2) 100%);
  color: white;
  border: none;
}}
.featured-project * {{
  color: white !important;
}}

.stButton > button {{
  width: 100%;
  background: linear-gradient(135deg, var(--accent1) 0%, var(--accent2) 100%);
  color: white !important;
  border: none;
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  font-weight: 600;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
  transition: all 0.3s ease;
}}
.stButton > button:hover {{
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(102, 126, 234, 0.5);
}}

.stTabs [data-baseweb="tab-list"] {{
  gap: 8px;
  background: var(--panel);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 8px;
}}
.stTabs [data-baseweb="tab"] {{
  border-radius: 12px;
  color: var(--muted);
  font-weight: 600;
  padding: 12px 24px;
}}
.stTabs [aria-selected="true"] {{
  background: linear-gradient(135deg, var(--accent1) 0%, var(--accent2) 100%);
  color: white !important;
}}

/* Scrollbar */
::-webkit-scrollbar {{ width: 10px; height: 10px; }}
::-webkit-scrollbar-track {{ background: rgba(255, 255, 255, 0.1); }}
::-webkit-scrollbar-thumb {{
  background: linear-gradient(135deg, var(--accent1) 0%, var(--accent2) 100%);
  border-radius: 10px;
}}

/* ---------------------------
   MOBILE RESPONSIVE FIXES
--------------------------- */
@media (max-width: 768px) {{
  [data-testid="stSidebar"] {{
    width: 260px !important;
  }}
  [data-testid="stSidebar"] > div:first-child {{
    width: 260px !important;
  }}

  .hero-glass {{
    padding: 2rem !important;
    border-radius: 24px !important;
  }}

  .profile-img {{
    width: 130px !important;
    height: 130px !important;
  }}

  .glass-card {{
    padding: 1.5rem !important;
    border-radius: 18px !important;
  }}

  .project-card {{
    padding: 1.5rem !important;
  }}
}}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# SIDEBAR CONTENT
# ---------------------------
with st.sidebar:
    st.markdown('<div class="profile-container">', unsafe_allow_html=True)

    img_base64 = get_image_base64("profile_photo.png")
    if img_base64:
        st.markdown(
            f'<img src="data:image/png;base64,{img_base64}" class="profile-img">',
            unsafe_allow_html=True
        )
    else:
        st.info("📸 Add 'profile_photo.png' for your profile picture")

    st.markdown("<h2 style='text-align: center; margin: 1rem 0 0.5rem 0;' class='gradient-text'>RAJA ROY</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: var(--muted); font-weight: 700; font-size: 0.85rem; letter-spacing: 0.1em;'>AI ENGINEER & DATA SCIENTIST</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 📬 Contact")
    st.markdown("""
        <div class="contact-item">
            <strong>📧 Email</strong><br>
            rajaroybca6@gmail.com
        </div>
        <div class="contact-item">
            <strong>📱 Phone</strong><br>
            +39 388 381 8145
        </div>
        <div class="contact-item">
            <strong>📍 Location</strong><br>
            Torino, Italy
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🌍 Languages")
    st.markdown("""
        <div style="padding: 0.5rem; color: var(--text);">
            🇬🇧 <strong>English</strong> - Native<br>
            🇮🇹 <strong>Italian</strong> - B2<br>
            🇮🇳 <strong>Hindi</strong> - Native
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🎓 Current Study")
    st.markdown("""
        <div style="padding: 0.75rem; background: rgba(102, 126, 234, 0.12); border-radius: 12px; border-left: 3px solid var(--accent1); color: var(--text);">
            <strong>AI Specialist Master's</strong><br>
            INFOR ELEA Academy<br>
            <small>Oct 2025 - Present</small>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ---------------------------
    # REAL CV DOWNLOAD
    # ---------------------------
    cv_filename = "Raja_Roy_CV.pdf"  # put this file in same folder as app.py
    cv_bytes = get_file_bytes(cv_filename)

    if cv_bytes:
        st.download_button(
            label="📥 Download CV (PDF)",
            data=cv_bytes,
            file_name=cv_filename,
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.warning(f"⚠️ CV not found. Add '{cv_filename}' to your app folder.")


# ---------------------------
# HERO SECTION
# ---------------------------
st.markdown("""
    <div class="hero-glass">
        <p style="font-weight: 700; font-size: 0.85rem; letter-spacing: 0.2em; margin-bottom: 1rem; opacity: 0.9;">SENIOR DATA ANALYST • FULL-STACK DEVELOPER</p>
        <h1 style="font-size: 4rem; line-height: 1; margin-bottom: 1.5rem;">
            Building Intelligent<br>
            <span style="color: #fff; text-shadow: 0 0 30px rgba(255,255,255,0.5);">Data Solutions</span>
        </h1>
        <p style="font-size: 1.2rem; max-width: 800px; margin-bottom: 2.5rem; line-height: 1.7; opacity: 0.95;">
            Transforming complex data into actionable insights with 8+ years of expertise in analytics,
            machine learning, and full-stack development. Specialized in creating production-grade
            AI-enabled solutions that drive measurable business value.
        </p>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
            <span style="background: rgba(255,255,255,0.25); padding: 10px 20px; border-radius: 12px; font-weight: 600; backdrop-filter: blur(10px);">Python</span>
            <span style="background: rgba(255,255,255,0.25); padding: 10px 20px; border-radius: 12px; font-weight: 600; backdrop-filter: blur(10px);">SQL</span>
            <span style="background: rgba(255,255,255,0.25); padding: 10px 20px; border-radius: 12px; font-weight: 600; backdrop-filter: blur(10px);">Machine Learning</span>
            <span style="background: rgba(255,255,255,0.25); padding: 10px 20px; border-radius: 12px; font-weight: 600; backdrop-filter: blur(10px);">Power BI</span>
            <span style="background: rgba(255,255,255,0.25); padding: 10px 20px; border-radius: 12px; font-weight: 600; backdrop-filter: blur(10px);">PHP</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ---------------------------
# STATS
# ---------------------------
st.markdown("## 📊 Professional Impact")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""<div class="stat-box"><div class="stat-number">8+</div><div class="stat-label">YEARS EXPERIENCE</div></div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""<div class="stat-box"><div class="stat-number">5</div><div class="stat-label">COMPANIES</div></div>""", unsafe_allow_html=True)
with c3:
    st.markdown("""<div class="stat-box"><div class="stat-number">15+</div><div class="stat-label">TECH SKILLS</div></div>""", unsafe_allow_html=True)
with c4:
    st.markdown("""<div class="stat-box"><div class="stat-number">100%</div><div class="stat-label">DEDICATION</div></div>""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------------
# TABS
# (Your same content, shortened here — you can paste your existing tab content below)
# ---------------------------
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Projects", "💼 Experience", "🎓 Education & Skills", "👤 About Me"])

with tab1:
    st.markdown("## Featured Projects")
    st.info("✅ Paste your existing Projects code here (same as before).")

with tab2:
    st.markdown("## Professional Experience")
    st.info("✅ Paste your existing Experience code here (same as before).")

with tab3:
    st.markdown("## Education & Skills")
    st.info("✅ Paste your existing Education/Skills code here (same as before).")

with tab4:
    st.markdown("## About Me")
    st.info("✅ Paste your existing About Me code here (same as before).")

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
    <div class="hero-glass" style="text-align: center;">
        <h2 style="margin-bottom: 1rem;">Let's Connect 🤝</h2>
        <p style="font-size: 1.1rem; margin-bottom: 2rem; opacity: 0.9;">
            I'm always open to discussing new opportunities, collaborations, or innovative projects
        </p>
        <div style="margin-bottom: 1.5rem; font-size: 2rem;">
            📧 📱 💼
        </div>
        <p style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem;">rajaroybca6@gmail.com</p>
        <p style="font-size: 1.1rem; font-weight: 600;">+39 388 381 8145</p>
        <p style="opacity: 0.7; font-size: 0.85rem; margin-top: 2rem; letter-spacing: 0.2em;">
            RAJA ROY — AI ENGINEER & DATA SCIENTIST — PORTFOLIO 2026
        </p>
    </div>
""", unsafe_allow_html=True)