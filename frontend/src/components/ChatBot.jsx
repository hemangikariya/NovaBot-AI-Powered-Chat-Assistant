import React, { useState, useEffect, useRef } from "react";
import "./ChatBot.css";
import ReactMarkdown from "react-markdown";

const ChatBot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const chatContainerRef = useRef(null);

  useEffect(() => {
    const welcome = "Hi there! 👋 I'm NovaBot. How can I assist you today?";
    const timestamp = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    setMessages([{ sender: "bot", text: welcome, time: timestamp }]);
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
      const res = await fetch("${process.env.REACT_APP_BACKEND_URL}/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text, context: lastTopic }),
      });

      const data = await res.json();

      if (data.topic) {
        setLastTopic(data.topic);
      }

      const delay = Math.floor(Math.random() * 2000) + 2000;
      setTimeout(() => {
        const botReply = data.response;
        const botOptions = data.options || [];
        const botMsg = { sender: "bot", text: botReply, time };
        setMessages((prev) => [...prev, botMsg]);

        if (botOptions.length > 0) {
          setMessages((prev) => [
            ...prev,
            {
              sender: "bot-options",
              options: botOptions,
            },
          ]);
        }

        setIsTyping(false);
      }, delay);

    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "❌ Error connecting to server." },
      ]);
      setIsTyping(false);
    }
  };

  return (
    <div className="chatbot-container">
      <div className="chat-window">

        <div className="chat-header">
          <span className="chat-name">NovaBot</span>
          <div className="menu-icon" onClick={toggleMenu}>☰</div>
        </div>

        {menuOpen && (
          <div className="menu-dropdown">
            <div>✏️ Change Name</div>
            <div>📧 Email transcript</div>
            <div>🔊 Sound On</div>
            <div>🔲 Pop out widget</div>
            <div>🔗 Add Chat to your website</div>
          </div>
        )}

        {/* ✅ Scrollable message area */}
        <div className="chat-messages" ref={chatContainerRef}>
          {messages.map((msg, i) => {
            if (msg.sender === "bot-options") {
              return (
                <div key={i} className="chat-bubble bot">
                  <div className="options-wrap">
                    {msg.options.map((opt, idx) => (
                      <button key={idx} className="option-button" onClick={() => sendMessage(opt)}>
                        {opt}
                      </button>
                    ))}
                  </div>
                </div>
              );
            }

            return (
              <div key={i} className={`chat-bubble ${msg.sender}`}>
                <div className="markdown-text">
                  <ReactMarkdown>{msg.text}</ReactMarkdown>
                </div>
                {msg.time && <div className="chat-time">{msg.time}</div>}
              </div>
            );
          })}

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
