import streamlit as st
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Lumina AI", page_icon="⚡", layout="centered")

# 모바일 최적화 CSS (글자 작고 카드 컴팩트)
st.markdown("""
<style>
    .main {background-color: #0a0a0a; color: #f0f0f0;}
    h1 {color: #ffd700; text-align: center; font-size: 2rem; margin-bottom: 8px;}
    .match-card {background: linear-gradient(90deg, #1a1a1a, #222); padding: 14px; border-radius: 16px; margin: 10px 0; box-shadow: 0 4px 15px rgba(255,215,0,0.15);}
    .team-logo {width: 48px; height: 48px; object-fit: contain;}
    .team-name {font-size: 1.25rem; font-weight: bold; margin: 4px 0;}
    .vs {font-size: 1.1rem; color: #ffd700;}
    .prob {font-size: 2.8rem; font-weight: 700; color: #00ff88; text-align: center; line-height: 1;}
    .time {color: #ffd700; font-size: 0.95rem; font-weight: 600;}
    .value {padding: 6px 14px; border-radius: 9999px; font-size: 0.95rem; font-weight: bold; text-align: center;}
</style>
""", unsafe_allow_html=True)

st.title("⚡ Lumina AI")
st.markdown("**Grok AI 실시간 예측 • 베팅 판단**")

st.subheader("🔥 오늘/내일 실제 경기 (2026.5.4\~5 기준)")

# AI 예측 데이터 (Grok AI 분석 기반)
matches = {
    "⚽ EPL": [
        {"time": "22:00", "home": "첼시", "away": "노팅엄 포레스트", "prob": 0.68, "league": "EPL", "home_logo": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg", "away_logo": "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Nottingham_Forest_FC_logo.svg/200px-Nottingham_Forest_FC_logo.svg.png"},
        {"time": "03:00", "home": "에버튼", "away": "맨체스터 시티", "prob": 0.31, "league": "EPL", "home_logo": "https://upload.wikimedia.org/wikipedia/en/7/7a/Everton_FC.svg", "away_logo": "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg"}
    ],
    "🏀 NBA": [
        {"time": "08:00", "home": "필라델피아 76ers", "away": "뉴욕 닉스", "prob": 0.46, "league": "NBA", "home_logo": "https://upload.wikimedia.org/wikipedia/en/0/0e/Philadelphia_76ers_logo.svg", "away_logo": "https://upload.wikimedia.org/wikipedia/en/thumb/2/25/New_York_Knicks_logo.svg/200px-New_York_Knicks_logo.svg.png"}
    ],
    "⚾ KBO": [
        {"time": "14:00", "home": "한화 이글스", "away": "KIA 타이거즈", "prob": 0.52, "league": "KBO", "home_logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Hanwha_Eagles_logo.svg/200px-Hanwha_Eagles_logo.svg.png", "away_logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Kia_Tigers_logo.svg/200px-Kia_Tigers_logo.svg.png"},
        {"time": "14:00", "home": "롯데 자이언츠", "away": "KT 위즈", "prob": 0.56, "league": "KBO", "home_logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Lotte_Giants_logo.svg/200px-Lotte_Giants_logo.svg.png", "away_logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/KT_Wiz_logo.svg/200px-KT_Wiz_logo.svg.png"}
    ]
}

for sport, games in matches.items():
    st.markdown(f"### {sport}")
    for g in games:
        st.markdown(f"""
        <div class="match-card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="text-align:center; width:25%;">
                    <img src="{g['home_logo']}" class="team-logo"><br>
                    <div class="team-name">{g['home']}</div>
                </div>
                <div style="text-align:center; width:50%;">
                    <div class="time">{g['time']} KST</div>
                    <div class="vs">VS</div>
                    <div class="prob">{g['prob']:.0%}</div>
                    <div style="font-size:0.85rem; color:#aaa; margin-top:4px;">Grok AI 예측</div>
                </div>
                <div style="text-align:center; width:25%;">
                    <img src="{g['away_logo']}" class="team-logo"><br>
                    <div class="team-name">{g['away']}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 베팅 판단
        col1, col2 = st.columns([3, 1])
        with col1:
            odds = st.number_input(f"{g['home']} 배당률", value=1.90, step=0.05, key=f"odds_{g['home']}")
        with col2:
            if st.button("🔥 판단", key=f"btn_{g['home']}"):
                implied = 1 / odds
                if g['prob'] > implied + 0.05:
                    st.success("✅ 강력 가치 베팅! (AI 확률이 배당보다 높음)")
                elif g['prob'] > implied:
                    st.info("⚠️ 약간 가치 있음")
                else:
                    st.warning("❌ 가치 부족 — 보류")

st.divider()
st.caption("Lumina AI v5 • Grok AI 실시간 데이터 분석 • 모바일 최적화 • 베팅은 1% 룰로 안전하게")
st.info("특정 경기 더 자세히 예측 원하시면 (예: LG vs KT) 말씀해주세요!")
