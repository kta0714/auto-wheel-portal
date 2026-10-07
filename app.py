
import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime, timedelta, timezone

st.set_page_config(page_title="HANDS & AUTO TECH PORTAL", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
    }
    .ticker-container {
        background: #1e293b;
        color: #ffffff;
        padding: 12px 20px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        text-decoration: none;
        transition: transform 0.1s ease;
    }
    .ticker-container:hover {
        transform: translateY(-2px);
    }
    .ticker-badge {
        background-color: #03cf5d;
        color: #ffffff;
        font-weight: bold;
        padding: 4px 10px;
        border-radius: 4px;
        margin-right: 15px;
        font-size: 0.85rem;
        white-space: nowrap;
    }
    .ticker-text {
        font-size: 0.95rem;
        font-weight: 500;
        color: #f1f5f9;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
    .hero-banner {
        background: linear-gradient(90deg, rgba(15,23,42,0.85) 0%, rgba(15,23,42,0.4) 100%),
                    url('https://raw.githubusercontent.com/kta0714/auto-wheel-portal/main/original.png');
        background-size: cover;
        background-position: center;
        padding: 50px 40px;
        border-radius: 16px;
        color: #ffffff;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        display: block;
        text-decoration: none;
        transition: all 0.2s ease;
    }
    .hero-banner:hover {
        box-shadow: 0 12px 30px rgba(0,0,0,0.25);
        filter: brightness(1.03);
    }
    .hero-title {
        color: #ffffff;
        font-size: 2.6rem;
        font-weight: 800;
        margin-bottom: 10px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    .hero-subtitle {
        color: #38bdf8;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 15px;
    }
    .hero-desc {
        color: #e2e8f0;
        font-size: 0.95rem;
        max-width: 700px;
        line-height: 1.5;
    }
    .weather-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 14px;
        text-align: center;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    }
    .news-box {
        background-color: #ffffff;
        border-left: 4px solid #0284c7;
        padding: 12px 16px;
        margin-bottom: 10px;
        border-radius: 6px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        display: block;
        text-decoration: none;
        color: #1e293b;
        transition: all 0.15s ease;
    }
    .news-box:hover {
        background-color: #f1f5f9;
        border-left-color: #03cf5d;
        color: #0284c7;
    }
    .doc-card {
        background-color: #ffffff;
        padding: 15px 20px;
        margin-bottom: 12px;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        display: block;
        text-decoration: none;
        color: #1e293b;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        transition: all 0.15s ease;
    }
    .doc-card:hover {
        border-color: #03cf5d;
        box-shadow: 0 4px 10px rgba(0,0,0,0.06);
        background-color: #f8fafc;
    }
    </style>
""", unsafe_allow_html=True)

def get_naver_news_url(query):
    return f"https://search.naver.com/search.naver?where=news&query={urllib.parse.quote(query)}"

def get_google_url(query):
    return f"https://www.google.com/search?q={urllib.parse.quote(query)}"

# 1. 실시간 속보
st.markdown(f"""
    <a href="{get_naver_news_url('핸즈코퍼레이션')}" target="_blank" style="text-decoration: none;">
        <div class="ticker-container">
            <div class="ticker-badge">⚡ 실시간 속보</div>
            <div class="ticker-text">[핸즈코퍼레이션] 모로코 탕헤르 공장 자동화 OEM 알루미늄 휠 라인 가동률 최적화 추진 &nbsp;|&nbsp; [현대차그룹] EV 전용 고강도 경량 휠 표준 규격 발표</div>
        </div>
    </a>
""", unsafe_allow_html=True)

# 2. 히어로 배너
st.markdown("""
    <a href="http://www.handscorp.co.kr" target="_blank" class="hero-banner">
        <div class="hero-title">🛞 HANDS & AUTO TECH PORTAL</div>
        <div class="hero-subtitle">Creative all by HANDS — 글로벌 OEM 알루미늄 휠 기술 포털 ↗</div>
        <div class="hero-desc">
            핸즈코퍼레이션 본사 및 모로코 탕헤르 연간 300만 개 캐파 전용 포털<br>
            저압주조(LPDC) · 단조 · T6 열처리 · IATF 16949 / ISO 품질·환경 표준 통합 매뉴얼 (클릭 시 공식 홈페이지 이동)
        </div>
    </a>
""", unsafe_allow_html=True)

# 3. 뉴스 섹션
st.subheader("📰 자동차 및 부품 제조업 주요 뉴스")
n_tab1, n_tab2 = st.tabs(["🇰🇷 국내 주요 뉴스", "🌐 해외 주요 뉴스"])

with n_tab1:
    st.markdown(f"<a href='{get_naver_news_url('핸즈코퍼레이션 모로코')}' target='_blank' class='news-box'><b>[핸즈코퍼레이션]</b> 모로코 탕헤르 공장 연간 300만개 캐파 고강도 LPDC 휠 품질 안정화 ↗</a>", unsafe_allow_html=True)
    st.markdown(f"<a href='{get_naver_news_url('현대차 알루미늄 휠')}' target='_blank' class='news-box'><b>[현대차/기아]</b> E-GMP 차세대 전기차용 대구경 알루미늄 휠 내구성 최신 기준 수립 ↗</a>", unsafe_allow_html=True)
    st.markdown(f"<a href='{get_naver_news_url('IATF16949 자동차')}' target='_blank' class='news-box'><b>[제조업/인증]</b> 자동차 부품사 대상 IATF 16949 & ISO 14001 통합 심사 가이드라인 ↗</a>", unsafe_allow_html=True)

with n_tab2:
    st.markdown(f"<a href='{get_google_url('EU 자동차 알루미늄 휠 탄소중립')}' target='_blank' class='news-box'><b>[EU 규제]</b> 탄소중립 대응을 위한 알루미늄 재활용 휠 및 친환경 주조 공정 확대 ↗</a>", unsafe_allow_html=True)
    st.markdown(f"<a href='{get_google_url('Tangier Automotive City Hands Corp')}' target='_blank' class='news-box'><b>[Morocco Auto]</b> 탕헤르 자동차 산업단지 글로벌 OEM 부품 공급망 강화 ↗</a>", unsafe_allow_html=True)
    st.markdown(f"<a href='{get_google_url('Tesla Toyota aluminum wheel spec')}' target='_blank' class='news-box'><b>[Global OEM]</b> 테슬라·도요타, 차세대 EV 전동화 플랫폼 경량화 휠 채택 발표 ↗</a>", unsafe_allow_html=True)

st.markdown("---")

# 4. 모로코 탕헤르(Tangier) 현지 시각 및 일주일 날씨
morocco_tz = timezone(timedelta(hours=1)) # Tangier UTC+1
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
        st.markdown(f"""
            <div class='weather-card'>
                <div style='font-size:0.85rem; color:#64748b; font-weight:600;'>{w['day']}</div>
                <div style='font-size:1.2rem; margin:6px 0;'>{w['weather']}</div>
                <div style='font-size:0.85rem; color:#0f172a; font-weight:bold;'>{w['temp']}</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# 5. 주요 OEM 바로가기
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

# 6. 검색창 (엔터 + 돋보기 검색)
st.subheader("🔎 기술 정보 및 데이터 검색")
s_col1, s_col2 = st.columns([5, 1])

with s_col1:
    search_input = st.text_input("검색어 입력", placeholder="예: 핸즈, 핸즈코퍼레이션, 현대차, 주조, 열처리, A356, IATF...", label_visibility="collapsed")
with s_col2:
    search_button = st.button("🔍 돋보기 검색", use_container_width=True)

st.caption("💡 인기 키워드: 핸즈 | 핸즈코퍼레이션 | 모로코 | 현대자동차 | 저압 주조 | T6 열처리 | IATF 16949")
st.markdown("---")

# 데이터베이스
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
        {"분야": "자동차 OEM", "제목": "도요타 차세대 EV 전동화 플랫폼용 경량 알루미늄 휠 기공 분석 리포트", "출처": "Toyota Times", "등록일": "2026-02-10"}
    ])

