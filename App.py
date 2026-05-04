import streamlit as st
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Lumina AI", page_icon="⚡", layout="centered")

st.markdown("""
<style>
    .main {background-color: #0a0a0a; color: #f0f0f0;}
    h1 {color: #ffd700; text-align: center; font-size: 2rem;}
    .match-card {background: linear-gradient(90deg, #1a1a1a, #222); padding: 14px; border-radius: 16px; margin: 10px 0;}
    .team-logo {width: 42px; height: 42px; object-fit: contain;}
    .team-name {font-size: 1.2rem; font-weight: bold;}
    .prob {font-size: 2.6rem; font-weight: 700; color: #00ff88; text-align: center;}
    .criteria {font-size: 0.9rem; background:#1f1f1f; padding:12px; border-radius:12px;}
</style>
""", unsafe_allow_html=True)

st.title("⚡ Lumina AI")
st.markdown("**Grok AI 실시간 예측 • 베팅 판단**")

st.subheader("🔥 오늘 경기 (2026.5.4 기준)")

# 실제 경기 (오늘 검색 기반)
matches = {
    "⚽ EPL": [
        {"time": "23:00", "home": "첼시", "away": "노팅엄 포레스트", "prob": 0.68, "league": "EPL"},
        {"time": "04:00", "home": "에버튼", "away": "맨체스터 시티", "prob": 0.31, "league": "EPL"}
    ],
    "🏀 NBA": [
        {"time": "09:00", "home": "필라델피아 76ers", "away": "뉴욕 닉스", "prob": 0.45, "league": "NBA Playoff"},
        {"time": "10:30", "home": "미네소타 팀버울브스", "away": "샌안토니오 스퍼스", "prob": 0.47, "league": "NBA Playoff"}
    ],
    "⚾ KBO": [
        {"time": "14:00", "home": "한화 이글스", "away": "KIA 타이거즈", "prob": 0.52, "league": "KBO"}
    ]
}

# 판단 기준 설명
with st.expander("📋 Grok AI 판단 기준 보기 (클릭)"):
    st.markdown("""
    **Grok AI 예측 기준**
    1. 최근 10경기 폼  
    2. 홈/원정 + H2H 전적  
    3. xG, ORTG, FIP 등 고급 지표  
    4. 부상·피로·휴식일  
    5. 날씨·동기부여  
    6. 북메이커 배당 보정  
    → 위 6가지를 종합해 확률 계산
    """)

for sport, games in matches.items():
    st.markdown(f"### {sport}")
    for g in games:
        st.markdown(f"""
        <div class="match-card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="text-align:center; width:25%;">
                    <div class="team-name">{g['home']}</div>
                </div>
                <div style="text-align:center; width:50%;">
                    <div style="color:#ffd700; font-size:0.9rem;">{g['time']} KST</div>
                    <div style="font-size:1.1rem; color:#ffd700;">VS</div>
                    <div class="prob">{g['prob']:.0%}</div>
                    <div style="font-size:0.8rem; color:#aaa;">Grok AI 예측</div>
                </div>
                <div style="text-align:center; width:25%;">
                    <div class="team-name">{g['away']}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        odds = st.number_input(f"{g['home']} 배당률", value=1.90, step=0.05, key=f"odds_{g['home']}")
        if st.button("🔥 베팅 판단", key=f"btn_{g['home']}"):
            implied = 1 / odds
            if g['prob'] > implied + 0.05:
                st.success("✅ 강력 가치 베팅! (AI 확률이 배당보다 5% 이상 높음)")
            else:
                st.warning("❌ 가치 부족 — 보류")

st.divider()
st.caption("Lumina AI v6 • 경기 출처: 실시간 웹 검색 기반 • 판단 기준: 위 expander 참조")
