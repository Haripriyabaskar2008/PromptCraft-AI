import streamlit as st
from llm import generate_response
from prompt_templates import build_prompt

st.set_page_config(
    page_title="PromptCraft AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 PromptCraft AI")
st.write(
    "Explore different prompt engineering techniques "
    "and generate responses using an AI language model."
)

technique = st.selectbox(
    "Select Prompting Technique",
    [
        "Zero-shot",
        "One-shot",
        "Few-shot",
        "CoT",
        "Manual CoT",
        "ToT"
    ]
)

task = st.text_area(
    "Enter your task:",
    placeholder=(
        "Example: Explain the difference between "
        "AI and Machine Learning."
    )
)

temperature = st.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.2,
    step=0.1
)

max_tokens = st.slider(
    "Maximum Tokens",
    min_value=100,
    max_value=1000,
    value=500,
    step=100
)

if st.button("Generate Response"):

    if task.strip() == "":
        st.warning("Please enter a task.")

    else:
        try:
            final_prompt = build_prompt(
                technique,
                task
            )

            st.subheader("Generated Prompt")

            st.code(
                final_prompt,
                language="text"
            )

            with st.spinner(
                "Generating the response..."
            ):
                answer = generate_response(
                    final_prompt,
                    temperature,
                    max_tokens
                )

            st.subheader("AI Response")
            st.write(answer)

        except Exception as e:
            st.error(
                f"Error while generating response: {e}"
            )