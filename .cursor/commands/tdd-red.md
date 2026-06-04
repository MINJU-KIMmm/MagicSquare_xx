# TDD RED — 실패 테스트 먼저

MagicSquare_1004 Dual-Track TDD **RED 단계만**. 구현 없이 **실패하는 테스트**를 먼저 작성한다.

## 필수 선언

응답 **첫 줄** (한국어 본문 전):

```
Phase: red | Layer: {entity|control|boundary} | Track: {D-*|U-*}
```

예: `Phase: red | Layer: control | Track: D-*`

- Logic Track → `D-*`, `tests/{entity|control}/test_d_*.py`
- UI Track → `U-*`, `tests/boundary/test_u_*.py`
- ID 목록: `.cursor/skills/magic-square-tdd/reference.md` (Logic `D-*`)

## 절차

1. **ID 확인** — 대상 `D-*` / `U-*` 선택. Mom Test·Rule(`Report/02`)과 1:1 대응 확인.
2. **파일 배치** — 레이어에 맞는 `tests/` 하위에 `test_d_*` 또는 `test_u_*` 생성·추가.
3. **AAA 테스트 작성**
   - **Arrange** — 4×4 격자 fixture, `MagicConstant` import(테스트에서 허용), 기대 결과
   - **Act** — 아직 없을 수 있는 `src/` 함수·클래스 import 및 호출
   - **Assert** — 완전한 기대값 (valid/false, `failed_lines`, `int[6]` 등)
4. **import 허용** — RED에서는 `src/` **수정 없이** import만; `ImportError` 또는 assertion FAIL 모두 RED 성공.
5. **pytest FAIL 확인** — 아래 명령 실행; **반드시 1개 이상 FAIL**. PASS면 assert 부족 또는 잘못된 GREEN.
6. **보고** — 아래 § 보고 형식으로 마무리.

## pytest 예시 (bash)

```bash
# 대상 테스트 1파일 (RED 직후)
pytest tests/control/test_d_rows_only_not_valid.py -v

# entity 레이어 RED
pytest tests/entity/test_d_magic_constant.py -v

# UI Track RED
pytest tests/boundary/test_u_grid_display.py -v

# Logic Track 회귀 확인 금지 — RED는 대상 파일만
# pytest tests/entity tests/control   ← RED 단계에서 전체 Green 확인하지 않음
```

설치: `pip install -e ".[dev]"` (최초 1회)

## 보고

RED 완료 시 다음만 출력:

| 항목 | 내용 |
|------|------|
| **테스트 ID** | `D-xxx` / `U-xxx` |
| **FAIL 요약** | 실패 테스트 함수명 + pytest 메시지 1~2줄 |
| **변경 파일** | `tests/` 아래 경로만 (예: `tests/control/test_d_*.py`) |

## 금지

- `src/` **수정** (GREEN까지 구현 금지)
- Logic Track(`D-*`)에서 **Domain Mock** (entity/control Mock·Stub)
- **assert 완화** — 기대값 느슨하게 변경, `pytest.skip`, `pytest.mark.xfail`
- RED 통과를 위한 **테스트 삭제·주석 처리**
- `34`·`16` **리터럴** — 테스트 Arrange에서도 `MagicConstant` 사용
- entity 테스트에서 **boundary/control import**
- **git commit·push** (사용자 요청 시만)
