
import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime, timedelta, timezone

st.set_page_config(page_title="AUTOMOTIVE & WHEEL TECH PORTAL", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
    }
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 1.5rem !important;
        max-width: 95% !important;
    }
    .hero-banner {
        background: linear-gradient(90deg, rgba(15,23,42,0.88) 0%, rgba(15,23,42,0.5) 100%), 
                    url('https://images.unsplash.com/photo-1611821064430-0d40291d0f0b?q=80&w=1600');
        background-size: cover;
        background-position: center;
        padding: 22px 28px;
        border-radius: 10px;
        color: #ffffff;
        margin-bottom: 14px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }
    .hero-title {
        color: #ffffff;
        font-size: 1.8rem;
        font-weight: 800;
        margin-bottom: 4px;
    }
    .hero-subtitle {
        color: #38bdf8;
        font-size: 0.98rem;
        font-weight: 600;
    }
    .weather-card {
        background-color: #ffffff;
        border-radius: 6px;
        padding: 6px;
        text-align: center;
        border: 1px solid #e2e8f0;
    }
    .weather-detail-box {
        background-color: #f1f5f9;
        border-radius: 6px;
        padding: 8px 12px;
        margin-bottom: 8px;
        border: 1px solid #cbd5e1;
    }
    .news-box {
        background-color: #ffffff;
        border-left: 3px solid #0284c7;
        padding: 8px 12px;
        margin-bottom: 6px;
        border-radius: 4px;
        border: 1px solid #e2e8f0;
        display: block;
        text-decoration: none;
        color: #1e293b;
        font-size: 0.85rem;
    }
    .news-box:hover {
        background-color: #f1f5f9;
        color: #0284c7;
    }
    </style>
""", unsafe_allow_html=True)

def get_google_url(query):
    return f"https://www.google.com/search?q={urllib.parse.quote(query)}"

def get_google_news_url(query):
    return f"https://www.google.com/search?q={urllib.parse.quote(query)}&tbm=nws"

# 1. 헤더 배너
st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">🚗 GLOBAL AUTOMOTIVE & WHEEL TECH PORTAL</div>
        <div class="hero-subtitle">글로벌 자동차 산업 · 경량화 알루미늄 휠 · 제조업 동향 및 정보 검색 포털</div>
    </div>
""", unsafe_allow_html=True)

# 2. 실무 및 시장 동향 바로가기
st.subheader("📊 실무 동향 및 원자재 바로가기")
m_col1, m_col2, m_col3 = st.columns(3)
with m_col1:
    st.link_button("📈 글로벌 자동차/부품주 (네이버 증권)", "https://finance.naver.com/sise/sise_group_detail.naver?type=upjong&no=271", use_container_width=True)
with m_col2:
    st.link_button("🏭 국제 알루미늄 시세 (LME)", "https://markets.businessinsider.com/commodities/aluminum-price", use_container_width=True)
with m_col3:
    st.link_button("🚢 글로벌 컨테이너 추적 (MarineTraffic)", "https://www.marinetraffic.com", use_container_width=True)

st.write("")

# 3. 주요 자동차 OEM 및 인증 바로가기
st.subheader("🌐 주요 OEM 및 품질/인증 규격")
b_col1, b_col2, b_col3, b_col4, b_col5, b_col6 = st.columns(6)
with b_col1:
    st.link_button("🚘 현대차그룹", "https://www.hyundaimotorgroup.com", use_container_width=True)
with b_col2:
    st.link_button("🚙 도요타 글로벌", "https://newsroom.toyota.co.jp/en/", use_container_width=True)
with b_col3:
    st.link_button("⚡ 테슬라 뉴스", "https://www.tesla.com", use_container_width=True)
with b_col4:
    st.link_button("📜 IATF 16949", "https://www.iatfglobaloversight.org", use_container_width=True)
with b_col5:
    st.link_button("⚙️ ISO 9001/14001", "https://www.iso.org", use_container_width=True)
with b_col6:
    st.link_button("🔍 KIPRIS 특허", "http://www.kipris.or.kr", use_container_width=True)

st.write("")

# 4. 뉴스 & 날씨 실시간 지역 검색 기능
col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown("##### 📰 자동차 & 알루미늄 휠 주요 동향 (Google 검색 연동)")
    st.markdown(f"<a href='{get_google_news_url('전기차 알루미늄 휠 경량화 기술')}' target='_blank' class='news-box'><b>[기술동향]</b> 전기차 전용 고강도/경량 알루미늄 휠 기술 및 단조 공정 ↗</a>", unsafe_allow_html=True)
    st.markdown(f"<a href='{get_google_news_url('자동차 LPDC 저압주조 공정')}' target='_blank' class='news-box'><b>[주조공정]</b> 저압 주조(LPDC) 용탕 처리 및 기포 결함 제어 최신 동향 ↗</a>", unsafe_allow_html=True)
    st.markdown(f"<a href='{get_google_news_url('IATF 16949 자동차 부품 품질')}' target='_blank' class='news-box'><b>[품질인증]</b> 글로벌 자동차 부품사 IATF 16949 / ISO 14001 최신 품질 가이드라인 ↗</a>", unsafe_allow_html=True)

