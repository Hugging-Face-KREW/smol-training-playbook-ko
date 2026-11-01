# Smol Training Playbook 한국어 번역 가이드

각자 맡은 구간을 브랜치에서 번역하고, GitHub PR로 서로 리뷰합니다. 리뷰가 끝난 구간은 `main`에 머지해 바로 공개합니다.

책의 앞부분부터 순차적으로 완성해가는 MEAP 같은 방식으로 진행합니다. 번역한 구간은 한국어로, 아직 번역하지 않은 구간은 영어로 남겨둡니다. 전체 번역이 끝날 때까지 공개를 기다리지 않습니다.

## 1. 번역할 파일과 담당 범위 확인

| 구분 | 파일 | 용도 |
| --- | --- | --- |
| 번역본 | [`app/src/content/article.mdx`](app/src/content/article.mdx) | 실제 Space에 표시되는 전체 본문. 담당 구간을 이 파일에서 수정합니다. |
| 영문 원본 | [`docs/original/article.en.mdx`](docs/original/article.en.mdx) | 번역과 리뷰 때 비교할 고정 원문. 수정하지 않습니다. |
| 그림과 차트 | [`app/src/content/embeds/`](app/src/content/embeds) | 인터랙티브 그림의 문구. 본문 담당 범위와 별도로 작업 범위를 정합니다. |

