import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Mobile App Forge | Bold Frame Studio",
    page_icon="📱",
    layout="wide"
)

# Load HTML file
html_path = Path("index.html")
if not html_path.exists():
    st.error("❌ index.html not found.")
    st.stop()

html_content = html_path.read_text(encoding="utf-8")

# Get API Key from Streamlit Secrets
api_key = st.secrets.get("OPENROUTER_API_KEY", "")

# Debug info
if api_key:
    st.success(f"✅ API Key loaded! (First 20 chars: {api_key[:20]}...)")
else:
    st.error("❌ OPENROUTER_API_KEY not found in secrets")
    st.stop()

# Replace placeholder with actual key - ensure it works
html_content = html_content.replace("{{OPENROUTER_API_KEY}}", api_key)

# Also try alternative placeholder formats
html_content = html_content.replace("{{ OPENROUTER_API_KEY }}", api_key)
html_content = html_content.replace("${OPENROUTER_API_KEY}", api_key)

# Render the app
st.components.v1.html(html_content, height=1300, scrolling=True)
