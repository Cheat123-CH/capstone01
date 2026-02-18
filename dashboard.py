import streamlit as st

st.set_page_config(layout="wide")

# =============================
# CUSTOM CSS
# =============================
st.markdown("""
<style>

body {
    background-color: #f5f7fa;
}

.main-title {
    background-color: #fdecec;
    padding: 40px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 30px;
}

.quarantine-title {
    color: red;
    font-size: 28px;
    font-weight: bold;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
}

/* MAKE BUTTON LOOK LIKE CARD */
div.stButton > button {
    width: 100%;
    text-align: left;
    padding: 12px 15px;
    border-radius: 10px;
    border: 2px solid #e5e7eb;
    background-color: white;
    font-size: 14px;
    transition: 0.2s;
    white-space: pre-wrap !important;
    line-height: 1.4;
    font-family: monospace;
}

div.stButton > button:hover {
    border: 2px solid #4a90e2;
    background-color: #f9fbff;
}

.selected-card > button {
    border: 2px solid #4a90e2 !important;
}

/* Status colors */
.quarantined-status {
    color: #ff0000;
    font-weight: bold;
}

.suspicious-status {
    color: #ff8800;
    font-weight: bold;
}

.low-status {
    color: #4a90e2;
    font-weight: bold;
}

.security-tip {
    background-color: #fff4e5;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-weight: 500;
}

/* Bullet point styling */
.bullet {
    font-size: 16px;
    margin-right: 5px;
}

/* AI Assistant styling */
.ai-container {
    background-color: white;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

.ai-header {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 15px;
    padding-bottom: 10px;
    border-bottom: 1px solid #e5e7eb;
}

.ai-online {
    color: #22c55e;
    font-size: 14px;
    font-weight: 500;
}

.ai-online-dot {
    color: #22c55e;
    font-size: 20px;
}

.ai-message {
    background-color: #f0f7ff;
    padding: 15px;
    border-radius: 12px;
    margin: 15px 0;
    border-left: 4px solid #4a90e2;
}

.ai-analysis {
    margin: 20px 0;
}

.ai-analysis h4 {
    margin: 15px 0 5px 0;
    color: #1e293b;
    font-size: 16px;
}

.ai-analysis p {
    margin: 5px 0 15px 0;
    color: #475569;
    line-height: 1.6;
}

.ai-suggestions {
    background-color: #fef3c7;
    padding: 20px;
    border-radius: 12px;
    margin: 20px 0;
    color: #92400e;
    font-weight: 500;
}

/* Quick question buttons */
.ai-questions {
    display: flex;
    gap: 15px;
    margin: 15px 0;
    flex-wrap: wrap;
}

.ai-question-btn {
    background: none;
    border: 1px solid #e2e8f0;
    padding: 8px 16px;
    border-radius: 20px;
    color: #4a90e2;
    font-weight: 500;
    cursor: pointer;
    transition: 0.2s;
}

.ai-question-btn:hover {
    background-color: #4a90e2;
    color: white;
    border-color: #4a90e2;
}

.ai-chat-input {
    display: flex;
    gap: 10px;
    margin-top: 15px;
}

.ai-chat-input input {
    flex: 1;
    padding: 12px 15px;
    border: 1px solid #e2e8f0;
    border-radius: 25px;
    font-size: 14px;
}

.ai-chat-input button {
    background-color: #4a90e2;
    color: white;
    border: none;
    border-radius: 25px;
    padding: 0 20px;
    font-weight: 500;
    cursor: pointer;
    transition: 0.2s;
}

.ai-chat-input button:hover {
    background-color: #2563eb;
}

.divider {
    border-top: 1px solid #e5e7eb;
    margin: 15px 0;
}

</style>
""", unsafe_allow_html=True)

# =============================
# HEADER
# =============================
st.markdown("""
<div class="main-title">
    <div class="quarantine-title">🔒 QUARANTINED</div>
    <div>Threats found and safely isolated. Your system is protected.</div>
</div>
""", unsafe_allow_html=True)