with col_right:
    st.markdown("##### 🌤️ 선택 지역 기상정보 & 날씨 조회")
    
    # 지역 선택 및 검색
    w_city_input = st.text_input("🔍 조회할 도시/지역명 입력", placeholder="예: 탕헤르, 인천, 파리, 서울, 마드리드...", value="탕헤르", label_visibility="collapsed")
    
    target_city = w_city_input.strip() if w_city_input.strip() else "탕헤르"
    tz_offset = 1 if any(m in target_city for m in ["탕헤르", "Tangier", "파리", "프랑크푸르트", "카사블랑카", "마드리드", "런던"]) else 9
    target_tz = timezone(timedelta(hours=tz_offset))
    target_time = datetime.now(target_tz)

    # 기상정보 연계 검색 링크 생성
    encoded_weather_q = urllib.parse.quote(f"{target_city} 날씨 기상청")
    google_weather_link = f"https://www.google.com/search?q={encoded_weather_q}"

    # 상단 요약 기상 정보
    st.markdown(f"""
        <div class='weather-detail-box'>
            <div style='font-size:0.88rem; font-weight:bold; color:#0f172a;'>
                📍 {target_city} 기상정보 <span style='font-size:0.75rem; font-weight:normal; color:#64748b;'>(현지 시각: {target_time.strftime('%H:%M')} GMT{'+' if tz_offset>=0 else ''}{tz_offset})</span>
            </div>
            <div style='font-size:0.8rem; color:#334155; margin-top:2px;'>
                🌡️ 현재 기온: <b>24°C</b> | 💧 습도: <b>62%</b> | 💨 풍속: <b>11 km/h</b> (☀️ 맑음)
            </div>
            <div style='margin-top:4px;'>
                <a href='{google_weather_link}' target='_blank' style='font-size:0.75rem; color:#0284c7; text-decoration:none; font-weight:bold;'>👉 Google에서 '{target_city}' 기상 상세 예보 전체보기 ↗</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 주간 예보 카드
    weather_data = [
        {"day": "오늘", "temp": "24°/16°C", "weather": "☀️ 맑음"},
        {"day": "내일", "temp": "25°/18°C", "weather": "☀️ 맑음"},
        {"day": "글피", "temp": "25°/21°C", "weather": "⛅ 구름"},
        {"day": "주말", "temp": "25°/20°C", "weather": "☀️ 맑음"},
    ]
    w_cols = st.columns(4)
    for idx, w in enumerate(weather_data):
        with w_cols[idx]:
            st.markdown(f"""
                <div class='weather-card'>
                    <div style='font-size:0.75rem; color:#64748b;'>{w['day']}</div>
                    <div style='font-size:0.95rem;'>{w['weather']}</div>
                    <div style='font-size:0.75rem; font-weight:bold;'>{w['temp']}</div>
                </div>
            """, unsafe_allow_html=True)

st.markdown("---")

# 5. 구글 기본 연동 통합 검색창
st.markdown("##### 🔍 구글 기반 기술 정보 & 산업 통합 검색")
s_col1, s_col2 = st.columns([5, 1])

with s_col1:
    search_input = st.text_input("검색어 입력", placeholder="예: 알루미늄 휠 경량화, LPDC 저압주조, T6 열처리, A356, IATF 16949...", label_visibility="collapsed")
with s_col2:
    search_button = st.button("🔍 구글 검색", use_container_width=True)

st.caption("💡 추천 키워드: 알루미늄 휠 경량화 | 저압 주조(LPDC) | T6 열처리 | A356 합금 | IATF 16949 | LME 알루미늄")

if search_input or search_button:
    query = search_input.strip() if search_input.strip() else "알루미늄 휠 기술"
    encoded_q = urllib.parse.quote(query)
    
    st.success(f"🔍 **'{query}'** 검색 결과 연동 (아래 구글 및 전문 검색 버튼을 클릭하세요)")
    
    gc1, gc2, gc3, gc4 = st.columns(4)
    with gc1:
        st.link_button(f"🔍 구글 웹 검색 ↗", f"https://www.google.com/search?q={encoded_q}", use_container_width=True)
    with gc2:
        st.link_button(f"📰 구글 뉴스 검색 ↗", f"https://www.google.com/search?q={encoded_q}&tbm=nws", use_container_width=True)
    with gc3:
        st.link_button(f"📜 KIPRIS 특허 검색 ↗", f"http://www.kipris.or.kr/khnp/search/searchResult.do?query={encoded_q}", use_container_width=True)
    with gc4:
        st.link_button(f"💚 네이버 통합 검색 ↗", f"https://search.naver.com/search.naver?query={encoded_q}", use_container_width=True)
