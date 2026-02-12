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
        print(f"Error loading image: {e}")
        return None


# --- MODERN GLASSMORPHISM STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

    * { font-family: 'Poppins', sans-serif; }

    /* Main Background with Gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }

    /* IMPORTANT: Do NOT hide header (sidebar toggle lives there in many versions) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* header {visibility: hidden;}  <-- REMOVED */

    /* Ensure content doesn't overlap the top-left toggle */
    .block-container {
        padding-top: 2.5rem !important;
    }

    /* Sidebar toggle button (works across more versions) */
    [data-testid="collapsedControl"],
    [data-testid="stSidebarCollapsedControl"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        z-index: 9999 !important;
        border-radius: 999px !important;
        background: rgba(255,255,255,0.95) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 4px 0 24px rgba(0, 0, 0, 0.1);
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 2rem;
    }

    /* Glass Card Effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 2.5rem;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
        transition: all 0.3s ease;
    }

    .glass-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.2);
    }

    /* Hero Glass Card */
    .hero-glass {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 32px;
        padding: 4rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        margin-bottom: 3rem;
        color: white;
    }

    /* Profile Image */
    .profile-container {
        text-align: center;
        margin-bottom: 2rem;
    }

    .profile-img {
        border-radius: 50%;
        width: 200px;
        height: 200px;
        object-fit: cover;
        border: 5px solid white;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        margin: 0 auto;
        display: block;
        transition: all 0.3s ease;
    }

    .profile-img:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6);
    }

    /* Skill Badge */
    .skill-badge {
        display: inline-block;
        padding: 8px 16px;
        margin: 5px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
    }

    .skill-badge:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
    }

    /* Stat Box */
    .stat-box {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }

    .stat-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
    }

    .stat-number {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
        margin-bottom: 0.5rem;
    }

    .stat-label {
        font-size: 0.85rem;
        color: #6B7280;
        font-weight: 600;
        letter-spacing: 0.05em;
    }

    /* Experience Timeline */
    .timeline-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-left: 4px solid #667eea;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
    }

    .timeline-card:hover {
        transform: translateX(8px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
        border-left-color: #764ba2;
    }

    /* Gradient Text */
    .gradient-text {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
    }

    /* Button Styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.5);
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 12px;
        color: #6B7280;
        font-weight: 600;
        padding: 12px 24px;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }

    /* Contact Info Styling */
    .contact-item {
        padding: 0.75rem;
        margin: 0.5rem 0;
        background: rgba(102, 126, 234, 0.1);
        border-radius: 12px;
        border-left: 3px solid #667eea;
        transition: all 0.3s ease;
    }

    .contact-item:hover {
        background: rgba(102, 126, 234, 0.2);
        transform: translateX(5px);
    }

    /* Project Card */
    .project-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
        height: 100%;
        transition: all 0.3s ease;
    }

    .project-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.15);
    }

    /* Featured Project */
    .featured-project {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
    }

    .featured-project:hover {
        transform: scale(1.02);
    }

    /* Scrollbar */
    ::-webkit-scrollbar { width: 10px; height: 10px; }
    ::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.1); }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }

    @media (max-width: 768px) {
        .hero-glass { padding: 2rem !important; }
        .profile-img { width: 140px; height: 140px; }
    }
    </style>
""", unsafe_allow_html=True)


# --- SIDEBAR ---
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
    st.markdown("<p style='text-align: center; color: #6B7280; font-weight: 600; font-size: 0.9rem; letter-spacing: 0.1em;'>AI ENGINEER & DATA SCIENTIST</p>", unsafe_allow_html=True)
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
        <div style="padding: 0.5rem;">
            🇬🇧 <strong>English</strong> - Native<br>
            🇮🇹 <strong>Italian</strong> - B2<br>
            🇮🇳 <strong>Hindi</strong> - Native
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🎓 Current Study")
    st.markdown("""
        <div style="padding: 0.5rem; background: rgba(102, 126, 234, 0.1); border-radius: 12px; border-left: 3px solid #667eea;">
            <strong>AI Specialist Master's</strong><br>
            INFOR ELEA Academy<br>
            <small>Oct 2025 - Present</small>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    if st.button("📥 Download CV"):
        st.success("✅ CV download ready!")


