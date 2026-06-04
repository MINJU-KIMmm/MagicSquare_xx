---
name: magic-square-tdd
description: >-
  MagicSquare_1004 Dual-Track TDD·ECB 개발 시 Agent가 따를 절차. Use when
  implementing or testing MagicSquare_xx code, writing test_d_* / test_u_*,
  RED/GREEN/REFACTOR cycles, SquareValidator/Solver/GridUI, or ECB layer work.
---

# MagicSquare TDD Skill

MagicSquare_1004 ECB + Dual-Track TDD 절차. `.cursorrules`, `Report/02`, `docs/PRD.md`와 함께 사용.

## 언제 이 Skill을 켜는가

| 트리거 | 예 |
|--------|-----|
| TDD 사이클 요청 | “RED 테스트 작성”, “Green 구현”, “Refactor” |
| ECB 레이어 구현 | `entity` / `control` / `boundary` 코드·테스트 |
| Dual-Track 테스트 | `test_d_*`, `test_u_*`, `D-*`, `U-*` ID 언급 |
| 검증·솔버·UI | `SquareValidator`, `Solver`, `GridUI`, `validate_magic_square` |
| Rule·Mom Test 연계 | 10줄 합=34, 실패 조건, `MagicConstant` |

**Skill 미적용:** 문서만 편집, git 작업, Harness 구조 변경(명시 요청 없을 때).

작업 시작 시 **한국어** + 선언 한 줄:
`Phase: RED | Layer: control | Track: D-*`

---

## Logic Track vs UI Track

| | Logic Track (`D-*`) | UI Track (`U-*`) |
|---|---------------------|------------------|
| **Layer** | `entity`, `control` | `boundary` |
| **테스트 ID** | `D-*` | `U-*` |
| **파일명** | `test_d_*.py` | `test_u_*.py` |
| **경로** | `tests/entity/`, `tests/control/` | `tests/boundary/` |
| **Mock** | **Domain Mock 금지** | Mock **허용** |
| **검증 대상** | 도메인 규칙·유스케이스·순수 로직 | I/O·표시·E001~E007 매핑 |
| **우선 순위** | Session 3 핵심 (Validator) | Rule·Logic Green 후 |

Logic Track ID 목록 → [reference.md](reference.md)

---

## ECB · Mock · E001~E007

### ECB 의존

```
boundary → control → entity
```

| Layer | 역할 | import |
|-------|------|--------|
| **entity** | `MagicSquare`, `Cell`, `MagicConstant` | **entity → \* 금지** |
| **control** | `SquareValidator`, `Solver`, `MissingFinder` | entity만 |
| **boundary** | `GridUI`, `ResultDisplay` | control·(표시용 DTO) |

### Mock 허용/금지

| 허용 | 금지 |
|------|------|
| UI Track에서 control **인터페이스** Mock | Logic Track에서 entity/control **Domain Mock** |
| boundary 테스트의 외부 I/O Stub | entity 테스트에서 boundary/control import |
| | `34`·`16` 리터럴 (→ `MagicConstant` SSOT) |

### E001~E007 (boundary 전담)

| 코드 | boundary | entity |
|------|----------|--------|
| E001~E005 | 입력·형식·범위·빈칸 수·중복 등 **매핑·표현** | **처리 금지** |
| E006~E007 | 솔버/런타임 등 **매핑·표현** | 도메인 결과만 반환; 코드 매핑은 boundary |

entity/control은 **예외 코드 문자열·HTTP 코드**를 만들지 않는다. boundary가 도메인 결과 → E00x 변환.

---

## RED (5~7단계)

1. **Phase/Layer/Track 선언** — 대상 테스트 ID·파일 확정 (`D-*` 목록: reference.md).
2. **Rule 확인** — Mom Test 증거·10줄·실패 조건과 1:1 대응하는지 `Report/02`·Rule 문서 대조.
3. **테스트 파일 생성** — `tests/{layer}/test_d_*.py` (Logic) 또는 `test_u_*.py` (UI); 테스트 함수 docstring에 `D-xxx` / `U-xxx` 명시.
4. **실패 assertion 작성** — 기대값·격자 fixture·`failed_lines` 등 **완전한** assert (완화·skip·xfail **금지**).
5. **구현 import** — 아직 없는 모듈/함수 import (RED: ImportError 또는 AssertionError 예상).
6. **pytest 실행 (실패 확인)** — 아래 Test Loop § RED 참고; **반드시 실패**해야 다음 단계.
7. **RED 완료 보고** — 실패 테스트명·실패 메시지·연결 Mom Test 증거 1줄.

