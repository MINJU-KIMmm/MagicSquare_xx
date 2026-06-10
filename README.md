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
│   ├── PRD.md
│   └── tdd-red-todo.md                 # RED 단계 To-Do (상세)
├── src/entity|control|boundary/        # ECB (구현 예정)
├── tests/entity|control|boundary/      # Dual-Track pytest
├── Report/
└── Prompting/
```

> Harness: `pyproject.toml` + `src/`·`tests/`. `pyproject.toml`의 `pythonpath`·`--import-mode=importlib`로 `entity` import.

---

## 개발 환경 (`.venv`)

프로젝트 루트에서 **가상환경**을 만들고 pytest를 설치한다. (`src/` 패키지 설치 없이 `pythonpath = ["src"]`로 테스트)

**Windows PowerShell (최초 1회):**

```powershell
cd C:\DEV\MagicSquare_xx
python -m venv .venv
.\scripts\setup-venv.ps1
# 또는
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

**활성화 후 테스트:**

```powershell
.\.venv\Scripts\Activate.ps1
pytest
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
python -m pytest tests/entity/test_d_loc_01.py -v
```

**활성화 없이:**

```powershell
.\.venv\Scripts\python.exe -m pytest tests/entity/test_d_loc_01.py -v
```

회사 프록시 등으로 pip SSL 오류가 나면 `scripts\setup-venv.ps1`의 `--trusted-host` 옵션을 사용한다. Cursor/VS Code는 인터프리터를 **`.venv\Scripts\python.exe`** 로 선택한다.

---

## 문서

