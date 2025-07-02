// export default ChatBot;
// import React, { useState, useEffect, useRef } from "react";
// import "./ChatBot.css";

// const ChatBot = () => {
//   const [messages, setMessages] = useState([]);
//   const [input, setInput] = useState("");
//   const [isTyping, setIsTyping] = useState(false);
//   const chatContainerRef = useRef(null);

//   useEffect(() => {
//     const welcome = "Hi there! 👋 I'm NovaBot. How can I assist you today?";
//     setMessages([{ sender: "bot", text: welcome }]);
//     speak(welcome);
//   }, []);

//   useEffect(() => {
//     chatContainerRef.current?.scrollTo({
//       top: chatContainerRef.current.scrollHeight,
//       behavior: "smooth",
//     });
//   }, [messages]);

//   const sendMessage = async (text) => {
//     if (!text.trim()) return;

//     const userMsg = { sender: "user", text };
//     setMessages((prev) => [...prev, userMsg]);
//     setInput("");
//     setIsTyping(true);

//     try {
//       const res = await fetch("http://localhost:5000/chat", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ message: text }),
//       });

//       const data = await res.json();

//       const botReply = typeof data.response === "string" ? data.response : "";
//       const delay = Math.floor(Math.random() * 2000) + 2000;

//       setTimeout(() => {
//         setMessages((prev) => [...prev, { sender: "bot", text: botReply }]);

//         speak(botReply);
//         setIsTyping(false);

//         const lower = botReply.toLowerCase();

//         // Show options menu if relevant
//         if (
//           lower.includes("here's what i can help") ||
//           lower.includes("please choose") ||
//           lower.includes("main menu")
//         ) {
//           setMessages((prev) => [
//             ...prev,
//             {
//               sender: "bot-options",
//               options: [
//                 "MCA",
//                 "Fees",
//                 "Admission",
//                 "Hostel",
//                 "Syllabus",
//                 "Placement",
//                 "AI/ML Career",
//                 "Main Menu",
//               ],
//             },
//           ]);
//         } else {
//           // Show satisfaction buttons after every bot response
//           setMessages((prev) => [
//             ...prev,
//             {
//               sender: "bot-options",
//               options: ["Yes ✅", "No ❌"],
//               feedback: true,
//             },
//           ]);
//         }
//       }, delay);
//     } catch (err) {
//       setMessages((prev) => [
//         ...prev,
//         { sender: "bot", text: "❌ Error connecting to server." },
//       ]);
//       setIsTyping(false);
//     }
//   };

//   const handleVoiceInput = () => {
//     const recognition = new (window.SpeechRecognition ||
//       window.webkitSpeechRecognition)();
//     recognition.lang = "en-US";
//     recognition.onresult = (e) => sendMessage(e.results[0][0].transcript);
//     recognition.start();
//   };

//   const speak = (text) => {
//     const synth = window.speechSynthesis;
//     const utterance = new SpeechSynthesisUtterance(text);
//     synth.speak(utterance);
//   };

//   const handleOptionClick = (option) => {
//     if (option.toLowerCase().includes("yes")) {
//       setMessages((prev) => [
//         ...prev,
//         { sender: "user", text: option },
//         { sender: "bot", text: "✅ Great! Let me know if you need anything else." },
//       ]);
//     } else if (option.toLowerCase().includes("no")) {
//       setMessages((prev) => [
//         ...prev,
//         { sender: "user", text: option },
//         {
//           sender: "bot",
//           text: "😥 I'm sorry it wasn't helpful. Try rephrasing or type 'Main Menu'",
//         },
//         {
//           sender: "bot-options",
//           options: [
//             "MCA",
//             "Fees",
//             "Admission",
//             "Hostel",
//             "Syllabus",
//             "Placement",
//             "AI/ML Career",
//             "Main Menu",
//           ],
//         },
//       ]);
//     } else {
//       sendMessage(option);
//     }
//   };

//   return (
//     <div className="chatbot-container">
//       <h2>NovaBot 🤖</h2>

//       <div className="chat-window" ref={chatContainerRef}>
//         {messages.map((msg, i) => {
//           if (msg.sender === "bot-options") {
//             return (
//               <div key={i} className="chat-bubble bot">
//                 <div className="options-wrap">
//                   {msg.options.map((opt, idx) => (
//                     <button
//                       key={idx}
//                       className="option-button"
//                       onClick={() => handleOptionClick(opt)}
//                     >
//                       {opt}
//                     </button>
//                   ))}
//                 </div>
//               </div>
//             );
//           }

//           return (
//             <div key={i} className={`chat-bubble ${msg.sender}`}>
//               <span>{msg.text}</span>
//             </div>
//           );
//         })}

//         {isTyping && (
//           <div className="chat-bubble bot">
//             <div className="typing-dots">
//               <span>.</span>
//               <span>.</span>
//               <span>.</span>
//             </div>
//           </div>
//         )}
//       </div>

//       <div className="input-area">
//         <input
//           value={input}
//           onChange={(e) => setInput(e.target.value)}
//           onKeyDown={(e) => e.key === "Enter" && sendMessage(input)}
//           placeholder="Type a message..."
//         />
//         <button onClick={() => sendMessage(input)}>Send</button>
//         <button onClick={handleVoiceInput}>🎤</button>
//       </div>
//     </div>
//   );
// };

// export default ChatBot;



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

    // const userMsg = { sender: "user", text };
    setMessages((prev) => [...prev, { sender: "user", text, time }]);
    setInput("");
    setIsTyping(true);

    try {
      const res = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text, context: lastTopic }),
      });

      const data = await res.json();
      // const botReply = data.response;
      // const botOptions = data.options || [];

      // 🧠 Save context if available
      if (data.topic) {
        setLastTopic(data.topic);
      }

      const delay = Math.floor(Math.random() * 2000) + 2000;
      setTimeout(() => {
        const botReply = data.response;
        const botOptions = data.options || [];
        const botMsg = { sender: "bot", text: botReply, time };
        setMessages((prev) => [...prev, botMsg]);
        // speak(botReply);

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