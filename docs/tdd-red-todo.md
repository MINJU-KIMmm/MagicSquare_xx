# MagicSquare_1004 — RED 단계 To-Do List

| 항목 | 내용 |
|------|------|
| 문서 | TDD RED 설계 · Dual-Track To-Do |
| 버전 | 0.1 |
| 일자 | 2026-06-04 |
| 상태 | Draft — `tests/` 미구현 (Harness만 존재) |
| 근거 | `docs/PRD.md`, `.cursorrules`, `.cursor/skills/magic-square-tdd/reference.md`, Report/02 |

---

## Dual-Track 요약

| Track | 레이어 | 테스트 ID | 파일 패턴 | Then (기대값) | Domain Mock |
|-------|--------|-----------|-----------|---------------|-------------|
| **Boundary** | `boundary` | `U-*` | `tests/boundary/test_u_*.py` | **E001~E007** | 허용 |
| **Logic** | `entity`, `control` | `D-*` | `tests/entity/`, `tests/control/` | 도메인 결과 (`valid`, `failed_lines`, `blank_coords` 등) | **금지** |

**금지 (RED 공통):** `src/` 수정(GREEN 전), `skip`/`xfail`, assert 완화, Logic Track Domain Mock, entity에서 E001~E005 emit.

---

## 권장 RED 진행 순서

- [ ] **1.** Logic · entity — D-006, D-007, D-LOC-01~03
- [ ] **2.** Logic · control — D-001, D-002, D-003 → D-004, D-005, D-008
- [ ] **3.** Boundary · 입력 — U-IN-01~06
- [ ] **4.** Boundary · 출력·플로우·표시 — U-OUT-01~02, U-FLOW-01~02, U-DISP-01

> Session 3 PRD In Scope는 Validator 중심 → **`red` 브랜치 1차 목표: D-001~D-003** (Report/02 Mom Test 3건). U-*·D-LOC는 Entity/Boundary 확장 시 진행.

---

## Logic Track — Entity (`tests/entity/`)

| 파일 (예상) | `test_d_magic_constant.py`, `test_d_line_sums.py`, `test_d_loc_01.py` |
|-------------|------------------------------------------------------------------------|

### D-006 · D-007 · MagicConstant / 10줄 합산

- [ ] **D-006** — `MagicConstant` SSOT  
  - **Given:** (없음) import  
  - **Then:** `TARGET_SUM == 34`, `GRID_SIZE == 4`  
  - **Expected RED:** `ImportError`  
  - **pytest:** `tests/entity/test_d_magic_constant.py -v`

- [ ] **D-007** — 4×4 **10줄** 합산 (순수 계산)  
  - **Given:** 완성 격자 **G_valid** (10줄 합 34)  
  - **Then:** 10줄 합 전부 `MagicConstant.TARGET_SUM`  
  - **Expected RED:** `ImportError` / `AssertionError`  
  - **pytest:** `tests/entity/test_d_line_sums.py -v`

### D-LOC-01~03 · 빈칸 좌표 (FR-LOC-01 확정안)

- [ ] **D-LOC-01** — `blank_coords` row-major  
  - **Given:** **G1**, 빈칸 `None` at (2,4), (3,1) — 1-index  
  - **Then:** `blank_coords() == [(2, 4), (3, 1)]`  
  - **Expected RED:** `ImportError` / `AttributeError`  
  - **pytest:** `tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v`

- [ ] **D-LOC-02** — 좌표 1-index  
  - **Given:** **G1**  
  - **Then:** 모든 `r, c ∈ {1, 2, 3, 4}` (0 없음)  
  - **Expected RED:** `AssertionError`  
  - **pytest:** `tests/entity/test_d_loc_01.py::test_d_loc_02_blank_coords_one_indexed -v`

- [ ] **D-LOC-03** — 동일 행 좌→우  
  - **Given:** **G2**, 빈칸 (2,1), (2,3)  
  - **Then:** `blank_coords() == [(2, 1), (2, 3)]`  
  - **Expected RED:** `AssertionError`  
  - **pytest:** `tests/entity/test_d_loc_01.py::test_d_loc_03_blank_coords_same_row_left_to_right -v`

