import streamlit as st

# Page Config
st.set_page_config(page_title="Himanshu Dutta | Profilo", layout="wide")

st.markdown("""
    <div style="margin: 40px 0; text-align: center;">
        <h1 style="color: #4CAF50; margin-bottom: 0.2em;">HIMANSHU DUTTA</h1>
        <h3 style="margin-top: 0; color: #333;">
            AI Engineer (NLP + GenAI) &nbsp; | &nbsp; Business Strategy-Oriented &nbsp; | &nbsp; IBM Data Science Certified
        </h3>
        <p style="font-size: 18px; margin: 0.5em 0;">
            📞 <a href="tel:+918409120774" style="color: #4CAF50; text-decoration: none;">+91 84091 20774</a> &nbsp; | &nbsp;
            📧 <a href="mailto:dutthimsun@gmail.com" style="color: #4CAF50; text-decoration: none;">dutthimsun@gmail.com</a> &nbsp; | &nbsp;
            <a href="https://www.linkedin.com/in/himanshu-dutta06" target="_blank" style="color: #4CAF50; text-decoration: none;">🔗 LinkedIn</a>
        </p>
        <p style="font-size: 24px; font-weight: bold; text-align: center; margin-bottom: 0; color: #444;">ॐ</p>
        <p style="font-size: 16px; font-style: italic; color: #666; text-align: center; margin-top: 0.2em;">
            कृष्णाय वासुदेवाय हरये परमात्मने ।<br>
            प्रणतः क्लेशनाशाय गोविन्दाय नमो नमः ॥
        </p>
    </div>
""", unsafe_allow_html=True)

# Resume Download
with open("assets/Himanshu_Dutta_Resume.pdf", "rb") as f:
    resume_data = f.read()

st.download_button(
    label="📄 Download Resume (PDF)",
    data=resume_data,
    file_name="Himanshu_Dutta_Resume.pdf",
    mime="application/pdf"
)

# Sidebar Navigation
st.sidebar.title("📄 Navigation")
section = st.sidebar.radio("Go to", ["Summary", "Education", "Skills", "Professional Experience", "Projects", "Certifications & Workshops", "Achievements",
                                     "Interests", "Life Beyond Work"])

# Sections
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

import base64

