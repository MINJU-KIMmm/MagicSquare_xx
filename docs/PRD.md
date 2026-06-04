# MagicSquare_1004 — Product Requirements Document (PRD)

| 항목 | 내용 |
|------|------|
| 제품 | MagicSquare_1004 |
| 버전 | 0.1 (초안) |
| 일자 | 2026-06-04 |
| 상태 | Draft |
| Problem Definition | `Report/01.MagicSquare_ProblemDefinition_Report.md` |

---

## 1. 개요

### 1.1 배경

OO 과제 **4.1 Magic Square** — 4×4 마방진에서 빈칸 2개를 채워 행·열·대각선 합을 **34**로 맞춘다.  
Mom Test에 따르면 학습자는 **행 4개만 검산하고 끝**내는 습관으로 대각선 누락 시 **약 20분**을 낭비한다.

### 1.2 제품 목표 (Session 3)

> **4×4 마방진에서 “행만 맞으면 끝” 판정을 제거하고, 10줄(행 4·열 4·대각선 2) 합=34 검증 기준을 코드·테스트로 고정한다.**

### 1.3 비목표 (Non-Goals)

- 마방진 **자동 풀이** (Solver)
- **GUI** / PyQt / 웹 앱
- 빈칸 **자동 탐색** (MissingFinder)
- ECB 전체 일괄 구현
- “검증 앱” UX·원클릭 체크

---

## 2. 사용자

### 2.1 Primary Persona

**4×4 부분 마방진 학습자**

- OO 과제 수행 (빈칸 2개)
- 현재: 손 검산 위주, 코드 경험 없음
- 검산 습관: 1행 → 2행 → 3·4행 → **끝**

### 2.2 사용자 스토리 (Mom Test 기반)

| ID | As a… | I want… | So that… | Mom Test 근거 |
|----|-------|---------|----------|---------------|
| US-1 | 학습자 | 대각선이 틀린 격자를 **즉시 실패**로 알 수 | 20분 재덧셈을 피한다 | “대각선 빼먹어 20분” |
| US-2 | 학습자 | 행 4개만 맞아도 **완료로 보지 않** | “1행→4행→끝” 습관을 깬다 | “끝” |
| US-3 | 학습자 | 10줄 검산 항목이 **명시**되어 | 과제 조건을 다시 보지 않아도 누락이 없다 | “과제 조건 다시보기” |

---

## 3. 도메인 요구사항

### 3.1 Magic Square 규칙

| ID | 규칙 |
|----|------|
| DR-1 | 격자 크기: **4×4** |
| DR-2 | 사용 숫자: **1~16**, 각 1회 (중복·누락 없음) |
| DR-3 | 목표 합: **34** |
| DR-4 | 검산 대상: **10줄** — 행 4, 열 4, 주대각선, 반대각선 |
| DR-5 | 과제 입력: **빈칸 2개** (미채움 또는 채운 후 검증) |

### 3.2 실패 조건 (Failure Conditions)

최소 3개 — 슬라이드 연습 목표 + Mom Test 매핑:

| ID | 조건 | Mom Test 연결 |
|----|------|---------------|
| FC-1 | 행 4개 합=34, **열 하나** ≠34 | 10줄 검증 |
| FC-2 | 행·열=34, **주대각선** ≠34 | “대각선 빼먹음” |
| FC-3 | 행·열·주대각선=34, **반대각선** ≠34 | 10줄 완전성 |
| FC-4 | (추가) 빈칸, 범위 밖, 중복 | 도메인 무결성 |

---

## 4. 기능 요구사항 (Session 3)

### 4.1 SquareValidator — `validate_magic_square`

| ID | 요구사항 | 우선순위 |
|----|----------|----------|
| FR-1 | 4×4 격자 + 목표 합 34 입력 | P0 |
| FR-2 | **10줄** 각각 합 계산 및 34 비교 | P0 |
| FR-3 | `valid: bool` 반환 | P0 |
| FR-4 | 실패 시 `failed_lines[]` (예: `row_2`, `col_3`, `diag_main`, `diag_anti`) | P0 |
| FR-5 | **행 4개만** 통과 시 `valid: true` **금지** | P0 |
| FR-6 | **대각선만** 실패 시 `valid: false` | P0 |

