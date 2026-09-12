# goal-driven-1day-reset

**목표를 입력·수정하고, 그 목표에 맞춘 1일 리셋 How를 만든다.**

## 설치

### Cursor IDE에서

1. Settings > Cursor > Plugins
2. "Install from URL" 클릭
3. 다음 URL 입력:
   ```
   https://github.com/thecosmicpine/grok-bot-plugins?plugin=goal-driven-1day-reset
   ```
4. Install 클릭

### 또는 로컬 설치

```bash
git clone https://github.com/thecosmicpine/grok-bot-plugins.git
cd grok-bot-plugins/plugins/goal-driven-1day-reset
```

Cursor Settings에서 이 폴더를 plugin으로 추가.

## 첫 실행

플러그인 설치 후:

1. **Grok Bot 실행**: Cursor에서 `/grok 1일 목표 리셋` 입력
2. **목표 설정**: 봇이 목표를 물어보면 입력 (예: "건강한 부자 되기")
3. **아침 체크인**: "오늘 집중할 것 1가지" 답변
4. **저녁 리뷰**: 하루가 끝나면 "/grok 1일 목표 리셋"으로 리뷰

## 사용 흐름

```
목표 입력/수정 (언제든 가능)
    ↓
아침: 오늘 집중할 것
    ↓
낮: 막혔을 때 체크인
    ↓
저녁: 배운 점 리뷰
    ↓
게임 보드: 진행 상황 확인
```

## 특징

- **목표 중심**: 당신의 목표에 맞춘 일일 계획
- **유연함**: 목표는 언제든 수정 가능
- **짧고 명확**: 한 번에 한 질문
- **실천적**: 구체적인 How 제시

## 예시 목표

기본 목표가 없다면 "건강한 부자" 예시로 안내합니다:
- 건강: 매일 30분 운동
- 부자: 수입원 1개 더 만들기

## Anti-jobs

이 봇은 다음을 **하지 않습니다**:
- ❌ 의료 진단이나 처방
- ❌ 수익 보장
- ❌ 모르는 것을 지어내기
- ❌ X(트위터) 포스팅

## 기술 스택

- **Skill 기반**: `skills/goal-driven-1day-reset/SKILL.md`
- **MCP 선택적**: 필수 아님
- **데이터**: 로컬 저장 (storageKey: `goal-driven-state`)

## 라이선스

MIT

## 기여

이슈나 PR 환영합니다:
https://github.com/thecosmicpine/grok-bot-plugins