### Entity fixture To-Do (conftest — 로직 없음)

- [ ] `tests/entity/conftest.py` — **G1_GRID** (빈칸 (2,4), (3,1))  
- [ ] `tests/entity/conftest.py` — **G2_GRID** (빈칸 (2,1), (2,3))  
- [ ] `tests/entity/conftest.py` — **G_valid** (완성 4×4, D-007용)  
- [ ] **판단 T1:** 빈칸 sentinel = `None` (E002/E003는 boundary 전담)

**G1_GRID (참고):**

```text
[[8, 3, 4, 12], [1, 10, 11, None], [None, 7, 6, 15], [4, 13, 16, 1]]
```

**G2_GRID (참고):**

```text
[[8, 3, 4, 12], [None, 10, None, 14], [2, 7, 6, 15], [4, 13, 16, 1]]
```

---

## Logic Track — Control · Validator (`tests/control/`)

| 파일 (예상) | `test_d_validator_diagonal.py`, `test_d_rows_only_not_valid.py`, `test_d_validator_full.py` |
|-------------|----------------------------------------------------------------------------------------------|

### Session 3 / Mom Test 핵심 (우선)

- [ ] **D-001** — 주대각선만 실패 (US-1, FC-2, FR-6)  
  - **Given:** 행·열 OK, **주대각선** ≠ 34  
  - **Then:** `valid is False`, `"diag_main" in failed_lines`  
  - **Expected RED:** `ImportError` / `AssertionError`  
  - **PRD 매핑:** `test_rows_ok_but_main_diagonal_fails`

- [ ] **D-002** — 행 4개만 OK (US-2, FR-5)  
  - **Given:** **행 4개** 합=34, 열·대각 미충족  
  - **Then:** `valid is False`  
  - **Expected RED:** `AssertionError`  
  - **PRD 매핑:** `test_all_rows_pass_is_not_valid`

- [ ] **D-003** — 10줄 전부 OK (US-3, DR-4)  
  - **Given:** **10줄** 전부 합=34  
  - **Then:** `valid is True`, `failed_lines == []`  
  - **Expected RED:** `AssertionError`  
  - **PRD 매핑:** `test_checklist_covers_ten_lines`

### FC·FR 확장

- [ ] **D-004** — 열 하나 실패 (FC-1)  
  - **Given:** 행 OK, **열 하나** ≠ 34  
  - **Then:** `valid is False`, `"col_*" in failed_lines`  
  - **Expected RED:** `AssertionError`

- [ ] **D-005** — 반대각선만 실패 (FC-3)  
  - **Given:** 행·열·주대각 OK, **반대각선** ≠ 34  
  - **Then:** `valid is False`, `"diag_anti" in failed_lines`  
  - **Expected RED:** `AssertionError`

- [ ] **D-008** — `failed_lines` 식별 (FR-4, FR-5)  
  - **Given:** D-004와 동일 격자  
  - **Then:** `failed_lines`에 **틀린 열만** (행-only early return 없음)  
  - **Expected RED:** `AssertionError`

---

## Boundary Track — 입력 검증 (`tests/boundary/`)

| 파일 (예상) | `tests/boundary/test_u_input_validation.py` |
|-------------|---------------------------------------------|

- [ ] **U-IN-01** — null 입력  
  - **Given:** `grid=None`  
  - **Then:** `E003` `INVALID_NULL`  
  - **Expected RED:** `ModuleNotFoundError` / `ImportError`

- [ ] **U-IN-02** — 크기 불일치  
  - **Given:** `grid=3×4`  
  - **Then:** `E001` `INVALID_SIZE`  
  - **Expected RED:** `AssertionError`

- [ ] **U-IN-03** — 빈칸 0개  
  - **Given:** 빈칸 **0개** (DR-5 위반)  
  - **Then:** `E002` `INVALID_BLANKS`  
  - **Expected RED:** `AssertionError`

