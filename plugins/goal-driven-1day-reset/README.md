# goal-driven-1day-reset

**1일 목표 리셋 봇** — 당신의 목표에 맞춘 맞춤 How 생성

[grok-bot-plugins](../..) marketplace의 일부입니다.

---

## 출처

**[Dan Koe — "How to fix your entire life in 1 day"](https://x.com/thedankoe/status/2010751592346030461)** (X 포스트)

원본은 1일 프로토콜을 제시합니다:
- **아침**: Anti-vision(방해 요소) 제거 → Vision(진짜 원하는 것) 발굴
- **낮**: Autopilot 인터럽트 (막혔을 때 즉각 개입)
- **저녁**: 1년/1개월/1일 레버로 합성 + 게임보드 제약 생성

이 플러그인은 그 How를 **Grok Bot**으로 적용합니다. 고정 스크립트가 아닌, **사용자가 입력한 목표(수정 가능)에 맞춘 맞춤 How**를 생성합니다.

---

## 설치

### Grok Bot 설치 (주 사용)

**대상**: Grok Bot (Cursor app의 agent chat)

#### 방법 1: GitHub 링크로 자동 설치 (추천 ⭐)

Grok Bot에서:

```
https://github.com/thecosmicpine/grok-bot-plugins 이걸로 1일 목표 리셋 봇 설치해줘
```

또는 플러그인 경로 지정:

```
https://github.com/thecosmicpine/grok-bot-plugins
plugins/goal-driven-1day-reset 설치해줘
```

**English:**
```
Install the 1-day reset bot from https://github.com/thecosmicpine/grok-bot-plugins
```

**봇이 자동으로:**
1. `bot.json` 읽기
2. `skills/goal-driven-1day-reset/SKILL.md` 읽기
3. Persona를 프로필에 반영
4. Skill 저장

**첫 실행:**
```
사용자: 리셋 시작
봇: 1일 리셋 시작합니다. 당신의 목표는?
사용자: [예: 자유롭게 일하면서 수입도 늘리기]
봇: 알겠어요. "[목표]" 저장.
    지금 당신을 방해하는 3가지는?
```

**목표 수정:**
```
사용자: 목표 수정
봇: [새 목표 입력 받고 How 자동 재생성]
```

---

#### 방법 2: 수동 설치 (fallback)

자동 설치가 안 되면:

1. Grok Bot (Cursor app)에서 새 봇 생성
2. **Persona**: [`bot.json`](bot.json) 파일 내용 복사
3. **Skill**: [`SKILL.md`](skills/goal-driven-1day-reset/SKILL.md) 파일 내용 복사
4. 첫 실행: `리셋 시작`

---

### Cursor Plugin 설치 (선택적)

Cursor IDE Settings > Plugins > Install from URL:
```
https://github.com/thecosmicpine/grok-bot-plugins?plugin=goal-driven-1day-reset
```

---

## 사용 흐름 (Dan Koe protocol)

```
목표 입력/수정 → How 재생성
    ↓
아침: Anti-vision 제거 → Vision 발굴
    ↓
낮: Autopilot 인터럽트
    ↓
저녁: 1년/1개월/1일 레버
    ↓
게임 보드: 제약 + 진행
```

## 특징

- **목표 중심**: 사용자 목표에 맞춘 맞춤 How
- **유연함**: 목표 수정 시 How 자동 재생성
- **Dan Koe 프로토콜**: Anti-vision → Vision → Levers → Game Board
- **짧고 직설적**: 한 번에 한 질문

## Anti-jobs

이 봇은 다음을 **하지 않습니다**:
- ❌ 의료 진단/처방
- ❌ 수익 보장
- ❌ 모르는 것 지어내기
- ❌ X(트위터) 포스팅

## 파일 구조

```
goal-driven-1day-reset/
├── bot.json                         # Grok Bot persona (Dan Koe protocol)
├── skills/
│   └── goal-driven-1day-reset/
│       └── SKILL.md                 # 에이전트 워크플로우 (anti-vision, vision, levers, game board)
├── plugin.json                      # 플러그인 메타데이터
├── .cursor-plugin/plugin.json       # Cursor 연동
└── README.md                        # 이 문서
```

## 데이터

**저장 키**: `goal-driven-state`

**구조**:
- `goals[]`: 목표 목록
- `antiVision[]`: 방해 요소
- `vision`: 진짜 원하는 것
- `levers`: { oneYear, oneMonth, oneDay }
- `gameBoard`: { constraints[], streaks, completedDays[], insights[] }

## 라이선스

MIT

## 기여

이슈나 PR 환영: [grok-bot-plugins](https://github.com/thecosmicpine/grok-bot-plugins)
