import streamlit as st
from datetime import datetime
from database_chatbot.activities import activities

# Page config
st.set_page_config(
    page_title="AI-Sec Assistant",
    page_icon="🛡️",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles/style.css")

# =============================
# SESSION STATE
# =============================
if "selected_id" not in st.session_state:
    st.session_state.selected_id = activities[0]["id"]
    
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

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

#=============================
# FUNCTIONS
# =============================
def send_message():
    if st.session_state.user_input:
        st.session_state.chat_history.append({"role": "user", "content": st.session_state.user_input})
        # Simulate AI response
        ai_response = generate_ai_response(st.session_state.user_input, selected_item)
        st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
        st.session_state.user_input = ""

def generate_ai_response(query, file_info):
    responses = {
        "what is this": f"This is {file_info['name']}, a file that was scanned by our security system. It has been classified as {file_info['status']} risk based on our analysis.",
        "where did it come from": f"The file was found at: {file_info['path'] if file_info['path'] else 'External USB Drive'}",
        "what should i do": get_recommendation(file_info['status'])
    }
    
    for key, response in responses.items():
        if key in query.lower():
            return response
    
    return f"I've analyzed {file_info['name']}. Based on my analysis, this file is {file_info['status'].lower()} risk. You can ask me specific questions about its origin, what it is, or what actions to take."

def get_recommendation(status):
    if status == "Quarantined":
        return "The file has been automatically quarantined. You don't need to take any action - it's safely isolated."
    elif status == "Suspicious":
        return "I recommend keeping this file quarantined and not opening it. You can request a deeper scan if needed."
    else:
        return "The file appears safe, but always ensure you trust the source before opening."

# ---------- LEFT SIDE ----------
with col1:
    # this error
    st.subheader("🕒 Recent Activity")

    # Item 1
    for item in activities:
        is_selected = st.session_state.selected_id == item["id"]

        # Badge color based on status
        if item["status"].lower() == "low":
            badge_class = "blue"
        elif item["status"].lower() == "medium":
            badge_class = "orange"
        else:
            badge_class = "red"

        st.markdown(f"""
        <div class="activity-item">
            <div class="activity-left">
                <div class="activity-time">{item['time']}</div>
                <div class="activity-name">{item['name']}</div>
                <div class="activity-path">{item.get('path','')}</div>
            </div>
            <div class="badge {badge_class}">
                {item['status']}
            </div>
        </div>
        """, unsafe_allow_html=True)

# ---------- RIGHT SIDE ----------
with col2:
    
    selected_item = next(item for item in activities if item["id"] == st.session_state.selected_id)
    # this error
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
    st.write("")

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
    for message in st.session_state.chat_history[-6:]:
        if message["role"] == "user":
            st.markdown(f"""
            <div style="text-align:right; margin:5px 0;">
                <span style="background-color:#4a90e2; color:white; padding:8px 15px; border-radius:20px; display:inline-block; max-width:80%;">
                    {message['content']}
                </span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="text-align:left; margin:5px 0;">
                <span style="background-color:#f1f5f9; color:#1e293b; padding:8px 15px; border-radius:20px; display:inline-block; max-width:80%;">
                    🤖 {message['content']}
                </span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    # ---------- SECURITY TIP ----------
    col_input, col_send = st.columns([3,1])
    with col_input:
        st.text_input("Ask AI Assistant...", key="user_input", placeholder="Ask AI Assistant about this threat...")
    with col_send:
        st.button("Send", on_click=send_message) 

    # st.markdown("""
    # <div class="card">
    #     <div class="security-header">💡 Security Tip</div>
    #     <div class="security-box">
    #         Never click on links in unexpected emails, even if they look official.
    #     </div>
    # </div>
    # """, unsafe_allow_html=True)

st.write("")
st.write("")
st.caption("AI-Sec Assistant • Always protecting your digital workspace")


