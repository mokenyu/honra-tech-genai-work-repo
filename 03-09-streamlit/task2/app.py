import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="AI Model Hub", page_icon="🤖", layout="wide")

# 2. Sidebar Navigation & Controls
st.sidebar.title("Navigation")

# Radio buttons for page navigation
page = st.sidebar.radio("Go to Page", ["Home Dashboard", "Model Playground", "Docs & FAQ"])

st.sidebar.markdown("---")
st.sidebar.subheader("Quick Settings")
selected_model = st.sidebar.selectbox("Choose Model", ["Gemini-Pro", "Llama-3", "Claude-3"])
max_tokens = st.sidebar.slider("Max Tokens", 50, 500, 200)

# 3. Page 1: Home Dashboard
# ❌ BUG 1 FIX NEEDED: Check the exact string option in st.sidebar.radio above!
# 'if page == "Home":' doesn't match "Home Dashboard", so this page will never load!
if page == "Home Dashboard":
    st.title("AI Model Hub")
    st.markdown("Welcome to the **AI Model Hub**! Explore our AI models and run experiments in the playground.")
    
    st.write("") # Spacing
    
    # ❌ BUG 2 FIX NEEDED: 'border' argument must be a boolean (True/False), not a string "yes"!
    with st.container(border=True):
        st.markdown("### Platform Overview")
        
        # TODO 1: Create 3 metrics side-by-side using st.columns(3):
        # - Metric 1: "Active Models" -> "3 Models"
        # - Metric 2: "Selected Model" -> selected_model
        # - Metric 3: "Token Limit" -> f"{max_tokens} tokens"
        col1, col2, col3 = st.columns(3)


        # Metric 1
        with col1:
            st.metric(
                "Active Models",
                "3 Models"
            )


        # Metric 2
        with col2:
            st.metric(
                "Selected Model",
                selected_model
            )


        # Metric 3
        with col3:
            st.metric(
                "Token Limit",
                f"{max_tokens} tokens"
            )
        
        st.markdown(
            "Use the sidebar navigation to switch to the **Model Playground** "
            "and test custom prompts in real-time."
        )

# 4. Page 2: Model Playground
elif page == "Model Playground":
    st.title("Model Playground")
    st.markdown("Test your prompts with the selected model settings.")

    user_prompt = st.text_area("Enter your prompt instructions:", placeholder="e.g. Summarize the benefits of learning Python...")

    if st.button("Run Model"):
        if not user_prompt.strip():
            st.warning("Please enter a prompt before running the model!")
        else:
            with st.spinner(f"Running query on {selected_model}..."):
                time.sleep(1)

            st.markdown("### Output Result")
            with st.container(border=True):
                st.write(
                    f"**Selected Model:** {selected_model}"
                )

                st.write(
                    f"**Max Tokens:** {max_tokens}"
                )

                st.write(
                    f"**Your Prompt:** {user_prompt}"
                )

                st.markdown("---")

                st.markdown(
                    f"""
### Simulated AI Response

Your request has been processed using **{selected_model}**.

Based on your prompt:

> {user_prompt}

This is a simulated AI response. In a real application,
the selected model would generate a response based on your
prompt and the maximum token limit of **{max_tokens} tokens**.
"""
                )
# TODO 2: Wrap the output inside a bordered container (with st.container(border=True):)
# Display: selected_model, max_tokens, user_prompt, and a simulated response string!

# 5. Page 3: Docs & FAQ
elif page == "Docs & FAQ":
    st.title("Documentation & FAQ")
    st.markdown("Learn how to navigate and use the AI Model Hub.")

    # TODO 3: Create at least two collapsable expander boxes using st.expander()
    # Expander 1: "How do I choose between models?"
    with st.expander("How do I choose between models?"):

        st.write(
            "Different AI models have different strengths. "
            "Some models are better for creative writing, "
            "while others may be better for coding, analysis, "
            "or complex reasoning."
        )
    # Expander 2: "What does 'Max Tokens' do?"
    with st.expander("What does 'Max Tokens' do?"):

        st.write(
            "The 'Max Tokens' setting limits the number of tokens (words or subwords) that the AI model will generate in its response. This helps control the length of the output and manage computational resources."
        )
