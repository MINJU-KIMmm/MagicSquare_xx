# MagicSquare_xx (MagicSquare_1004)

OO 과제 **4×4 Magic Square(마방진)** — Mom Test로 문제를 정의하고, **10줄(행 4·열 4·대각선 2) 합=34** 검증 기준을 코드·테스트로 고정하는 프로젝트.

---

## 문제 (Mom Test)

**페르소나:** 4×4 부분 마방진(빈칸 2개)을 손으로/코드로 다루는 학습자

**진짜 문제:** 손으로 4×4 부분 마방진을 풀 때 **행 4개 합만 맞으면 끝**이라고 판정하고, 열·대각선 검산을 빠뜨려 **틀렸을 때 같은 덧셈을 반복**하며 **약 20분**을 쓴다.

**Session 3 목표:** “행만 맞으면 끝” 판정을 제거하고, **10줄 합=34** 검증 기준을 Rule + Test Loop로 고정한다.

---

## 도메인

| 항목 | 값 |
|------|-----|
| 격자 | 4×4 |
| 숫자 | 1~16 (각 1회) |
| 목표 합 | **34** |
| 검산 | **10줄** — 행 4 + 열 4 + 주대각선 + 반대각선 |
| 과제 | **빈칸 2개** 채우기 |

---

## 프로젝트 구조

```
MagicSquare_xx/
├── README.md
├── docs/
│   └── PRD.md                          # 제품 요구사항 (Session 3)
├── Report/
│   ├── 01.MagicSquare_ProblemDefinition_Report.md
│   ├── 01. MagicSquare_1004 Mom Test STEP1 보고서.md
│   └── 02. MagicSquare_1004 Session3 워크북.md
└── Prompting/
    └── 01. cursor_magic_square_1004_mom_test_step1.md
```

> `src/`, `tests/` — Session 3 구현 시 추가 예정 (`validate_magic_square`, pytest)

---

## 문서

| 문서 | 설명 |
|------|------|
| [Problem Definition Report](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test 기반 문제 정의 |
| [PRD](docs/PRD.md) | 기능 요구사항, 성공 기준, 8계층 로드맵 |
| [Mom Test STEP1 보고서](Report/01.%20MagicSquare_1004%20Mom%20Test%20STEP1%20보고서.md) | 인터뷰 원본·증거 |
| [Session 3 워크북](Report/02.%20MagicSquare_1004%20Session3%20워크북.md) | Rule / Command / Test Loop |

---

## Session 3 범위

**In Scope**

- Rule: 10줄 검산, 실패 조건 3개+
- Command: `validate_magic_square(grid) → ValidationResult`
- Test Loop: Red → Green → Refactor (pytest)

**Out of Scope**

- Solver, MissingFinder, GUI
- ECB Boundary / Integration 전체

---

## 진행 상태

| 단계 | 상태 |
|------|------|
| Mom Test STEP 1 | ✅ 완료 |
| Problem Definition / PRD | ✅ 초안 |
| Rule + Validator + Tests | ⬜ 예정 |

---

## 다음 단계

1. `docs/rule_magic_square_validation.md` — 10줄 Rule 문서
2. `tests/test_square_validator.py` — Mom Test 기반 Red 테스트 3개
3. `src/square_validator.py` — Green 최소 구현

---

## Git · PR 워크플로

**원칙:** 변경은 **작업 브랜치**에만 커밋 → **`main`으로 PR**.

| 브랜치 | 용도 |
|--------|------|
| `main` | 통합 (PR 머지 대상) |
| `red` / `green` / `refactoring` | TDD RED / GREEN / REFACTOR |
| `spec` | Rule·문서·스펙 |
| `staging` | PR 전 확인 |

```bash
git checkout red          # 작업 브랜치
# ... 커밋 ...
git push -u origin HEAD   # 현재 브랜치만 푸시
# GitHub: base=main, compare=red → PR 생성
```

- **하지 않을 것:** `git push --all`, 모든 브랜치를 같은 커밋으로 `branch -f` (PR diff 없어짐)
- Cursor: `/push-pr` Command, PR 템플릿 `.github/pull_request_template.md`

---

## 참고

- 설계 맥락: ECB (`MagicSquare`, `SquareValidator`, `Solver`, `GridUI` 등)
- Mom Test 스타일: [Rob Fitzpatrick — The Mom Test](https://momtestbook.com/)
