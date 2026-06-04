# Review ECB — 계약 위반만 표로 리뷰

MagicSquare_1004 **ECB·도메인 계약** 정적 리뷰. **코드 수정 금지** — 위반만 표로 보고한다.

## 필수 선언

응답 **첫 줄**:

```
Phase: review | Scope: {src/|tests/|전체} | Mode: read-only
```

## 절차

1. **범위 확인** — 사용자가 지정한 파일·디렉터리, 또는 `src/` + `tests/` 전체.
2. **읽기 전용** — 파일 내용·import·테스트 패턴만 분석. 수정·포맷·리팩터 **하지 않음**.
3. **체크 5항** — 아래 § 체크리스트 기준으로 스캔.
4. **위반 표 출력** — § 보고 형식. 위반 0건이면 「위반 없음」 한 줄.
5. **수정 제안** — 표의 `권장` 열에 **한 줄**만 (코드 패치·diff 출력 금지).

## 체크리스트 (계약)

| # | 항목 | PASS 기준 | FAIL 예 |
|---|------|-----------|---------|
| 1 | **import 방향** | `boundary→control→entity`; entity는 `entity` 내부만; control은 entity만; boundary는 control(+표시 DTO) | entity가 control/boundary import; control이 boundary import |
| 2 | **entity E001~E005** | entity/control에 E001~E005 **문자열·분기·raise·매핑 없음** | entity에서 빈칸 수·범위·중복 검증 후 `E003` 반환 |
| 3 | **int[6] 1-index** | 솔루션 `[r1,c1,n1,r2,c2,n2]` 좌표 **1~4** (0-index 금지) | `(0,0)` 반환, 0-based API를 entity가 노출 |
| 4 | **MagicConstant SSOT** | `34`·`16`·격자 크기는 `MagicConstant`(또는 동등 SSOT)만 | 산술·assert·기본값에 `34`/`16` 리터럴 |
| 5 | **Logic Track Domain Mock** | `tests/entity/`, `tests/control/`, `test_d_*`에 entity/control **Mock·patch·Fake Domain 없음** | `@patch("control.square_validator.MagicSquare")` on Logic test |

참고: `.cursorrules`, `.cursor/skills/magic-square-tdd/SKILL.md`

## 보고 (위반 표)

위반이 있을 때만 아래 표 사용 (복수 행 가능):

| # | 체크 | 파일:줄 | 위반 내용 | 권장 (1줄) |
|---|------|---------|-----------|------------|
| 1 | import 방향 | `src/entity/foo.py:3` | `from control import …` | import 제거, entity 내부로 이동 |
| 2 | entity E001~E005 | … | … | boundary로 I/O 검증 이전 |
| 3 | int[6] 1-index | … | … | 좌표 +1 또는 boundary 변환 |
| 4 | MagicConstant SSOT | … | … | `MagicConstant.TARGET_SUM` 사용 |
| 5 | Logic Domain Mock | … | … | 실제 domain 객체 또는 fixture |

**요약** (표 아래 1줄): `위반 N건 / 검사 M파일`

위반 0건:

```
위반 없음 — 검사 M파일, 체크 5항 PASS
```

## 금지

- **코드·테스트 수정** (리뷰 Command는 read-only)
- 위반 없는데 **스타일·리팩터** 코멘트
- **git commit·push**
- Skill·Command 파일 생성·수정