def get_base64_image_from_path(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

if section == "Summary":
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

elif section == "Education":
    st.subheader("🎓 Education")
    st.markdown("""
    **B.Tech in Electronics and Communication Engineering**  
    *Indian Institute of Information Technology (IIIT), Kottayam*  
    Aug 2023 – May 2027  

    - CGPA: *[To be updated]*  
    - Mathematics : Discrete Mathematics, Calculus and Linear Algebra, Probability & Statistics, Differential Equations
    - Programming: C, C++, Data Structures And Algorithms  
    - Electronics: Control System, Analog and Digital Electronics
    - Communication: Signal and System, Digital Communication, Electromagnetic Theory
    - Business: Economics, Management
    - Academic Interests: Natural Language Processing, AI Systems, IOT, Robotics, Reinforcement Learning   
    """)


elif section == "Skills":
    st.subheader("🧠 Technical Skills")

    st.markdown("**🧑‍💻 Programming & Tools**: Python, C, SQL, Git, Jupyter, VS Code, Streamlit, Bash")
    st.markdown("**🗣️ NLP & Language Understanding**: Hugging Face Transformers, spaCy, NLTK, VADER, LangChain")
    st.markdown("**📄 Document & QA Pipelines**: RAG, LangChain, FAISS, ChromaDB, PyMuPDF")
    st.markdown("**📊 Modeling & ML Frameworks**: NMF, LDA, TextRank, CNN, PyTorch, Scikit-learn")
    st.markdown("**🎙️ Speech & Audio**: pyttsx3, Librosa")
    st.markdown("**🚀 Deployment**: Streamlit Cloud")
    st.markdown("**📈 Visualization**: Matplotlib, Seaborn, Plotly, Pandas")

    st.markdown("---")
    st.subheader("💬 Soft Skills *(in progress)*")
    st.markdown("• Communication  \n• Teamwork & Collaboration  \n• Adaptability  \n• Problem Solving  \n• Time Management")

    st.subheader("📊 Business & Management Skills *(developing)*")
    st.markdown("• Business Analysis  \n• Product Thinking  \n• Data-Driven Decision Making  \n• Project Management Basics")

elif section == "Professional Experience":
    st.subheader("Professional Experience")


    st.markdown("---")  # horizontal divider



elif section == "Projects":
    st.subheader("🚀 Projects")

    # project 1
    with st.expander("🧬 Swastha – AI-Powered Lifestyle Recommendation System", expanded=False):
        st.markdown("""
        A personalized health and wellness advisory system that provides lifestyle recommendations using biometric and behavioral data.

        🔸 **Use Case**: Helps individuals make better daily health decisions based on sleep, hydration, fitness, stress, and nutrition levels.  
        🔸 **Business Value**: Applicable for fitness apps, wellness dashboards, and preventive healthcare platforms focused on personalized user engagement.  
        🔸 **Approach**: Built a modular ML pipeline using Random Forest on synthetic wellbeing data. Engineered key features and heuristics to generate priority-based 
           health suggestions (e.g., hydration, sleep). Deployed via a real-time Streamlit app with dynamic feedback and wellbeing scoring.  
        **Tech Stack**: Python, NumPy, Pandas, Scikit-learn (Random Forest), Joblib, Streamlit, Modular ML Pipeline Design.

        🔗 **Demo Video**: [Watch on YouTube](https://m.youtube.com/watch?v=e7Vpl-sHtsU)  
        🗂 **GitHub Repo**: [View on GitHub](https://github.com/himanshudutta0/swastha-health-app)
        """)

    # project 2
    with st.expander("🎶 TuneDNA – Music Genre Classification using Deep Learning"):
        st.markdown("""
        A deep learning system that classifies audio tracks into music genres based on sound patterns.

        🔸 **Use Case**: Helps streaming platforms, independent musicians, and music apps to auto-tag and organize vast music libraries.  
        🔸 **Business Value**: Automates metadata tagging for better music discovery, personalization, and recommendation systems.  
        🔸 **Approach**: Converted audio into Mel Spectrograms and trained a CNN model to detect genre patterns.  
        🔸 **Outcome**: Achieved high-accuracy predictions with real-time genre identification via a Streamlit interface.

        **Tech Stack**: TensorFlow, Librosa, NumPy, Matplotlib, Streamlit; CNNs, Audio & Signal Processing, TensorFlow Image API, Model Optimization.

        🔗 [📺 Watch Demo on YouTube](https://m.youtube.com/watch?v=Q9VjfXhQdYA)  
        🔗 [📁 Access Project Files on Google Drive](https://drive.google.com/drive/u/0/mobile/folders/1Bha3zjPXOAKpYKgJAQul7yzfqGJgyw2N)
        """)

    # project 3
    with st.expander("📰 NewsGuard – AI-Powered News Assistant"):
        st.markdown("""
        A real-time NLP pipeline that scrapes, analyzes, and visualizes news articles through a dynamic dashboard.

        🔸 **Use Case**: Assists readers, researchers, and journalists in identifying bias, understanding topics, and consuming concise news.  
        🔸 **Business Value**: Supports media houses, PR firms, and analysts in real-time trend monitoring, reputation tracking, and content verification.  
        🔸 **Approach**: 
        - Automated scraping from news sources in real-time  
        - Bias detection through sentiment scoring  
        - NMF for topic modeling and TextRank for summarization  
        🔸 **Interface**: A timeline-based dashboard with filters, summaries, and named entities.

        **Tech Stack**: Python, Hugging Face Transformers, spaCy, NLTK, TextBlob, VADER, Pandas, Regex, JSON, LDA, 
                        newspaper3k, feedparser, BeautifulSoup, Streamlit, Matplotlib, Plotly.

        🔗 [GitHub Repository](https://github.com/himanshudutta0/newsguard-ai-news-assistant)  
        🔗 [Project Drive Folder](https://drive.google.com/drive/u/0/mobile/folders/17P59AUh_Z4PYwKYkFg9V9Y8xJ3iWDrBc)  
        🔗 [Live Demo](https://himanshudutta-newsguard-ai-news-assistant-hdngaina.streamlit.app/)
        """)

    # project 4
    with st.expander("📄 DocMind – AI-Powered Offline PDF Q&A App"):
        st.markdown("""
        **DocMind** is a smart, offline-capable AI assistant that allows users to upload PDF documents and ask natural language questions over them.  
        Powered by LLaMA 2 7B, the app performs semantic search and local inference to deliver fast, private, and cloud-free answers.

        🔸 **Key Features**:  
        - PDF upload, parsing, and intelligent chunking  
        - Embedding generation using `all-MiniLM-L6-v2`  
        - Vector store built with ChromaDB  
        - Local LLM inference via Hugging Face/Ollama (completely offline)  
        - Clean, modular Streamlit-based interface  

        🔸 **Business Value**:  
        - Empowers researchers, legal professionals, and corporate users to extract insights from documents without exposing sensitive data  
        - Eliminates cloud API costs and latency with full local processing  
        - Ideal for enterprise document review, offline reading, and compliance-sensitive environments  

        🔸 **Interface**:  
        - Intuitive Streamlit dashboard with drag-and-drop PDF upload  
        - Text input for natural language questions  
        - Real-time answers, highlighted context chunks, and document preview  

        **Tech Stack**: Python, LangChain, LLaMA 2 (HuggingFace/Ollama), Sentence Transformers, ChromaDB, Streamlit, PyPDF/PyMuPDF

        **Skills**: NLP, Hugging Face Transformers, LangChain, Vector Search, ChromaDB, Streamlit, Sentence Transformers, Question Answering Systems

        🔗 [Project Drive Folder](https://drive.google.com/drive/u/0/mobile/folders/1nOWGwDqGkZoihoLsM2Vx8gZZZoaAsMoP)
        """)

    # project 5
    # Project 4 (Updated)
    with st.expander("📄 DocuMind.ai – Domain-Specific AI Assistant Suite for Document Intelligence"):
        st.markdown("""
        **DocuMind.ai** (v2.0 of DocuMind)

        A multi-domain AI-powered document assistant designed for modern professionals. DocuMind.ai provides intelligent support across healthcare, legal, finance, and business domains. Built with advanced **Retrieval-Augmented Generation (RAG)**, fine-tuned language models, and agentic workflows via **LangGraph**, it understands, analyzes, and simplifies complex documents with precision and speed.

        🔸 **Tools & Modules**:

        - **MedMind.AI** (available now) – Your intelligent medical assistant powered by RAG, capable of answering complex health-related questions instantly and accurately.  
        - **CourtMind.AI** – An agentic legal research companion that analyzes court judgments, extracts insights, and supports case law interpretation, optimized for the Indian judiciary system.  
        - **LawMind.AI** – Smart assistant for reviewing, drafting, and explaining legal contracts, notices, and compliance documents using fine-tuned legal language models.  
        - **FinMind.AI** – Financial AI assistant to decode stock trends, analyze financial news, and interpret company reports via RAG-based pipelines.  
        - **BizMind.AI** – AI assistant for startups and businesses offering guidance on GST, company registration, compliance processes, and government schemes.  
        - **TaxMind.AI** – Fine-tuned assistant simplifying Indian income tax, covering deductions, planning, filings, and compliance tracking.  
        - **DocuTranslate.AI** – Translate legal, medical, and official documents into Indian regional languages with high accuracy and domain-sensitive handling.  
        - **WriteMind.AI** – Document refinement assistant that summarizes, corrects, and enhances writing across any domain using advanced AI writing tools.

        🔸 **Skills & Tech Stack**:  
        Artificial Intelligence (AI), Large Language Models (LLM), Streamlit, Retrieval-Augmented Generation (RAG), ChromaDB, LangGraph, Hugging Face Transformers, Sentence Transformers, Domain-Specific AI, Medical AI, FinTech AI.

        🔗 [Project Drive Folder](https://drive.google.com/drive/folders/12D_cz2Nk2ws-Amv9sx64UfX1kmo4JKjS)
        """)


elif section == "Certifications & Workshops":
    st.subheader("🎓 Certifications & Workshops")

    # IBM Certificate with clickable link
    st.markdown("""
    **IBM Data Science Specialization** – Coursera  
    [📜 View Certificate](https://www.coursera.org/account/accomplishments/specialization/W5EATQW69VBF)
    """, unsafe_allow_html=True)

    # Display certificate image with updated parameter
    st.image("assets/cert_ibm_datasci.png", caption="IBM Certificate Preview", width=500)

    # Workshops section
    st.markdown("""
    ---
    **🛠 Workshops Attended**
    """)



    # Workshop 1
    st.markdown("""
    ---
    ### 🧠 **Responsible Natural Language Processing Workshop**
    Proud to have participated in the 5-day Online Faculty Development Programme on Responsible Natural Language Processing (RNLP) by IIIT Kottayam, enhancing my skills in AI and NLP.
    """)
    st.image("assets/nlp.jpeg", caption="Responsible Natural Language Processing WORKSHOP", width=500)

    # Workshop 2
    st.markdown("""
    ---
    ### 🚁 **Advanced Computer Vision Workshop**
    Successfully completed a one-week FDP-cum-Workshop on Advanced Computer Vision for Image, Video, and Applications organized by IIIT Kottayam.
    """)
    st.image("assets/computer_vision.jpeg", caption="Advanced Computer Vision WORKSHOP", width=500)

    # Workshop 3
    st.markdown("""
    ---
    ### 🧠 **RISC-V (VEGA Microprocessor) Workshop**
    Gained exposure to open-source microprocessor design, low-level programming, and hardware-software co-design using India's indigenous **VEGA** chips.
    """)
    st.image("assets/vega_workshop_certificate.jpg", caption="VEGA PROCESSOR WORKSHOP", width=500)

    # Workshop 4
    st.markdown("""
    ---
    ### 🚁 **Drone Technology Workshop**
    Explored the principles of UAV design, flight mechanics, and real-time applications in automation.
    """)
    st.image("assets/drone_workshop_certificate.jpg", caption="DRONE WORKSHOP", width=500)


elif section == "Achievements":
    st.subheader("🏅 Achievements")
    st.markdown(""" 
    """)


elif section == "Interests":
    st.subheader("🎯 Interests")
    st.markdown("""
    - 📚 **Sanskrit & Linguistics** – Exploring classical language structures and their potential in NLP  
    - 🧘 **Yoga & Meditation** – Practicing for mental clarity, discipline, and daily balance  
    - 🎵 **Flute Performance & Music Appreciation** – Enhancing creativity, emotional intelligence, and rhythm  
    - 🏸 **Badminton** – Staying physically active while enjoying strategic gameplay  
    - 🌍 **Travel & Culture** – Exploring diverse places, people, and perspectives  
    """)

elif section == "Life Beyond Work":
    st.subheader("🌄 Life Beyond Work")
    st.markdown("A visual glimpse into the places that inspire me and refresh my perspective:")

    # First row of 3 images
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/jatayu_earth_center.jpg", caption="JATAYU EARTH CENTER", use_container_width=True)

    with col2:
        st.image("images/adiyogi_shiva_statue.jpg", caption="ADIYOGI SHIVA STATUE", use_container_width=True)

    with col3:
        st.image("images/mayurasana.jpg", caption="PERFORMING MAYURASANA ON MOUNTAIN IN JEHANABAD, BIHAR",
                 use_container_width=True)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.image(
            "images/cow_love.jpeg",
            caption="A quiet bond — not for attention, not to impress. Just a breath of peace shared between two beings.",
            use_container_width=True
        )
    with col5:
        st.image(
            "images/bird.jpeg",
            use_container_width=True
        )
    with col6:
        st.image(
            "images/bird_in_hand.jpeg",
            use_container_width=True
        )

    st.markdown("Nature, birds, and animals don’t chase deadlines. They simply live. A gentle reminder to pause, observe, and find balance.")
    # First row of 3 images
    # First row
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/1.jpeg", use_container_width=True)
    with col2:
        st.image("images/2.jpeg", use_container_width=True)
    with col3:
        st.image("images/3.jpeg", use_container_width=True)

    # Second row
    col4, col5, col6 = st.columns(3)

    with col4:
        st.image("images/4.jpeg", use_container_width=True)
    with col5:
        st.image("images/5.jpeg", use_container_width=True)
    with col6:
        st.image("images/6.jpeg", use_container_width=True)

    # Third row
    col7, col8, col9 = st.columns(3)

    with col7:
        st.image("images/7.jpeg", use_container_width=True)
    with col8:
        st.image("images/8.jpeg", use_container_width=True)
    with col9:
        st.image("images/9.jpeg", use_container_width=True)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center;'>Made with ❤️ by Himanshu Dutta</div>", unsafe_allow_html=True)
