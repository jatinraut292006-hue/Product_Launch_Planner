import streamlit as st
from crew import run_crew
from judge import evaluate_output
from image_generator import generate_marketing_image

st.set_page_config(
    page_title="Product Launch Planner",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Product Launch Planner")
st.subheader("AI-Powered Multi-Agent Launch Planning System")
st.markdown("---")

st.header("Tell us about your product")

product_name = st.text_input(
    "Product Name",
    placeholder="e.g. TaskFlow"
)

product_description = st.text_area(
    "Product Description",
    placeholder="e.g. A productivity app that helps remote teams manage tasks and deadlines in real time",
    height=120
)

target_market = st.text_input(
    "Target Market",
    placeholder="e.g. Remote teams in tech startups"
)

st.markdown("---")

if st.button("🚀 Generate Launch Plan", type="primary"):
    
    if not product_name or not product_description or not target_market:
        st.error("Please fill in all three fields before generating.")
    
    else:
        with st.spinner("Agents are working on your launch plan. This may take a few minutes..."):
            try:
                result = run_crew(product_name, product_description, target_market)
                st.session_state.result = result
                st.session_state.product_name = product_name
                st.session_state.target_market = target_market
                st.success("Launch plan generated successfully!")
            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")

if "result" in st.session_state:
    
    st.markdown("---")
    st.header("📋 Your Product Launch Plan")
    st.markdown(str(st.session_state.result))
    
    st.markdown("---")
    st.header("🎨 Marketing Visual")
    
    if st.button("Generate Marketing Image", type="primary"):
        with st.spinner("Generating your marketing image..."):
            try:
                image_data = generate_marketing_image(
                    str(st.session_state.result),
                    st.session_state.product_name
                )
                if image_data:
                    st.image(image_data, caption=f"Marketing Visual for {st.session_state.product_name}")
                else:
                    st.error("Image generation failed. Please try again.")
            except Exception as e:
                st.error(f"Image generation failed: {str(e)}")
    
    st.header("🏆 Quality Evaluation")
    
    if st.button("Evaluate Launch Plan Quality", type="secondary"):
        with st.spinner("Judge is evaluating your launch plan..."):
            try:
                evaluation = evaluate_output(
                    st.session_state.product_name,
                    st.session_state.target_market,
                    str(st.session_state.result)
                )
                st.markdown(evaluation)
            except Exception as e:
                st.error(f"Evaluation failed: {str(e)}")