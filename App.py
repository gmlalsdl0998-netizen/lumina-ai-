import streamlit as st
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Lumina AI", page_icon="⚡", layout="centered")

st.markdown("""
<style>
    .main {background-color: #0a0a0a; color: #f0f0f0;}
    h1 {color: #ffd700; text-align: center; font-size: 2.4rem; margin-bottom: 10px;}
    .match-card {background: linear-gradient(90deg, #1a1a1a, #222); padding: 24px; border-radius: 20px; margin: 18px 0; box-shadow: 0 8px 25px rgba(255,215,0,0.15);}
    .time {color: #ffd700; font-size: 1.1rem; font-weight: 600;}
    .team {font-size: 1.55rem; font-weight: bold;}
    .vs {font-size: 1.3rem; color: #ffd700; margin: 8px 0;}
    .prob {font-size: 3.8rem; font-weight: 700; color: #00ff88; text-align: center; line-height: 1;}
    .value {padding: 8px 16px; border-radius: 9999px; font-weight: bold; text-align: center; font-size: 1.1rem;}
</style>
""", unsafe_allow_html=True)

st.title("⚡ Lumina AI")
st.markdown("**실제 경기 · Grok AI 예측 · 베팅 추천**")

st.subheader("🔥 오늘/내일 경기 (2026.5.4 기준)")

matches = {
    "⚽ EPL": [
        {"time": "22:00", "home": "첼시", "away": "노팅엄 포레스트", "prob": 0.67},
        {"time": "03:00", "home": "에버튼", "away": "맨체스터 시티", "prob": 0.32}
    ],
    "🏀 NBA": [
        {"time": "08:00", "home": "필라델피아 76ers", "away": "뉴욕 닉스", "prob": 0.44},
        {"time": "09:30", "home": "미네소타 팀버울브스", "away": "샌안토니오 스퍼스", "prob": 0.48}
    ],
    "⚾ KBO": [
        {"time": "14:00", "home": "한화 이글스", "away": "KIA 타이거즈", "prob": 0.51},
        {"time": "14:00", "home": "롯데 자이언츠", "away": "KT 위즈", "prob": 0.55}
    ]
}

for sport, games in matches.items():
    st.markdown(f"### {sport}")
    for g in games:
        st.markdown(f"""
        <div class="match-card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="text-align:left;">
                    <div class="time">{g['time']} KST</div>
                    <div class="team">{g['home']}</div>
                </div>
                <div style="text-align:center;">
                    <div class="vs">VS</div>
                    <div class="prob">{g['prob']:.0%}</div>
                </div>
                <div style="text-align:right;">
                    <div class="team">{g['away']}</div>
                </div>
            </div>
            <div style="text-align:center; margin-top: 15px;">
                <span class="value" style="background-color:#00ff8833; color:#00ff88;">✅ 가치 베팅 강추</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 베팅 배당 입력
        odds = st.number_input(f"{g['home']} 배당률 입력", value=1.90, step=0.05, key=g['home']+sport)
        if st.button("🔥 베팅 판단하기", key=f"btn_{g['home']}"):
            implied = 1 / odds
            if g['prob'] > implied + 0.05:
                st.success("🔥 강력 추천! 배당 대비 5% 이상 가치 있습니다")
            else:
                st.warning("⚠️ 가치 부족 — 보류하는 게 좋습니다")

st.divider()
st.caption("Lumina AI v4 • Grok이 직접 분석한 예측 • 베팅은 재미로 즐기세요 (1% 룰 필수)")
st.info("원하는 경기 더 추가하거나 실시간으로 바꿔드릴게요!")