| 문서 | 설명 |
|------|------|
| [Problem Definition Report](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test 기반 문제 정의 |
| [PRD](docs/PRD.md) | 기능 요구사항, 성공 기준, 8계층 로드맵 |
| [Mom Test STEP1 보고서](Report/01.%20MagicSquare_1004%20Mom%20Test%20STEP1%20보고서.md) | 인터뷰 원본·증거 |
| [Session 3 워크북](Report/02.%20MagicSquare_1004%20Session3%20워크북.md) | Rule / Command / Test Loop |
| [RED To-Do (상세)](docs/tdd-red-todo.md) | Dual-Track RED 설계·Given/Then·pytest 경로 |
| [RED Phase Planning 보고서](Report/04.%20MagicSquare_1004%20RED%20Phase%20Planning%20보고서.md) | RED 설계·README 체크리스트 세션 |
| [RED 작업 보고서](Report/05.%20MagicSquare_1004%20RED%20%EC%9E%91%EC%97%85%20%EB%B3%B4%EA%B3%A0%EC%84%9C.md) | RED 스켈레톤·브랜치 정리·D-LOC-01 |
| [GREEN 작업 보고서](Report/06.%20MagicSquare_1004%20GREEN%20%EC%9E%91%EC%97%85%20%EB%B3%B4%EA%B3%A0%EC%84%9C.md) | D-LOC-01 최소 구현·`.venv` |
| [Golden Master 보고서](Report/07.%20MagicSquare_1004%20Golden%20Master%20%EB%B3%B4%EA%B3%A0%EC%84%9C.md) | D-SOL-01 golden · matched 검증 |

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
| ECB Harness + `.cursorrules` | ✅ 완료 |
| **RED** (`red` 브랜치) | ⬜ 진행 중 — D-LOC-01 skeleton 등 |
| **GREEN** (`green` 브랜치) | ✅ **entity** D-LOC-01 · D-SOL-01 PASS + Golden Master |
| REFACTOR (`refactoring`) | ⬜ 예정 |

상세 Given/Then·pytest 명령: [`docs/tdd-red-todo.md`](docs/tdd-red-todo.md)

---

## RED 단계 체크리스트

Dual-Track TDD **RED** — `tests/`만 작성, **pytest FAIL** 확인 후 체크. GREEN 전 **`src/` 수정 금지**.

**공통 금지:** `skip`/`xfail`, assert 완화, Logic Track Domain Mock, entity에서 E001~E005 emit.

### 권장 순서

- [ ] 1. Logic · entity — D-006, D-007, D-LOC-01~03
- [ ] 2. Logic · control — D-001~D-003 → D-004, D-005, D-008
- [ ] 3. Boundary · 입력 — U-IN-01~06
- [ ] 4. Boundary · 출력·플로우·표시 — U-OUT, U-FLOW, U-DISP

**Session 3 1차 (`red` 브랜치):** **D-001, D-002, D-003** (Mom Test 3건) 우선.

### RED 완료 기준 (묶음마다)

- [ ] `test_d_*` / `test_u_*` 작성 + docstring에 Test ID
- [ ] `python -m pytest <파일> -v` → **1건 이상 FAIL**
- [ ] Phase 선언: `Phase: red | Layer: … | Track: …`

---

### Logic · entity (`tests/entity/`)

**Fixture (`conftest.py`, 로직 없음)**

- [ ] G1_GRID — 빈칸 (2,4), (3,1)
- [ ] G2_GRID — 빈칸 (2,1), (2,3)
- [ ] G_valid — 완성 4×4 (D-007)
- [ ] 빈칸 sentinel = `None` 확정

**테스트**

- [ ] **D-006** — `MagicConstant`: `TARGET_SUM==34`, `GRID_SIZE==4`
- [ ] **D-007** — 10줄 합산, G_valid 전부 34
- [x] **D-LOC-01** — `find_blank_coords()` → `[(2,2),(3,3)]` row-major (G1, `0` 빈칸)
- [ ] **D-LOC-02** — 좌표 1-index (0 없음)
- [ ] **D-LOC-03** — G2 → `[(2,1),(2,3)]`

---

### Logic · control · Validator (`tests/control/`) — Session 3 핵심

- [ ] **D-001** — 주대각선만 ≠34 → `valid=False`, `diag_main` in `failed_lines` (US-1)
- [ ] **D-002** — 행 4개만 OK → `valid=False` (US-2)
- [ ] **D-003** — 10줄 전부 34 → `valid=True`, `failed_lines=[]` (US-3)
- [ ] **D-004** — 열 하나 ≠34 → `valid=False`, `col_*` in `failed_lines`
- [ ] **D-005** — 반대각선만 ≠34 → `valid=False`, `diag_anti` in `failed_lines`
- [ ] **D-008** — `failed_lines`에 틀린 열만 (행-only early return 없음)

---

### Boundary · UI Track (`tests/boundary/`)

**현재 RED 묶음** — `Phase: red | Layer: boundary | Track: UI` · **U-IN-01, U-IN-02**

| Test ID | Given | Then | Expected RED Failure |
|---------|-------|------|----------------------|
| **U-IN-01** | `grid=None` | `E003` `INVALID_NULL` | `ModuleNotFoundError` / `ImportError` |
| **U-IN-02** | `grid=3×4` (크기 불일치) | `E001` `INVALID_SIZE` | `AssertionError` |

| 항목 | 내용 |
|------|------|
| **파일** | `tests/boundary/test_u_input_validation.py` |
| **함수명 (후보)** | `test_u_in_01_grid_none_returns_e003` · `test_u_in_02_grid_3x4_returns_e001` |
| **pytest (1건)** | `python -m pytest tests/boundary/test_u_input_validation.py::test_u_in_01_grid_none_returns_e003 -v` |
| **pytest (묶음)** | `python -m pytest tests/boundary/test_u_input_validation.py -v` |
| **Mock** | UI Track — control **인터페이스** Mock 허용 · Domain Mock 금지 |
| **금지** | entity E001~E005 emit · `skip`/`xfail` · GREEN 전 `src/` 수정 |

**입력 (E001~E005) — 전체**

- [ ] **U-IN-01** — `grid=None` → `E003 INVALID_NULL` ← **현재 묶음**
- [ ] **U-IN-02** — `grid=3×4` → `E001 INVALID_SIZE` ← **현재 묶음**
- [ ] **U-IN-03** — 빈칸 0개 → `E002 INVALID_BLANKS`
- [ ] **U-IN-04** — 빈칸 3개+ → `E002 INVALID_BLANKS`
- [ ] **U-IN-05** — 값 17/0 → `E004 INVALID_RANGE`
- [ ] **U-IN-06** — 중복 → `E005 INVALID_DUPLICATE`

**출력 · 플로우 · 표시**

- [ ] **U-OUT-01** — G1 → `len(result)==6`
- [ ] **U-OUT-02** — G1 → 좌표 1-index (`result[0], result[2] ∈ {1..4}`)
- [ ] **U-FLOW-01** — `grid=None` → `Solver.execute()` 0회
- [ ] **U-FLOW-02** — E002 입력 → `SquareValidator.validate()` 0회
- [ ] **U-DISP-01** — `E003` → `ResultDisplay` 표시

**Fixture**

- [ ] G1 (entity와 공유)
- [ ] invalid grids (3×4, 0/3 blank, 범위·중복)

---

### 문서 (RED 병행)

- [ ] `docs/rule_magic_square_validation.md` — 10줄 Rule (FR-7)
- [ ] `docs/PRD.md` — FR-LOC-01, E001~E007 코드표

---

## GREEN 단계 (`green` 브랜치)

**RED가 끝난 묶음만** `green`에서 `src/` 최소 구현 → 해당 테스트 **PASS**.

```bash
git checkout green
git merge red             # RED 테스트·문서 반영 (RED 완료 후)
.\.venv\Scripts\python.exe -m pytest tests/entity/ -v
git push -u origin HEAD
# PR: base=main, compare=green
```

| Test ID | 상태 (`green`) |
|---------|----------------|
| **D-LOC-01** | ✅ `find_blank_coords` PASS |
| **D-SOL-01** | ✅ `solve_step_a` PASS + Golden matched |

### Golden Master (`D-SOL-01`)

| 항목 | 경로 |
|------|------|
| 헬퍼 | `tests/_approval.py` |
| Golden | `tests/golden/d_sol_01_g1_step_a.approved.txt` |
| 테스트 | `tests/entity/test_d_sol_01.py::test_d_sol_01_step_a_success` |

```powershell
# 기준 파일 생성 (1회)
$env:UPDATE_GOLDEN="1"
.\.venv\Scripts\python.exe -m pytest tests/entity/test_d_sol_01.py::test_d_sol_01_step_a_success -v
Remove-Item Env:UPDATE_GOLDEN

# 검증 (matched)
.\.venv\Scripts\python.exe -m pytest tests/entity/test_d_sol_01.py::test_d_sol_01_step_a_success -v
```

- [x] entity GREEN — D-LOC-01, D-SOL-01
- [x] Golden Master — `d_sol_01_g1_step_a.approved.txt` matched
- [ ] `pytest tests/control/ -v` — control Validator (Session 3)

---

## Git · PR 워크플로

**원칙:** TDD **단계마다 브랜치 분리** → **`main`으로 PR**.

| 브랜치 | TDD 단계 | 작업 내용 |
|--------|----------|-----------|
| `main` | 통합 | PR 머지 대상 |
| **`red`** | **RED** | `tests/` 실패 테스트만 (`src/` 수정 금지) |
| **`green`** | **GREEN** | `src/` 최소 구현 (테스트 PASS) |
| `refactoring` | REFACTOR | 구조 개선, 동작 동일 |
| `spec` | 문서·스펙 | PRD, Rule, RED 설계 문서 |
| `staging` | 확인 | PR 전 검토 |

```bash
# RED
git checkout red
# tests/ 작성 → pytest FAIL
git push -u origin HEAD

# GREEN (red 완료 후)
git checkout green
git merge red
# src/ 작성 → pytest PASS
git push -u origin HEAD
```

- **하지 않을 것:** RED를 `spec`/`green`에 넣기, GREEN을 `red`에 넣기, `git push --all`, `branch -f`로 타 브랜치 강제 동기화

- **하지 않을 것:** `git push --all`, 모든 브랜치를 같은 커밋으로 `branch -f` (PR diff 없어짐)
- Cursor: `/push-pr` Command, PR 템플릿 `.github/pull_request_template.md`

---

## 참고

- 설계 맥락: ECB (`MagicSquare`, `SquareValidator`, `Solver`, `GridUI` 등)
- Mom Test 스타일: [Rob Fitzpatrick — The Mom Test](https://momtestbook.com/)
