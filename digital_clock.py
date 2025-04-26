# # import streamlit as st
# # from datetime import datetime

# import streamlit as st
# from datetime import datetime

# def render_clock():
#     now = datetime.now().strftime("%H:%M:%S")
#     st.markdown(
#         f"""
#         <div style="position: fixed;
#                     top: 100px; right: 20px;
#                     background: rgba(0, 0, 0, 0.7);
#                     color: #00ffcc;
#                     font-family: 'Orbitron', sans-serif;
#                     font-size: 20px;
#                     padding: 10px 20px;
#                     border-radius: 12px;
#                     z-index: 9999;
#                     border: 1px solid #00ffff;
#                     box-shadow: 0 0 10px #00ffff;">
#              🕒{now}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )


# import streamlit as st
# from datetime import datetime

# def render_clock():
#     now = datetime.now().strftime("%H:%M:%S")
#     st.markdown(
#         f"""
#         <div style="
    
#             background: rgba(0, 0, 0, 0.85);
#             color: #00ffe7;
#             font-family: 'Orbitron', sans-serif;
#             font-size: 20px;
#             padding: 12px;
#             text-align: center;
#             width: 100%;
#             border-bottom: 2px solid #00ffff;
#             box-shadow: 0 0 10px #00ffff;
#             margin-bottom: 20px;
#         ">
#             ⏰ Current Time: {now}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

import streamlit.components.v1 as components

def show_live_clock():
    components.html(
        """
        <div id="clock" style="
                                top: 100px; right: 20px;
                                background: rgba(0, 0, 0, 0.7);
                                width: fit-content;
                                color: #00ffcc;
                                font-family: 'Orbitron', sans-serif;
                                font-size: 20px;
                                padding: 10px;
                                border-radius: 12px;
                                z-index: 9999;
                                border: 1px solid #00ffff;
                                box-shadow: 0 0 10px #00ffff;"></div>

        <script>
        function updateClock() {
            const now = new Date();
            const time = now.toLocaleTimeString();
            document.getElementById('clock').textContent = time;
        }
        setInterval(updateClock, 1000);
        updateClock();
        </script>
        """,
        height=60,
    )