- [ ] **U-IN-04** — 빈칸 3개 이상  
  - **Given:** 빈칸 **3개** 이상  
  - **Then:** `E002` `INVALID_BLANKS`  
  - **Expected RED:** `AssertionError`

- [ ] **U-IN-05** — 범위 밖 값  
  - **Given:** 셀 값 **17** 또는 **0** (DR-2 위반)  
  - **Then:** `E004` `INVALID_RANGE`  
  - **Expected RED:** `AssertionError`

- [ ] **U-IN-06** — 중복  
  - **Given:** 숫자 **중복** (DR-2)  
  - **Then:** `E005` `INVALID_DUPLICATE`  
  - **Expected RED:** `AssertionError`

---

## Boundary Track — 출력 · 플로우 · 표시

| 파일 (예상) | `tests/boundary/test_u_solver_flow.py`, 표시용 `test_u_result_display.py` |
|-------------|----------------------------------------------------------------------------|

- [ ] **U-OUT-01** — 솔루션 길이  
  - **Given:** 유효 입력 **G1**  
  - **Then:** `len(result) == 6` (`[r1,c1,n1,r2,c2,n2]`)  
  - **Expected RED:** `pytest.fail("RED")` / `ImportError`

- [ ] **U-OUT-02** — 1-index 좌표  
  - **Given:** 유효 입력 G1, 솔버 성공 가정  
  - **Then:** `result[0], result[2] ∈ {1,2,3,4}`  
  - **Expected RED:** `AssertionError`

- [ ] **U-FLOW-01** — null 시 솔버 미호출  
  - **Given:** `grid=None`  
  - **Then:** `Solver.execute()` **0회**  
  - **Expected RED:** `pytest.fail("RED")` (Mock 카운터)

- [ ] **U-FLOW-02** — 입력 오류 시 Validator 미호출  
  - **Given:** `E002` 입력 (빈칸 0개)  
  - **Then:** `SquareValidator.validate()` **0회**  
  - **Expected RED:** `pytest.fail("RED")`

- [ ] **U-DISP-01** — 오류 표시  
  - **Given:** `E003` 발생  
  - **Then:** `ResultDisplay`에 `E003` 표시  
  - **Expected RED:** `AssertionError` / `ImportError`

### Boundary fixture To-Do

- [ ] **G1** — Logic entity와 동일 4×4 유효 입력 fixture 공유  
- [ ] invalid grids — 3×4, 0 blank, 3 blank, out-of-range, duplicate (U-IN-02~06용)

---

## 문서 · PRD 후속 To-Do

- [ ] `docs/PRD.md` §4.6 — **FR-LOC-01** (`MagicSquare.blank_coords`, row-major, 1-index) 명문화  
- [ ] `docs/rule_magic_square_validation.md` — 10줄 Rule SSOT (FR-7)  
- [ ] `docs/PRD.md` — E001~E007 코드표 boundary 전담 정의  
- [ ] `.cursor/commands/red-test-plan.md`, `red-skeleton.md` — (선택) 슬래시 커맨드 추가

---

## RED 완료 체크 (묶음 단위)

각 To-Do 완료 시:

- [ ] 대상 `test_u_*` / `test_d_*` 작성 (`tests/`만, `src/` 없음)
- [ ] `python -m pytest <파일> -v` → **1건 이상 FAIL** 확인
- [ ] docstring에 Test ID (`D-*` / `U-*`) 명시
- [ ] Phase 선언: `Phase: red | Layer: … | Track: …`

---

## 참조

| 문서 | 경로 |
|------|------|
| PRD | `docs/PRD.md` |
| Logic ID 목록 | `.cursor/skills/magic-square-tdd/reference.md` |
| Session 3 워크북 | `Report/02. MagicSquare_1004 Session3 워크북.md` |
| TDD RED Command | `.cursor/commands/tdd-red.md` |
