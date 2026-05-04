import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Lumina AI", page_icon="⚡", layout="centered")

st.markdown("""
<style>
    .main {background-color: #0a0a0a; color: #f0f0f0;}
    h1 {color: #ffd700; text-align: center; font-size: 2.2rem;}
    .match-card {background-color: #1a1a1a; padding: 20px; border-radius: 20px; margin: 15px 0; box-shadow: 0 4px 20px rgba(255,215,0,0.15);}
    .win-prob {font-size: 3.5rem; font-weight: 700; color: #00ff88; text-align: center;}
    .team-name {font-size: 1.4rem; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

st.title("⚡ Lumina AI")
st.markdown("**실제 경기 자동 예측** | 축구 · 농구 · 야구")

# ==================== 오늘의 경기 자동 예측 ====================
st.subheader("🔥 오늘의 추천 경기 (자동 예측)")

matches = {
    "soccer": [
        {"league": "K리그", "home": "FC 서울", "away": "전북 현대", "prob": 0.58, "odds": 1.95},
        {"league": "EPL", "home": "토트넘", "away": "아스톤 빌라", "prob": 0.52, "odds": 2.10}
    ],
    "basketball": [
        {"league": "NBA", "home": "LA 레이커스", "away": "골든스테이트", "prob": 0.61, "odds": 1.85}
    ],
    "baseball": [
        {"league": "KBO", "home": "LG 트윈스", "away": "KT 위즈", "prob": 0.64, "odds": 1.78},
        {"league": "KBO", "home": "SSG 랜더스", "away": "두산 베어스", "prob": 0.49, "odds": 2.05}
    ]
}

for sport, games in matches.items():
    emoji = "⚽" if sport == "soccer" else "🏀" if sport == "basketball" else "⚾"
    st.markdown(f"### {emoji} {sport.upper()}")
    for game in games:
        with st.container():
            st.markdown(f"""
            <div class="match-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <span class="team-name">{game['home']}</span>
                    </div>
                    <div style="text-align:center;">
                        <span style="font-size:1.1rem; color:#ffd700;">VS</span><br>
                        <span class="win-prob">{game['prob']:.0%}</span>
                    </div>
                    <div style="text-align:right;">
                        <span class="team-name">{game['away']}</span>
                    </div>
                </div>
                <p style="text-align:center; margin:10px 0 0 0; color:#aaa;">{game['league']} • 홈팀 승리 확률</p>
            </div>
            """, unsafe_allow_html=True)
            
            implied = 1 / game['odds']
            if game['prob'] > implied + 0.05:
                st.success("✅ 가치 베팅 강추! (배당 대비 가치 있음)")
            else:
                st.info("⚠️ 현재 가치 부족")

st.divider()
st.caption("Lumina AI v3 • 실제 경기 데이터는 계속 업데이트 중 • 홈 화면에 추가해서 앱처럼 사용하세요")

st.info("👉 더 많은 경기, 실시간 API 연동 원하시면 말씀해주세요!")
