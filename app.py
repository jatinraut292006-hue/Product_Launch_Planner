import streamlit as st
from crew import run_crew
from judge import evaluate_output
from image_generator import generate_marketing_image

st.set_page_config(
    page_title="Product Launch Planner",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

* { font-family: 'DM Sans', sans-serif; }

.stApp {
    background: #020817;
    color: #e2e8f0;
}

/* Hide default streamlit elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* Hero Section */
.hero {
    background: linear-gradient(135deg, #020817 0%, #0f1729 50%, #020817 100%);
    border-bottom: 1px solid #1e293b;
    padding: 60px 80px 50px;
    position: relative;
    overflow: hidden;
}

.hero::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(ellipse at 30% 50%, rgba(99, 102, 241, 0.08) 0%, transparent 60%),
                radial-gradient(ellipse at 70% 50%, rgba(16, 185, 129, 0.06) 0%, transparent 60%);
    pointer-events: none;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(99, 102, 241, 0.1);
    border: 1px solid rgba(99, 102, 241, 0.3);
    border-radius: 100px;
    padding: 6px 16px;
    font-size: 12px;
    color: #818cf8;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-weight: 500;
    margin-bottom: 24px;
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 56px;
    font-weight: 800;
    line-height: 1.1;
    margin: 0 0 16px;
    background: linear-gradient(135deg, #ffffff 0%, #94a3b8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-title span {
    background: linear-gradient(135deg, #6366f1 0%, #10b981 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-sub {
    font-size: 18px;
    color: #64748b;
    font-weight: 300;
    max-width: 520px;
    line-height: 1.6;
    margin: 0 0 40px;
}

/* Agent Pills */
.agents-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 8px;
}

.agent-pill {
    display: flex;
    align-items: center;
    gap: 6px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 8px;
    padding: 6px 12px;
    font-size: 12px;
    color: #94a3b8;
}

.agent-pill .dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #10b981;
}

/* Main Content */
.main-content {
    padding: 50px 80px;
    max-width: 1400px;
    margin: 0 auto;
}

/* Input Card */
.input-card {
    background: #0d1117;
    border: 1px solid #1e293b;
    border-radius: 20px;
    padding: 40px;
    margin-bottom: 40px;
    position: relative;
    overflow: hidden;
}

.input-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, #6366f1, #10b981, transparent);
}

.section-label {
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #6366f1;
    font-weight: 600;
    margin-bottom: 8px;
}

.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 26px;
    font-weight: 700;
    color: #f1f5f9;
    margin: 0 0 30px;
}

/* Streamlit input overrides */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: #020817 !important;
    border: 1px solid #1e293b !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 15px !important;
    padding: 14px 18px !important;
    transition: border-color 0.2s !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
}

.stTextInput label, .stTextArea label {
    color: #94a3b8 !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    letter-spacing: 0.3px !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 32px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    font-family: 'DM Sans', sans-serif !important;
    cursor: pointer !important;
    transition: all 0.2s !important;
    letter-spacing: 0.3px !important;
    width: 100% !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 25px rgba(99, 102, 241, 0.35) !important;
}

.stButton > button[kind="secondary"] {
    background: rgba(16, 185, 129, 0.1) !important;
    border: 1px solid rgba(16, 185, 129, 0.3) !important;
    color: #10b981 !important;
}

.stButton > button[kind="secondary"]:hover {
    background: rgba(16, 185, 129, 0.2) !important;
    box-shadow: 0 8px 25px rgba(16, 185, 129, 0.2) !important;
}

/* Output Section */
.output-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 32px;
    padding-bottom: 24px;
    border-bottom: 1px solid #1e293b;
}

.output-badge {
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-radius: 8px;
    padding: 6px 14px;
    font-size: 12px;
    color: #10b981;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* Agent Output Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: #0d1117 !important;
    border-radius: 12px !important;
    padding: 4px !important;
    border: 1px solid #1e293b !important;
    gap: 4px !important;
}

.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #64748b !important;
    border-radius: 8px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    padding: 8px 16px !important;
    font-family: 'DM Sans', sans-serif !important;
}

