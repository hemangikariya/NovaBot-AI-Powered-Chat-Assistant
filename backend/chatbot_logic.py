# def get_bot_response(user_input):
#     user_input = user_input.lower()

#     # Main Menu trigger
#     if user_input in ["menu", "main menu", "go to main menu", "start"]:
#         return (
#             "📋 Here's what I can help you with:\n\n"
#             "1. 🎓 MCA Overview\n"
#             "2. 💸 Fees & Cost\n"
#             "3. 📥 Admission Process\n"
#             "4. 🏫 Hostel Facilities\n"
#             "5. 📚 Syllabus & Subjects\n"
#             "6. 💼 Placement & Jobs\n"
#             "7. 🧠 AI/ML Career Scope\n\n"
#             "🟢 Type the topic name or number (e.g., 'Fees', '2') to get started.\n"
#             "🔁 You can also type 'Main Menu' anytime to return to this menu."
#         )

#     # MCA Overview
#     elif "mca" in user_input or user_input.strip() == "1":
#         return (
#             "🎓 *MCA (Master of Computer Applications)* is a 2-year postgraduate course focused on software "
#             "development, system programming, networking, data structures, and emerging tech like AI & Cloud."
#         )

#     # Fees
#     elif any(k in user_input for k in ["fees", "fee", "cost", "structure", "2"]):
#         return (
#             "💸 *MCA Fees*: \n"
#             "- Govt. Colleges: ₹20k–80k per year\n"
#             "- Private Institutes: ₹1L–2.5L per year\n"
#             "💡 Tip: Check for scholarships & fee waivers."
#         )

#     # Admission
#     elif any(k in user_input for k in ["admission", "apply", "application", "3"]):
#         return (
#             "📥 *MCA Admission*: \n"
#             "- Based on entrance exams like CMAT, NIMCET, or state-level tests\n"
#             "- Admissions open between May–July\n"
#             "- Apply via college website or centralized portals like ACPC"
#         )

#     # Hostel
#     elif any(k in user_input for k in ["hostel", "accommodation", "room", "4"]):
#         return (
#             "🏫 *Hostel Info*: \n"
#             "- Most colleges offer hostels with mess, Wi-Fi, laundry & security\n"
#             "- Charges: ₹30k–₹80k/year (varies)\n"
#             "- Early applications are recommended as seats are limited."
#         )

#     # Syllabus
#     elif any(k in user_input for k in ["syllabus", "subjects", "course content", "5"]):
#         return (
#             "📚 *MCA Syllabus* covers:\n"
#             "- Programming: C/C++, Java, Python\n"
#             "- DBMS, OS, DSA, CN\n"
#             "- Web Dev, Mobile App Dev\n"
#             "- ML, Cloud Computing (in later semesters)"
#         )

#     # Placements
#     elif any(k in user_input for k in ["placement", "job", "companies", "6"]):
#         return (
#             "💼 *MCA Placements*:\n"
#             "- Top recruiters: TCS, Infosys, Wipro, Cognizant, IBM\n"
#             "- Average packages: ₹4LPA – ₹8LPA\n"
#             "- 💡 Build projects + internships for better chances."
#         )

#     # AI/ML Career
#     elif any(k in user_input for k in ["ai", "artificial intelligence", "machine learning", "career", "future", "scope", "7"]):
#         return (
#             "🧠 *AI/ML Career Path*:\n"
#             "- Start with Python, then learn ML libraries (scikit-learn, TensorFlow)\n"
#             "- Work on datasets & real-world projects\n"
#             "- Future is bright in roles like Data Scientist, ML Engineer & AI Developer!"
#         )

#     # Help or Identity
#     elif any(k in user_input for k in ["who are you", "help", "what can you do"]):
#         return (
#             "👋 I'm *NovaBot*, your virtual college assistant!\n"
#             "Ask me about MCA, Admissions, Placements, AI/ML and more.\n"
#             "Type 'Main Menu' 🔁 to explore topics."
#         )

#     # Unknown input
#     else:
#         return (
#             "❓ I didn't understand that.\n"
#             "Please choose from the following:\n"
#             "🎓 MCA | 💸 Fees | 📥 Admission | 🏫 Hostel | 📚 Syllabus | 💼 Placements | 🧠 AI/ML Career\n"
#             "Or type 'Main Menu' to start again 🔁"
#         )

import re
import json
from datetime import datetime

def log_feedback(topic, feedback):
    log_entry = {
        "topic": topic,
        "feedback": feedback,
        "timestamp": datetime.now().isoformat()
    }

    try:
        with open("feedback_log.json", "r+") as f:
            data = json.load(f)
            data.append(log_entry)
            f.seek(0)
            json.dump(data, f, indent=4)
    except FileNotFoundError:
        with open("feedback_log.json", "w") as f:
            json.dump([log_entry], f, indent=4)


def remove_emojis(text):
    return re.sub(r'[^\w\s]', '', text)

