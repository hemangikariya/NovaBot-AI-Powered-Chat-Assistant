# import re
# import json
# from datetime import datetime

# def log_feedback(topic, feedback):
#     log_entry = {
#         "topic": topic,
#         "feedback": feedback,
#         "timestamp": datetime.now().isoformat()
#     }

#     try:
#         with open("feedback_log.json", "r+") as f:
#             data = json.load(f)
#             data.append(log_entry)
#             f.seek(0)
#             json.dump(data, f, indent=4)
#     except FileNotFoundError:
#         with open("feedback_log.json", "w") as f:
#             json.dump([log_entry], f, indent=4)

# def remove_emojis(text):
#     return re.sub(r'[^\w\s]', '', text)

# def get_bot_response(user_input, context=""):
#     user_input = remove_emojis(user_input.lower().strip())

#     if user_input in ["tell me more", "more", "next"]:
#         if context:
#             return get_bot_response(context)  
#         else:
#             return {
#                 "text": "🧭 Please choose a topic first.",
#                 "options": ["Main Menu"]
#             }
            
#     if user_input in ["menu", "main menu", "go to main menu", "start"]:
#         return {
#             "text": "📋 Here's what I can help you with:",
#             "options": [ "MCA", "Admission", "Fees", "Placement", "AI/ML Career", "Syllabus", "Hostel"]
#         }

#     if user_input in ["mca", "overview"]:
#         return {
#             "text": "🎓 **MCA (Master of Computer Applications)** is a 2-year PG program focusing on software dev, AI, cloud, networks, and system design.\n\n✅ Was this helpful? (Yes/No)",
#             "topic": "mca"
#         }

#     if any(k in user_input for k in ["fees", "fee", "cost", "structure"]):
#         return{
#             "text": "💸 **MCA Fees** \n- Govt. Colleges: ₹20k–80k/year\n- Private: ₹1L–2.5L/year\n💡 Tip: Look for scholarships & state quota options.\n\n✅ Was this helpful? (Yes/No)",
#             "topic": "fees"
#         }

#     if any(k in user_input for k in ["admission", "apply", "application"]):
#         return {
#             "text": "📥 **MCA Admission Process**:\n- Via entrance exams (CMAT, NIMCET, ACPC, etc.)\n- Applications usually open in May–July.\n- Track your target college site for dates.\n\n✅ Was this helpful? (Yes/No)",
#             "topic": "admission"
#         }

#     if any(k in user_input for k in ["hostel", "accommodation", "room"]):
#         return {
#             "text": "🏫 **Hostel Details**:\n- Common amenities: Wi-Fi, mess, security, laundry\n- Charges vary ₹30k–80k/year\n- Early application is better!\n\n✅ Was this helpful? (Yes/No)",
#             "topic": "hostel"
#         }

#     if any(k in user_input for k in ["syllabus", "subjects", "course"]):
#         return {
#             "text": "📚 **MCA Syllabus Highlights**:\n- Core: DSA, DBMS, OS, CN\n- Tech: Python, Web Dev, Java, Android\n- Advanced: AI, ML, Cloud (later sem)\n\n✅ Was this helpful? (Yes/No)",
#             "topic": "hostel"
#         }

#     if any(k in user_input for k in ["placement", "job", "companies"]):
#         return {
#             "text": "💼 **Placements after MCA**:\n- Recruiters: Infosys, TCS, Wipro, Cognizant, IBM\n- Avg package: ₹4–8 LPA\n- Skill + projects + internships = success!\n\n✅ Was this helpful? (Yes/No)",
#             "topic": "hostel"
#         }

#     if any(k in user_input for k in ["ai", "artificial intelligence", "machine learning", "career", "future", "scope"]):
#         return {
#             "text": "🧠 **AI/ML Career**: \n- Start with Python → ML libraries (scikit-learn, TensorFlow) \n- Build projects on datasets\n- Roles: Data Scientist, ML Engineer, AI Developer \n\n✅ Was this helpful? (Yes/No)",
#             "topic": "hostel"
#         }

#     if user_input in ["yes", "thanks", "thank you", "thankyou", "yes ✅"]:
#         log_feedback(topic="last_topic", feedback="yes")  
#         return {
#             "text": "😊 I'm glad I could help!",
#             "options": ["Main Menu"]
#         }

#     if user_input in ["no", "not really", "nope", "no ❌"]:
#         log_feedback(topic="last_topic", feedback="no")
#         return {
#             "text": "😥 I'm sorry it wasn't helpful. Please choose from the options below:",
#             "options": ["Main Menu", "MCA", "Admission", "Fees", "Placement", "AI/ML Career"]
#         }

#     if any(k in user_input for k in ["who are you", "what can you do", "help", "nova", "your name"]):
#         return {
#             "text": "👋 I'm **NovaBot**, your friendly virtual college assistant.\nYou can ask me about:\n- MCA course & subjects\n- Admission process\n- Fees, hostel & placements\n- AI/ML career roadmap\nType 'Main Menu' to see all options 🔁"
#         }

#     return {
#         "text": "🤔 I didn’t quite get that. Select a topic below to continue.",
#         "options": ["Main Menu", "MCA", "Admission", "Fees", "Placement", "AI/ML Career"]
#     }

# backend\chatbot_logic.py
import re
import json
from datetime import datetime

# ------------------------------
# Save Feedback
# ------------------------------
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


