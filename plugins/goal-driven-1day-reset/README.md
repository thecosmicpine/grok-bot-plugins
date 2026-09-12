# goal-driven-1day-reset

**목표를 입력·수정하고, 그 목표에 맞춘 1일 리셋 How를 만든다.**

## 출처

**[Dan Koe — "How to fix your entire life in 1 day"](https://x.com/thedankoe/status/2010751592346030461)**

원본은 1일 프로토콜을 제시합니다:
- **아침**: Anti-vision(방해 요소) 제거 → Vision(진짜 원하는 것) 발굴
- **낮**: Autopilot 인터럽트 (막혔을 때 즉각 개입)
- **저녁**: 1년/1개월/1일 레버로 합성 + 게임보드 제약 생성

이 플러그인은 그 How를 **Grok Bot**으로 적용합니다. 고정된 스크립트가 아닌, **사용자가 입력한 목표(수정 가능)에 맞춘 맞춤 How**를 생성합니다.

---

## 설치

### ✅ Grok Bot 설치 (권장)

**주 사용 사례**: Grok Bot에서 사용

#### 1. Grok Bot 열기
Cursor 또는 X에서 Grok Bot 실행

#### 2. 새 봇 생성 또는 import
- **이름**: `1일 목표 리셋`
- **Persona**: 이 저장소의 `plugins/goal-driven-1day-reset/bot.json` 파일 내용을 복사
  ```
  https://github.com/thecosmicpine/grok-bot-plugins/blob/main/plugins/goal-driven-1day-reset/bot.json
  ```
- **Skill**: `plugins/goal-driven-1day-reset/skills/goal-driven-1day-reset/SKILL.md` 파일 내용을 봇의 skill/workflow에 복사
  ```
  https://github.com/thecosmicpine/grok-bot-plugins/blob/main/plugins/goal-driven-1day-reset/skills/goal-driven-1day-reset/SKILL.md
  ```

#### 3. 첫 실행
```
사용자: 리셋 시작
봇: 1일 리셋 시작합니다. 당신의 목표는?
사용자: 건강한 부자 되기
봇: [목표 기반 맞춤 How 생성]
```

#### 4. 목표 수정
언제든 `목표 수정`이라고 입력하면 → How 자동 재생성

---

### Cursor Plugin 설치 (선택적)

**부 사용 사례**: Cursor IDE plugin으로 사용

#### Cursor IDE에서

1. Settings > Cursor > Plugins
2. "Install from URL" 클릭
3. 다음 URL 입력:
   ```
   https://github.com/thecosmicpine/grok-bot-plugins?plugin=goal-driven-1day-reset
   ```
4. Install 클릭

#### 또는 로컬 설치

```bash
git clone https://github.com/thecosmicpine/grok-bot-plugins.git
cd grok-bot-plugins/plugins/goal-driven-1day-reset
```

Cursor Settings에서 이 폴더를 plugin으로 추가.

#### 첫 실행 (Cursor Plugin)

1. Cursor에서 `/grok 1일 목표 리셋` 입력
2. 목표 입력
3. 아침/저녁 체크인

## 사용 흐름 (Dan Koe 1-day protocol)

```
목표 입력/수정 (언제든 가능) → How 재생성
    ↓
아침: Anti-vision 제거 (방해 요소 3가지)
      → Vision 발굴 (진짜 원하는 것)
    ↓
낮: Autopilot 인터럽트 (막히면 즉각 개입)
    ↓
저녁: 1년 레버 → 1개월 레버 → 내일 할 것 1가지
    ↓
게임 보드: 제약 설정 + 진행 상황 시각화
```

## 특징

- **목표 중심**: 당신의 목표에 맞춘 맞춤 How (고정 스크립트 X)
- **유연함**: 목표 수정 시 How 자동 재생성
- **Dan Koe 프로토콜**: Anti-vision → Vision → Levers → Game Board
- **짧고 직설적**: 한 번에 한 질문, 격려보다 명확한 How

## Anti-jobs

이 봇은 다음을 **하지 않습니다**:
- ❌ 의료 진단이나 처방
- ❌ 수익 보장
- ❌ 모르는 것을 지어내기
- ❌ X(트위터) 포스팅

## 기술 스택

- **주 사용**: Grok Bot (persona + skill)
- **부 사용**: Cursor Plugin (dual-format packaging)
- **Skill 기반**: `skills/goal-driven-1day-reset/SKILL.md`
- **MCP**: 선택적 (필수 아님)
- **데이터**: 로컬 저장 (storageKey: `goal-driven-state`)

## 라이선스

MIT

## 기여

이슈나 PR 환영합니다:
https://github.com/thecosmicpine/grok-bot-plugins
