
import React, { useState, useEffect, useRef } from "react";
import "./ChatBot.css";
import ReactMarkdown from "react-markdown";

const ChatBot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const chatContainerRef = useRef(null);

useEffect(() => {
  const timestamp = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  const welcome = "Hi there! 👋 I'm NovaBot.\n\nHere are some things I can help with 👇";

  setMessages([
    {
      sender: "bot",
      text: welcome,
      time: timestamp,
      options: ["MCA", "Admission", "Fees", "Placement", "AI/ML Career", "Syllabus", "Hostel"]
    }
  ]);

  // speak(welcome);
}, []);


  useEffect(() => {
    chatContainerRef.current?.scrollTo({
      top: chatContainerRef.current.scrollHeight,
      behavior: "smooth",
    });
  }, [messages]);

  const [menuOpen, setMenuOpen] = useState(false);
  const toggleMenu = () => {
    setMenuOpen((prev) => !prev);
  };

  const [lastTopic, setLastTopic] = useState("");

  const now = new Date();
  const time = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
const sendMessage = async (text) => {
  if (!text.trim()) return;

  setMessages((prev) => [...prev, { sender: "user", text, time }]);
  setInput("");
  setIsTyping(true);

  try {
    const res = await fetch(process.env.REACT_APP_BACKEND_URL + "/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text, context: lastTopic }),
    });

    const data = await res.json();
    console.log("DATA FULL:", data);
    console.log("BOT OPTIONS:", data.options);

    if (data.topic) setLastTopic(data.topic);

    const delay = Math.floor(Math.random() * 2000) + 1000;

    // 👉 FIRST show bot message after delay
    setTimeout(() => {
       setMessages((prev) => [
    ...prev,
    {
      sender: "bot",
      text: data.response,
      time,
      options: data.options || []
    }
  ]);
      setIsTyping(false);
    }, delay);
  } catch (err) {
    setMessages((prev) => [
      ...prev,
      { sender: "bot", text: "❌ Error connecting to server." }
    ]);
    setIsTyping(false);
  }
};

 const clearChat = () => {
  const timestamp = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  const welcome = "Hi there! 👋 I'm NovaBot.\n\nHere are some things I can help with 👇";

  setMessages([
    {
      sender: "bot",
      text: welcome,
      time: timestamp,
      options: ["MCA", "Admission", "Fees", "Placement", "AI/ML Career", "Syllabus", "Hostel"]
    }
  ]);

  setLastTopic("");
  setMenuOpen(false);
};


  const showHelp = () => {
  const timestamp = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  setMessages((prev) => [
    ...prev,
    {
      sender: "bot",
      time: timestamp,
      text: `### 🤖 How to Use NovaBot

• Select a topic using the buttons  
• Ask follow-up questions using **Tell me more**  
• Click **Yes / No** to give feedback  
• Use **Main Menu** anytime to restart  

💡 Tip: Use buttons instead of typing for best experience.`,
      options: ["Main Menu"]
    }
  ]);

  setMenuOpen(false);
};

  // const speak = (text) => {
  //   const synth = window.speechSynthesis;
  //   const utterance = new SpeechSynthesisUtterance(text);
  //   synth.speak(utterance);
  // };

  return (
    <div className="chatbot-container">
      <div className="chat-window">

        <div className="chat-header">
          <span className="chat-name">NovaBot</span>
          <div className="menu-icon" onClick={toggleMenu}>☰</div>
        </div>

        {menuOpen && (
          <div className="menu-dropdown">
            <div onClick={clearChat}>🧹 Clear Chat</div><hr />
            <div onClick={showHelp}>❓ How to Use NovaBot</div>
          </div>
        )}

        {/* ✅ Scrollable message area */}
        <div className="chat-messages" ref={chatContainerRef}>
          {messages.map((msg, i) => (
            <div key={i} className={`chat-bubble ${msg.sender}`}>

              <div className="markdown-text">
                <ReactMarkdown>{msg.text}</ReactMarkdown>
              </div>

              {/* 👉 options below message */}
              {msg.options && msg.options.length > 0 && (
                <div className="options-wrap">
                  {msg.options.map((opt, idx) => (
                    <button
                      key={idx}
                      className="option-button"
                      onClick={() => sendMessage(opt)}
                    >
                      {opt}
                    </button>
                  ))}
                </div>
              )}

              {msg.time && <div className="chat-time">{msg.time}</div>}
            </div>
          ))}


          {isTyping && (
            <div className="chat-bubble bot">
              <div className="typing-dots">
                <span>.</span><span>.</span><span>.</span>
              </div>
            </div>
          )}
        </div>

        {/* ✅ Fixed input at bottom */}
        <div className="input-area">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage(input)}
            placeholder="Type a message..."
          />
          <button onClick={() => sendMessage(input)}>Send</button>
        </div>

      </div>
    </div>

  );
};

export default ChatBot;