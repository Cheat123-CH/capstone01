import streamlit as st
st.set_page_config(
    page_title="AI security",
    page_icon=" :tada",
    layout="wide"
)

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

col_input, col_send = st.columns([5,1])
with col_input:
    st.text_input("Ask AI Assistant...", key="user_input", placeholder="Ask AI Assistant about this threat...")
with col_send:
    st.button("Send", on_click=send_message)