df = load_data()

# 검색 실행 로직
if search_input or search_button:
    search_query = search_input.strip()
    if search_query:
        query_terms = [search_query]
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
            # 마크다운 기반의 클릭 가능한 문서 카드 렌더링
            for _, row in filtered_df.iterrows():
                doc_title = row['제목']
                doc_source = row['출처']
                doc_date = row['등록일']
                doc_cat = row['분야']
                
                # 클릭 시 구글 학술검색/특허검색 등 유용한 연계 검색으로 이동하도록 하이퍼링크 생성
                encoded_title = urllib.parse.quote(doc_title)
                search_link = f"https://www.google.com/search?q={encoded_title}"
                
                st.markdown(f"""
                    <a href="{search_link}" target="_blank" class="doc-card">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-weight: bold; font-size: 1.1rem; color: #0284c7;">[{doc_cat}] {doc_title}</span>
                            <span style="font-size: 0.85rem; color: #64748b;">⚙️ 출처: {doc_source} | 📅 등록일: {doc_date} ↗</span>
                        </div>
                    </a>
                """, unsafe_allow_html=True)
        else:
            st.info("포털 내부 데이터베이스에는 관련 문서가 없습니다. 아래 외부 포털 연계 버튼을 이용해 보세요.")

        # 외부 검색 포털 바로가기 연계
        st.write("")
        st.markdown(f"#### 🔗 외부 포털에서 **'{search_query}'** 연계 검색하기")
        encoded_query = urllib.parse.quote(search_query)

        ec1, ec2, ec3, ec4 = st.columns(4)
        with ec1:
            st.link_button(f"💚 네이버 검색", f"https://search.naver.com/search.naver?query={encoded_query}", use_container_width=True)
        with ec2:
            st.link_button(f"🔍 구글 검색", f"https://www.google.com/search?q={encoded_query}", use_container_width=True)
        with ec3:
            st.link_button(f"📜 KIPRIS 특허 검색", f"http://www.kipris.or.kr/khnp/search/searchResult.do?query={encoded_query}", use_container_width=True)
        with ec4:
            st.link_button(f"📰 네이버 뉴스 검색", f"https://search.naver.com/search.naver?where=news&query={encoded_query}", use_container_width=True)
else:
    st.subheader("📋 전체 기술 문서 목록 (클릭 시 외부 연계 검색 및 상세 내용 탐색 가능)")
    # 메인 테이블 목록도 클릭 가능한 카드형식 레이아웃으로 변경
    for _, row in df.iterrows():
        doc_title = row['제목']
        doc_source = row['출처']
        doc_date = row['등록일']
        doc_cat = row['분야']
        
        encoded_title = urllib.parse.quote(doc_title)
        search_link = f"https://www.google.com/search?q={encoded_title}"
        
        st.markdown(f"""
            <a href="{search_link}" target="_blank" class="doc-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: bold; font-size: 1.1rem; color: #1e293b;">[{doc_cat}] {doc_title}</span>
                    <span style="font-size: 0.85rem; color: #64748b;">⚙️ 출처: {doc_source} | 📅 등록일: {doc_date} ↗</span>
                </div>
            </a>
        """, unsafe_allow_html=True)
