import streamlit as st


def configure_page() -> None:
    """Configure Streamlit page metadata and layout."""
    st.set_page_config(
        page_title="Google Gemini AI Chatbot",
        page_icon="✨",
        layout="centered",
    )


def render_header() -> None:
    """Render the main application title and subtitle."""
    st.title("Chat with Google Gemini")
    st.caption("Phase 3: Basic Streamlit chat interface (Gemini API coming in Phase 4)")


def main() -> None:
    """Run the basic Streamlit chat interface."""
    configure_page()
    render_header()

    # Initial assistant welcome message
    with st.chat_message("assistant"):
        st.markdown(
            "Hello! I am your **Google Gemini AI Chatbot** interface. "
            "Type a message below to test the chat layout."
        )

    # Chat input pinned to the bottom of the page
    user_prompt = st.chat_input("Ask me anything...")

    if user_prompt and user_prompt.strip():
        cleaned_prompt = user_prompt.strip()

        # Display the user's message
        with st.chat_message("user"):
            st.markdown(cleaned_prompt)

        # Display a placeholder assistant response (replaced by Gemini API in Phase 4)
        with st.chat_message("assistant"):
            st.markdown(
                f"**Placeholder response:** I received your message:\n\n> {cleaned_prompt}\n\n"
                "_Live Gemini AI responses will be connected in Phase 4._"
            )


if __name__ == "__main__":
    main()