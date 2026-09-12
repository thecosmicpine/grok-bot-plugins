# grok-bot-plugins

**Public Grok Bot plugin marketplace**

## 개요

**Grok Bot** (Cursor app의 agent chat)에서 사용할 수 있는 플러그인 모음입니다. 각 플러그인은 persona + skill로 구성됩니다.

**주 사용**: Grok Bot에 persona와 skill import  
**부 사용**: Cursor Plugins UI

## 설치 방법 (모든 플러그인 공통)

### GitHub 링크로 자동 설치 (추천)

Grok Bot (Cursor app)에서 저장소 링크를 주고 설치 요청:

```
https://github.com/thecosmicpine/grok-bot-plugins 이걸로 [플러그인명] 설치해줘
```

또는 플러그인 경로 지정:

```
https://github.com/thecosmicpine/grok-bot-plugins
plugins/[플러그인명] 설치해줘
```

봇이 자동으로 `bot.json` + `SKILL.md` 읽고 설치합니다.

### 수동 설치 (fallback)

1. Grok Bot에서 새 봇 생성
2. `plugins/[플러그인명]/bot.json` 내용 → persona
3. `plugins/[플러그인명]/skills/[플러그인명]/SKILL.md` 내용 → skill

---

## 플러그인

### [`goal-driven-1day-reset`](plugins/goal-driven-1day-reset/)

**1일 목표 리셋** — 목표 입력/수정 → Dan Koe 1-day protocol 기반 맞춤 How 생성

[Dan Koe의 "How to fix your entire life in 1 day"](https://x.com/thedankoe/status/2010751592346030461)를 Grok Bot으로 적용.

**설치:**
```
https://github.com/thecosmicpine/grok-bot-plugins 이걸로 1일 목표 리셋 봇 설치해줘
```

상세: [`plugins/goal-driven-1day-reset/README.md`](plugins/goal-driven-1day-reset/)

---

## Layout

```
.cursor-plugin/marketplace.json    # name: grok-bot-plugins, pluginRoot: plugins
README.md
plugins/
  <plugin-name>/
    bot.json
    plugin.json
    .cursor-plugin/plugin.json
    skills/<plugin-name>/SKILL.md
    README.md
```

`pluginRoot`는 `plugins`입니다.

## License

MIT
