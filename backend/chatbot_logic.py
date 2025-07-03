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

    if user_input in ["tell me more", "more", "next"]:
        if context:
            return get_bot_response(context)  
        else:
            return {
                "text": "🧭 Please choose a topic first.",
                "options": ["Main Menu"]
            }
            
    if user_input in ["menu", "main menu", "go to main menu", "start"]:
        return {
            "text": "📋 Here's what I can help you with:",
            "options": [ "MCA", "Admission", "Fees", "Placement", "AI/ML Career", "Syllabus", "Hostel"]
        }

    if user_input in ["mca", "overview"]:
        return {
            "text": "🎓 **MCA (Master of Computer Applications)** is a 2-year PG program focusing on software dev, AI, cloud, networks, and system design.\n✅ Was this helpful? (Yes/No)",
            "topic": "mca"
        }

    if any(k in user_input for k in ["fees", "fee", "cost", "structure"]):
        return {
            "text": "💸 **MCA Fees**\n\n- Govt. Colleges: ₹20k–80k/year\n- Private: ₹1L–2.5L/year\n💡 Tip: Look for scholarships & state quota options.\n✅ Was this helpful? (Yes/No)",
            "topic": "fees"
        }


    if any(k in user_input for k in ["admission", "apply", "application"]):
        return {
            "text": "📥 **MCA Admission Process**:\n- Via entrance exams (CMAT, NIMCET, ACPC, etc.)\n- Applications usually open in May–July.\n- Track your target college site for dates.\n✅ Was this helpful? (Yes/No)",
            "topic": "admission"
        }

    if any(k in user_input for k in ["hostel", "accommodation", "room"]):
        return {
            "text": "🏫 **Hostel Details**:\n- Common amenities: Wi-Fi, mess, security, laundry\n- Charges vary ₹30k–80k/year\n- Early application is better!\n✅ Was this helpful? (Yes/No)",
            "topic": "hostel"
        }

    if any(k in user_input for k in ["syllabus", "subjects", "course"]):
        return {
            "text": "📚 **MCA Syllabus Highlights**:\n- Core: DSA, DBMS, OS, CN\n- Tech: Python, Web Dev, Java, Android\n- Advanced: AI, ML, Cloud (later sem)\n✅ Was this helpful? (Yes/No)",
            "topic": "hostel"
        }

    if any(k in user_input for k in ["placement", "job", "companies"]):
        return {
            "text": "💼 **Placements after MCA**:\n- Recruiters: Infosys, TCS, Wipro, Cognizant, IBM\n- Avg package: ₹4–8 LPA\n- Skill + projects + internships = success!\n✅ Was this helpful? (Yes/No)",
            "topic": "hostel"
        }

    if user_input in ["ai", "artificial intelligence", "machine learning", "career", "future", "scope"]:
        return {
            "text": "🧠 **AI/ML Career** \n- Start with Python → ML libraries (scikit-learn, TensorFlow) \n- Build projects on datasets\n- Roles: Data Scientist, ML Engineer, AI Developer \n✅ Was this helpful? (Yes/No)",
            "topic": "hostel"
        }

    if user_input in ["yes", "thanks", "thank you", "thankyou", "yes ✅"]:
        log_feedback(topic="last_topic", feedback="yes")  
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

    if any(k in user_input for k in ["who are you", "what can you do", "help", "nova", "your name"]):
        return {
            "text": "👋 I'm **NovaBot**, your friendly virtual college assistant.\nYou can ask me about:\n- MCA course & subjects\n- Admission process\n- Fees, hostel & placements\n- AI/ML career roadmap\nType 'Main Menu' to see all options 🔁"
        }

    return {
        "text": "🤔 I didn’t quite get that. Select a topic below to continue.",
        "options": ["Main Menu", "MCA", "Admission", "Fees", "Placement", "AI/ML Career"]
    }
