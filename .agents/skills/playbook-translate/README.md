# playbook-translate skill

From Smol to Ultra Scale 스터디의 Playbook 번역·교정·검토용 skill입니다. 이 저장소에 포함되어 있으므로 따로 설치하지 않습니다. `git pull`로 최신 `main`을 받으면 skill도 함께 업데이트됩니다.

- **Codex**: 저장소의 `.agents/skills/playbook-translate/`를 읽습니다. `$playbook-translate`로 호출합니다.
- **Claude Code**: `.claude/skills/playbook-translate`가 같은 폴더를 가리키는 심볼릭 링크입니다. `/playbook-translate`로 호출합니다. Windows에서 링크가 일반 파일로 받아지면 `.agents/skills/playbook-translate/` 폴더를 `.claude/skills/` 아래에 복사해서 사용하세요.
- 예전에 zip으로 받아 `~/.codex/skills/playbook-translate/` 등에 설치한 skill이 있다면 지워 주세요. 같은 이름의 skill이 두 개 있으면 옛 지침이 적용될 수 있습니다.

Python 3 스크립트 두 개(`check_translation.py` 검사, `lookup_terms.py` terms.kr 용어 조회)는 표준 라이브러리만 사용합니다. 용어 조회에는 인터넷 연결이 필요합니다.

**저장소 최상위에서** 아래처럼 요청합니다.

```text
$playbook-translate로 Smol 3주차 담당 구간을 번역해줘.
TRANSLATION_GUIDE.md와 배정표를 먼저 확인하고,
원문 한 줄 ↔ 번역 한 줄, 빈 줄 위치를 유지해줘.
커밋·push·PR 생성은 하지 마.
```

기존 번역을 읽기만 하는 리뷰는 다음처럼 요청합니다.

```text
$playbook-translate로 Smol 1주차 번역을 원문과 대조 검토해줘.
파일은 수정하지 말고, 오역·누락·용어·문체와 원문 자체 오류를 나눠 알려줘.
```

Ultra는 현재 저장소의 원문·번역 파일과 배정 범위가 정해져 있어야 합니다. Smol의 줄 번호를 그대로 쓰지 않습니다.

문체는 “-습니다 / -입니다”, 저자는 “우리”, 독자는 “여러분”입니다. 직역보다 읽기 편한 한국어를 우선하되 원문의 내용은 바꾸지 않습니다. “그것/이것/그들” 같은 대명사와 문장을 잇는 콜론은 쓰지 않습니다. 용어는 [팀 용어집](../../../docs/GLOSSARY.md), terms.kr, 판단 기준 순서로 정합니다. 코드·수식·논문명·모델명·URL은 보존합니다.

검사 도구의 FAIL은 반드시 고치고, WARN은 하나씩 판단합니다. 검사에 통과해도 뜻이 같은지, 각 줄 내용이 원문과 같은 줄에 있는지, 그림과 MDX가 제대로 동작하는지는 사람이 원문·diff·화면을 확인해야 합니다. skill은 팀의 동료 리뷰를 대체하지 않습니다.
