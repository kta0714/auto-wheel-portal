
import streamlit as st
import pandas as pd

st.set_page_config(page_title="NAV-AUTO 기술 정보 포털", layout="wide")

st.markdown("<h1 style='text-align: center; color: #03cf5d;'>🚗 AUTO & WHEEL TECH PORTAL</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #666;'>글로벌 자동차 OEM / 제조업 / 알루미늄 휠 기술 검색 포털</h4>", unsafe_allow_html=True)
st.markdown("---")

st.subheader("🌐 주요 OEM 및 품질/인증 정보 바로가기")
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
        {"분야": "알루미늄 휠", "제목": "저압 주조(LPDC) 방식을 적용한 고강도 알루미늄 휠 경량화 기술", "출처": "제조기술연구원", "등록일": "2026-03-12"},
        {"분야": "알루미늄 휠", "제목": "EV 전용 휠 단조 공정 및 T6 열처리 품질 안정화 방안", "출처": "한국소재공학회", "등록일": "2026-02-28"},
        {"분야": "알루미늄 휠", "제목": "A356 알루미늄 합금 용탕 처리 및 기포(Porosity) 결함 방지 주조 공정", "출처": "주조공학저널", "등록일": "2026-03-22"},
        {"분야": "자동차 OEM", "제목": "현대차그룹 E-GMP 3세대 차세대 알루미늄 휠 내구성 및 충격 규격", "출처": "HMG Tech", "등록일": "2026-04-01"},
        {"분야": "제조업/인증", "제목": "자동차 부품 제조업을 위한 IATF 16949 & ISO 14001 품질인증 실무 가이드", "출처": "품질인증원", "등록일": "2026-01-15"},
        {"분야": "자동차 OEM", "제목": "도요타 차세대 EV 전동화 플랫폼용 경량 알루미늄 휠 기공 분석 리포트", "출처": "Toyota Times", "등록일": "2026-02-10"},
        {"분야": "제조업/소재", "제목": "알루미늄 휠 절삭 가공 시 공구 마모 절감 및 표면 거칠기 개선 연구", "출처": "한국공학회", "등록일": "2026-03-05"}
    ])

df = load_data()

search_query = st.text_input("🔍 기술 정보, 주조/단조 공정, IATF 규격, OEM을 검색하세요", placeholder="예: 알루미늄 휠, 주조, 현대차, IATF, 열처리...")
st.caption("인기 키워드: 알루미늄 휠 | 저압 주조 | T6 열처리 | IATF 16949 | 현대차 | A356")
st.markdown("---")

if search_query:
    filtered_df = df[
        df['제목'].str.contains(search_query, case=False, na=False) |
        df['분야'].str.contains(search_query, case=False, na=False) |
        df['출처'].str.contains(search_query, case=False, na=False)
    ]
    st.subheader(f"🔍 '{search_query}' 검색 결과 ({len(filtered_df)}건)")
    if len(filtered_df) > 0:
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.warning("검색 결과가 없습니다. 다른 키워드로 검색해 보세요.")
else:
    st.subheader("📋 전체 제조업 및 알루미늄 휠 기술 정보 목록")
    st.dataframe(df, use_container_width=True)
