import streamlit as st
from pathlib import Path

# 1. Page Configuration
st.set_page_config(
    page_title="Mobile App Forge | Bold Frame Studio",
    page_icon="📱",
    layout="wide"
)

# 2. Load HTML File
html_path = Path("index.html")
if not html_path.exists():
    st.error("❌ index.html not found. Please upload the HTML file.")
    st.stop()

html_content = html_path.read_text(encoding="utf-8")

# 3. Inject API Key from Secrets
api_key = st.secrets.get("OPENROUTER_API_KEY", "")

if api_key:
    # Replace the placeholder with the actual key from secrets.toml
    html_content = html_content.replace("{{OPENROUTER_API_KEY}}", api_key)
else:
    st.error("❌ OPENROUTER_API_KEY missing in secrets.toml")

# 4. Render the Application
st.components.v1.html(html_content, height=1300, scrolling=True)
