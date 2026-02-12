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
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, image_filename)

        # Try the script directory first
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()

        # Try current working directory
        if os.path.exists(image_filename):
            with open(image_filename, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()

        print(f"Image not found at: {image_path}")
        print(f"Script directory: {script_dir}")
        print(f"Files in directory: {os.listdir(script_dir)}")
        return None

    except Exception as e:
        print(f"Error loading image: {e}")
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

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

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
    # Load Raja's professional profile photo
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
    st.caption("**English** - Fluent")
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
            <span style="background: rgba(59, 130, 246, 0.2); padding: 8px 16px; border-radius: 8px; font-size: 0.85rem;">Python</span>
            <span style="background: rgba(59, 130, 246, 0.2); padding: 8px 16px; border-radius: 8px; font-size: 0.85rem;">SQL</span>
            <span style="background: rgba(59, 130, 246, 0.2); padding: 8px 16px; border-radius: 8px; font-size: 0.85rem;">Machine Learning</span>
            <span style="background: rgba(59, 130, 246, 0.2); padding: 8px 16px; border-radius: 8px; font-size: 0.85rem;">Power BI</span>
            <span style="background: rgba(59, 130, 246, 0.2); padding: 8px 16px; border-radius: 8px; font-size: 0.85rem;">PHP</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- STATS SECTION ---
st.markdown("### 📊 Professional Impact")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">8+</div>
            <div class="stat-label">YEARS EXPERIENCE</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">5</div>
            <div class="stat-label">COMPANIES</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">15+</div>
            <div class="stat-label">TECH SKILLS</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">100%</div>
            <div class="stat-label">DEDICATION</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- NAVIGATION TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Projects", "💼 Experience", "🎓 Education & Skills", "👤 About Me"])

# --- TAB 1: PROJECTS ---
with tab1:
    st.markdown("### Featured Projects")

    # Featured Project
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
            <div class="project-card" style="background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); color: white; border: none;">
                <p style="color: #3B82F6; font-size: 0.65rem; font-weight: 900; letter-spacing: 0.2em; margin-bottom: 0.5rem;">🏆 FEATURED ML PROJECT</p>
                <h3 style="color: white; margin-bottom: 1rem;">Fraud Detection & Supply Chain Analytics</h3>
                <p style="color: #CBD5E1; margin-bottom: 1.5rem; line-height: 1.6;">
                    Designed and implemented machine learning models to detect fraudulent transactions and predict on-time versus delayed shipments. 
                    Leveraged data preprocessing, feature engineering, and classification techniques (Random Forest, Logistic Regression, XGBoost) 
                    to support operational decision-making with 90%+ accuracy.
                </p>
                <div style="margin-bottom: 1rem;">
                    <a href="https://logisticmanagement.streamlit.app/" target="_blank" style="
                        display: inline-block;
                        background: #3B82F6;
                        color: white;
                        padding: 10px 20px;
                        border-radius: 8px;
                        text-decoration: none;
                        font-weight: 600;
                        font-size: 0.85rem;
                        transition: all 0.3s ease;
                    ">
                        🚀 View Live Demo
                    </a>
                </div>
                <div>
                    <span class="skill-tag" style="background: rgba(59, 130, 246, 0.3); color: white; border-color: rgba(59, 130, 246, 0.5);">Python</span>
                    <span class="skill-tag" style="background: rgba(59, 130, 246, 0.3); color: white; border-color: rgba(59, 130, 246, 0.5);">Scikit-learn</span>
                    <span class="skill-tag" style="background: rgba(59, 130, 246, 0.3); color: white; border-color: rgba(59, 130, 246, 0.5);">Pandas</span>
                    <span class="skill-tag" style="background: rgba(59, 130, 246, 0.3); color: white; border-color: rgba(59, 130, 246, 0.5);">Feature Engineering</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="background: #3B82F6; padding: 2rem; border-radius: 2rem; color: white; height: 100%;">
                <h4 style="margin-top:0;">🎯 Key Achievements</h4>
                <p style="font-size: 0.85rem; line-height: 1.6; margin-bottom: 1rem;">
                    ✓ Built classification models<br>
                    ✓ Data preprocessing & cleaning<br>
                    ✓ Feature engineering pipeline<br>
                    ✓ Model evaluation & tuning<br>
                    ✓ Business-ready insights
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Other Projects Grid
    st.markdown("### Web Development Projects")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="project-card">
                <h4 style="margin-bottom: 0.5rem;">🛒 Amazon Clone (E-Commerce)</h4>
                <p style="font-size: 0.85rem; color: #64748B; margin-bottom: 1rem;">
                    Full-stack e-commerce platform with user authentication, shopping cart functionality, and payment integration. 
                    Built with modern web technologies and responsive design.
                </p>
                <div style="margin-bottom: 1rem;">
                    <a href="#" target="_blank" style="
                        display: inline-block;
                        background: #E2E8F0;
                        color: #475569;
                        padding: 8px 16px;
                        border-radius: 6px;
                        text-decoration: none;
                        font-weight: 600;
                        font-size: 0.8rem;
                    ">
                        🔗 Add Project Link
                    </a>
                </div>
                <div style="margin-top: 1rem;">
                    <span class="skill-tag">HTML</span>
                    <span class="skill-tag">CSS</span>
                    <span class="skill-tag">JavaScript</span>
                    <span class="skill-tag">PHP</span>
                    <span class="skill-tag">SQL</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="project-card">
                <h4 style="margin-bottom: 0.5rem;">🏔️ West Bengal Tourism Portal</h4>
                <p style="font-size: 0.85rem; color: #64748B; margin-bottom: 1rem;">
                    Informational tourism website featuring regional attractions, interactive maps, and booking capabilities. 
                    Optimized for performance and SEO.
                </p>
                <div style="margin-bottom: 1rem;">
                    <a href="#" target="_blank" style="
                        display: inline-block;
                        background: #E2E8F0;
                        color: #475569;
                        padding: 8px 16px;
                        border-radius: 6px;
                        text-decoration: none;
                        font-weight: 600;
                        font-size: 0.8rem;
                    ">
                        🔗 Add Project Link
                    </a>
                </div>
                <div style="margin-top: 1rem;">
                    <span class="skill-tag">PHP</span>
                    <span class="skill-tag">Bootstrap</span>
                    <span class="skill-tag">MySQL</span>
                    <span class="skill-tag">JavaScript</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- TAB 2: EXPERIENCE ---
with tab2:
    st.markdown("### Professional Experience")

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
            <div class="experience-card">
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
                    <div>
                        <h4 style="margin: 0; color: #1E293B;">{exp['role']}</h4>
                        <p style="margin: 0.25rem 0; color: #3B82F6; font-weight: 600; font-size: 0.9rem;">{exp['company']}</p>
                    </div>
                    <div style="text-align: right;">
                        <p style="margin: 0; color: #64748B; font-size: 0.85rem; font-weight: 600;">{exp['period']}</p>
                        <p style="margin: 0.25rem 0; color: #94A3B8; font-size: 0.8rem;">📍 {exp['location']}</p>
                    </div>
                </div>
                <p style="color: #475569; font-size: 0.9rem; line-height: 1.6; margin: 1rem 0;">
                    {exp['description']}
                </p>
                <div>
                    {''.join([f'<span class="skill-tag">{skill}</span>' for skill in exp['skills']])}
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- TAB 3: EDUCATION & SKILLS ---
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎓 Education")

        st.markdown("""
            <div class="experience-card">
                <h4 style="margin: 0; color: #1E293B;">Professional Master's in AI (AI Specialist)</h4>
                <p style="margin: 0.5rem 0; color: #3B82F6; font-weight: 600;">INFOR ELEA Smart Business Academy</p>
                <p style="color: #64748B; font-size: 0.85rem;">📍 Torino, Italy | 🗓️ Oct 2025 - Present</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="experience-card">
                <h4 style="margin: 0; color: #1E293B;">Web Development Specialization</h4>
                <p style="margin: 0.5rem 0; color: #3B82F6; font-weight: 600;">Forte Chance ETS</p>
                <p style="color: #64748B; font-size: 0.85rem;">📍 Torino, Italy | 🗓️ Feb 2025 - Aug 2025 | Grade: A</p>
                <p style="color: #475569; font-size: 0.85rem; margin-top: 0.5rem;">
                    PHP, HTML, CSS, Bootstrap, JavaScript, WordPress, SQL, Apache, Cyber Security, Prompt Engineering
                </p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="experience-card">
                <h4 style="margin: 0; color: #1E293B;">Bachelor of Computer Application</h4>
                <p style="margin: 0.5rem 0; color: #3B82F6; font-weight: 600;">IGNOU (Indira Gandhi National Open University)</p>
                <p style="color: #64748B; font-size: 0.85rem;">📍 New Delhi, India | 🗓️ 2012 - 2015 | Grade: B</p>
                <p style="color: #475569; font-size: 0.85rem; margin-top: 0.5rem;">
                    Information Technology, Data Structures, DBMS, System Analysis, Computer Networks, Programming
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### 💻 Technical Skills")

        skills_data = {
            "Data Science & AI": ["Python", "Machine Learning", "Pandas", "NumPy", "Scikit-learn",
                                  "Feature Engineering"],
            "Data Analytics": ["SQL", "Power BI", "Excel (Advanced)", "Data Visualization", "Statistical Analysis"],
            "Web Development": ["PHP", "JavaScript", "HTML/CSS", "Bootstrap", "WordPress", "Django"],
            "Databases": ["MySQL", "SQL Server", "Database Design"],
            "Tools & DevOps": ["Git", "Apache", "Streamlit", "VS Code", "Linux"],
            "Soft Skills": ["Problem Solving", "Team Collaboration", "Project Management", "Analytical Thinking"]
        }

        for category, skills in skills_data.items():
            st.markdown(f"""
                <div class="project-card" style="margin-bottom: 1rem;">
                    <h5 style="color: #1E293B; margin-bottom: 0.75rem;">{category}</h5>
                    <div>
                        {''.join([f'<span class="skill-tag">{skill}</span>' for skill in skills])}
                    </div>
                </div>
            """, unsafe_allow_html=True)

# --- TAB 4: ABOUT ME ---
with tab4:
    st.markdown("### 👋 About Me")

    st.markdown("""
        <div class="project-card">
            <p style="color: #475569; font-size: 1rem; line-height: 1.8;">
                I am a <strong>Senior Data Analyst and Full-Stack Web Developer</strong> with over 8+ years of hands-on experience 
                delivering production-grade analytics platforms and ML/AI-enabled solutions. I have deep expertise in 
                <strong>Python, SQL, PHP, Power BI, Excel, and JavaScript</strong>, with a strong background in data modeling, 
                feature engineering, dashboarding, and automation.
            </p>
            <p style="color: #475569; font-size: 1rem; line-height: 1.8; margin-top: 1rem;">
                Throughout my career, I have proven my ability to translate business requirements into scalable data products 
                and intelligent web applications, leading projects end-to-end from architecture to deployment. I have worked 
                across various industries and roles, including <strong>Data Analytics & Business Intelligence, Web Development, 
                and Operations</strong>.
            </p>
            <p style="color: #475569; font-size: 1rem; line-height: 1.8; margin-top: 1rem;">
                Currently, I am pursuing a <strong>Professional Master's Program in Artificial Intelligence</strong>, where I am 
                strengthening my expertise in machine learning, feature engineering, and applied AI systems. My recent projects 
                include fraud detection and supply chain performance prediction, where I applied classification models and 
                evaluation techniques to solve real-world business problems.
            </p>
            <p style="color: #475569; font-size: 1rem; line-height: 1.8; margin-top: 1rem;">
                What sets me apart is my ability to take ownership of projects end-to-end — from understanding business 
                requirements and designing data architectures, to implementing analytical models and deploying usable solutions. 
                I am highly analytical, detail-oriented, and driven by continuous learning, with a strong interest in building 
                intelligent systems that create tangible value.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Career Goals")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="project-card" style="background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%); color: white; border: none;">
                <h4 style="color: white; margin-bottom: 1rem;">Current Focus</h4>
                <p style="color: #E0E7FF; line-height: 1.6;">
                    Actively pursuing roles in <strong>AI Engineering, Data Science,</strong> and 
                    <strong>Machine Learning Engineering</strong> where I can leverage my unique combination of 
                    analytics expertise and full-stack development skills to build intelligent, 
                    production-ready solutions.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="project-card">
                <h4 style="margin-bottom: 1rem;">Interests & Hobbies</h4>
                <p style="color: #475569; line-height: 1.6;">
                    📚 <strong>Reading & Self-Learning:</strong> Technology, Business, Personal Development<br><br>
                    🤖 <strong>AI & ML Research:</strong> Staying updated with latest trends<br><br>
                    💻 <strong>Coding Projects:</strong> Building practical solutions<br><br>
                    🌍 <strong>Languages:</strong> Learning Italian (currently B2 level)
                </p>
            </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("""
    <div style="text-align: center; margin-top: 3rem; padding: 2rem; background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); border-radius: 2rem;">
        <h3 style="color: white; margin-bottom: 1rem;">Let's Connect</h3>
        <p style="color: #94A3B8; font-size: 0.95rem; margin-bottom: 1.5rem;">
            I'm always open to discussing new opportunities, collaborations, or innovative projects
        </p>
        <div style="margin-bottom: 1rem;">
            <span style="color: #3B82F6; font-size: 1.5rem; margin: 0 1rem;">📧</span>
            <span style="color: #3B82F6; font-size: 1.5rem; margin: 0 1rem;">📱</span>
            <span style="color: #3B82F6; font-size: 1.5rem; margin: 0 1rem;">💼</span>
        </div>
        <p style="color: white; font-size: 0.9rem;">rajaroybca6@gmail.com | +39 388 381 8145</p>
        <p style="color: #64748B; font-size: 0.75rem; margin-top: 1.5rem; letter-spacing: 0.3em;">
            RAJA ROY — AI ENGINEER & DATA SCIENTIST — PORTFOLIO 2026
        </p>
    </div>
""", unsafe_allow_html=True)
#cd D:\Github_code_back\My_Cv
#streamlit run My_Cv.py