import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="AI-Sec Assistant",
    page_icon="🛡️",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main {
    background-color: #f4f6f9;
}
.big-alert {
    background-color: #ffe5e5;
    padding: 30px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #ff4d4d;
}
.section-box {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}
.grey-box {
    background-color: #e9ecef;
    padding: 20px;
    border-radius: 12px;
    margin-top: 15px;
}
.green-box {
    background-color: #e6f7ee;
    padding: 15px;
    border-radius: 10px;
}
.red-box {
    background-color: #fdeaea;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🛡️ AI-Sec Assistant")
st.caption("Intelligent Security Protection")

# ---------- QUARANTINED ALERT ----------
st.markdown("""
<div class="big-alert">
    <h1 style="color:#d90429;">🔒 QUARANTINED</h1>
    <p>Threats found and safely isolated. Your system is protected.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ---------- TWO COLUMN LAYOUT ----------
col1, col2 = st.columns([1, 2])

# ---------- LEFT SIDE ----------
with col1:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("🕒 Recent Activity")

    st.write("**2:34 PM Today**  🔴 Quarantined")
    st.write("C:/Users/Downloads/invoice_2024.exe")

    st.write("")
    st.write("**1:15 PM Today** 🟠 Suspicious")
    st.write("C:/Users/Documents/report.docx")

    st.write("")
    st.write("**11:42 AM Today** 🔵 Low")
    st.write("External USB Drive (E:)")

    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("🔒 Quarantine")
    st.error("1 Item Isolated")
    st.caption("Quarantined files are safely isolated and cannot harm your system.")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- RIGHT SIDE ----------
with col2:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("🤖 AI Security Assistant")

    st.markdown("""
    <div class="grey-box">
    <h3>What happened:</h3>
    <p>A file pretending to be an invoice was detected as malicious.</p>

    <h3>Where:</h3>
    <pre>C:/Users/Downloads/invoice_2024.exe</pre>

    <h3>Why it's risky:</h3>
    <p>The file came from an unknown email attachment and attempted unauthorized system access.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="green-box">
    <h3>✅ What to do:</h3>
    <ul>
    <li>Continue using your computer normally</li>
    <li>Delete suspicious emails</li>
    <li>Report phishing attempts</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="red-box">
    <h3>❌ What not to do:</h3>
    <ul>
    <li>Don't restore the quarantined file</li>
    <li>Don't download unknown attachments</li>
    <li>Don't click suspicious links</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- SECURITY TIP ----------
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("💡 Security Tip")
    st.info("Never click on links in unexpected emails, even if they look official.")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.write("")
st.caption("AI-Sec Assistant • Always protecting your digital workspace")