영문 원본은 [초기 Space 커밋](https://huggingface.co/spaces/huggingface-KREW/smol-training-playbook-ko/commit/179c71bb4a1c10c8be98768dea04fbc2cfc8e9f9)의 `article.mdx`를 그대로 보관한 파일입니다. 번역본과 원문의 줄을 대조하는 기준이며, 렌더링용 파일은 아닙니다. 원문 Space를 나중에 업데이트하더라도 이 기준 파일은 임의로 교체하지 않습니다.

작업 전에 주차별 담당자와 범위를 확인합니다. 범위는 **시작 줄과 끝 줄을 모두 포함**하며, PR에도 아래처럼 적습니다. 다음은 형식 예시이며 실제 배정표가 아닙니다.

```text
주차: 1주차
담당자: 이름
섹션: Introduction
원문 기준 범위: L114-L146
```

## 2. 줄 번호는 반드시 유지

여러 사람이 같은 본문 파일을 나눠 번역하므로, 번역 전후 줄 번호가 같아야 합니다. 그래야 다른 사람이 맡은 범위와 리뷰 위치가 밀리지 않습니다.

- **원문 한 줄을 번역본 한 줄로 대응**시킵니다. 긴 문장도 파일 안에서 임의로 줄바꿈하지 않습니다.
- 빈 줄을 추가하거나 삭제하지 않고, 문단을 합치거나 나누지 않습니다.
- 에디터의 자동 줄바꿈(soft wrap)은 사용해도 됩니다. 화면에서만 접혀 보이고 실제 줄은 늘어나지 않습니다.
- 전체 파일 포맷팅과 저장 시 자동 포맷팅은 끕니다. Prettier로 본문 전체를 정렬하지 않습니다.
- 담당 범위 밖의 문장, 상단 metadata, import를 함께 수정하지 않습니다. 필요한 수정은 별도 PR로 제안합니다.
- 리뷰 suggestion도 선택한 줄 수와 같은 줄 수로 작성하고 적용합니다.

파일 전체 줄 수가 같다는 것만으로는 충분하지 않습니다. 앞에서 한 줄을 추가하고 뒤에서 한 줄을 삭제해도 총 줄 수는 같기 때문입니다. **각 줄의 대응과 빈 줄 위치까지 유지**해야 합니다.

MDX는 Markdown에 컴포넌트를 함께 쓰는 형식입니다. 설명 문장은 번역하되 아래 요소는 유지합니다.

| 유지할 요소 | 예시 |
| --- | --- |
| import, 파일 경로, URL | `import Image ...`, `/embeds/training-compass.html` |
| 컴포넌트 이름, 속성 이름 | `<Note title="...">`, `<Reference caption="...">` |
| 인용 키, 식별자, 수식 | 인용 참조, `id`, LaTeX 수식 |
| 코드와 실험 출력 | 명령어, 변수명, 모델의 입력·출력 예시 |

`title`, `caption`, `alt` 등의 값이 독자에게 보여주는 자연어 설명이면 담당 범위 안에서 번역합니다. 따옴표, 중괄호, 태그 등 MDX 문법은 유지하세요. 코드나 모델 출력 자체의 언어가 실험의 일부인 경우에는 번역하지 않습니다.

## 3. 작업 브랜치 만들기

최초 한 번 저장소를 받습니다. Git LFS가 없다면 먼저 설치합니다. macOS에서는 `brew install git-lfs`를 사용할 수 있습니다.

```bash
git clone https://github.com/Hugging-Face-KREW/smol-training-playbook-ko.git
cd smol-training-playbook-ko
git lfs install
git lfs pull
```

매번 작업을 시작할 때는 최신 `main`에서 새 브랜치를 만듭니다. 아래 이름의 주차와 섹션은 본인 담당에 맞게 바꿉니다. 기존 미커밋 작업이 있다면 먼저 정리하세요.

```bash
git switch main
git pull --ff-only origin main
git switch -c translate/week01-introduction
```

조직 저장소에 push 권한이 없는 경우에는 관리자에게 권한을 요청하거나, fork에서 작업하고 이 저장소의 `main`으로 PR을 보냅니다.

## 4. AI로 초안을 만들고 직접 읽기

Codex나 Claude에 담당 구간의 번역 초안을 요청합니다. 처음부터 작업 범위와 줄 유지 조건을 함께 전달하세요.

```text
Smol Training Playbook의 한국어 번역 초안을 작성해줘.
먼저 TRANSLATION_GUIDE.md를 읽고 따라줘.

원문: docs/original/article.en.mdx
수정할 파일: app/src/content/article.mdx
담당 범위: L시작-L끝 (양 끝 줄 포함)

- 담당 범위의 자연어 설명만 번역해줘.
- 원문 한 줄을 번역본 한 줄로 대응시키고, 실제 줄바꿈과 빈 줄 위치를 유지해줘.
- 줄 추가·삭제, 문단 재배치, 전체 파일 포맷팅은 하지 마.
- 코드, 실험 출력, 수식, 인용 키, URL, import, 컴포넌트 문법은 유지해줘.
- title/caption/alt 안의 자연어 설명은 번역하되 문법은 보존해줘.
- 담당 범위 밖과 영문 원본은 수정하지 마.
- 애매한 번역은 본문에 메모를 넣지 말고 대화에서 따로 알려줘.
- 수정 후 diff를 확인하고 범위·줄 대응을 지켰는지 보고해줘.
- 커밋, push, PR 생성은 하지 마.
```

AI 초안은 출발점입니다. **번역본과 영문 원본을 에디터에서 나란히 열고 담당 구간 전체를 한 번 쭉 읽습니다.** 줄 번호를 켜고 같은 줄끼리 비교하세요. 원문 Space도 함께 보면 그림과 주변 문맥을 이해하기 좋습니다.

- 원문의 뜻이 빠지거나 새 의미가 추가되지 않았는지 확인합니다.
- 수치, 단위, 비교 대상, 조건, 부정 표현이 정확한지 확인합니다.
- 기술 용어가 일관되고 한국어 문장이 자연스러운지 확인합니다.
- 캡션·표·각주가 빠지지 않았는지 확인합니다.
- 줄 대응과 MDX 문법이 유지됐는지 확인합니다.

애매한 용어와 해석은 PR 본문에 적어 리뷰어와 논의합니다. 원문이나 번역본에 검토 메모용 줄을 추가하지 않습니다.

## 5. 변경 확인, 커밋, PR

저장소 최상위에서 변경 범위를 확인합니다.

```bash
git diff -- app/src/content/article.mdx
git diff --check
git status --short
```

담당 구간만 바뀌었는지, 빈 줄과 줄바꿈이 유지됐는지 확인합니다. 필요하면 로컬 화면과 빌드도 확인하세요. Node.js 20 이상이 필요합니다.

```bash
cd app
npm install
npm run dev
# 터미널의 로컬 주소로 화면을 확인한 뒤 Ctrl+C로 종료
npm run build
cd ..
```

설치 과정에서 lock 파일이 변경됐다면 번역과 관계없는 변경을 섞지 않습니다. 커밋에는 담당 본문 파일만 지정합니다.

```bash
git add app/src/content/article.mdx
git commit -m "Translate introduction into Korean"
git push -u origin translate/week01-introduction
```

GitHub에서 **Compare & pull request**를 눌러 대상(`base`)을 `main`, 작업 브랜치(`compare`)를 본인의 번역 브랜치로 선택합니다. PR을 만든 뒤 리뷰어를 지정합니다.

PR 제목 예시: `[번역] 1주차 Introduction (L114-L146)`

PR 본문에 아래 내용을 채웁니다.

```markdown
## 번역 범위
- 주차 / 담당자:
- 섹션:
- 원문 기준 줄: L시작-L끝

## 확인
- [ ] 담당 구간 전체를 원문과 나란히 읽었습니다.
- [ ] 담당 범위 밖을 수정하지 않았습니다.
- [ ] 각 줄의 대응과 빈 줄 위치를 유지했습니다.
- [ ] 코드·수식·인용 키·링크·MDX 문법을 유지했습니다.

## 검토가 필요한 표현
- 없으면 '없음'으로 적습니다.

## 화면 / 빌드 확인
- 실행한 확인과 결과를 적습니다. 하지 않았다면 미실행으로 적습니다.
```

## 6. GitHub에서 번역 리뷰하기

리뷰어도 영문 원본과 번역본을 함께 읽습니다. PR의 **Files changed**에서 번역 정확성, 자연스러운 표현, 줄 유지 여부를 확인합니다.

정확한 수정 문구를 제안할 때는 일반 댓글 대신 **suggestion**을 사용합니다.

1. 수정할 줄에 마우스를 올리고 왼쪽의 **`+`**를 누릅니다. 여러 줄이면 `+`를 드래그해 범위를 선택합니다. 번역된 오른쪽 줄을 기준으로 선택하세요.
2. 댓글 입력창의 **Insert a suggestion** 버튼을 누릅니다. 툴팁으로 이름을 확인할 수 있습니다.
3. 생성된 suggestion 블록 안에 **선택한 줄 전체를 대체할 문구**를 적습니다. 선택한 줄 수와 빈 줄 구조를 유지합니다.
4. **Start a review** 또는 **Add review comment**로 리뷰에 추가합니다.
5. 리뷰를 마치면 **Review changes → Submit review**로 제출합니다. 보류 중인 리뷰 댓글은 제출하기 전까지 작성자에게 보이지 않습니다.

수정이 필요하면 **Request changes**, 머지해도 되면 **Approve**, 질문이나 의견만 남기면 **Comment**를 선택합니다.

예를 들어 한 줄의 번역을 고치려면 아래처럼 한 줄로 제안합니다. 실제 문구는 선택한 줄의 내용에 맞춰 작성하세요.

````markdown
조건이 드러나도록 아래 표현을 제안합니다.

```suggestion
작은 규모에서 확인한 결과가 큰 규모에서도 그대로 이어지는 것은 아닙니다.
```
````

해석을 먼저 논의해야 한다면 댓글로 질문합니다. 의견이 정리된 뒤 suggestion으로 최종 문구를 남기면 반영하기 편합니다.

## 7. 리뷰 반영과 머지

번역자는 제안을 읽고 동의하는 수정만 반영합니다.

- 한 건씩 적용: **Commit suggestion**
- 여러 건을 묶어서 적용: **Add suggestion to batch → Commit suggestions**
- 직접 고쳐야 하는 수정: 같은 브랜치에서 수정하고 커밋·push. 기존 PR에 자동으로 추가됩니다.

Suggestion을 적용하면 PR 브랜치에 새 커밋이 생깁니다. 이후 로컬에서 계속 작업하려면 해당 브랜치에서 `git pull --ff-only`로 먼저 받아오세요. 로컬 미커밋 변경은 먼저 정리합니다.

반영 뒤에는 원문과 다시 비교하고 줄 대응을 확인합니다. 논의가 끝난 댓글은 **Resolve conversation**으로 정리하고, 필요한 경우 재리뷰를 요청합니다. 담당 구간의 리뷰와 수정이 끝나면 머지합니다. 미번역 구간은 영어로 그대로 둡니다.

> 이 문서의 리뷰 절차는 팀의 작업 방식입니다. GitHub에서 승인이나 머지를 강제로 제한하는 규칙이 설정됐다는 뜻은 아닙니다.

## 8. 머지 후 공개 확인

`main`에 머지하면 **GitHub Actions 동기화 → Space 빌드 → 공개 페이지 반영** 순서로 배포됩니다. PR 작성이나 작업 브랜치 push만으로는 공개되지 않습니다.

1. [GitHub Actions](https://github.com/Hugging-Face-KREW/smol-training-playbook-ko/actions)에서 해당 커밋의 **Sync to Hugging Face Space** 성공을 확인합니다.
2. [한국어 Space](https://huggingface.co/spaces/huggingface-KREW/smol-training-playbook-ko)가 빌드를 마치고 **Running**인지 확인합니다.
3. 페이지를 새로고침해 담당 구간이 한국어로 바뀌었는지 확인합니다. Actions 성공만으로 빌드 성공까지 확인한 것은 아닙니다.

배포가 실패하면 Actions나 Space의 빌드 로그를 공유해 함께 확인합니다. 수정은 GitHub에서 진행합니다. Space에서 직접 고치면 다음 동기화 때 덮어써질 수 있습니다.

다음 주차 작업은 최신 `main`을 받은 뒤 새 브랜치에서 시작합니다.

## 참고

- [영문 원문 Space](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook)
- [GitHub 리뷰와 suggestion 사용법](https://docs.github.com/en/pull-requests/get-started/reviewing-pull-requests-quickstart)
- [GitHub suggestion 반영 방법](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/incorporating-feedback-in-your-pull-request)
