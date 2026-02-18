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