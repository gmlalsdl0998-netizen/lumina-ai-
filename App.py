import streamlit as st
import pandas as pd
from xgboost import XGBClassifier
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Lumina AI", page_icon="⚡", layout="centered")

st.markdown("""
<style>
    .main {background-color: #0a0a0a; color: #f0f0f0;}
    h1, h2 {color: #ffd700; text-align: center;}
    .stButton>button {width: 100%; height: 60px; font-size: 1.2rem; border-radius: 16px;}
    .win-prob {font-size: 3.8rem; font-weight: 700; color: #00ff88; text-align: center; margin: 20px 0;}
    .metric-card {background-color: #1a1a1a; padding: 18px; border-radius: 16px;}
</style>
""", unsafe_allow_html=True)

st.title("⚡ Lumina AI")
st.markdown("**핸드폰 앱** 체계적 스포츠 예측")

class AdvancedPredictor:
    def __init__(self, sport):
        self.sport = sport
        self.model = XGBClassifier(n_estimators=300, learning_rate=0.05, max_depth=6, random_state=42)
    
    def train(self):
        df = pd.DataFrame({
            'home_form': [0.6,0.7,0.4,0.8,0.65,0.55,0.72,0.68],
            'away_form': [0.5,0.3,0.6,0.4,0.45,0.7,0.48,0.52],
            'h2h': [0.55,0.65,0.45,0.7,0.6,0.5,0.58,0.62],
            'injury_factor': [0.9,0.85,0.95,0.8,0.88,0.92,0.87,0.9],
            'weather_factor': [1.0,0.95,1.0,0.9,0.98,1.0,0.96,0.97],
            'home_win': [1,1,0,1,1,0,1,1]
        })
        X = df.drop('home_win', axis=1)
        y = df['home_win']
        self.model.fit(X, y)
    
    def predict(self, inputs):
        self.train()
        input_df = pd.DataFrame([inputs])
        prob = self.model.predict_proba(input_df)[0][1]
        return prob

predictors = {s: AdvancedPredictor(s) for s in ["soccer", "basketball", "baseball"]}

tab1, tab2, tab3 = st.tabs(["⚽ 축구", "🏀 농구", "⚾ 야구"])

for tab, sport, emoji in zip([tab1, tab2, tab3], ["soccer", "basketball", "baseball"], ["⚽", "🏀", "⚾"]):
    with tab:
        st.subheader(f"{emoji} {sport.upper()}")
        col1, col2 = st.columns(2)
        with col1:
            home_form = st.slider("홈팀 최근 폼", 0.0, 1.0, 0.68, 0.01)
            h2h = st.slider("H2H 승률", 0.0, 1.0, 0.55, 0.01)
        with col2:
            away_form = st.slider("원정팀 최근 폼", 0.0, 1.0, 0.45, 0.01)
            injury = st.slider("부상 영향", 0.7, 1.0, 0.9, 0.01)
        
        book_odds = st.number_input("북메이커 홈팀 배당률", value=1.85, step=0.05)
        
        if st.button(f"🔥 {sport.upper()} 예측하기", type="primary"):
            inputs = {'home_form': home_form, 'away_form': away_form, 'h2h': h2h, 
                      'injury_factor': injury, 'weather_factor': 0.97}
            prob = predictors[sport].predict(inputs)
            st.markdown(f"<div class='win-prob'>{prob:.1%}</div>", unsafe_allow_html=True)
            st.caption("홈팀 승리 확률")
            
            implied = 1 / book_odds
            if prob > implied + 0.05:
                st.success("✅ 가치 베팅 추천!")
            else:
                st.warning("❌ 보류")

st.caption("Lumina AI • 홈 화면에 추가해서 앱처럼 사용하세요")
