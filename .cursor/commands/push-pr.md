# Push & PR — 현재 브랜치만 푸시 후 PR

MagicSquare_1004 **변경사항 → PR** 워크플로. **현재 브랜치만** 원격에 올리고, `main`과 차이가 있으면 PR을 연다.

## 필수 선언

응답 **첫 줄**:

```
Phase: push-pr | Branch: {현재브랜치} | Base: main
```

## 절차

1. **상태 확인** — `git status`, `git branch -vv`, `git log main..HEAD --oneline`
2. **커밋** — 미커밋 변경이 있고 사용자가 업로드·PR을 요청했을 때만 커밋 (메시지: 변경 요약 1~2문장)
3. **main과 비교**
   - `main..HEAD` 커밋 **0건** → PR 불가; “변경 없음” 보고 후 종료
   - **1건 이상** → 4단계 진행
4. **현재 브랜치만 푸시** — `git push -u origin HEAD`
   - **`git push --all` 금지**
   - **`git branch -f {다른브랜치}` 금지**
5. **PR 생성**
   - `gh` 사용 가능: `gh pr create --base main --head {브랜치} --title "..." --body "..."`
   - `gh` 없음: Compare URL 출력 (아래 § URL)
6. **보고** — § 보고 형식

## PR 본문 템플릿

```markdown
## Summary
- (변경 1~3 bullet)

## Phase / Layer / Track
- Phase: red|green|refactor|docs|...
- Layer: entity|control|boundary|...
- Track: D-*|U-*|—

## Test plan
- [ ] pytest (해당 범위)
- [ ] /review-ecb (해당 시)
```

## Compare URL (gh 미설치 시)

```
https://github.com/MINJU-KIMmm/MagicSquare_xx/compare/main...{브랜치}?expand=1
```

## 브랜치 역할

| 브랜치 | 용도 |
|--------|------|
| `main` | 통합·머지 대상 (**직접 push 금지**, PR로만 반영) |
| `spec` | Rule·문서·스펙 |
| `red` | TDD RED (실패 테스트) |
| `green` | TDD GREEN (최소 구현) |
| `refactoring` | TDD REFACTOR |
| `staging` | PR 전 최종 확인 |
| `new_features` | 기능 확장 |

작업 브랜치에서만 커밋·푸시. 다른 브랜치를 현재 커밋에 **강제 맞추지 않음**.

## 보고

| 항목 | 내용 |
|------|------|
| **브랜치** | `{branch}` |
| **main 대비 커밋** | N건 (해시 목록) |
| **push** | 성공 / 실패 |
| **PR** | URL 또는 Compare 링크 / “변경 없음” |

## 금지

- `git push --all origin`
- `git branch -f` 로 타 브랜치 동기화
- `main`에 직접 push (사용자가 명시적으로 요청한 경우 제외)
- PR 없이 모든 브랜치를 동일 커밋으로 맞추기
