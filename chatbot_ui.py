import streamlit as st
from crypto_data import get_crypto_price, get_historical_price  # Import CoinGecko functions
from designs import apply_glitch_title, apply_status_bar, load_custom_fonts, glassmorphic_chat, style_chat_bubbles, style_input_box, futuristic_buttons
st.set_page_config(page_title="CryptoBot 💬", layout="centered")
from digital_clock import show_live_clock
show_live_clock()
glassmorphic_chat()
futuristic_buttons()
load_custom_fonts()
style_chat_bubbles()
style_input_box()

import google.generativeai as genai
import json
import re
import random
from rapidfuzz import fuzz

def get_fallback_crypto_response():
    return random.choice([
        "I couldn’t quite catch which coin you're referring to 🧐. Could you rephrase that?",
        "Hmm, I didn’t find the coin. Maybe try saying something like 'price of Ethereum'?",
        "Oops! Can you let me know the coin name again?",
    ])

def extract_time_range(user_input):
    if "7 day" in user_input or "week" in user_input:
        return 7
    elif "30 day" in user_input or "month" in user_input:
        return 30
    elif "90 day" in user_input or "3 month" in user_input:
        return 90
    elif "year" in user_input or "365 day" in user_input:
        return 365
    else:
        return 10  # default to last 10 days

def extract_coin_name(text):
    coins = {
        "bitcoin": "bitcoin",
        "btc": "bitcoin",
        "ethereum": "ethereum",
        "eth": "ethereum",
        "dogecoin": "dogecoin",
        "doge": "dogecoin",
        "sol": "solana",
        "solana": "solana",
        # Add more here
    }

    text = text.lower()
    for keyword, coin in coins.items():
        if keyword in text:
            return coin
    return None


def get_last_n_turns(history, n=2):
    """Return the last n user+bot turns (up to 4 messages total if n=2)."""
    return history[-2*n:] if len(history) >= 2*n else history

