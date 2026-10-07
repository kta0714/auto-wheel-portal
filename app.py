
import streamlit as st
import pandas as pd
import urllib.parse

st.set_page_config(page_title="NAV-AUTO 기술 정보 포털", layout="wide")

st.markdown("<h1 style='text-align: center; color: #03cf5d;'>🚗 AUTO & WHEEL TECH PORTAL</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #666;'>핸즈코퍼레이션 / 글로벌 OEM / 알루미늄 휠 / 제조업 기술 전문 포털</h4>", unsafe_allow_html=True)
st.markdown("---")

st.subheader("🌐 주요 OEM 및 품질/인증 바로가기")
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.link_button("🚘 현대차그룹", "https://www.hyundaimotorgroup.com", use_container_width=True)
with col2:
    st.link_button("🚙 도요타 글로벌", "https://newsroom.toyota.co.jp/en/", use_container_width=True)
with col3:
    st.link_button("⚡ 테슬라 뉴스", "https://www.tesla.com", use_container_width=True)
with col4:
    st.link_button("📜 IATF 16949", "https://www.iatfglobaloversight.org", use_container_width=True)
with col5:
    st.link_button("⚙️ ISO 9001/14001", "https://www.iso.org", use_container_width=True)
with col6:
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

search_query = st.text_input("🔍 기술 정보, 주조/단조, IATF 규격, OEM, 회사명을 검색하세요", placeholder="예: 핸즈, 핸즈코퍼레이션, 현대차, 주조, 열처리, A356...")
st.caption("💡 추천 검색어: 핸즈 | 핸즈코퍼레이션 | 현대자동차 | 알루미늄 휠 | 저압 주조 | T6 열처리 | IATF 16949")
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

    # 🌐 외부 검색 포털 바로가기 연계 기능
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
