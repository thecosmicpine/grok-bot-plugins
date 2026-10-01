---
name: pocketbase-connect
description: >-
  use when any bot needs PocketBase (health check, create/update/list, midnight
  backup) — Mac Shell + .env.local only; if Mac/PB down, keep data in memory and
  flush pending days on next successful connect
---
# PocketBase connect (shared)

## When
Any bot that reads or writes PocketBase collections (`health_daily`, `work_events`, queues, `bot_*`, etc.).

## Runtime (required)
- PocketBase runs on the **user Mac** (k8s → `http://127.0.0.1:8090`), **not** on the box.
- Box `curl http://127.0.0.1:8090` **always fails**. Use Shell with the user's Mac `machineId` (from `[Sent from machine …]` or the registered Mac).
- Env on Mac: `/Users/hyun_song/pocketbase/.env.local` → `PB_URL`, `PB_TOKEN`.
- Never print the raw token. Redact as `PB_TOKEN=***set***`.

## Auth load (every Mac Shell call)
```bash
set -a
source /Users/hyun_song/pocketbase/.env.local
set +a
```

## Health check (before every write/backup)
```bash
curl -sS -o /tmp/pb-health.json -w "%{http_code}" "$PB_URL/api/health"
```
Expect HTTP `200` and healthy JSON. Anything else = **offline**.

## Offline / Mac down (required)
1. If health fails, Mac Shell fails, or `.env.local`/token missing → **do not drop data**.
2. Keep the day's records in **agent memory** (same-day ops as usual).
3. Also keep a durable **pending PB backup** fact/list: closed days (and any day-summary payload) not yet written to PocketBase. Update it whenever a day closes or a midnight backup fails.
4. Do **not** spam the user on every failed midnight backup unless they asked for status. One short note is enough when a multi-day backlog builds.
5. On the **next successful** health check (midnight routine, manual write, or reconnect probe): **flush pending days first** (oldest → newest upsert), then clear those entries from the pending list, then continue.
6. Never dual-write Notion unless that bot's standing policy says so.

## CRUD (Authorization header)
List:
```bash
curl -sS -G "$PB_URL/api/collections/<collection>/records" \
  -H "Authorization: $PB_TOKEN" \
  --data-urlencode 'filter=(date="YYYY-MM-DD 00:00:00.000Z")'
```

Create:
```bash
curl -sS -X POST "$PB_URL/api/collections/<collection>/records" \
  -H "Authorization: $PB_TOKEN" -H 'Content-Type: application/json' \
  -d '{ ...fields... }'
```

Update:
```bash
curl -sS -X PATCH "$PB_URL/api/collections/<collection>/records/<id>" \
  -H "Authorization: $PB_TOKEN" -H 'Content-Type: application/json' \
  -d '{ ...fields... }'
```

## Upsert pattern
1. GET/list with the bot's unique key (often `date` / `record_date`).
2. Found → PATCH that id (only fields you mean to change).
3. Missing → POST create.
4. After success, remove that day from the pending-backup list in memory.

## Collections map
See `Documents/grokbot/pocketbase/COLLECTIONS.md` (and `~/pocketbase/COLLECTIONS.md` on Mac). Bot-specific field shapes stay in that bot's memory/routine — not here.

| collection | purpose |
|------------|---------|
| health_daily | health bot daily |
| work_events | work-hours events / day-summary |
| quote_queue / research_queue / publish_slots / info_x_queue / trending | content queues |
| bot_profiles / bot_memories / bot_routines | bot backup |

## Do not
- Call PocketBase from the box as localhost.
- Embed tokens in skills, routines, or chat.
- Treat a failed backup as data loss — queue in memory until reconnect.
- Dual-write Notion unless that bot's standing policy says so.