# =============================
# DATABASE
# =============================
activities = [
    {
        "id": "invoice",
        "time": "2:34 PM Today",
        "name": "invoice_2024.exe",
        "path": "C:\\Users\\Downloads\\invoice_2024.exe",
        "status": "Quarantined",
        "analysis": "This executable attempted suspicious registry modifications and tried to create persistence mechanisms.",
        "risk": "High-risk malware behavior detected. The file attempted to modify Windows registry keys used for startup programs."
    },
    {
        "id": "report",
        "time": "1:15 PM Today",
        "name": "report.docx",
        "path": "C:\\Users\\Documents\\report.docx",
        "status": "Suspicious",
        "analysis": "This document contains macros that attempt to execute PowerShell scripts upon opening. The macros are obfuscated to avoid detection.",
        "risk": "Macro-enabled documents are a common vector for malware. The script attempts to connect to an external server to download additional payloads."
    },
    {
        "id": "usb",
        "time": "11:42 AM Today",
        "name": "External USB Drive (E:)",
        "path": "",
        "status": "Low",
        "analysis": "USB drive scanned successfully. No threats detected in the automatic scan.",
        "risk": "No major threat detected. However, always be cautious with external devices."
    },
    {
        "id": "update",
        "time": "10:20 AM Today",
        "name": "update.dll",
        "path": "C:\\Program Files\\UpdateService\\update.dll",
        "status": "Low",
        "analysis": "DLL file scanned successfully. The file appears to be a legitimate system component.",
        "risk": "No major threat detected. File is digitally signed and verified."
    },
    {
        "id": "project",
        "time": "9:05 AM Today",
        "name": "project_files.zip",
        "path": "C:\\Users\\Desktop\\project_files.zip",
        "status": "Low",
        "analysis": "ZIP archive scanned successfully. All files inside have been verified.",
        "risk": "No major threat detected. Archive contains only document files."
    }
]

# =============================
# SESSION STATE
# =============================
if "selected_id" not in st.session_state:
    st.session_state.selected_id = activities[0]["id"]
    
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# =============================
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

# =============================
# LAYOUT
# =============================
col1, col2 = st.columns([1, 1.5])

# =============================
# LEFT SIDE (RECENT ACTIVITY)
# =============================
with col1:

    st.markdown("## Recent Activity")

    for item in activities:
        is_selected = st.session_state.selected_id == item["id"]
        
        # Build the button label
        if item["name"] == "External USB Drive (E:)":
            button_label = f"""• **{item['time']}**
  {item['status']}

• **{item['name']}**"""
        else:
            button_label = f"""• **{item['time']}**
  {item['status']}

• **{item['name']}**
  {item['path']}"""

        if is_selected:
            container = st.container()
            container.markdown('<div class="selected-card">', unsafe_allow_html=True)
            if container.button(button_label, key=item["id"], use_container_width=True):
                st.session_state.selected_id = item["id"]
            container.markdown('</div>', unsafe_allow_html=True)
        else:
            if st.button(button_label, key=item["id"], use_container_width=True):
                st.session_state.selected_id = item["id"]

    # Quarantine box
    st.markdown("## 🔐 Quarantine")
    st.markdown("""
    <div class="card">
        <div style="font-size:24px;color:red;">1</div>
        <div>Item Isolated</div>
        <small>Quarantined files are safely isolated and cannot harm your system.</small>
    </div>
    """, unsafe_allow_html=True)

# =============================
# RIGHT SIDE - AI SECURITY ASSISTANT CHATBOT
# =============================
# RIGHT SIDE - AI SECURITY ASSISTANT CHATBOT
with col2:
    selected_item = next(item for item in activities if item["id"] == st.session_state.selected_id)

    st.markdown("## AI Security Assistant")

    # --- AI info card ---
    ai_html = f"""
    <div class="ai-container">
        <div class="ai-header">
            <span class="ai-online-dot">🟢</span>
            <span class="ai-online">Online • Analyzing {selected_item['name']}</span>
        </div>

        <div class="ai-message">
            <strong>Analysis Summary:</strong> I've scanned <strong>{selected_item['name']}</strong>.
        </div>

        <div class="ai-analysis">
            <h4>🔍 Detailed Analysis</h4>
            <p>{selected_item['analysis']}</p>

            <h4>⚠️ Risk Assessment</h4>
            <p>{selected_item['risk']}</p>
        </div>

        <div class="ai-suggestions">
            💡 You can ask me about its origin, recommendations, or safety tips.
        </div>
    </div>
    """
    st.markdown(ai_html, unsafe_allow_html=True)

    # --- Quick question buttons ---
    col_q1, col_q2, col_q3 = st.columns(3)
    with col_q1:
        if st.button("❓ What is this?", key="q1"):
            st.session_state.chat_history.append({"role": "user", "content": "What is this?"})
            st.session_state.chat_history.append({"role": "assistant", "content": generate_ai_response("what is this", selected_item)})
    with col_q2:
        if st.button("📍 Where did it come from?", key="q2"):
            st.session_state.chat_history.append({"role": "user", "content": "Where did it come from?"})
            st.session_state.chat_history.append({"role": "assistant", "content": generate_ai_response("where did it come from", selected_item)})
    with col_q3:
        if st.button("🛡️ What should I do?", key="q3"):
            st.session_state.chat_history.append({"role": "user", "content": "What should I do?"})
            st.session_state.chat_history.append({"role": "assistant", "content": generate_ai_response("what should i do", selected_item)})

    # --- Display chat history ---
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

    # --- Chat input ---
    col_input, col_send = st.columns([5,1])
    with col_input:
        st.text_input("Ask AI Assistant...", key="user_input", placeholder="Ask AI Assistant about this threat...")
    with col_send:
        st.button("Send", on_click=send_message)