.stTabs [aria-selected="true"] {
    background: #1e293b !important;
    color: #f1f5f9 !important;
}

.stTabs [data-baseweb="tab-panel"] {
    background: #0d1117 !important;
    border: 1px solid #1e293b !important;
    border-radius: 16px !important;
    padding: 30px !important;
    margin-top: 12px !important;
}

/* Score Cards */
.score-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin: 24px 0;
}

.score-card {
    background: #0d1117;
    border: 1px solid #1e293b;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}

.score-number {
    font-family: 'Syne', sans-serif;
    font-size: 32px;
    font-weight: 800;
    color: #6366f1;
}

.score-label {
    font-size: 12px;
    color: #64748b;
    margin-top: 4px;
}

/* Success/Error messages */
.stSuccess {
    background: rgba(16, 185, 129, 0.1) !important;
    border: 1px solid rgba(16, 185, 129, 0.3) !important;
    border-radius: 12px !important;
    color: #10b981 !important;
}

.stError {
    background: rgba(239, 68, 68, 0.1) !important;
    border: 1px solid rgba(239, 68, 68, 0.3) !important;
    border-radius: 12px !important;
}

/* Spinner */
.stSpinner > div {
    border-top-color: #6366f1 !important;
}

/* Divider */
hr {
    border-color: #1e293b !important;
    margin: 40px 0 !important;
}

/* Markdown content */
.stMarkdown h3 {
    font-family: 'Syne', sans-serif !important;
    color: #f1f5f9 !important;
    font-size: 18px !important;
    border-bottom: 1px solid #1e293b !important;
    padding-bottom: 10px !important;
    margin-top: 24px !important;
}

.stMarkdown p, .stMarkdown li {
    color: #94a3b8 !important;
    line-height: 1.8 !important;
}

.stMarkdown strong {
    color: #e2e8f0 !important;
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <div class="hero-badge">⚡ Multi-Agent AI System</div>
    <h1 class="hero-title">Product Launch<br><span>Planner</span></h1>
    <p class="hero-sub">Six specialized AI agents working in sequence to build your complete product launch plan — from market research to marketing visuals.</p>
    <div class="agents-row">
        <div class="agent-pill"><span class="dot"></span> Market Research</div>
        <div class="agent-pill"><span class="dot"></span> Audience Profiling</div>
        <div class="agent-pill"><span class="dot"></span> SEO & Keywords</div>
        <div class="agent-pill"><span class="dot"></span> Launch Strategy</div>
        <div class="agent-pill"><span class="dot"></span> Marketing & Messaging</div>
        <div class="agent-pill"><span class="dot"></span> Visual Advertising</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Main Content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Input Card
st.markdown("""
<div class="input-card">
    <div class="section-label">Step 01</div>
    <div class="section-title">Tell us about your product</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    product_name = st.text_input(
        "Product Name",
        placeholder="e.g. TaskFlow",
        key="product_name"
    )
    target_market = st.text_input(
        "Target Market",
        placeholder="e.g. Remote teams in tech startups",
        key="target_market"
    )

with col2:
    product_description = st.text_area(
        "Product Description",
        placeholder="e.g. A productivity app that helps remote teams manage tasks and deadlines in real time",
        height=130,
        key="product_description"
    )

st.markdown("<br>", unsafe_allow_html=True)

col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    generate_clicked = st.button("🚀 Generate Launch Plan", type="primary", use_container_width=True)

if generate_clicked:
    if not product_name or not product_description or not target_market:
        st.error("Please fill in all three fields before generating.")
    else:
        with st.spinner("Six agents are analyzing your product and building your launch plan. This takes 2-3 minutes..."):
            try:
                result = run_crew(product_name, product_description, target_market)
                st.session_state.result = result
                st.session_state.product_name = product_name
                st.session_state.target_market = target_market
                st.success("✅ Launch plan generated successfully!")
            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")

# Output Section
if "result" in st.session_state:

    st.markdown("---")

    st.markdown(f"""
    <div class="output-header">
        <div>
            <div class="section-label">Step 02</div>
            <div class="section-title" style="margin:0">Your Complete Launch Plan</div>
        </div>
        <div class="output-badge">✓ Generated</div>
    </div>
    """, unsafe_allow_html=True)

    # Parse output into sections
    result_text = str(st.session_state.result)
    sections = result_text.split("---")

    agent_names = [
        "🔍 Market Research",
        "👥 Audience Profile",
        "📈 SEO & Keywords",
        "🗺️ Launch Strategy",
        "📣 Marketing & Messaging",
        "🎨 Visual Advertising"
    ]

    # Display in tabs
    if len(sections) > 1:
        tabs = st.tabs(agent_names[:len(sections)-1])
        for i, tab in enumerate(tabs):
            with tab:
                if i + 1 < len(sections):
                    content = sections[i + 1].strip()
                    lines = content.split('\n')
                    clean_content = '\n'.join(lines[1:]) if lines else content
                    st.markdown(clean_content)
    else:
        st.markdown(result_text)

    st.markdown("---")

    # Judge Section
    st.markdown("""
    <div class="section-label">Step 03</div>
    <div class="section-title">Quality Evaluation</div>
    <p style="color:#64748b; margin-bottom:24px; font-size:14px;">An independent LLM-as-Judge evaluates your launch plan against a 7-criteria rubric and scores it out of 70.</p>
    """, unsafe_allow_html=True)

    col_j1, col_j2, col_j3 = st.columns([1, 2, 1])
    with col_j2:
        evaluate_clicked = st.button("⚖️ Evaluate Launch Plan Quality", type="secondary", use_container_width=True)

    if evaluate_clicked:
        with st.spinner("Judge is evaluating your launch plan against the rubric..."):
            try:
                evaluation = evaluate_output(
                    st.session_state.product_name,
                    st.session_state.target_market,
                    str(st.session_state.result)
                )
                st.session_state.evaluation = evaluation
            except Exception as e:
                st.error(f"Evaluation failed: {str(e)}")

    if "evaluation" in st.session_state:
        st.markdown("<br>", unsafe_allow_html=True)
        eval_text = st.session_state.evaluation

        # Extract total score if present
        total_score = None
        for line in eval_text.split('\n'):
            if 'TOTAL SCORE' in line:
                try:
                    total_score = line.split(':')[1].strip()
                except:
                    pass

        if total_score:
            col_s1, col_s2, col_s3 = st.columns([1, 1, 1])
            with col_s2:
                st.markdown(f"""
                <div class="score-card" style="text-align:center; padding:30px;">
                    <div style="font-size:13px; color:#64748b; letter-spacing:1px; text-transform:uppercase; margin-bottom:8px;">Total Score</div>
                    <div class="score-number" style="font-size:52px;">{total_score}</div>
                    <div style="font-size:12px; color:#64748b; margin-top:8px;">LLM-as-Judge Evaluation</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(eval_text)

# Image Generation Section
    if "result" in st.session_state:
        st.markdown("---")
        st.markdown("""
        <div class="section-label">Step 04</div>
        <div class="section-title">Marketing Visual</div>
        <p style="color:#64748b; margin-bottom:24px; font-size:14px;">Generate an eye-catching marketing image for your product using Gemini's image generation model.</p>
        """, unsafe_allow_html=True)

        col_i1, col_i2, col_i3 = st.columns([1, 2, 1])
        with col_i2:
            image_clicked = st.button("🎨 Generate Marketing Image", use_container_width=True)

        if image_clicked:
            with st.spinner("Generating your marketing visual..."):
                try:
                    from image_generator import generate_marketing_image
                    image_data = generate_marketing_image(
                        str(st.session_state.result),
                        st.session_state.product_name
                    )
                    if image_data:
                        st.markdown("<br>", unsafe_allow_html=True)
                        col_img1, col_img2, col_img3 = st.columns([1, 3, 1])
                        with col_img2:
                            st.image(image_data, caption=f"Marketing Visual — {st.session_state.product_name}", use_container_width=True)
                    else:
                        st.error("Image generation failed. Please try again.")
                except Exception as e:
                    st.error(f"Image generation failed: {str(e)}")

st.markdown('</div>', unsafe_allow_html=True)