# ------------------------------
# Remove special characters
# ------------------------------
def remove_emojis(text):
    return re.sub(r'[^\w\s]', '', text)


# ------------------------------
# Main Bot Logic
# ------------------------------
def get_bot_response(user_input, context=""):

    user_input = remove_emojis(user_input.lower().strip())


  # ---- Greeting ----
    if user_input in ["hi","hello","hii","hey","hola"]:
        return {
            "text": "👋 Hello! How can I help you?",
            "options": ["MCA", "Admission", "Fees", "Placement", "AI/ML Career"]
        }
    # ---- CONTEXT continuation ----
    
# ---- CONTEXT continuation ----
    if user_input in ["tell me more", "more", "next"]:
        if context == "mca":
            return {
                "text": "📌 MCA focuses on programming, databases, AI & Cloud.\nWant fees or placement? \nWas this helpful?",
                "topic": "mca",
                "options": ["Fees", "Placement", "Yes", "No", "Main Menu"]
            }

        if context == "fees":
            return {
                "text": "💡 Scholarships available. Govt quota reduces cost. \nWas this helpful?",
                "topic": "fees",
                "options": ["Hostel", "Placement", "Yes", "No", "Main Menu"]
            }

        if context == "admission":
            return {
                "text": "🔥 Tip: entrance score matters for top colleges. \nWas this helpful?",
                "topic": "admission",
                "options": ["Fees", "Placement", "Yes", "No", "Main Menu"]
            }

        if context == "placement":
            return {
                "text": "💼 Internships + projects help placement a LOT. \nWas this helpful?",
                "topic": "placement",
                "options": ["AI/ML Career", "Yes", "No", "Main Menu"]
            }

        if context == "ai":
            return {
                "text": "🧠 Build projects + Kaggle + ML libraries = success \nWas this helpful?",
                "topic": "ai",
                "options": ["Placement", "Yes", "No", "Main Menu"]
            }

        return {
            "text": "🧭 Please choose a topic first.",
            "options": ["Main Menu"]
        }


    # ---- Main Menu ----
    if user_input in ["menu", "main menu", "start"]:
        return {
            "text": "📋 What do you want to know?",
            "options": ["MCA", "Admission", "Fees", "Placement", "AI/ML Career", "Syllabus", "Hostel"]
        }


    # ---- MCA Overview ----
    if any(k in user_input for k in ["mca", "overview"]):
        return {
            "text": "🎓 **MCA (Master of Computer Applications)** is a 2-year PG program focused on software & modern tech.\n\nWant syllabus or placement?",
            "topic": "mca",
            "options": ["Syllabus", "Placement", "Tell me more","Main Menu"]
        }


    if any(k in user_input for k in ["fees", "fee", "cost"]):
        return {
            "text": "💸 **MCA Fees**\nGovt: ₹20k–80k/year\nPrivate: ₹1L–2.5L/year\n\nWant hostel or admission?",
            "topic": "fees",
            "options": ["Hostel", "Admission", "Tell me more","Main Menu"]
        }


    if any(k in user_input for k in ["admission", "apply", "application"]):
        return {
            "text": "📥 **Admission** via entrance (CMAT/NIMCET/ACPC)\nApplications → May–July.",
            "topic": "admission",
            "options": ["Tell me more", "Fees", "Placement","Main Menu"]
        }


    if any(k in user_input for k in ["hostel", "accommodation"]):
        return {
            "text": "🏫 Hostel: Wi-Fi, mess, security. Cost: ₹30k–80k/year.",
            "topic": "hostel",
            "options": ["Fees", "Admission","Main Menu"]
        }


    if any(k in user_input for k in ["syllabus", "subjects"]):
        return {
            "text": "📚 MCA Syllabus includes CS fundamentals + modern areas like AI & Cloud. \nWas this helpful?",
            "topic": "syllabus",
            "options": ["Tell me more", "Yes", "No", "Main Menu"]
        }


    if any(k in user_input for k in ["placement", "job"]):
        return {
            "text": "💼 Recruiters: Infosys, TCS, IBM etc. Avg: ₹4–8 LPA.\nBoost with internships & projects.",
            "topic": "placement",
            "options": ["Tell me more", "AI/ML Career","Main Menu"]
        }


    if any(k in user_input for k in ["ai", "machine learning", "career"]):
        return {
            "text": "🧠 AI/ML Career: Start Python → ML → Projects.\nRoles: ML Engineer, DS, AI Dev",
            "topic": "ai",
            "options": ["Tell me more","Main Menu"]
        }


    # ---- Feedback ----
    if user_input in ["yes", "thanks", "thank you"]:
        log_feedback(context, "yes")
        return {
            "text": "😊 Glad it helped!",
            "options": ["Main Menu"]
        }

    if user_input in ["no", "nope"]:
        log_feedback(context, "no")
        return {
            "text": "😥 I'll improve. Choose next:",
            "options": ["Main Menu"]
        }


    # ---- Who are you? ----
    if any(k in user_input for k in ["who", "help", "nova"]):
        return {
            "text": "👋 I'm NovaBot.\nAsk me about MCA, Fees, Admission, Placement or AI."
        }


    # ---- Default fallback ----
    return {
        "text": "🤔 I didn’t get that. Try one:",
        "options": ["Main Menu", "MCA", "Fees", "Placement"]
    }