# Normalize function
def normalize(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

# Find best cached match
def find_best_cached_match(user_input, cache_keys, threshold=85):
    norm_input = normalize(user_input)
    for q in cache_keys:
        norm_q = normalize(q)
        if fuzz.ratio(norm_input, norm_q) >= threshold:
            return q  # Return the original cached key
    return None

btc_price = random.randint(30000, 70000)
eth_price = random.randint(1000, 5000)
doge_price = round(random.uniform(0.05, 0.1), 3)
xrp_price = round(random.uniform(0.4, 0.7), 2)
ada_price = round(random.uniform(0.3, 0.6), 2)

def crypto_ticker():
    ticker_html = f"""
    <marquee behavior="scroll" direction="left" scrollamount="5" style="color:yellow; font-weight:bold; background:#0d1117; padding:6px; border-radius:5px;">
    🚀 BTC: ${btc_price:,} | ETH: ${eth_price:,} | DOGE: ${doge_price} | ADA: ${ada_price} | XRP: ${xrp_price} 💹 Stay sharp, crypto ninja!
    </marquee>
    """
    st.markdown(ticker_html, unsafe_allow_html=True)

def has_exact_word(words, text):
    text = re.sub(r'\s+', ' ', text.lower().strip())
    return any(re.search(rf"\b{re.escape(word)}\b", text) for word in words)

# ✅ Configure Gemini
genai.configure(api_key="")  # Replace with your Gemini API key
model = genai.GenerativeModel("gemini-2.5-flash")

# ✅ Allowed greetings/meta prompts
greeting_keywords = ["hello", "hola", "hi", "hey", "good morning", "good evening", "good night", "thanks", "thank you", "bye", "goodbye"]
meta_prompts = ["who is your owner", "who created you", "who made you", "what are you", "are you an ai", "who built you"]

# ✅ Load cache
try:
    with open("cache.json", "r") as f:
        question_cache = json.load(f)
except FileNotFoundError:
    question_cache = {}

# View cached Q&A in sidebar
with st.sidebar:
    st.markdown("### 📂 View Cached Questions")

    if "show_cache" not in st.session_state:
        st.session_state.show_cache = False

    if st.button("🧠 Toggle Cache"):
        st.session_state.show_cache = not st.session_state.show_cache

    if st.session_state.show_cache:
        if question_cache:
            st.markdown(f"🧠 **Total Cached Questions:** {len(question_cache)}")
            for q, a in question_cache.items():
                st.markdown(f"**Q:** {q}")
                st.markdown(f"**A:** {a}")
                st.markdown("---")
        else:
            st.info("No cached questions yet.")

    st.markdown("---")

    if st.button("🧹 Clear Cache"):
        question_cache.clear()
        with open("cache.json", "w") as f:
            json.dump(question_cache, f)
        st.success("Cache cleared!")

    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    with st.expander("📈 Live Prices (Simulated)", expanded=True):
        st.metric("Bitcoin (BTC)", f"${btc_price:,}")
        st.metric("Ethereum (ETH)", f"${eth_price:,}")
        st.metric("Dogecoin (DOGE)", f"${doge_price}")
        st.metric("Ripple (XRP)", f"${xrp_price}")
        st.metric("Cardano (ADA)", f"${ada_price}")

    with st.expander("ℹ️ About CryptoBot"):
        st.markdown(""" 
        **CryptoBot 🤖** is a Gemini-powered assistant designed to answer questions related to:
        - 🪙 Cryptocurrency
        - 📈 Trading strategies
        - 🧱 Blockchain tech
        - 💹 Market trends
        - 📰 Financial news
        Created with 💡 using Streamlit + Gemini API
        Developed by Aditya Raj
        """)

# ✅ System instruction
system_instruction = "answer questions about crypto, trading, or blockchain. Politely refuse unrelated topics."

# ✅ Streamlit UI setup
apply_glitch_title()
crypto_ticker()  # 🟡 Add this line
st.caption("Ask me anything about cryptocurrency!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Type your question here...")

if user_input:
    normalized_input = user_input.strip().lower()
    st.session_state.chat_history.append({"role": "user", "text": user_input})

    if user_input.lower() == "exit":
        with open("cache.json", "w") as f:
            json.dump(question_cache, f)
        st.session_state.chat_history.append({"role": "bot", "text": "Hoping your doubts are solved. Goodbye 👋"})

    elif len(normalized_input) < 3:
        st.session_state.chat_history.append({"role": "bot", "text": "🤖 I couldn’t understand that. Please ask a valid question."})

    else:
        best_match = find_best_cached_match(user_input, question_cache.keys())

        if best_match:
            answer = question_cache[best_match]
            st.session_state.chat_history.append({"role": "bot", "text": answer})
        else:
            try:
                short_context = get_last_n_turns(st.session_state.chat_history, n=2)
                context_prompt = "\n".join([f"{msg['role'].capitalize()}: {msg['text']}" for msg in short_context])
                context_prompt += f"\nUser: {user_input}\nAssistant:"
            
                normalized_input = user_input.lower().strip()
            
                # Special case: Price questions
                if "price" in normalized_input:
                    coin_name = extract_coin_name(normalized_input)
                    if coin_name:
                        price = get_crypto_price(coin_name)
                        answer = f"The current price of {coin_name.capitalize()} is ${price:,.2f}."
                    else:
                        answer = get_fallback_crypto_response()
            
                # Special case: Chart questions
                elif "chart" in normalized_input or "graph" in normalized_input:
                    coin_name = extract_coin_name(normalized_input)
                    days = extract_time_range(normalized_input)
                    if coin_name:
                        historical_data = get_historical_price(coin_name, days=days)
                        if not historical_data.empty:
                            st.line_chart(historical_data.set_index('Date')['Price'])
                            answer = f"Here's the price chart for {coin_name.capitalize()} over the last {days} days 📈"
                        else:
                            answer = f"Sorry, I couldn't retrieve chart data for {coin_name.capitalize()}."
                    else:
                        answer = get_fallback_crypto_response()
            
                # General questions go to Gemini
                else:
                    response = model.generate_content([system_instruction, context_prompt])
                    answer = response.text
            
                # Cache the answer
                question_cache[normalized_input] = answer
                with open("cache.json", "w") as f:
                    json.dump(question_cache, f)
            
            except Exception as e:
                answer = f"Error processing request: {e}"
            
            # Add to chat history
            st.session_state.chat_history.append({"role": "bot", "text": answer})


    for msg in st.session_state.chat_history:
        st.chat_message(msg["role"]).markdown(msg["text"])

st.markdown("""
<hr style="margin-top: 50px;">
<div style='text-align: center; font-size: 14px; color: gray;'>
    🤖 Made with ❤️ by <strong><a href="https://github.com/Raj-3435" target="_blank">Aditya Raj</a></strong>  
</div>

""", unsafe_allow_html=True)
