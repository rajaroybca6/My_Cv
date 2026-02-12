import streamlit as st
import base64
import os

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Raja Roy | AI & Data Science Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LOAD PROFILE IMAGE ---
def get_image_base64(image_filename):
    """Convert image to base64 for embedding"""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, image_filename)

        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()

        if os.path.exists(image_filename):
            with open(image_filename, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
        return None
    except Exception as e:
        return None

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #F8FAFC;
    }

    /* Custom Card Styling */
    .project-card {
        background-color: white;
        border-radius: 2rem;
        padding: 2rem;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        margin-bottom: 20px;
        height: 100%;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        border-color: #3B82F6;
    }

    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        border-radius: 3rem;
        padding: 3rem;
        color: white;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
    }

    /* Skill Tags */
    .skill-tag {
        display: inline-block;
        padding: 6px 14px;
        margin: 4px;
        background-color: #F1F5F9;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        color: #64748B;
    }

    /* Experience Card */
    .experience-card {
        background-color: white;
        border-left: 4px solid #3B82F6;
        border-radius: 1rem;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    /* Custom Sidebar */
    [data-testid="stSidebar"] {
        background-color: white;
        border-right: 1px solid #E2E8F0;
    }

    .profile-img {
        border-radius: 2rem;
        width: 180px;
        height: 180px;
        object-fit: cover;
        margin: 0 auto 1.5rem auto;
        display: block;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        border: 4px solid #3B82F6;
    }

    /* --- SIDEBAR TOGGLE FIX --- */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Show header only when sidebar is hidden to allow opening it again */
    header {
        visibility: hidden;
    }
    [data-collapsed="true"] header {
        visibility: visible;
    }

    /* Style the sidebar open button (the > arrow) */
    .st-emotion-cache-hp888a, button[kind="header"] {
        visibility: visible !important;
        color: #3B82F6 !important;
    }

    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        font-weight: 900 !important;
        letter-spacing: -0.05em !important;
    }

    .contact-icon {
        color: #3B82F6;
        margin-right: 8px;
    }

    .stat-box {
        background: white;
        border-radius: 1rem;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    .stat-number {
        font-size: 2.5rem;
        font-weight: 900;
        color: #3B82F6;
        line-height: 1;
    }

    .stat-label {
        font-size: 0.8rem;
        color: #64748B;
        margin-top: 0.5rem;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    img_base64 = get_image_base64("profile_photo.png")

    if img_base64:
        st.markdown(
            f'<img src="data:image/png;base64,{img_base64}" class="profile-img">',
            unsafe_allow_html=True
        )
    else:
        st.warning("⚠️ Place 'profile_photo.png' in the same folder as this Python file")

    st.markdown("<h2 style='text-align: center; margin-bottom: 0;'>RAJA ROY</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; color: #3B82F6; font-weight: bold; font-size: 0.85rem; letter-spacing: 0.2em;'>AI ENGINEER & DATA SCIENTIST</p>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### 📧 Contact")
    st.write("**Email:** rajaroybca6@gmail.com")
    st.write("**Phone:** +39 388 381 8145")
    st.write("**Location:** Torino, Italy")

    st.markdown("---")
    st.markdown("### 🌍 Languages")
    st.caption("**English** - Native")
    st.caption("**Italian** - B2")
    st.caption("**Hindi** - Native")

    st.markdown("---")
    st.markdown("### 🎓 Current Education")
    st.caption("**AI Specialist Master's**")
    st.caption("INFOR ELEA Academy")
    st.caption("Oct 2025 - Present")

    st.markdown("---")
    if st.button("📄 Download CV", use_container_width=True):
        st.success("CV download initiated!")

# --- HERO SECTION ---
st.markdown("""
    <div class="hero-section">
        <p style="color: #3B82F6; font-weight: 900; font-size: 0.75rem; letter-spacing: 0.3em; margin-bottom: 1rem;">SENIOR DATA ANALYST • FULL-STACK DEVELOPER</p>
        <h1 style="font-size: 3.5rem; line-height: 1.1; margin-bottom: 1.5rem;">Building Intelligent<br><span style="color: #3B82F6;">Data Solutions.</span></h1>
        <p style="color: #94A3B8; font-size: 1.15rem; max-width: 700px; margin-bottom: 2rem; line-height: 1.6;">
            Transforming complex data into actionable insights with 8+ years of expertise in analytics, machine learning, and full-stack development. 
            Specialized in creating production-grade AI-enabled solutions that drive measurable business value.
        </p>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
            <span class="skill-tag" style="background: rgba(59, 130, 246, 0.2); color: white;">Python</span>
            <span class="skill-tag" style="background: rgba(59, 130, 246, 0.2); color: white;">SQL</span>
            <span class="skill-tag" style="background: rgba(59, 130, 246, 0.2); color: white;">Machine Learning</span>
            <span class="skill-tag" style="background: rgba(59, 130, 246, 0.2); color: white;">Power BI</span>
            <span class="skill-tag" style="background: rgba(59, 130, 246, 0.2); color: white;">PHP</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- STATS SECTION ---
st.markdown("### 📊 Professional Impact")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="stat-box"><div class="stat-number">8+</div><div class="stat-label">YEARS EXPERIENCE</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-box"><div class="stat-number">5</div><div class="stat-label">COMPANIES</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-box"><div class="stat-number">15+</div><div class="stat-label">TECH SKILLS</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="stat-box"><div class="stat-number">100%</div><div class="stat-label">DEDICATION</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- NAVIGATION TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Projects", "💼 Experience", "🎓 Education & Skills", "👤 About Me"])

# --- TAB 1: PROJECTS ---
with tab1:
    st.markdown("### Featured Projects")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
            <div class="project-card" style="background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); color: white; border: none;">
                <p style="color: #3B82F6; font-size: 0.65rem; font-weight: 900; letter-spacing: 0.2em; margin-bottom: 0.5rem;">🏆 FEATURED ML PROJECT</p>
                <h3 style="color: white; margin-bottom: 1rem;">Fraud Detection & Supply Chain Analytics</h3>
                <p style="color: #CBD5E1; margin-bottom: 1.5rem; line-height: 1.6;">
                    Designed and implemented machine learning models to detect fraudulent transactions and predict on-time versus delayed shipments with 90%+ accuracy.
                </p>
                <div style="margin-bottom: 1rem;">
                    <a href="https://logisticmanagement.streamlit.app/" target="_blank" style="display: inline-block; background: #3B82F6; color: white; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 0.85rem;">🚀 View Live Demo</a>
                </div>
                <div>
                    <span class="skill-tag" style="background: rgba(59, 130, 246, 0.3); color: white;">Python</span>
                    <span class="skill-tag" style="background: rgba(59, 130, 246, 0.3); color: white;">Scikit-learn</span>
                    <span class="skill-tag" style="background: rgba(59, 130, 246, 0.3); color: white;">Pandas</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown('<div style="background: #3B82F6; padding: 2rem; border-radius: 2rem; color: white; height: 100%;"><h4>🎯 Key Achievements</h4><p>✓ ML Models<br>✓ Data Cleaning<br>✓ Business Insights</p></div>', unsafe_allow_html=True)

# --- TAB 2: EXPERIENCE ---
with tab2:
    st.markdown("### Professional Experience")
    experiences = [
        {"role": "Web Developer", "company": "Elwood", "period": "Jun 2025 - Oct 2025", "desc": "Developed full-stack web apps and WordPress themes."},
        {"role": "Data Analytics", "company": "NETWAY INDIA", "period": "2019 - 2023", "desc": "Automated reporting and built Power BI dashboards."},
        {"role": "Data Analyst", "company": "AUTHENZA MEDIA", "period": "2016 - 2019", "desc": "Visualization and reporting for business operations."}
    ]
    for exp in experiences:
        st.markdown(f'<div class="experience-card"><h4>{exp["role"]}</h4><p style="color: #3B82F6;">{exp["company"]} | {exp["period"]}</p><p>{exp["desc"]}</p></div>', unsafe_allow_html=True)

# --- TAB 3: EDUCATION & SKILLS ---
with tab3:
    col_ed, col_sk = st.columns(2)
    with col_ed:
        st.markdown("### 🎓 Education")
        st.markdown('<div class="experience-card"><h4>AI Specialist Master\'s</h4><p>INFOR ELEA Academy | 2025-Present</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="experience-card"><h4>Bachelor of Computer Application</h4><p>IGNOU | 2012-2015</p></div>', unsafe_allow_html=True)
    with col_sk:
        st.markdown("### 💻 Technical Skills")
        st.markdown('<div class="project-card">Python, SQL, Machine Learning, Power BI, PHP, JavaScript, Streamlit, Linux</div>', unsafe_allow_html=True)

# --- TAB 4: ABOUT ME ---
with tab4:
    st.markdown("### 👋 About Me")
    st.markdown('<div class="project-card">Senior Data Analyst & Full-Stack Developer with 8+ years experience building intelligent data products.</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("""
    <div style="text-align: center; margin-top: 3rem; padding: 2rem; background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); border-radius: 2rem;">
        <h3 style="color: white;">Let's Connect</h3>
        <p style="color: white;">rajaroybca6@gmail.com | +39 388 381 8145</p>
    </div>
""", unsafe_allow_html=True)