# --- HERO SECTION ---
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


# --- STATS ---
st.markdown("## 📊 Professional Impact")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""<div class="stat-box"><div class="stat-number">8+</div><div class="stat-label">YEARS EXPERIENCE</div></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="stat-box"><div class="stat-number">5</div><div class="stat-label">COMPANIES</div></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="stat-box"><div class="stat-number">15+</div><div class="stat-label">TECH SKILLS</div></div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class="stat-box"><div class="stat-number">100%</div><div class="stat-label">DEDICATION</div></div>""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Projects", "💼 Experience", "🎓 Education & Skills", "👤 About Me"])

with tab1:
    st.markdown("## Featured Projects")
    colA, colB = st.columns([2, 1])

    with colA:
        st.markdown("""
            <div class="featured-project project-card">
                <p style="font-size: 0.75rem; font-weight: 700; letter-spacing: 0.2em; margin-bottom: 0.5rem; opacity: 0.9;">🏆 FEATURED ML PROJECT</p>
                <h3 style="margin-bottom: 1rem;">Fraud Detection & Supply Chain Analytics</h3>
                <p style="margin-bottom: 2rem; line-height: 1.7; opacity: 0.95;">
                    Designed and implemented machine learning models to detect fraudulent transactions and predict
                    on-time versus delayed shipments. Leveraged data preprocessing, feature engineering, and
                    classification techniques (Random Forest, Logistic Regression, XGBoost) to support operational
                    decision-making with 90%+ accuracy.
                </p>
                <div style="margin-bottom: 1.5rem;">
                    <a href="https://logisticmanagement.streamlit.app/" target="_blank" style="
                        display: inline-block;
                        background: white;
                        color: #667eea;
                        padding: 12px 24px;
                        border-radius: 12px;
                        text-decoration: none;
                        font-weight: 700;
                        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                    ">
                        🚀 View Live Demo →
                    </a>
                </div>
                <div>
                    <span style="background: rgba(255,255,255,0.25); padding: 6px 14px; margin: 4px; border-radius: 12px; display: inline-block; font-size: 0.85rem; font-weight: 600;">Python</span>
                    <span style="background: rgba(255,255,255,0.25); padding: 6px 14px; margin: 4px; border-radius: 12px; display: inline-block; font-size: 0.85rem; font-weight: 600;">Scikit-learn</span>
                    <span style="background: rgba(255,255,255,0.25); padding: 6px 14px; margin: 4px; border-radius: 12px; display: inline-block; font-size: 0.85rem; font-weight: 600;">Pandas</span>
                    <span style="background: rgba(255,255,255,0.25); padding: 6px 14px; margin: 4px; border-radius: 12px; display: inline-block; font-size: 0.85rem; font-weight: 600;">Feature Engineering</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with colB:
        st.markdown("""
            <div class="glass-card" style="background: rgba(102, 126, 234, 0.95); color: white; height: 100%;">
                <h4 style="margin-top: 0;">🎯 Key Achievements</h4>
                <p style="line-height: 1.8;">
                    ✓ Built classification models<br>
                    ✓ Data preprocessing & cleaning<br>
                    ✓ Feature engineering pipeline<br>
                    ✓ Model evaluation & tuning<br>
                    ✓ Business-ready insights
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## Web Development Projects")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="project-card">
                <h4 style="margin-bottom: 1rem;">🛒 Amazon Clone (E-Commerce)</h4>
                <p style="color: #6B7280; line-height: 1.7; margin-bottom: 1.5rem;">
                    Full-stack e-commerce platform with user authentication, shopping cart functionality,
                    and payment integration. Built with modern web technologies and responsive design.
                </p>
                <div>
                    <span class="skill-badge">HTML</span>
                    <span class="skill-badge">CSS</span>
                    <span class="skill-badge">JavaScript</span>
                    <span class="skill-badge">PHP</span>
                    <span class="skill-badge">SQL</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="project-card">
                <h4 style="margin-bottom: 1rem;">🏔️ West Bengal Tourism Portal</h4>
                <p style="color: #6B7280; line-height: 1.7; margin-bottom: 1.5rem;">
                    Informational tourism website featuring regional attractions, interactive maps,
                    and booking capabilities. Optimized for performance and SEO.
                </p>
                <div>
                    <span class="skill-badge">PHP</span>
                    <span class="skill-badge">Bootstrap</span>
                    <span class="skill-badge">MySQL</span>
                    <span class="skill-badge">JavaScript</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("## Professional Experience")
    experiences = [
        {
            "company": "Elwood",
            "location": "Torino, Italy",
            "role": "Web Developer",
            "period": "Jun 2025 - Oct 2025",
            "description": "Developed and maintained full-stack web applications, customized WordPress themes and plugins, built responsive websites using PHP, HTML, CSS, Bootstrap, and JavaScript. Collaborated with designers and clients to deliver high-quality digital solutions.",
            "skills": ["PHP", "WordPress", "JavaScript", "HTML/CSS", "Bootstrap"]
        },
        {
            "company": "NETWAY INDIA PVT. LTD",
            "location": "New Delhi, India",
            "role": "Data Analytics & Business Intelligence",
            "period": "May 2019 - May 2023",
            "description": "Conducted data cleaning, mining, and analysis. Developed interactive dashboards and automated reports using Power BI, Python, SQL, and Excel to enable data-driven business decisions. Led end-to-end analytics projects from requirements gathering to deployment.",
            "skills": ["Python", "SQL", "Power BI", "Excel", "Data Analysis"]
        },
        {
            "company": "Global Digital Baba",
            "location": "Torino, Italy",
            "role": "Customer Support & Store Operations",
            "period": "Apr 2024 - Jan 2025",
            "description": "Assisted customers with product selection, troubleshooting, and after-sales support while managing billing, merchandising, and stock control.",
            "skills": ["Customer Service", "Operations", "Inventory Management"]
        },
        {
            "company": "AUTHENZA MEDIA INFOTECH PVT. LTD",
            "location": "Kolkata, India",
            "role": "Data Analyst",
            "period": "Sep 2016 - Feb 2019",
            "description": "Performed data analysis, visualization, and reporting for business operations while ensuring data integrity and developing dashboards to support management insights.",
            "skills": ["Data Analysis", "SQL", "Excel", "Reporting"]
        }
    ]

    for exp in experiences:
        st.markdown(f"""
            <div class="timeline-card">
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
                    <div>
                        <h4 style="margin: 0;" class="gradient-text">{exp['role']}</h4>
                        <p style="margin: 0.5rem 0; font-weight: 600; font-size: 1rem; color: #667eea;">{exp['company']}</p>
                    </div>
                    <div style="text-align: right;">
                        <p style="margin: 0; font-weight: 600; font-size: 0.9rem; color: #6B7280;">{exp['period']}</p>
                        <p style="margin: 0.25rem 0; font-size: 0.85rem; color: #9CA3AF;">📍 {exp['location']}</p>
                    </div>
                </div>
                <p style="color: #4B5563; line-height: 1.7; margin: 1rem 0;">
                    {exp['description']}
                </p>
                <div>
                    {''.join([f'<span class="skill-badge">{skill}</span>' for skill in exp['skills']])}
                </div>
            </div>
        """, unsafe_allow_html=True)

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("## 🎓 Education")
        st.markdown("""
            <div class="timeline-card">
                <h4 style="margin: 0;" class="gradient-text">Professional Master's in AI (AI Specialist)</h4>
                <p style="margin: 0.75rem 0; font-weight: 600; color: #667eea;">INFOR ELEA Smart Business Academy</p>
                <p style="color: #6B7280; font-size: 0.9rem;">📍 Torino, Italy | 🗓️ Oct 2025 - Present</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="timeline-card">
                <h4 style="margin: 0;" class="gradient-text">Web Development Specialization</h4>
                <p style="margin: 0.75rem 0; font-weight: 600; color: #667eea;">Forte Chance ETS</p>
                <p style="color: #6B7280; font-size: 0.9rem;">📍 Torino, Italy | 🗓️ Feb 2025 - Aug 2025 | Grade: A</p>
                <p style="color: #4B5563; font-size: 0.9rem; margin-top: 1rem; line-height: 1.6;">
                    PHP, HTML, CSS, Bootstrap, JavaScript, WordPress, SQL, Apache, Cyber Security, Prompt Engineering
                </p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="timeline-card">
                <h4 style="margin: 0;" class="gradient-text">Bachelor of Computer Application</h4>
                <p style="margin: 0.75rem 0; font-weight: 600; color: #667eea;">IGNOU (Indira Gandhi National Open University)</p>
                <p style="color: #6B7280; font-size: 0.9rem;">📍 New Delhi, India | 🗓️ 2012 - 2015 | Grade: B</p>
                <p style="color: #4B5563; font-size: 0.9rem; margin-top: 1rem; line-height: 1.6;">
                    Information Technology, Data Structures, DBMS, System Analysis, Computer Networks, Programming
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("## 💻 Technical Skills")
        skills_data = {
            "Data Science & AI": ["Python", "Machine Learning", "Pandas", "NumPy", "Scikit-learn", "Feature Engineering"],
            "Data Analytics": ["SQL", "Power BI", "Excel (Advanced)", "Data Visualization", "Statistical Analysis"],
            "Web Development": ["PHP", "JavaScript", "HTML/CSS", "Bootstrap", "WordPress", "Django"],
            "Databases": ["MySQL", "SQL Server", "Database Design"],
            "Tools & DevOps": ["Git", "Apache", "Streamlit", "VS Code", "Linux"],
            "Soft Skills": ["Problem Solving", "Team Collaboration", "Project Management", "Analytical Thinking"]
        }

        for category, skills in skills_data.items():
            st.markdown(f"""
                <div class="glass-card" style="margin-bottom: 1.5rem;">
                    <h5 class="gradient-text" style="margin-bottom: 1rem;">{category}</h5>
                    <div>
                        {''.join([f'<span class="skill-badge">{skill}</span>' for skill in skills])}
                    </div>
                </div>
            """, unsafe_allow_html=True)

with tab4:
    st.markdown("## 👋 About Me")
    st.markdown("""
        <div class="glass-card">
            <p style="color: #4B5563; font-size: 1.05rem; line-height: 1.8;">
                I am a <strong class="gradient-text">Senior Data Analyst and Full-Stack Web Developer</strong> with over 8+ years of hands-on experience
                delivering production-grade analytics platforms and ML/AI-enabled solutions. I have deep expertise in
                <strong>Python, SQL, PHP, Power BI, Excel, and JavaScript</strong>, with a strong background in data modeling,
                feature engineering, dashboarding, and automation.
            </p>
            <p style="color: #4B5563; font-size: 1.05rem; line-height: 1.8; margin-top: 1.5rem;">
                Throughout my career, I have proven my ability to translate business requirements into scalable data products
                and intelligent web applications, leading projects end-to-end from architecture to deployment.
            </p>
            <p style="color: #4B5563; font-size: 1.05rem; line-height: 1.8; margin-top: 1.5rem;">
                Currently pursuing a <strong class="gradient-text">Professional Master's Program in Artificial Intelligence</strong>,
                strengthening my expertise in machine learning, feature engineering, and applied AI systems.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🎯 Career Goals & Interests")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="featured-project project-card">
                <h4 style="margin-bottom: 1.5rem;">Current Focus</h4>
                <p style="line-height: 1.8; opacity: 0.95;">
                    Actively pursuing roles in <strong>AI Engineering, Data Science,</strong> and
                    <strong>Machine Learning Engineering</strong> where I can leverage my unique combination of
                    analytics expertise and full-stack development skills to build intelligent,
                    production-ready solutions.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="glass-card">
                <h4 style="margin-bottom: 1.5rem;">Interests & Hobbies</h4>
                <p style="color: #4B5563; line-height: 1.8;">
                    📚 <strong>Reading & Self-Learning</strong><br>
                    Technology, Business, Personal Development<br><br>
                    🤖 <strong>AI & ML Research</strong><br>
                    Staying updated with latest trends<br><br>
                    💻 <strong>Coding Projects</strong><br>
                    Building practical solutions<br><br>
                    🌍 <strong>Languages</strong><br>
                    Learning Italian (currently B2 level)
                </p>
            </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
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