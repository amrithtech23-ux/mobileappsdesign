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

# Debug: Show API key status
if api_key:
    st.success(f"✅ API Key loaded successfully!")
    st.info(f"🔑 Key length: {len(api_key)} characters")
    st.info(f"🔑 Key starts with: {api_key[:10]}...")
else:
    st.error("❌ OPENROUTER_API_KEY not found in secrets.toml")
    st.warning("Please add it in Settings → Secrets")
    st.stop()

# Replace placeholder with actual key
html_content = html_content.replace("{{OPENROUTER_API_KEY}}", api_key)

# Verify replacement worked
if "{{OPENROUTER_API_KEY}}" in html_content:
    st.error("❌ Placeholder still exists in HTML - replacement failed!")
else:
    st.success("✅ API key successfully injected into HTML")

# Render the app
st.components.v1.html(html_content, height=1300, scrolling=True)
