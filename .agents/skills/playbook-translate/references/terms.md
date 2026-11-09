# 용어 결정 기준

## 결정 순서

1. **팀 용어집**: 저장소의 [`docs/GLOSSARY.md`](../../../../docs/GLOSSARY.md)를 먼저 따릅니다. 팀에서 정한 번역이 다른 자료보다 우선합니다.
2. **terms.kr**: [PyTorchKR의 AI/ML 용어집](https://terms.kr/)을 아래 스크립트로 조회합니다. 사이트는 JavaScript로 화면을 그리므로 웹페이지를 읽지 말고 JSON 데이터를 사용합니다. KREW 딥러닝 용어사전은 terms.kr에 통합되었으므로 따로 찾지 않습니다.

   ```bash
   python3 .agents/skills/playbook-translate/scripts/lookup_terms.py loss "gradient accumulation" ablation
   python3 .agents/skills/playbook-translate/scripts/lookup_terms.py --search parallel
   ```

   terms.kr는 PoC 단계이고 수록 데이터는 AI가 만든 초안입니다. 문맥에 맞지 않으면 팀 용어집에서 다르게 정할 수 있습니다. 같은 사전 안에서도 표기가 섞인 경우가 있습니다. 예를 들어 tensor parallelism은 “텐서 병렬화”, data parallel은 “데이터 병렬 처리”입니다. 이 스터디에서는 한 가지 표기로 통일합니다.
3. **둘 다 없으면** 아래 판단 기준으로 정하고, PR 본문의 “검토가 필요한 표현”에 `영어 → 선택한 번역 (근거)` 형식으로 적습니다. 리뷰에서 확정되면 팀 용어집에 추가합니다. terms.kr에 없는 용어는 [새 용어 요청 이슈](https://github.com/PyTorchKR/terms-kr/issues/new?template=new-term.yml)로 제안할 수 있습니다. 이슈 작성은 사용자가 요청한 경우에만 합니다.

## 판단 기준

| 경우 | 쓰는 방식 | 예 |
| --- | --- | --- |
| 한국어 번역어가 널리 쓰이는 개념 | 한국어 | 손실, 학습률, 사후 학습, 혼합 정밀도, 그래디언트 누적 |
| 음차가 더 익숙한 용어 | 한글 음차 | 토크나이저, 옵티마이저, 체크포인트, 그래디언트 |
| 고유명사, 약어, API 이름 | 영어 그대로 | PyTorch, Nanotron, SmolLM3, ZeRO, FSDP, AdamW, `torch.compile` |
| 번역어가 어색하거나 아직 없는 용어 | 첫 등장에 “한국어(영어)”, 이후 하나로 통일 | 중간 학습(mid-training) |

- 한 번 정한 표기는 담당 범위 전체에서 통일합니다. 같은 개념에 “손실”과 `loss`를 섞지 않습니다.
- 약어는 첫 등장에 연결한 뒤 구분을 유지합니다. 전문가 혼합(MoE), 객관식 형식(MCF), 빈칸 채우기 형식(CF), 자유 형식 생성(FG) 등입니다.
- 논문·모델·도구 이름을 부분 치환하지 않습니다. `Dataset` 하나만 한국어로 바뀐 영문 논문 제목은 허용하지 않습니다.
- 문맥에 따라 뜻이 달라지는 단어를 구분합니다. `reasoning`은 사람의 사고와 모델의 추론 능력, `compute`는 연산량·연산 비용·연산 자원 중 문맥에 맞게 옮깁니다.
- 기계적인 전역 치환은 수식 아래첨자, URL, 논문 제목까지 손상시킬 수 있으므로 사용하지 않습니다.

## 영한 혼용 줄이기

일반 개념과 동사까지 영어로 남기지 않습니다.

| 피할 표현 | 문맥에 맞는 표현 |
| --- | --- |
| `learning 용량`, `추론 time` | 학습 용량, 추론 시점·추론 시간 |
| `deployment constraints` | 배포 제약·제약 조건 |
| `The 토크나이저`, `Measuring 토크나이저 Quality` | 토크나이저, 토크나이저 품질 측정하기 |
| `loss`, `optimizer`, `context`, `downstream task` | 손실, 옵티마이저, 컨텍스트, 후속 과제 |
| `at scale` → “규모에서” | 대규모에서·규모를 키웠을 때 |
| `compute scales linearly with size` | 연산량이 모델 크기에 비례해 증가합니다. |
| `the whole post-training alphabet` | SFT, DPO, GRPO를 비롯해 여러 약어로 불리는 사후 학습 기법 |

## 아직 정하지 않은 용어

- `ablation`은 terms.kr에 없습니다. 후보는 “어블레이션”, “절제 실험”, “제거 실험”입니다. 팀이 정하기 전에는 첫 등장에 영어를 병기하고 PR에 선택 근거를 적습니다.
