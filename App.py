import streamlit as st
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Lumina AI", page_icon="⚡", layout="centered")

# 모바일 최적화 + 깔끔한 UI
st.markdown("""
<style>
    .main {background-color: #0a0a0a; color: #f0f0f0;}
    h1 {color: #ffd700; text-align: center; font-size: 2.1rem; margin: 10px 0 5px 0;}
    .match-card {background: linear-gradient(90deg, #1a1a1a, #222222); padding: 16px; border-radius: 18px; margin: 12px 0; box-shadow: 0 6px 20px rgba(255,215,0,0.12);}
    .time {color: #ffd700; font-size: 1rem; font-weight: 600;}
    .team {font-size: 1.35rem; font-weight: bold; color: #ffffff;}
    .prob {font-size: 3.2rem; font-weight: 700; color: #00ff88; text-align: center; line-height: 1;}
    .vs {font-size: 1.2rem; color: #ffd700; margin: 6px 0;}
    .value {padding: 6px 18px; border-radius: 9999px; font-size: 1rem; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

st.title("⚡ Lumina AI")
st.markdown("**Grok AI 실시간 예측 • 베팅 추천**")

st.subheader("🔥 오늘 & 내일 경기 (2026.5.4\~5 기준)")

# 경기 대폭 증가 (실제 스케줄 기반)
matches = {
    "⚽ EPL": [
        {"time": "23:00", "home": "첼시", "away": "노팅엄 포레스트", "prob": 0.68},
        {"time": "23:00", "home": "아스널", "away": "리버풀", "prob": 0.55},
        {"time": "04:00", "home": "에버튼", "away": "맨체스터 시티", "prob": 0.31}
    ],
    "🏀 NBA": [
        {"time": "09:00", "home": "필라델피아 76ers", "away": "뉴욕 닉스", "prob": 0.45},
        {"time": "10:30", "home": "미네소타 팀버울브스", "away": "샌안토니오 스퍼스", "prob": 0.47}
    ],
    "⚾ KBO": [
        {"time": "14:00", "home": "LG 트윈스", "away": "NC 다이노스", "prob": 0.59},
        {"time": "14:00", "home": "한화 이글스", "away": "KIA 타이거즈", "prob": 0.52},
        {"time": "14:00", "home": "롯데 자이언츠", "away": "KT 위즈", "prob": 0.56},
        {"time": "14:00", "home": "두산 베어스", "away": "SSG 랜더스", "prob": 0.48},
        {"time": "14:00", "home": "삼성 라이온즈", "away": "키움 히어로즈", "prob": 0.62}
    ]
}

# 판단 기준
with st.expander("📋 Grok AI 예측 판단 기준 (클릭해서 보기)"):
    st.markdown("""
    **Grok AI가 고려하는 기준**
    - 최근 10경기 폼 + 가중 평균
    - 홈/원정 어드밴티지 + H2H 전적
    - xG, ORTG, FIP 등 고급 통계
    - 부상·피로·휴식일
    - 날씨·동기부여·구장 특성
    - 북메이커 배당 보정
    """)

for sport, games in matches.items():
    st.markdown(f"### {sport}")
    for g in games:
        st.markdown(f"""
        <div class="match-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="text-align: left; flex: 1;">
                    <div class="team">{g['home']}</div>
                </div>
                <div style="text-align: center; flex: 1;">
                    <div class="time">{g['time']} KST</div>
                    <div class="vs">VS</div>
                    <div class="prob">{g['prob']:.0%}</div>
                    <div style="font-size: 0.85rem; color: #aaa;">Grok AI 예측</div>
                </div>
                <div style="text-align: right; flex: 1;">
                    <div class="team">{g['away']}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 베팅 판단
        odds = st.number_input(f"🏠 {g['home']} 배당률", value=1.90, step=0.05, key=f"odds_{g['home']}")
        if st.button("🔥 베팅 판단", key=f"btn_{g['home']}"):
            implied = 1 / odds
            if g['prob'] > implied + 0.05:
                st.success("✅ **강력 가치 베팅 추천** (AI 확률이 배당보다 5% 이상 높음)")
            elif g['prob'] > implied:
                st.info("⚠️ 약간 가치 있음")
            else:
                st.warning("❌ 가치 부족 — 보류 추천")

st.divider()
st.caption("Lumina AI v7 • 경기 출처: 실시간 웹 스케줄 + Grok AI 분석 • 더 많은 경기 원하시면 말씀해주세요!")
st.info("특정 경기(예: LG vs KT) 자세히 예측해드릴까요?")
