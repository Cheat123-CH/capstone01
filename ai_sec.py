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
    max-hight: 300px;
    padding-top: 5;
    background-color: #e9ecef;
    padding-left: 20px; 
    border-radius: 12px;
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
.section-box {
    background-color: #f9fafb;
    height: 150px;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

.activity-item {
    background-color:  #f3f4f6;
    padding: 12px 16px;
    border-radius: 12px;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}

.activity-left {
    font-size: 14px; 
}

.activity-time {
    color: gray;
    font-size: 12px;
}

.badge {
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
}
<style>
.card {
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    background-color: #fff;
}

.quarantine-header {
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 8px;
    color: #d32f2f;
}

.quarantine-box {
    margin-top: 10px;
    background-color: #fdecea;
    padding: 15px;
    border-radius: 8px;
    font-size: 18px;
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 10px;
}

.quarantine-caption {
    margin-top: 8px;
    font-size: 14px;
    color: #555;
    display: flex;
    align-items: center;
    gap: 6px;
}

.security-header {
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 8px;
    color: #f9a825;
}

.security-box {
    margin-top: 10px;
    background-color: #fff8e1;
    padding: 15px;
    border-radius: 8px;
    font-size: 14px;
}

.red { background-color: #ffe5e5; color: #d90429; }
.orange { background-color: #fff3e0; color: #f77f00; }
.blue { background-color: #e3f2fd; color: #1d4ed8; }
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

# ---------- TWO COLUMN LAYOUT ----------
col1, col2 = st.columns([1, 2])

# ---------- LEFT SIDE ----------
with col1:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("🕒 Recent Activity")

    # Item 1
    st.markdown("""
    <div class="activity-item">
        <div class="activity-left">
            <div class="activity-time">2:34 PM Today</div>
            C:/Users/Downloads/invoice_2024.exe
        </div>
        <div class="badge red">Quarantined</div>
    </div>
    """, unsafe_allow_html=True)

    # Item 2
    st.markdown("""
    <div class="activity-item">
        <div class="activity-left">
            <div class="activity-time">1:15 PM Today</div>
            C:/Users/Documents/report.docx
        </div>
        <div class="badge orange">Suspicious</div>
    </div>
    """, unsafe_allow_html=True)

    # Item 3
    st.markdown("""
    <div class="activity-item">
        <div class="activity-left">
            <div class="activity-time">11:42 AM Today</div>
            External USB Drive (E:)
        </div>
        <div class="badge blue">Low</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="activity-item">
        <div class="activity-left">
            <div class="activity-time">11:42 AM Today</div>
            External USB Drive (E:)
        </div>
        <div class="badge blue">Low</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="activity-item">
        <div class="activity-left">
            <div class="activity-time">11:42 AM Today</div>
            External USB Drive (E:)
        </div>
        <div class="badge blue">Low</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="activity-item">
        <div class="activity-left">
            <div class="activity-time">11:42 AM Today</div>
            External USB Drive (E:)
        </div>
        <div class="badge blue">Low</div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

# ---------- RIGHT SIDE ----------
with col2:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("🤖 AI Security Assistant")

    # -------- GREY BOX --------
    # change the word ""test " to function that query data/api 

    st.markdown(f"""
    <div class="grey-box">
    <strong>What happened:</strong><br>   
    test<br><br>
    <strong>Where:</strong><br>
    <code>test</code><br><br>
    <strong>Why it's risky:</strong><br>
    test
    </div>
    """, unsafe_allow_html=True)

 # -------- GREEN BOX --------
    st.markdown(f"""
    <div class="green-box">
    <strong>What to do:</strong><br>
    - Continue using your computer normally<br>
    - Delete suspicious emails<br>
    - Report phishing attempts
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # -------- RED BOX --------
    st.markdown(f"""
    <div class="red-box">
    <strong>What not to do:</strong><br>
    - Don't restore the quarantined file<br>
    - Don't download unknown attachments<br>
    - Don't click suspicious links
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

colb1, colb2 = st.columns([1, 2])

with colb1:
    # ---------- QUARANTINE BOX ----------
    st.markdown("""
    <div class="card">
        <div class="quarantine-header">🔒 Quarantine</div>
        <div class="quarantine-box">📄 1 Item Isolated</div>
        <div class="quarantine-caption">🔐 Quarantined files are safely isolated and cannot harm your system.</div>
    </div>
    """, unsafe_allow_html=True)

with colb2 :
    # ---------- SECURITY TIP ----------
    st.markdown("""
    <div class="card">
        <div class="security-header">💡 Security Tip</div>
        <div class="security-box">
            Never click on links in unexpected emails, even if they look official.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")
st.caption("AI-Sec Assistant • Always protecting your digital workspace")


