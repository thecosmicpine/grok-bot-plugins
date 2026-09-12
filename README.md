# grok-bot-plugins

**Public Grok Bot plugin marketplace** (Cursor plugin packaging is secondary)

## 개요

**Grok Bot**에서 사용할 수 있는 플러그인 모음입니다. 각 플러그인은 Grok Bot persona + skill로 구성되며, Cursor IDE에서도 설치 가능합니다.

**주 사용 사례**: Grok Bot에 persona와 skill을 import하여 사용  
**부 사용 사례**: Cursor Plugins UI를 통해 설치

## 플러그인

### `goal-driven-1day-reset`

목표 입력·수정 → 1일 리셋 How 생성

**출처**: [Dan Koe — "How to fix your entire life in 1 day"](https://x.com/thedankoe/status/2010751592346030461)

원본은 1일 프로토콜 (아침 anti-vision/vision 발굴, 낮 autopilot 인터럽트, 저녁 1y/1m/daily 레버 + 게임보드 제약 생성)을 제시합니다. 이 플러그인은 그 How를 **사용자 목표 기반 Grok Bot**으로 적용합니다. 고정된 「건강한 부자」 스크립트가 아닌, **입력한 목표(수정 가능)에 맞춘 맞춤 How**를 생성합니다.

## Grok Bot 설치 (권장)

### 1. Grok Bot 열기
Cursor 또는 X에서 Grok Bot 실행

### 2. 새 봇 생성
- 이름: `1일 목표 리셋`
- Persona: `plugins/goal-driven-1day-reset/bot.json` 내용 복사
- Skill: `plugins/goal-driven-1day-reset/skills/goal-driven-1day-reset/SKILL.md` 내용 복사

### 3. 첫 실행
```
사용자: 리셋 시작
봇: 1일 리셋 시작합니다. 당신의 목표는?
사용자: [목표 입력]
봇: [목표 기반 How 생성]
```

### 4. 목표 수정
언제든 `목표 수정`이라고 입력 → How 자동 재생성

---

## Cursor Plugin 설치 (선택적)

Cursor IDE Settings > Plugins > Install from URL:
```
https://github.com/thecosmicpine/grok-bot-plugins?plugin=goal-driven-1day-reset
```

## Layout

```
.cursor-plugin/marketplace.json
plugins/<plugin-name>/
```

`pluginRoot` is `plugins`.

## License

MIT