---

## GREEN (5~7단계)

1. **Phase/Layer/Track 선언** — RED에서 만든 테스트 ID 그대로.
2. **최소 구현 범위 확정** — 해당 RED만 통과하는 코드; 다른 레이어·기능 확장 금지.
3. **레이어 준수** — entity에 I/O·E001~E005 없음; `MagicConstant` 사용; ECB import 방향 유지.
4. **최소 코드 작성** — “행만 검사하고 return” 등 Mom Test 반패 패턴 **금지** (10줄 전부).
5. **pytest 실행 (통과 확인)** — 대상 `test_d_*` / `test_u_*`만 먼저, 이후 Logic/UI 레이어 스uite.
6. **회귀 확인** — `pytest tests/entity tests/control` (Logic) 또는 boundary 포함 범위 실행; 기존 Green 유지.
7. **GREEN 완료 보고** — 통과 테스트·추가/변경 파일·의도적 미구현 항목.

---

## REFACTOR (5~7단계)

1. **Phase/Layer/Track 선언** — Refactor 대상(중복·명명·SSOT) 명시.
2. **Green 고정** — Refactor 전 현재 pytest **전부 Green** 확인.
3. **구조 개선** — 중복 합산 제거, `MagicConstant` 집약, ECB 경계 유지; **동작 변경 없음**.
4. **테스트 변경 최소화** — assert 완화·삭제로 Green 만들기 **금지**; 필요 시 테스트 **강화**만.
5. **pytest 전체 실행** — `pytest` (또는 Logic + UI 순).
6. **규칙 점검** — Domain Mock 없음, entity E001~E005 없음, 리터럴 34/16 없음.
7. **REFACTOR 완료 보고** — 변경 요약·pytest 결과·다음 RED 후보 ID.

---

## Test / Review Loop

| 시점 | 명령 | 기대 |
|------|------|------|
| **RED 직후** | `pytest tests/{layer}/test_d_xxx.py -v` | **FAIL** (1개 이상) |
| **GREEN 직후** | `pytest tests/{layer}/test_d_xxx.py -v` | **PASS** (대상 전부) |
| **Logic Review** | `pytest tests/entity tests/control -v` | **PASS** |
| **UI Review** | `pytest tests/boundary -v` | **PASS** (해당 Track 작업 시) |
| **REFACTOR / 세션 마감** | `pytest -v` | **PASS** (전체) |
| **회귀 (Logic 우선)** | `pytest tests/entity tests/control -q` | Green 유지 확인 |

**원칙:** RED에서 전체 suite 돌려 Green 확인하지 않음. REFACTOR·Review에서만 넓은 범위.

설치: `pip install -e ".[dev]"` (최초 1회).

---

## 완료 보고 항목

매 Phase 종료 시 아래를 **한국어**로 보고:

| # | 항목 |
|---|------|
| 1 | **Phase / Layer / Track** |
| 2 | **테스트 ID** (`D-*` / `U-*`) 및 파일 경로 |
| 3 | **pytest 명령·결과** (pass/fail 개수) |
| 4 | **Mom Test·Rule 연결** (증거 또는 FC 번호 1줄) |
| 5 | **변경 파일 목록** |
| 6 | **ECB·Mock·E00x 준수 여부** (위반 시 수정 내역) |
| 7 | **다음 단계** (다음 RED ID 또는 Green 대상) |

git commit·push·PR은 **사용자 요청 시에만**. 업로드 시 **`/push-pr`** — 현재 브랜치만 push, `main` 대비 diff 있으면 PR. `git push --all`·`branch -f` **금지**.

---

## 추가 자료

- Logic Track `D-*` ID: [reference.md](reference.md)
- 프로젝트 규칙: `.cursorrules`
- Session 3 범위: `Report/02. MagicSquare_1004 Session3 워크북.md`
