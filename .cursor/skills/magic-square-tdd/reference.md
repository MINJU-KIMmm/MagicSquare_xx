# D-* Logic Track 테스트 ID

| ID | Layer | 요약 |
|----|-------|------|
| D-001 | control | 행·열 OK, **주대각선**만 ≠34 → invalid (FC-2, US-1) |
| D-002 | control | **행 4개만** OK → invalid (US-2) |
| D-003 | control | **10줄** 전부 34 → valid (US-3) |
| D-004 | control | 행 OK, **열 하나** ≠34 → invalid (FC-1) |
| D-005 | control | 행·열·주대각선 OK, **반대각선**만 ≠34 → invalid (FC-3) |
| D-006 | entity | `MagicConstant` — 목표 합·격자 크기 SSOT |
| D-007 | entity | 4×4 **10줄** 합산 (행·열·대각선) 순수 계산 |
| D-008 | control | `failed_lines`에 틀린 줄 식별 (행-only early return 금지) |

파일 매핑 예: `tests/control/test_d_validator_diagonal.py` (D-001, D-005), `test_d_rows_only_not_valid.py` (D-002).
