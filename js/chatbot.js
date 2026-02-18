// Chatbot functionality
import { GEMINI_API_KEY } from './config.js';

document.addEventListener("DOMContentLoaded", () => {
  const chatMessages = document.querySelector(".chat-messages");
  const chatInput = document.querySelector(".chat-input");
  const chatSend = document.querySelector(".chat-send");
  const themeToggle = document.getElementById("theme-toggle");
  
  // Check for saved user preference and apply theme
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark') {
    document.body.classList.add('dark-mode');
    themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
  }

  // Theme toggle functionality
  themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    
    // Update toggle icon
    if (document.body.classList.contains('dark-mode')) {
      themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
      localStorage.setItem('theme', 'dark');
    } else {
      themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
      localStorage.setItem('theme', 'light');
    }
    
    // Add a little animation to the icon
    themeToggle.querySelector('i').style.animation = 'spin 0.5s ease';
    setTimeout(() => {
      themeToggle.querySelector('i').style.animation = '';
    }, 500);
  });

  // Gemini API configuration (imported from config.js)
  const API_url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${GEMINI_API_KEY}`;

  function smoothScrollToBottom() {
    chatMessages.scrollTo({
      top: chatMessages.scrollHeight,
      behavior: "smooth"
    });
  }
  
  function addUserMessage(message) {
    const messageDiv = document.createElement("div");
    messageDiv.className = "message user-message";
    messageDiv.innerHTML = `
      <div class="message-content">
        <div class="message-text">${message}</div>
      </div>
    `;
    chatMessages.appendChild(messageDiv);
    smoothScrollToBottom();
  }

  let typingIndicatorElement = null;

  function showTypingIndicator() {
    typingIndicatorElement = document.createElement("div");
    typingIndicatorElement.className = "typing-indicator";
    typingIndicatorElement.innerHTML = `
      <div class="typing-avatar">
        <img src="../assets/images/google-gemini-icon.png" alt="Loading..." />
      </div>

    `;
    chatMessages.appendChild(typingIndicatorElement);
    smoothScrollToBottom();
  }

  function hideTypingIndicator() {
    if (typingIndicatorElement) {
      typingIndicatorElement.remove();
      typingIndicatorElement = null;
    }
  }

  async function getBotResponse(userMessage) {
    try {
      const response = await fetch(API_url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          contents: [
            {
              role: "user",
              parts: [
                {
                  text: `You are a helpful career advisor AI assistant named Yuki. Provide professional , friendly and accurate career advice. Keep responses concise, short and practical until the user asks for detailed explaination. User question: ${userMessage}`,
                },
              ],
            },
          ],
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        console.error("API Error:", errorData);
        throw new Error(`API Error: ${errorData.error?.message || "Unknown error occurred"}`);
      }

      const data = await response.json();
      console.log("API Response:", data);
      const rawReply = data.candidates?.[0]?.content?.parts?.[0]?.text || "Sorry, I didn't get that.";

      const cleanedReply = rawReply.replace(/[*-]\s?/g, '').trim();
      return cleanedReply;
    } catch (error) {
      console.error("Error:", error);
      return `Error: ${error.message}. Please try again later or contact support if the issue persists.`;
    }
  }

 // Modify this function in chatbot.js
function typeBotMessage(text) {
  return new Promise((resolve) => {
    const messageDiv = document.createElement("div");
    messageDiv.className = "message bot-message";

    const messageContentDiv = document.createElement("div");
    messageContentDiv.className = "message-content";

    const messageTextDiv = document.createElement("div");
    messageTextDiv.className = "message-text";

    messageContentDiv.appendChild(messageTextDiv);
    messageDiv.appendChild(messageContentDiv);
    chatMessages.appendChild(messageDiv);
    smoothScrollToBottom();

    let index = 0;
    // Remove the isLongText check since we don't want dots animation at all

    function typeNextChar() {
      if (index < text.length) {
        messageTextDiv.textContent += text.charAt(index);
        index++;
        smoothScrollToBottom();

        let typingSpeed = Math.random() * (60 - 20) + 20;

        const currentChar = text.charAt(index - 1);
        if (/[.,!?]/.test(currentChar)) {
          typingSpeed += 100;
        }

        setTimeout(typeNextChar, typingSpeed);
      } else {
        // Simply resolve the promise when typing is complete, no dots animation
        resolve();
      }
    }

    typeNextChar();
  });
}

// You can either remove this function or leave it unused
// function animateDots(messageTextDiv, resolve) {
//   // This function is no longer needed
//   resolve();
// }
  
  // function animateDots(messageTextDiv, resolve) {
  //   let dotText = '';
  //   let count = 0;
  //   const maxDots = 3;
  //   const interval = setInterval(() => {
  //     count = (count + 1) % (maxDots + 1);
  //     dotText = '.'.repeat(count);
  //     messageTextDiv.textContent += dotText;
  //     smoothScrollToBottom();
  
  //     if (count === 0) {
  //       clearInterval(interval);
  //       resolve();
  //     }
  //   }, 400);
  // }
  
  function smoothScrollToBottom() {
    chatMessages.scrollTo({
      top: chatMessages.scrollHeight,
      behavior: "smooth"
    });
  }

  async function handleSendMessage() {
    const message = chatInput.value.trim();
    if (message) {
      addUserMessage(message);
      chatInput.value = "";
  
      // Disable input + show loading spinner
      chatInput.disabled = true;
      chatSend.disabled = true;
      showLoadingSpinner();
  
      showTypingIndicator();
      const botResponse = await getBotResponse(message);
      hideTypingIndicator();
  
      await typeBotMessage(botResponse); // Animate bot typing
  
      // Enable input + restore normal send button
      chatInput.disabled = false;
      chatSend.disabled = false;
      hideLoadingSpinner();
      chatInput.focus();
    }
  }
  
  function showLoadingSpinner() {
    const sendIcon = chatSend.querySelector("i");
    sendIcon.className = ""; // Remove paper-plane icon
    const spinner = document.createElement("div");
    spinner.className = "spinner";
    chatSend.innerHTML = ""; // clear old icon
    chatSend.appendChild(spinner);
  }
  
  function hideLoadingSpinner() {
    chatSend.innerHTML = '<i class="fas fa-paper-plane"></i>'; // Restore paper plane icon
  }
  
  // Add welcome animation when page loads
  setTimeout(() => {
    document.querySelector('.bot-message').style.animation = 'slideIn 0.6s ease forwards';
  }, 300);
  
  chatSend.addEventListener("click", handleSendMessage);

  chatInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      handleSendMessage();
    }
  });
  
  // Add focus to input when page loads
  setTimeout(() => {
    chatInput.focus();
  }, 800);
});