def get_bot_response(user_input, context=""):
    user_input = remove_emojis(user_input.lower().strip())

    # Handle follow-ups like "tell me more"
    if user_input in ["tell me more", "more", "next"]:
        if context:
            return get_bot_response(context)  # call again with topic as input
        else:
            return {
                "text": "🧭 Please choose a topic first.",
                "options": ["Main Menu"]
            }
# def get_bot_response(user_input):
#     user_input = user_input.lower().strip()

    # --- Trigger main menu ---
    if user_input in ["menu", "main menu", "go to main menu", "start"]:
        return {
            "text": "📋 Here's what I can help you with:",
            "options": [ "MCA", "Admission", "Fees", "Placement", "AI/ML Career", "Syllabus", "Hostel"]
        }

    # --- Individual topics ---
    if user_input in ["mca", "overview"]:
        return {
            "text": "🎓 **MCA (Master of Computer Applications)** is a 2-year PG program focusing on software dev, AI, cloud, networks, and system design.\n\n✅ Was this helpful? (Yes/No)",
            "topic": "mca"
        }

    if any(k in user_input for k in ["fees", "fee", "cost", "structure"]):
        return{
            "text":'''💸 **MCA Fees**:\n
        - Govt. Colleges: ₹20k–80k/year\n
        - Private: ₹1L–2.5L/year\n
        💡 Tip: Look for scholarships & state quota options.\n
        ✅ Was this helpful? (Yes/No)''',
            "topic": "fees"
        }

    if any(k in user_input for k in ["admission", "apply", "application"]):
        return {
            "text": '''📥 **MCA Admission Process**:\n
        - Via entrance exams (CMAT, NIMCET, ACPC, etc.)\n
        - Applications usually open in May–July.\n
        - Track your target college site for dates.\n
        ✅ Was this helpful? (Yes/No)''',
            "topic": "admission"
        }

    if any(k in user_input for k in ["hostel", "accommodation", "room"]):
        return {
            "text": '''🏫 **Hostel Details**:\n
        - Common amenities: Wi-Fi, mess, security, laundry\n
        - Charges vary ₹30k–80k/year\n
        - Early application is better!\n
        ✅ Was this helpful? (Yes/No)''',
            "topic": "hostel"
        }

    if any(k in user_input for k in ["syllabus", "subjects", "course"]):
        return {
            "text": '''📚 **MCA Syllabus Highlights**:\n
        - Core: DSA, DBMS, OS, CN\n
        - Tech: Python, Web Dev, Java, Android\n
        - Advanced: AI, ML, Cloud (later sem)\n
        ✅ Was this helpful? (Yes/No)''',
            "topic": "hostel"
        }

    if any(k in user_input for k in ["placement", "job", "companies"]):
        return {
            "text": '''💼 **Placements after MCA**:\n
        - Recruiters: Infosys, TCS, Wipro, Cognizant, IBM\n
        - Avg package: ₹4–8 LPA\n
        - Skill + projects + internships = success!\n
        ✅ Was this helpful? (Yes/No)''',
            "topic": "hostel"
        }

    if any(k in user_input for k in ["ai", "artificial intelligence", "machine learning", "career", "future", "scope"]):
        return {
            "text": '''🧠 **AI/ML Career**:\n
        - Start with Python → ML libraries (scikit-learn, \nTensorFlow)\n
        - Build projects on datasets\n
        - Roles: Data Scientist, ML Engineer, AI Developer\n
        ✅ Was this helpful? (Yes/No)''',
            "topic": "hostel"
        }

    # --- If user says Yes after a reply ---
    if user_input in ["yes", "thanks", "thank you", "thankyou", "yes ✅"]:
        log_feedback(topic="last_topic", feedback="yes")  # later we’ll make this dynamic
        return {
            "text": "😊 I'm glad I could help!",
            "options": ["Main Menu"]
        }

    if user_input in ["no", "not really", "nope", "no ❌"]:
        log_feedback(topic="last_topic", feedback="no")
        return {
            "text": "😥 I'm sorry it wasn't helpful. Please choose from the options below:",
            "options": ["Main Menu", "MCA", "Admission", "Fees", "Placement", "AI/ML Career"]
        }


    # --- Bot identity or help ---
    if any(k in user_input for k in ["who are you", "what can you do", "help", "nova", "your name"]):
        return {
            "text": '''👋 I'm **NovaBot**, your friendly virtual college assistant.\n
        You can ask me about:\n
        - MCA course & subjects\n
        - Admission process\n
        - Fees, hostel & placements\n
        - AI/ML career roadmap\n
        Type 'Main Menu' to see all options 🔁'''
        }

    # --- Fallback unknown ---
    return {
        "text": "🤔 I didn’t quite get that. Select a topic below to continue.",
        "options": ["Main Menu", "MCA", "Admission", "Fees", "Placement", "AI/ML Career"]
    }

