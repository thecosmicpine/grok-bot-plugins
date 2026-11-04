#!/usr/bin/env python3
"""사주 간이 계산: 사주팔자, 십성(식신·인성), 천을귀인 여부.
사용: python3 saju_calc.py YYYY-MM-DD HH:MM [--zi jo|ya]
  양력 입력만 지원. 음력이면 먼저 양력으로 바꿔 넣는다.
  23:00~23:59(야자시)는 --zi ya(기본: 일주는 당일, 시주는 다음날 일간 기준),
  00:00~00:59(조자시)는 당일 일간 기준.
의존성: pip install sxtwl
"""
import sys
import sxtwl

TG = "갑을병정무기경신임계"
DZ = "자축인묘진사오미신유술해"
ELEM_TG = ["목", "목", "화", "화", "토", "토", "금", "금", "수", "수"]
YANG_TG = [i % 2 == 0 for i in range(10)]
GEN = {"목": "화", "화": "토", "토": "금", "금": "수", "수": "목"}
# 지장간(본기 마지막이 아니라 전통 순서: 여기·중기·본기)
HIDDEN = {
    "자": "임계", "축": "계신기", "인": "무병갑", "묘": "갑을", "진": "을계무", "사": "무경병",
    "오": "병기정", "미": "정을기", "신": "무임경", "유": "경신", "술": "신정무", "해": "무갑임",
}
# 천을귀인(일간 기준, 두 지지) — 학파 따라 갑·무·경 등이 다름. 아래는 흔한 표.
CHEONEUL = {
    "갑": "축미", "무": "축미", "경": "축미",
    "을": "자신", "기": "자신",
    "병": "해유", "정": "해유",
    "임": "묘사", "계": "묘사",
    "신": "인오",
}


def sipseong(day_tg, other_tg):
    d, o = TG.index(day_tg), TG.index(other_tg)
    de, oe = ELEM_TG[d], ELEM_TG[o]
    same = YANG_TG[d] == YANG_TG[o]
    if de == oe:
        return "비견" if same else "겁재"
    if GEN[de] == oe:
        return "식신" if same else "상관"
    if GEN[oe] == de:
        return "편인" if same else "정인"
    if GEN[GEN[de]] == oe:  # de가 극하는 것(재성): 목->토 등 (생→생)
        return "편재" if same else "정재"
    return "편관" if same else "정관"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    zi = "ya" if "--zi" in sys.argv and sys.argv[sys.argv.index("--zi") + 1] == "ya" else "jo"
    ymd, hm = args[0], args[1]
    y, m, d = map(int, ymd.split("-"))
    hh, mm = map(int, hm.split(":"))
    day = sxtwl.fromSolar(y, m, d)
    yg, mg, dg = day.getYearGZ(), day.getMonthGZ(), day.getDayGZ()
    hour_idx = ((hh + 1) // 2) % 12
    if hh == 23 and zi == "ya":
        nxt = day.after(1)
        hg = sxtwl.getShiGz(nxt.getDayGZ().tg, 0)
        note = "야자시(23시대): 일주 당일, 시주 다음날 일간 기준"
    else:
        hg = sxtwl.getShiGz(dg.tg, hour_idx)
        note = "조자시(0시 이후) 또는 일반 시각" if hour_idx == 0 else "일반 시각"
    pillars = {
        "년": (TG[yg.tg], DZ[yg.dz]),
        "월": (TG[mg.tg], DZ[mg.dz]),
        "일": (TG[dg.tg], DZ[dg.dz]),
        "시": (TG[hg.tg], DZ[hg.dz]),
    }
    dm = pillars["일"][0]
    print("사주:", " ".join(f"{k}{s}{b}" for k, (s, b) in pillars.items()), f"| 일간 {dm} ({note})")
    found = {"식신": [], "인성": []}
    for k, (s, b) in pillars.items():
        if k != "일":
            ss = sipseong(dm, s)
            if ss == "식신": found["식신"].append(f"{k}간")
            if ss in ("편인", "정인"): found["인성"].append(f"{k}간 {ss}")
        for h in HIDDEN[b]:
            ss = sipseong(dm, h)
            if ss == "식신": found["식신"].append(f"{k}지 {h}")
            if ss in ("편인", "정인"): found["인성"].append(f"{k}지 {h} {ss}")
    print("식신:", found["식신"] or "없음")
    print("인성:", found["인성"] or "없음")
    branches = [b for _, b in pillars.values()]
    ce = [b for b in CHEONEUL.get(dm, "") if b in branches]
    print("천을귀인:", f"있음({','.join(ce)})" if ce else f"없음(해당 지지 {CHEONEUL.get(dm,'?')})")


if __name__ == "__main__":
    main()