### 4.2 R-G-I-O

| | |
|---|---|
| **Role** | `SquareValidator` |
| **Goal** | 10줄 전체 검산을 한 번의 판정으로 재현 |
| **Input** | `grid: 4×4 int`, `target_sum: 34` |
| **Output** | `ValidationResult { valid, failed_lines[] }` |

### 4.3 Rule 문서

| ID | 요구사항 |
|----|----------|
| FR-7 | `docs/rule_magic_square_validation.md` — 10줄 체크리스트 |
| FR-8 | Rule 항목과 테스트 케이스 **1:1 대응** |

### 4.4 Test Loop

| ID | 요구사항 |
|----|----------|
| FR-9 | `tests/test_square_validator.py` — TDD Red → Green → Refactor |
| FR-10 | Red 테스트 3개 — Mom Test 증거 각 1개 이상 연결 |

**필수 테스트 (Red)**

```text
test_rows_ok_but_main_diagonal_fails     # US-1 / FC-2
test_all_rows_pass_is_not_valid          # US-2 / FC-1
test_checklist_covers_ten_lines          # US-3 / DR-4
```

### 4.5 Skill (선택)

| ID | 요구사항 |
|----|----------|
| FR-11 | `validate-before-submit` — 검증 코드 변경 시 10줄 테스트 선행 |
| FR-12 | “행만 통과” 테스트 추가 시 리뷰 거부 |

---

## 5. 성공 지표 (Session 3 완료)

| # | 기준 | 검증 방법 |
|---|------|-----------|
| AC-1 | 대각선만 틀린 격자 → `valid: false` | `test_rows_ok_but_main_diagonal_fails` |
| AC-2 | 행 4개만 OK → `valid: false` | `test_all_rows_pass_is_not_valid` |
| AC-3 | Rule 10줄 ↔ Test 1:1 | `test_checklist_covers_ten_lines` + Rule 문서 리뷰 |
| AC-4 | Solver / UI 미착수 | 코드베이스에 해당 모듈 없음 |

---

## 6. 8계층 — 세션별 로드맵

| 계층 | Session 3 | 이후 세션 |
|------|-----------|-----------|
| **Rule** | ✅ 10줄, FC 3+ | 유지 |
| **Command** | ✅ `validate_magic_square` | 확장 |
| **(Skill)** | ✅ validate-before-submit | — |
| **Test Loop** | ✅ Red/Green/Refactor | 회귀 |
| Entity | — | `MagicSquare`, `Cell` |
| Control | — | `MissingFinder`, `Solver` |
| Boundary | — | `GridUI`, `ResultDisplay` |
| Integration | — | ECB 전체 |

---

## 7. 기술 제약 (초안)

| 항목 | 내용 |
|------|------|
| 언어 | Python (과제·VIBECODING 관례) |
| 테스트 | pytest |
| 아키텍처 | ECB (Session 3는 Validator/Rule만) |
| UI | Session 3 범위 외 |

---

## 8. 리스크 및 가정

### 8.1 가정

- Mom Test 1건(지난주 OO 과제)이 대표적이다.
- 학습자는 Validator를 **코드 학습 경로**로 처음 접한다.

### 8.2 리스크

| 리스크 | 완화 |
|--------|------|
| 단일 인터뷰 | STEP 2 추궁 질문 추가 |
| 행-only Validator 재발 | FR-5, FR-12 |
| Solver 선행 유혹 | Non-Goals 명시 |

---

## 9. 일정 (Session 3)

| 단계 | 산출물 |
|------|--------|
| Rule | `docs/rule_magic_square_validation.md` |
| Red | `tests/test_square_validator.py` (3 tests fail) |
| Green | `src/square_validator.py` (minimal) |
| Refactor | 중복 제거, `failed_lines` 정리 |
| Skill | validate-before-submit 초안 |

---

## 10. 참조

- `Report/01.MagicSquare_ProblemDefinition_Report.md`
- `Report/01. MagicSquare_1004 Mom Test STEP1 보고서.md`
- `Report/02. MagicSquare_1004 Session3 워크북.md`
