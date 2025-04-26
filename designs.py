# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 21:09:27 2025

@author: Aditya Raj
"""

# designs.py

import streamlit as st

def apply_glitch_title():
    st.markdown("""
    <style>
    .glitch {
      color: #58a6ff;
      font-size: 2.5rem;
      font-weight: bold;
      position: relative;
      font-family: monospace;
      text-shadow: 0 0 5px #58a6ff, 0 0 10px #58a6ff;
      animation: flicker 2s infinite alternate;
    }

    .glitch::before,
    .glitch::after {
      content: attr(data-text);
      position: absolute;
      left: 0;
      width: 100%;
      overflow: hidden;
      color: #ff7b72;
      animation: glitch 2s infinite linear;
    }

    .glitch::after {
      color: #00ff9f;
      animation-delay: 1s;
    }

    @keyframes flicker {
      0% { opacity: 1; }
      50% { opacity: 0.85; }
      100% { opacity: 1; }
    }

    @keyframes glitch {
      0% { clip-path: inset(0 0 90% 0); }
      10% { clip-path: inset(10% 0 85% 0); }
      20% { clip-path: inset(15% 0 60% 0); }
      30% { clip-path: inset(50% 0 40% 0); }
      40% { clip-path: inset(80% 0 5% 0); }
      50% { clip-path: inset(10% 0 85% 0); }
      60% { clip-path: inset(40% 0 45% 0); }
      70% { clip-path: inset(70% 0 20% 0); }
      80% { clip-path: inset(20% 0 70% 0); }
      90% { clip-path: inset(90% 0 0 0); }
      100% { clip-path: inset(0 0 90% 0); }
    }
    </style>

    <h1 class="glitch" data-text="🤖 CryptoBot">🤖 CryptoBot</h1>
    """, unsafe_allow_html=True)
    

def apply_status_bar():
    st.markdown("""
        <hr style="border: 0.5px solid #30363d;" />
        <p style="font-family:monospace; color:#8b949e; font-size:12px;">
        🔐 Securely querying <strong>Gemini 1.5 Flash</strong> |
        ⛓️ <strong>Blockchain Only Mode</strong> Enabled |
        🧠 <strong>Cache</strong> Active
        </p>
    """, unsafe_allow_html=True)

def glassmorphic_chat():
    st.markdown(
        """
        <style>
        .stChatMessage {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(8px);
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
            color: #00ffff;
            border: 1px solid rgba(0, 255, 255, 0.3);
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_chat_bubbles():
    st.markdown(
        """
        <style>
        .stChatMessage {
            background: rgba(0, 255, 204, 0.1);
            border-left: 4px solid #00ffcc;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
def style_input_box():
    st.markdown(
        """
        <style>
        textarea {
            border: 2px solid #00ffc8 !important;
            border-radius: 12px !important;
            background-color: #0d0d0d !important;
            color: #00ffc8 !important;
            box-shadow: 0 0 8px #00ffc8;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def glowing_input_box():
    st.markdown(
        """
        <style>
        .stTextInput>div>div>input {
            border: 2px solid #0ff;
            background-color: #000;
            color: #0ff;
            box-shadow: 0 0 8px #0ff;
            font-family: 'Fira Code', monospace;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def futuristic_buttons():
    st.markdown(
        """
        <style>
        button {
            background-color: #111 !important;
            color: #0ff !important;
            border: 1px solid #0ff !important;
            border-radius: 8px;
            transition: 0.3s ease-in-out;
        }

        button:hover {
            background-color: #0ff !important;
            color: #111 !important;
            transform: scale(1.05);
            box-shadow: 0 0 15px #0ff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    
def load_custom_fonts():
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">
        """,
        unsafe_allow_html=True
    )

def digital_clock():
    st.markdown(
        """
        <style>
        #clock {
            position: fixed;
            top: 10px;
            right: 20px;
            font-size: 18px;
            font-family: 'Courier New', monospace;
            color: #00ffff;
            background-color: rgba(0, 0, 0, 0.6);
            padding: 5px 10px;
            border-radius: 5px;
            z-index: 9999;
        }
        </style>
        <div id="clock"></div>

        <script>
        const clock = document.getElementById("clock");
        setInterval(() => {
            const now = new Date();
            clock.innerHTML = now.toLocaleTimeString();
        }, 1000);
        </script>
        """,
        unsafe_allow_html=True
    )
