# pocketbase-connect

**PocketBase 헬퍼** — PocketBase 연결·CRUD·오프라인 큐 (Mac Shell + .env.local)

[grok-bot-plugins](../..) marketplace의 일부입니다. 어떤 Grok Bot이든 PocketBase와 말할 때 쓰는 **공유 스킬**입니다.

---

## 설치

### Grok Bot 설치 (주 사용)

**대상**: Grok Bot (Cursor app의 agent chat)

#### 방법 1: GitHub 링크로 자동 설치 (추천 ⭐)

Grok Bot에서:

```
https://github.com/thecosmicpine/grok-bot-plugins 이걸로 PocketBase 헬퍼 설치해줘
```

또는 플러그인 경로 지정:

```
https://github.com/thecosmicpine/grok-bot-plugins
plugins/pocketbase-connect 설치해줘
```

**English:**
```
Install pocketbase-connect from https://github.com/thecosmicpine/grok-bot-plugins
```

**봇이 자동으로:**
1. `bot.json` 읽기
2. `skills/pocketbase-connect/SKILL.md` 읽기
3. Persona를 프로필에 반영
4. Skill 저장

**첫 실행:**
```
사용자: PocketBase 연결해줘
봇: pocketbase-connect 스킬을 로드하고 Mac Shell + .env.local로 health check를 한다.
```

---

#### 방법 2: 수동 설치 (fallback)

자동 설치가 안 되면:

1. Grok Bot (Cursor app)에서 새 봇 생성
2. **Persona**: [`bot.json`](bot.json) 파일 내용 복사
3. **Skill**: [`SKILL.md`](skills/pocketbase-connect/SKILL.md) 파일 내용 복사
4. 첫 실행: `PocketBase 연결해줘`

---

### Cursor Plugin 설치 (선택적)

Cursor IDE Settings > Plugins > Install from URL:
```
https://github.com/thecosmicpine/grok-bot-plugins?plugin=pocketbase-connect
```

---

## 하는 일

연결·쓰기 요청이 있을 때만 이 스킬을 로드합니다.

- Health check 후 list / create / update / upsert
- Mac이 꺼지거나 PocketBase가 내려가면 데이터를 버리지 않고 메모리 큐에 보관
- 다음 성공 연결 때 pending day를 오래된 것부터 flush

시크릿·토큰은 이 저장소에 넣지 않습니다. Mac의 `.env.local`만 사용합니다.

## 파일 구조

```
pocketbase-connect/
├── bot.json                         # PocketBase 헬퍼 persona (요청 시에만 스킬 사용)
├── skills/
│   └── pocketbase-connect/
│       └── SKILL.md                 # 공유 스킬 (health, CRUD, 오프라인 큐)
├── plugin.json                      # 플러그인 메타데이터
├── .cursor-plugin/plugin.json       # Cursor 연동
└── README.md                        # 이 문서
```

## 라이선스

MIT

## 기여

이슈나 PR 환영: [grok-bot-plugins](https://github.com/thecosmicpine/grok-bot-plugins)
