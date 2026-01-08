import streamlit as st

# Page Config
st.set_page_config(page_title="Himanshu Dutta | Profilo", layout="wide")

# Custom CSS for animations and interactivity
st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }

    @keyframes slideIn {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    .animated-header {
        animation: fadeIn 1s ease-out;
    }

    .hover-lift {
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .hover-lift:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(76, 175, 80, 0.3);
    }

    .skill-badge {
        display: inline-block;
        padding: 8px 16px;
        margin: 5px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px;
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .skill-badge:hover {
        transform: scale(1.1) rotate(2deg);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }

    .project-card {
        background: linear-gradient(135deg, #667eea22 0%, #764ba222 100%);
        border-left: 4px solid #4CAF50;
        padding: 20px;
        margin: 10px 0;
        border-radius: 10px;
        transition: all 0.3s ease;
    }

    .project-card:hover {
        background: linear-gradient(135deg, #667eea44 0%, #764ba244 100%);
        transform: translateX(10px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }

    .floating {
        animation: pulse 2s ease-in-out infinite;
    }

    .section-title {
        position: relative;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    .section-title::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #4CAF50, #667eea);
        transition: width 0.3s ease;
    }

    .section-title:hover::after {
        width: 120px;
    }

    .interactive-stat {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .interactive-stat:hover {
        transform: scale(1.05) rotate(-2deg);
        box-shadow: 0 10px 30px rgba(245, 87, 108, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="margin: 40px 0; text-align: center;" class="animated-header">
        <h1 style="color: #4CAF50; margin-bottom: 0.2em;" class="floating">HIMANSHU DUTTA</h1>
        <h3 style="margin-top: 0; color: #333;">
            AI Engineer (NLP + GenAI) &nbsp; | &nbsp; Business Strategy-Oriented &nbsp; | &nbsp; IBM Data Science Certified
        </h3>
        <p style="font-size: 18px; margin: 0.5em 0;">
            📞 <a href="tel:+918409120774" style="color: #4CAF50; text-decoration: none;">+91 84091 20774</a> &nbsp; | &nbsp;
            📧 <a href="mailto:dutthimsun@gmail.com" style="color: #4CAF50; text-decoration: none;">dutthimsun@gmail.com</a> &nbsp; | &nbsp;
            <a href="https://www.linkedin.com/in/himanshu-dutta06" target="_blank" style="color: #4CAF50; text-decoration: none;">🔗 LinkedIn</a>
        </p>
        <p style="font-size: 24px; font-weight: bold; text-align: center; margin-bottom: 0; color: #444;" class="floating">ॐ</p>
        <p style="font-size: 16px; font-style: italic; color: #666; text-align: center; margin-top: 0.2em;">
            कृष्णाय वासुदेवाय हरये परमात्मने ।<br>
            प्रणतः क्लेशनाशाय गोविन्दाय नमो नमः ॥
        </p>
    </div>
""", unsafe_allow_html=True)

# Resume Download with hover effect
with open("assets/Himanshu_Dutta_Resume.pdf", "rb") as f:
    resume_data = f.read()

st.download_button(
    label="📄 Download Resume (PDF)",
    data=resume_data,
    file_name="Himanshu_Dutta_Resume.pdf",
    mime="application/pdf"
)

# Sidebar Navigation with emojis
st.sidebar.title("📄 Navigation")
section = st.sidebar.radio("Go to", ["🏠 Summary", "🎓 Education", "🧠 Skills", "💼 Professional Experience",
                                     "🚀 Projects", "📜 Certifications & Workshops", "🏅 Achievements",
                                     "🎯 Interests", "🌄 Life Beyond Work"])

# Sections
import base64


def get_base64_image_from_path(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


if section == "🏠 Summary":
    img_path = "assets/himanshu.jpg"
    bg_img = get_base64_image_from_path(img_path)

    st.markdown(f"""
        <style>
            .summary-section {{
                position: relative;
                background-image: url("data:image/png;base64,{bg_img}");
                background-size: cover;
                background-position: center;
                padding: 64px 24px;
                border-radius: 50px;
                color: white;
                margin: 0 auto 100px auto;
                max-width: 900px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.4);
                filter: brightness(0.75);
                backdrop-filter: blur(5px);
                transition: all 0.3s ease;
            }}

            .summary-section:hover {{
                transform: scale(1.02);
                box-shadow: 0 15px 40px rgba(76, 175, 80, 0.3);
            }}

            .summary-overlay {{
                position: relative;
                background-color: rgba(0, 0, 0, 0.65);
                padding: 30px;
                border-radius: 16px;
                font-size: 18px;
                line-height: 1.6;
                z-index: 1;
            }}

            .summary-overlay ul {{
                padding-left: 24px;
            }}

            .summary-overlay li {{
                margin: 10px 0;
                transition: all 0.3s ease;
            }}

            .summary-overlay li:hover {{
                transform: translateX(10px);
                color: #4CAF50;
            }}

            .summary-section::before {{
                content: "";
                position: absolute;
                top: 0; left: 0; right: 0; bottom: 0;
                border-radius: 50px;
                backdrop-filter: blur(2.5px);
                z-index: 0;
            }}
        </style>

        <div class="summary-section">
            <div class="summary-overlay">
                <h2>🔍 Profile Summary</h2>
                <p>
                    A multidisciplinary engineer blending <strong>AI</strong>, <strong>Electronics</strong>, and <strong>Systems Thinking</strong> to build meaningful, inclusive, and real-time digital solutions.
                </p>
                <ul>
                    <li><strong>Experienced in full-stack AI development</strong>: NLP pipelines, document-based QA systems, sentiment analysis, and multimodal interfaces.</li>
                    <li><strong>Rooted in Electronics & Communication</strong>: Skilled in transformer models, RAG architectures, and production-grade Streamlit dashboards.</li>
                    <li><strong>Driven by systems thinking & digital accessibility</strong>: Passionate about AI's impact on behavior, decisions, and product ecosystems.</li>
                    <li><strong>Focused and self-directed</strong>: Committed to building ethical, user-centric, and culturally aware AI systems with real-world relevance.</li>
                    <li><strong>Anchored in reflection and discipline</strong>: Dedicated to crafting inclusive, purpose-driven technology for an evolving digital world.</li>
                </ul>
                <p>
                    From multilingual document bots to bias-aware news assistants — I build with empathy, clarity, and an unwavering sense of purpose.
                </p>
                <p style="margin-top: 24px; font-style: italic;">
                    The background reflects my roots — grounded, empathetic, and always curious.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif section == "🎓 Education":
    st.markdown("<h2 class='section-title'>🎓 Education</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='interactive-stat'><h3>2023-2027</h3><p>B.Tech Journey</p></div>",
                    unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='interactive-stat'><h3>IIIT Kottayam</h3><p>Premier Institute</p></div>",
                    unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='interactive-stat'><h3>ECE</h3><p>Electronics & Comm</p></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="hover-lift" style="background: linear-gradient(135deg, #667eea22 0%, #764ba222 100%); padding: 25px; border-radius: 15px; margin: 20px 0;">
    <h3>📚 Academic Focus</h3>

    **Mathematics**: Discrete Mathematics, Calculus and Linear Algebra, Probability & Statistics, Differential Equations<br>
    **Programming**: C, C++, Data Structures And Algorithms<br>
    **Electronics**: Control System, Analog and Digital Electronics<br>
    **Communication**: Signal and System, Digital Communication, Electromagnetic Theory<br>
    **Business**: Economics, Management<br>
    **Academic Interests**: Natural Language Processing, AI Systems, IOT, Robotics, Reinforcement Learning
    </div>
    """, unsafe_allow_html=True)

elif section == "🧠 Skills":
    st.markdown("<h2 class='section-title'>🧠 Technical Skills</h2>", unsafe_allow_html=True)

    skills_categories = {
        "🧑‍💻 Programming & Tools": ["Python", "C", "SQL", "Git", "Jupyter", "VS Code", "Streamlit", "Bash"],
        "🗣️ NLP & Language": ["Hugging Face", "spaCy", "NLTK", "VADER", "LangChain"],
        "📄 Document & QA": ["RAG", "LangChain", "FAISS", "ChromaDB", "PyMuPDF"],
        "📊 Modeling & ML": ["NMF", "LDA", "TextRank", "CNN", "PyTorch", "Scikit-learn"],
        "🎙️ Speech & Audio": ["pyttsx3", "Librosa"],
        "📈 Visualization": ["Matplotlib", "Seaborn", "Plotly", "Pandas"]
    }

    for category, skills in skills_categories.items():
        st.markdown(f"<h4>{category}</h4>", unsafe_allow_html=True)
        skills_html = "".join([f"<span class='skill-badge'>{skill}</span>" for skill in skills])
        st.markdown(f"<div style='margin-bottom: 20px;'>{skills_html}</div>", unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="hover-lift" style="background: linear-gradient(135deg, #f093fb22 0%, #f5576c22 100%); padding: 20px; border-radius: 15px;">
        <h3>💬 Soft Skills </h3>
        • Communication<br>
        • Teamwork & Collaboration<br>
        • Adaptability<br>
        • Problem Solving<br>
        • Time Management
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="hover-lift" style="background: linear-gradient(135deg, #667eea22 0%, #764ba222 100%); padding: 20px; border-radius: 15px;">
        <h3>📊 Business Skills </h3>
        • Business Analysis<br>
        • Product Thinking<br>
        • Data-Driven Decision Making<br>
        • Project Management Basics
        </div>
        """, unsafe_allow_html=True)

elif section == "💼 Professional Experience":
    st.markdown("<h2 class='section-title'>💼 Professional Experience</h2>", unsafe_allow_html=True)
    st.info("🚀 Currently building experience through cutting-edge projects and continuous learning!")

elif section == "🚀 Projects":
    st.markdown("<h2 class='section-title'>🚀 Projects</h2>", unsafe_allow_html=True)

    # Project 1
    with st.expander("🧬 Swastha – AI-Powered Lifestyle Recommendation System", expanded=False):
        st.markdown("""
        <div class='project-card'>
        A personalized health and wellness advisory system that provides lifestyle recommendations using biometric and behavioral data.

        🔸 <b>Use Case</b>: Helps individuals make better daily health decisions based on sleep, hydration, fitness, stress, and nutrition levels.<br><br>
        🔸 <b>Business Value</b>: Applicable for fitness apps, wellness dashboards, and preventive healthcare platforms focused on personalized user engagement.<br><br>
        🔸 <b>Approach</b>: Built a modular ML pipeline using Random Forest on synthetic wellbeing data. Engineered key features and heuristics to generate priority-based 
           health suggestions (e.g., hydration, sleep). Deployed via a real-time Streamlit app with dynamic feedback and wellbeing scoring.<br><br>
        <b>Tech Stack</b>: Python, NumPy, Pandas, Scikit-learn (Random Forest), Joblib, Streamlit, Modular ML Pipeline Design.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**🔗 Links:**")
        st.markdown("- [📺 Watch Demo on YouTube](https://m.youtube.com/watch?v=e7Vpl-sHtsU)")
        st.markdown("- [📁 View GitHub Repository](https://github.com/himanshudutta0/swastha-health-app)")

    # Project 2
    with st.expander("🎶 TuneDNA – Music Genre Classification using Deep Learning", expanded=False):
        st.markdown("""
        <div class='project-card'>
        A deep learning system that classifies audio tracks into music genres based on sound patterns.

        🔸 <b>Use Case</b>: Helps streaming platforms, independent musicians, and music apps to auto-tag and organize vast music libraries.<br><br>
        🔸 <b>Business Value</b>: Automates metadata tagging for better music discovery, personalization, and recommendation systems.<br><br>
        🔸 <b>Approach</b>: Converted audio into Mel Spectrograms and trained a CNN model to detect genre patterns.<br><br>
        🔸 <b>Outcome</b>: Achieved high-accuracy predictions with real-time genre identification via a Streamlit interface.<br><br>
        <b>Tech Stack</b>: TensorFlow, Librosa, NumPy, Matplotlib, Streamlit; CNNs, Audio & Signal Processing, TensorFlow Image API, Model Optimization.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**🔗 Links:**")
        st.markdown("- [📺 Watch Demo on YouTube](https://m.youtube.com/watch?v=Q9VjfXhQdYA)")
        st.markdown(
            "- [📁 Access Project Files on Google Drive](https://drive.google.com/drive/u/0/mobile/folders/1Bha3zjPXOAKpYKgJAQul7yzfqGJgyw2N)")

    # Project 3
    with st.expander("📰 NewsGuard – AI-Powered News Assistant", expanded=False):
        st.markdown("""
        <div class='project-card'>
        A real-time NLP pipeline that scrapes, analyzes, and visualizes news articles through a dynamic dashboard.

        🔸 <b>Use Case</b>: Assists readers, researchers, and journalists in identifying bias, understanding topics, and consuming concise news.<br><br>
        🔸 <b>Business Value</b>: Supports media houses, PR firms, and analysts in real-time trend monitoring, reputation tracking, and content verification.<br><br>
        🔸 <b>Approach</b>:<br>
        - Automated scraping from news sources in real-time<br>
        - Bias detection through sentiment scoring<br>
        - NMF for topic modeling and TextRank for summarization<br><br>
        🔸 <b>Interface</b>: A timeline-based dashboard with filters, summaries, and named entities.<br><br>
        <b>Tech Stack</b>: Python, Hugging Face Transformers, spaCy, NLTK, TextBlob, VADER, Pandas, Regex, JSON, LDA, 
                        newspaper3k, feedparser, BeautifulSoup, Streamlit, Matplotlib, Plotly.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**🔗 Links:**")
        st.markdown("- [📁 GitHub Repository](https://github.com/himanshudutta0/newsguard-ai-news-assistant)")
        st.markdown(
            "- [📁 Project Drive Folder](https://drive.google.com/drive/u/0/mobile/folders/17P59AUh_Z4PYwKYkFg9V9Y8xJ3iWDrBc)")
        st.markdown("- [🌐 Live Demo](https://himanshudutta-newsguard-ai-news-assistant-hdngaina.streamlit.app/)")

    # Project 4
    with st.expander("📄 DocMind – AI-Powered Offline PDF Q&A App", expanded=False):
        st.markdown("""
        <div class='project-card'>
        <b>DocMind</b> is a smart, offline-capable AI assistant that allows users to upload PDF documents and ask natural language questions over them.  
        Powered by LLaMA 2 7B, the app performs semantic search and local inference to deliver fast, private, and cloud-free answers.

        🔸 <b>Key Features</b>:<br>
        - PDF upload, parsing, and intelligent chunking<br>
        - Embedding generation using all-MiniLM-L6-v2<br>
        - Vector store built with ChromaDB<br>
        - Local LLM inference via Hugging Face/Ollama (completely offline)<br>
        - Clean, modular Streamlit-based interface<br><br>

        🔸 <b>Business Value</b>:<br>
        - Empowers researchers, legal professionals, and corporate users to extract insights from documents without exposing sensitive data<br>
        - Eliminates cloud API costs and latency with full local processing<br>
        - Ideal for enterprise document review, offline reading, and compliance-sensitive environments<br><br>

        <b>Tech Stack</b>: Python, LangChain, LLaMA 2 (HuggingFace/Ollama), Sentence Transformers, ChromaDB, Streamlit, PyPDF/PyMuPDF
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**🔗 Links:**")
        st.markdown(
            "- [📁 Project Drive Folder](https://drive.google.com/drive/u/0/mobile/folders/1nOWGwDqGkZoihoLsM2Vx8gZZZoaAsMoP)")

    # Project 5
    with st.expander("📄 DocuMind.ai – Domain-Specific AI Assistant Suite", expanded=False):
        st.markdown("""
        <div class='project-card'>
        <b>DocuMind.ai</b> (v2.0 of DocuMind)

        A multi-domain AI-powered document assistant designed for modern professionals. DocuMind.ai provides intelligent support across healthcare, legal, finance, and business domains.

        🔸 <b>Tools & Modules</b>:<br><br>

        - <b>MedMind.AI</b> – Your intelligent medical assistant powered by RAG<br>
        - <b>CourtMind.AI</b> – Agentic legal research companion for Indian judiciary<br>
        - <b>LawMind.AI</b> – Smart assistant for legal contracts and compliance<br>
        - <b>FinMind.AI</b> – Financial AI assistant for stock trends and reports<br>
        - <b>BizMind.AI</b> – AI assistant for startups and business compliance<br>
        - <b>TaxMind.AI</b> – Simplifying Indian income tax planning<br>
        - <b>DocuTranslate.AI</b> – Document translation to Indian languages<br>
        - <b>WriteMind.AI</b> – Document refinement and enhancement<br><br>

        <b>Tech Stack</b>: AI, LLM, Streamlit, RAG, ChromaDB, LangGraph, Hugging Face Transformers
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**🔗 Links:**")
        st.markdown(
            "- [📁 Project Drive Folder](https://drive.google.com/drive/folders/12D_cz2Nk2ws-Amv9sx64UfX1kmo4JKjS)")

elif section == "📜 Certifications & Workshops":
    st.markdown("<h2 class='section-title'>📜 Certifications & Workshops</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="hover-lift" style="background: linear-gradient(135deg, #667eea22 0%, #764ba222 100%); padding: 25px; border-radius: 15px; margin: 20px 0;">
    <h3>IBM Data Science Specialization – Coursera</h3>
    <a href="https://www.coursera.org/account/accomplishments/specialization/W5EATQW69VBF" target="_blank">📜 View Certificate</a>
    </div>
    """, unsafe_allow_html=True)

    st.image("assets/cert_ibm_datasci.png", caption="IBM Certificate Preview", width=500)

    st.markdown("---")
    st.markdown("### 🛠 Workshops Attended")

    workshops = [
        ("🧠 Responsible Natural Language Processing Workshop", "assets/nlp.jpeg", "5-day FDP on RNLP by IIIT Kottayam"),
        ("🚁 Advanced Computer Vision Workshop", "assets/computer_vision.jpeg",
         "One-week FDP on CV for Image, Video, and Applications"),
        ("🧠 RISC-V (VEGA Microprocessor) Workshop", "assets/vega_workshop_certificate.jpg",
         "Open-source microprocessor design with VEGA chips"),
        ("🚁 Drone Technology Workshop", "assets/drone_workshop_certificate.jpg",
         "UAV design, flight mechanics, and automation")
    ]

    for title, img, desc in workshops:
        with st.expander(title):
            st.markdown(f"<p>{desc}</p>", unsafe_allow_html=True)
            st.image(img, width=500)

elif section == "🏅 Achievements":
    st.markdown("<h2 class='section-title'>🏅 Achievements</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="hover-lift" style="background: linear-gradient(135deg, #f093fb22 0%, #f5576c22 100%); padding: 25px; border-radius: 15px; margin: 20px 0;">
    <h3>🏆 Smart India Hackathon (SIH) 2025 – Finalist</h3>
    <p>Selected among the top teams nationwide after multiple evaluation rounds, demonstrating strong problem-solving, innovation, and technical execution.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📄 View Certificate"):
        st.image("assets/SIH_2025_Certificate.png", width=450)

elif section == "🎯 Interests":
    st.markdown("<h2 class='section-title'>🎯 Interests</h2>", unsafe_allow_html=True)

    interests = [
        ("📚", "Sanskrit & Linguistics", "Exploring classical language structures and their potential in NLP"),
        ("🧘", "Yoga & Meditation", "Practicing for mental clarity, discipline, and daily balance"),
        ("🎵", "Music & Dance", "Flute performance, enhancing creativity and emotional intelligence"),
        ("🏸", "Badminton", "Staying physically active while enjoying strategic gameplay"),
        ("🌍", "Travel & Culture", "Exploring diverse places, people, and perspectives")
    ]

    for emoji, title, desc in interests:
        st.markdown(f"""
        <div class="hover-lift" style="background: linear-gradient(135deg, #667eea22 0%, #764ba222 100%); padding: 20px; border-radius: 15px; margin: 15px 0;">
        <h3>{emoji} {title}</h3>
        <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

elif section == "🌄 Life Beyond Work":
    st.markdown("<h2 class='section-title'>🌄 Life Beyond Work</h2>", unsafe_allow_html=True)
    st.markdown("### A visual glimpse into the places that inspire me and refresh my perspective:")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/jatayu_earth_center.jpg", caption="JATAYU EARTH CENTER", use_container_width=True)

    with col2:
        st.image("images/adiyogi_shiva_statue.jpg", caption="ADIYOGI SHIVA STATUE", use_container_width=True)

    with col3:
        st.image("images/mayurasana.jpg", caption="PERFORMING MAYURASANA ON MOUNTAIN", use_container_width=True)

    st.markdown("---")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.image("images/cow_love.jpeg", caption="A quiet bond — peace shared between beings", use_container_width=True)
    with col5:
        st.image("images/bird.jpeg", use_container_width=True)
    with col6:
        st.image("images/bird_in_hand.jpeg", use_container_width=True)

    st.markdown("""
    <div style="text-align: center; font-style: italic; margin: 20px 0; color: #666;">
    Nature, birds, and animals don't chase deadlines. They simply live. A gentle reminder to pause, observe, and find balance.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    for i in range(3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            img_num = i * 3 + j + 1
            with col:
                st.image(f"images/{img_num}.jpeg", use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p style='font-size: 18px; color: #4CAF50;'>Made with ❤️ by Himanshu Dutta</p>
    <p style='font-size: 14px; color: #666;'>✨ Building meaningful technology, one project at a time</p>
</div>
""", unsafe_allow_html=True)
