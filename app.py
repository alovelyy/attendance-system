def render_login():
    st.markdown("""
    <style>
        /* Hide Streamlit UI */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp {margin: 0; padding: 0; background: #0a0e1a;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        .stApp > div:first-child {padding: 0 !important;}
        .st-emotion-cache-1r6slb0 {padding: 0 !important;}
        .st-emotion-cache-1gv3huu {padding: 0 !important;}
        body {background: #0a0e1a; margin: 0; overflow: hidden; height: 100vh; width: 100vw;}
        
        /* ---- BACKGROUND: nebula + particles ---- */
        #nebula {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            z-index: 0;
            background: radial-gradient(ellipse at 20% 30%, #1a2a4a, #070b12 80%);
            overflow: hidden;
        }
        .nebula-blob {
            position: absolute;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.3;
            animation: floatBlob 20s infinite alternate ease-in-out;
        }
        .nebula-blob:nth-child(1) { width: 500px; height: 500px; top: -10%; left: -10%; background: #f0c040; }
        .nebula-blob:nth-child(2) { width: 400px; height: 400px; bottom: -10%; right: -10%; background: #4a6a9a; animation-delay: 5s; }
        @keyframes floatBlob {
            0% { transform: translate(0, 0) scale(1); }
            100% { transform: translate(50px, 30px) scale(1.1); }
        }
        .particle {
            position: absolute;
            width: 3px; height: 3px;
            background: rgba(255,255,255,0.5);
            border-radius: 50%;
            animation: twinkle 4s infinite alternate;
        }
        @keyframes twinkle {
            0% { opacity: 0.1; transform: scale(0.8); }
            100% { opacity: 0.8; transform: scale(1.2); }
        }
        
        /* ---- FLEX CONTAINER for all content ---- */
        .login-container {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 5;
            pointer-events: none; /* allow clicks on inputs/buttons inside children */
        }
        .login-container > * { pointer-events: auto; }
        
        /* Top section: DPSR + title */
        .top-section {
            flex: 1 1 60%;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            align-items: center;
            text-align: center;
            padding-bottom: 20px;
            width: 100%;
        }
        .dpsr-letters {
            font-size: clamp(50px, 10vw, 90px);
            font-weight: 900;
            color: #f0c040;
            text-shadow: 0 0 60px rgba(240,192,64,0.6), 0 0 120px rgba(240,192,64,0.3);
            letter-spacing: 0.2em;
            font-family: 'Impact', 'Arial Black', sans-serif;
            opacity: 0;
            animation: dpsrAppear 2s ease-out forwards;
            animation-delay: 0.3s;
        }
        .dpsr-letters span {
            display: inline-block;
            opacity: 0;
            animation: letterSlide 1.8s ease-out forwards;
        }
        .dpsr-letters span:nth-child(1) { animation-delay: 0.2s; transform: translateX(-300px) rotate(-25deg); }
        .dpsr-letters span:nth-child(2) { animation-delay: 0.5s; transform: translateX(-200px) rotate(25deg); }
        .dpsr-letters span:nth-child(3) { animation-delay: 0.8s; transform: translateX(200px) rotate(-20deg); }
        .dpsr-letters span:nth-child(4) { animation-delay: 1.1s; transform: translateX(300px) rotate(20deg); }
        @keyframes letterSlide {
            0% { opacity: 0; transform: translateX(var(--tx)) rotate(var(--rot)); }
            100% { opacity: 1; transform: translateX(0) rotate(0deg); }
        }
        .dpsr-letters span:nth-child(1) { --tx: -300px; --rot: -25deg; }
        .dpsr-letters span:nth-child(2) { --tx: -200px; --rot: 25deg; }
        .dpsr-letters span:nth-child(3) { --tx: 200px; --rot: -20deg; }
        .dpsr-letters span:nth-child(4) { --tx: 300px; --rot: 20deg; }
        @keyframes dpsrAppear {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        .company-title {
            font-size: clamp(28px, 5vw, 56px);
            font-weight: 900;
            background: linear-gradient(90deg, #f0c040, #ffd700, #f0c040);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 40px rgba(240,192,64,0.2);
            letter-spacing: 0.1em;
            font-family: 'Impact', 'Arial Black', sans-serif;
            opacity: 0;
            animation: fadeUp 1.2s ease-out forwards;
            animation-delay: 2.8s;
            margin-top: 6px;
        }
        .company-sub {
            font-size: clamp(12px, 1.6vw, 18px);
            color: rgba(255,255,255,0.3);
            letter-spacing: 0.5em;
            font-weight: 300;
            opacity: 0;
            animation: fadeUp 1s ease-out forwards;
            animation-delay: 3.2s;
            margin-top: 4px;
        }
        .title-divider {
            width: 140px; height: 2px;
            background: linear-gradient(90deg, transparent, #f0c040, transparent);
            margin: 10px auto 0;
            opacity: 0;
            animation: fadeUp 1s ease-out forwards;
            animation-delay: 3.4s;
        }
        @keyframes fadeUp {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        
        /* Bottom section: login card */
        .bottom-section {
            flex: 1 1 40%;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: center;
            width: 100%;
            padding-top: 20px;
        }
        .login-wrapper {
            width: 90%;
            max-width: 420px;
            opacity: 0;
            animation: cardRise 1.4s ease-out forwards;
            animation-delay: 4.0s;
        }
        @keyframes cardRise {
            0% { opacity: 0; transform: translateY(30px) scale(0.95); }
            100% { opacity: 1; transform: translateY(0) scale(1); }
        }
        .login-card {
            padding: 35px 30px 30px;
            background: rgba(20, 30, 50, 0.5);
            backdrop-filter: blur(18px);
            border: 1px solid rgba(255,215,0,0.15);
            border-radius: 30px;
            box-shadow: 0 30px 80px rgba(0,0,0,0.7), 0 0 30px rgba(240,192,64,0.05);
            position: relative;
            overflow: hidden;
        }
        .login-card::before {
            content: '';
            position: absolute;
            top: -50%; left: -50%;
            width: 200%; height: 200%;
            background: conic-gradient(from 0deg, transparent, rgba(240,192,64,0.03), transparent 60%);
            animation: spinGlow 10s linear infinite;
        }
        @keyframes spinGlow {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .login-card h2 {
            color: #fff;
            font-weight: 300;
            letter-spacing: 1px;
            margin-bottom: 4px;
            font-size: 24px;
            position: relative;
            z-index: 1;
        }
        .login-card h2 span { color: #f0c040; font-weight: 700; }
        .login-card .sub {
            color: rgba(255,255,255,0.2);
            font-size: 13px;
            margin-bottom: 25px;
            letter-spacing: 6px;
            position: relative;
            z-index: 1;
        }
        .car-icon {
            font-size: 32px;
            display: block;
            margin-bottom: 6px;
            position: relative;
            z-index: 1;
        }
        /* Streamlit inputs override (keep consistent) */
        .stTextInput > div > div > input {
            background: rgba(255,255,255,0.06) !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 50px !important;
            color: #fff !important;
            padding: 14px 20px !important;
            font-size: 16px !important;
            width: 100% !important;
            transition: all 0.3s !important;
            position: relative;
            z-index: 1;
        }
        .stTextInput > div > div > input:focus {
            border-color: #f0c040 !important;
            box-shadow: 0 0 25px rgba(240,192,64,0.15) !important;
        }
        .stButton > button {
            width: 100% !important;
            background: linear-gradient(135deg, #f0c040, #d4a020) !important;
            border: none !important;
            border-radius: 50px !important;
            color: #0b0e17 !important;
            font-size: 18px !important;
            font-weight: 700 !important;
            padding: 14px !important;
            margin-top: 18px !important;
            box-shadow: 0 8px 30px rgba(240,192,64,0.25) !important;
            transition: all 0.3s !important;
            position: relative;
            z-index: 1;
        }
        .stButton > button:hover {
            transform: scale(1.02) !important;
            box-shadow: 0 12px 40px rgba(240,192,64,0.4) !important;
        }
        .stAlert {
            background: rgba(255,107,107,0.08) !important;
            border: 1px solid rgba(255,107,107,0.15) !important;
            border-radius: 12px !important;
            color: #ff6b6b !important;
            padding: 10px 20px !important;
            margin-top: 12px !important;
            font-size: 14px !important;
            position: relative;
            z-index: 1;
        }
        /* Responsive tweaks */
        @media (max-height: 700px) {
            .dpsr-letters { font-size: clamp(40px, 8vw, 60px); }
            .company-title { font-size: clamp(24px, 4vw, 40px); }
            .company-sub { font-size: 12px; }
            .login-card { padding: 25px 20px 20px; }
            .login-card h2 { font-size: 20px; }
            .login-card .sub { font-size: 11px; margin-bottom: 18px; }
            .stTextInput > div > div > input { padding: 12px 16px; font-size: 14px; }
            .stButton > button { padding: 12px; font-size: 16px; }
        }
        @media (max-height: 600px) {
            .top-section { flex: 1 1 50%; }
            .bottom-section { flex: 1 1 50%; }
            .car-icon { font-size: 24px; }
        }
    </style>
    """, unsafe_allow_html=True)

    # ---- Background: nebula + particles ----
    st.markdown("""
    <div id="nebula">
        <div class="nebula-blob"></div>
        <div class="nebula-blob"></div>
    </div>
    <script>
        (function() {
            const nebula = document.getElementById('nebula');
            for (let i=0; i<100; i++) {
                const p = document.createElement('div');
                p.className = 'particle';
                p.style.left = Math.random() * 100 + '%';
                p.style.top = Math.random() * 100 + '%';
                p.style.width = (1 + Math.random() * 3) + 'px';
                p.style.height = p.style.width;
                p.style.animationDelay = Math.random() * 5 + 's';
                p.style.animationDuration = (3 + Math.random() * 3) + 's';
                nebula.appendChild(p);
            }
        })();
    </script>
    """, unsafe_allow_html=True)

    # ---- Flexible container ----
    st.markdown("""
    <div class="login-container">
        <div class="top-section">
            <div class="dpsr-letters">
                <span>D</span><span>P</span><span>S</span><span>R</span>
            </div>
            <div class="company-title">Doosan Power Systems Arabia</div>
            <div class="company-sub">— ULTIMATE ATTENDANCE SYSTEM —</div>
            <div class="title-divider"></div>
        </div>
        <div class="bottom-section">
            <div class="login-wrapper">
                <div class="login-card">
                    <span class="car-icon">🚗</span>
                    <h2>✨ <span>Ultimate</span> Attendance</h2>
                    <div class="sub">SYSTEM v3.0</div>
    """, unsafe_allow_html=True)

    # ---- Streamlit fields ----
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        username = st.text_input("Username", placeholder="👤 Username", key="login_username", label_visibility="collapsed")
        password = st.text_input("Password", placeholder="🔑 Password", type="password", key="login_password", label_visibility="collapsed")
        if st.button("🚀 Login", use_container_width=True):
            if username == "AhmedShawky" and password == "iloveshawky":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("❌ Invalid username or password.")

    st.markdown("""
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
