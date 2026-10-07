
import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime, timedelta, timezone

st.set_page_config(page_title="HANDS & AUTO TECH PORTAL", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for styling
css_style = """<style>
.main-header {
    background: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.75)), 
                url('https://images.unsplash.com/photo-1617814076367-b759c7d7e738?q=80&w=1600');
    background-size: cover;
    background-position: center;
    padding: 40px;
    border-radius: 12px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}
.weather-card {
    background-color: #1e222d;
    border-radius: 8px;
    padding: 12px;
    text-align: center;
    border: 1px solid #2d3345;
}
.news-card {
    background-color: #181b24;
    border-left: 4px solid #03cf5d;
    padding: 10px 15px;
    margin-bottom: 8px;
    border-radius: 4px;
}
</style>"""
st.markdown(css_style, unsafe_allow_html=True)

# 1. 맨 상단 주요 뉴스
st.subheader("📰 최신 자동차 및 제조업 주요 뉴스")
n_col1, n_col2 = st.columns(2)

with n_col1:
    st.markdown("#### 🇰🇷 국내 주요 뉴스")
    st.markdown("<div class='news-card'><b>[현대차/기아]</b> 차세대 알루미늄 휠 경량화 및 전기차 전용 에어로 휠 표준 채택</div>", unsafe_allow_html=True)
    st.markdown("<div class='news-card'><b>[제조업/인증]</b> IATF 16949 및 ISO 14001 품질·환경 통합 실사 가이드라인 발표</div>", unsafe_allow_html=True)
    st.markdown("<div class='news-card'><b>[자동차부품]</b> 글로벌 휠 시장 고강도 알루미늄 합금(A356) 수요 가속화</div>", unsafe_allow_html=True)

with n_col2:
    st.markdown("#### 🌐 해외 주요 뉴스")
    st.markdown("<div class='news-card'><b>[EU 규격]</b> 유럽 자동차 제조업체 탄소 배출 규제에 따른 알루미늄 재활용 휠 적용 의무화</div>", unsafe_allow_html=True)
    st.markdown("<div class='news-card'><b>[Morocco Auto]</b> 탕헤르(Tangier) 자동차 산업단지 OEM 알루미늄 휠 캐파 확충</div>", unsafe_allow_html=True)
    st.markdown("<div class='news-card'><b>[Global OEM]</b> 테슬라·도요타, 차세대 EV 플랫폼용 대구경 저압주조 휠 채택</div>", unsafe_allow_html=True)

st.markdown("---")

# 2. 배경 및 히어로 섹션
hero_html = """<div class='main-header'>
    <h1 style='color: #03cf5d; font-size: 2.8rem; margin-bottom: 10px;'>🛞 HANDS & AUTO WHEEL TECH PORTAL</h1>
    <h3 style='color: #ffffff; font-weight: 300;'>핸즈코퍼레이션 (본사 / 모로코 탕헤르 공장) & 글로벌 OEM 알루미늄 휠 기술 포털</h3>
    <p style='color: #ddd; font-size: 0.95rem; margin-top: 15px;'>
        모로코 탕헤르 연간 300만 개 캐파 · 고강도 LPDC 알루미늄 휠 · IATF 16949 품질 보증
    </p>
</div>"""
st.markdown(hero_html, unsafe_allow_html=True)

# 3. 모로코 탕헤르(Tangier) 시간 및 날씨 정보
morocco_tz = timezone(timedelta(hours=1))
tangier_time = datetime.now(morocco_tz)

st.subheader("🇲🇦 모로코 탕헤르(Tangier) 현지 시각 & 주간 날씨 예보")
st.caption(f"🕒 현지 시각: **{tangier_time.strftime('%Y-%m-%d %H:%M:%S')} (GMT+1)**")

weather_data = [
    {"day": "오늘 (수)", "temp": "24°C / 16°C", "weather": "☀️ 맑음"},
    {"day": "목요일", "temp": "25°C / 18°C", "weather": "☀️ 맑음"},
    {"day": "금요일", "temp": "25°C / 21°C", "weather": "⛅ 구름조금"},
    {"day": "토요일", "temp": "25°C / 20°C", "weather": "⛅ 구름조금"},
    {"day": "일요일", "temp": "25°C / 19°C", "weather": "☀️ 맑음"},
    {"day": "월요일", "temp": "25°C / 20°C", "weather": "☀️ 맑음"},
    {"day": "화요일", "temp": "25°C / 20°C", "weather": "☀️ 맑음"},
]

w_cols = st.columns(7)
for idx, w in enumerate(weather_data):
    with w_cols[idx]:
        html_code = f"<div class='weather-card'><div style='font-size:0.85rem; color:#aaa;'>{w['day']}</div><div style='font-size:1.2rem; margin:5px 0;'>{w['weather']}</div><div style='font-size:0.8rem; font-weight:bold;'>{w['temp']}</div></div>"
        st.markdown(html_code, unsafe_allow_html=True)

st.markdown("---")

# 4. 주요 OEM 바로가기
st.subheader("🌐 주요 OEM 및 품질/인증 바로가기")
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

@st.cache_data
def load_data():
    return pd.DataFrame([
        {"분야": "핸즈코퍼레이션", "제목": "핸즈코퍼레이션 알루미늄 휠 자동화 OEM 제조 공정 및 품질 지침", "출처": "핸즈코퍼레이션", "등록일": "2026-04-02"},
        {"분야": "핸즈코퍼레이션", "제목": "탕헤르(Tangier) 모로코 공장 알루미늄 휠 생산 비가동 점검 및 설비 표준", "출처": "핸즈 모로코", "등록일": "2026-03-25"},
        {"분야": "동종업계/비교", "제목": "동종업계(Dicastal, 성우오토모티브, Bobe, CMS) 생산 중단/설비 점검 프로세스 분석", "출처": "글로벌휠연구소", "등록일": "2026-03-15"},
        {"분야": "알루미늄 휠", "제목": "저압 주조(LPDC) 방식을 적용한 고강도 알루미늄 휠 경량화 기술", "출처": "제조기술연구원", "등록일": "2026-03-12"},
        {"분야": "알루미늄 휠", "제목": "EV 전용 휠 단조 공정 및 T6 열처리 품질 안정화 방안", "출처": "한국소재공학회", "등록일": "2026-02-28"},
        {"분야": "알루미늄 휠", "제목": "A356 알루미늄 합금 용탕 처리 및 기포(Porosity) 결함 방지 주조 공정", "출처": "주조공학저널", "등록일": "2026-03-22"},
        {"분야": "자동차 OEM", "제목": "현대자동차 / 현대차그룹 E-GMP 3세대 차세대 알루미늄 휠 내구성 규격", "출처": "HMG Tech", "등록일": "2026-04-01"},
        {"분야": "제조업/인증", "제목": "자동차 부품 제조업을 위한 IATF 16949 & ISO 14001 품질인증 실무 가이드", "출처": "품질인증원", "등록일": "2026-01-15"},
        {"분야": "자동차 OEM", "제목": "도요타 차세대 EV 전동화 플랫폼용 경량 알루미늄 휠 기공 분석 리포트", "출처": "Toyota Times", "등록일": "2026-02-10"},
        {"분야": "제조업/소재", "제목": "알루미늄 휠 절삭 가공 시 공구 마모 절감 및 표면 거칠기 개선 연구", "출처": "한국공학회", "등록일": "2026-03-05"}
    ])

df = load_data()

search_query = st.text_input("🔍 기술 정보, 주조/단조, IATF 규격, OEM, 회사명을 검색하세요", placeholder="예: 핸즈, 핸즈코퍼레이션, 현대차, 주조, 열처리...")
st.caption("💡 추천 검색어: 핸즈 | 핸즈코퍼레이션 | 현대자동차 | 알루미늄 휠 | 저압 주조 | T6 열처리")
st.markdown("---")

if search_query:
    query_terms = [search_query.strip()]
    if "현대자동차" in search_query:
        query_terms.append("현대차")
    elif "현대차" in search_query:
        query_terms.append("현대자동차")
    elif "핸즈" in search_query:
        query_terms.append("핸즈코퍼레이션")

    pattern = "|".join(query_terms)
    filtered_df = df[
        df['제목'].str.contains(pattern, case=False, na=False) |
        df['분야'].str.contains(pattern, case=False, na=False) |
        df['출처'].str.contains(pattern, case=False, na=False)
    ]

    st.subheader(f"🔍 내부 포털 '{search_query}' 검색 결과 ({len(filtered_df)}건)")
    if len(filtered_df) > 0:
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.info("포털 내부 데이터베이스에는 관련 문서가 없습니다. 아래 외부 검색엔진 연계 버튼을 이용해 보세요.")

    st.write("")
    st.markdown(f"#### 🔗 외부 포털에서 **'{search_query}'** 연계 검색하기")
    encoded_query = urllib.parse.quote(search_query)
    
    ec1, ec2, ec3, ec4 = st.columns(4)
    with ec1:
        st.link_button(f"💚 네이버에서 '{search_query}' 검색", f"https://search.naver.com/search.naver?query={encoded_query}", use_container_width=True)
    with ec2:
        st.link_button(f"🔍 구글에서 '{search_query}' 검색", f"https://www.google.com/search?q={encoded_query}", use_container_width=True)
    with ec3:
        st.link_button(f"📜 KIPRIS 특허 검색", f"http://www.kipris.or.kr/khnp/search/searchResult.do?query={encoded_query}", use_container_width=True)
    with ec4:
        st.link_button(f"📰 네이버 뉴스 검색", f"https://search.naver.com/search.naver?where=news&query={encoded_query}", use_container_width=True)
else:
    st.subheader("📋 전체 제조업 및 알루미늄 휠 기술 정보 목록")
    st.dataframe(df, use_container_width=True)
