# 번역 용어집

Smol·Ultra Playbook 번역에서 쓰는 용어 표기입니다. **현재는 초안입니다.** 이 문서를 추가한 PR의 리뷰에서 함께 확정합니다.

## 쓰는 방법

1. 이 용어집에 있는 용어는 여기 적힌 표기를 따릅니다.
2. 없는 용어는 [용어 판단 기준](../.agents/skills/playbook-translate/references/terms.md)에 따라 표기를 제안하고, PR 본문의 “검토가 필요한 표현”에 `영어 → 선택한 번역 (근거)` 형식으로 적습니다.
3. 리뷰에서 표기가 확정되면 이 용어집에 추가합니다.

공통 원칙은 아래와 같습니다.

- 한 번 정한 표기는 문서 전체에서 통일합니다.
- 약어의 첫 등장 표기는 [괄호와 약어 기준](../.agents/skills/playbook-translate/references/terms.md#괄호와-약어)을 따릅니다.
- “~ 학습”은 띄어 씁니다. 사전 학습, 중간 학습, 사후 학습, 강화 학습
- 고유명사, 라이브러리, 논문 원제, API 이름은 영어 그대로 둡니다. 예: PyTorch, Nanotron, SmolLM3, ZeRO, FSDP, AdamW, `torch.compile`

“근거” 열의 `terms.kr`은 기존 표기의 출처입니다. `팀 표기`는 이 프로젝트에서 정한 표기이며, `제안`은 리뷰에서 검토할 표기입니다.

## 학습 일반

| 영어 | 한국어 표기 | 근거 | 비고 |
| --- | --- | --- | --- |
| loss | 손실 | terms.kr | `loss`와 섞어 쓰지 않습니다. |
| learning rate | 학습률 | terms.kr | |
| learning rate schedule | 학습률 스케줄 | 제안 | |
| warmup | 워밍업 | 제안 | |
| weight decay | 가중치 감쇠(weight decay) | 제안 | |
| gradient | 그래디언트 | terms.kr | “기울기”와 섞어 쓰지 않습니다. |
| gradient accumulation | 그래디언트 누적 | terms.kr | |
| gradient clipping | 그래디언트 클리핑 | 제안 | |
| optimizer | 옵티마이저 | terms.kr | |
| hyperparameter | 하이퍼파라미터 | terms.kr | |
| checkpoint | 체크포인트 | terms.kr | |
| batch size | 배치 크기 | 제안 | |
| dataset | 데이터셋 | 팀 표기 | |
| tokenizer | 토크나이저 | terms.kr | |
| prompt | 프롬프트 | 팀 표기 | |
| sequence | 시퀀스 | 팀 표기 | |
| packing | 패킹 | 팀 표기 | |
| context length | 컨텍스트 길이 | 제안 | |
| context window | 컨텍스트 윈도우 | 팀 표기 | |
| benchmark | 벤치마크 | terms.kr | |
| baseline | 베이스라인 | 제안 | terms.kr는 “기준선”입니다. 실험 비교 대상이라는 뜻에는 “베이스라인”이 더 널리 쓰입니다. |
| evaluation | 평가 | 제안 | |
| downstream evaluation | 다운스트림 평가 | 팀 표기 | |
| overfitting | 오버피팅 | 팀 표기 | |
| inference | 추론 | terms.kr | |
| throughput | 처리량 | 제안 | |
| latency | 지연 시간 | 제안 | |
| scaling law | 스케일링 법칙 | 제안 | |
| compute | 연산량, 연산 비용, 연산 자원 | 제안 | 문맥에 맞게 고릅니다. |
| reasoning | 추론 능력, 사고 | 제안 | 모델의 능력이면 “추론 능력”, 사람의 사고면 “사고”입니다. |

## 학습 단계와 모델 구조

| 영어 | 한국어 표기 | 근거 | 비고 |
| --- | --- | --- | --- |
| pre-training, pretraining | 사전 학습 | terms.kr | terms.kr는 “사전학습”이지만 띄어쓰기 원칙에 따라 띄어 씁니다. |
| mid-training | 중간 학습(mid-training) | 제안 | |
| post-training | 사후 학습 | terms.kr | |
| fine-tuning | 파인튜닝 | 팀 표기 | |
| reinforcement learning | 강화 학습(RL) | terms.kr | 띄어쓰기 원칙에 따라 띄어 씁니다. |
| preference optimization | 선호 최적화 | 제안 | |
| Direct Preference Optimization (DPO) | Direct Preference Optimization(이하 DPO) | 팀 표기 | 이후 DPO로 씁니다. |
| data curation | 데이터 큐레이션 | 팀 표기 | |
| data mixture | 데이터 혼합 | 제안 | 비율을 뜻하면 “데이터 혼합 비율”로 씁니다. |
| architecture | 아키텍처 | 팀 표기 | |
| transformer | 트랜스포머 | 팀 표기 | |
| parameter | 파라미터 | 팀 표기 | |
| layer | 레이어 | 팀 표기 | |
| attention | 어텐션 | terms.kr | |
| KV cache | KV 캐시 | 팀 표기 | |
| masking | 마스킹 | 팀 표기 | |
| embedding | 임베딩 | terms.kr | |
| logit | 로짓 | 팀 표기 | |
| softmax | 소프트맥스 | 팀 표기 | |
| mixture of experts (MoE) | MoE | 팀 표기 | 첫 등장부터 MoE로 씁니다. |
| expert | Expert | 팀 표기 | MoE 문맥에서 씁니다. |
| shared expert | 공유 Expert | 팀 표기 | |
| router | 라우터 | 제안 | |

## 분산 학습과 인프라

| 영어 | 한국어 표기 | 근거 | 비고 |
| --- | --- | --- | --- |
| data parallelism | 데이터 병렬화(DP) | 제안 | terms.kr는 “데이터 병렬 처리”입니다. TP, PP와 맞춰 “병렬화”로 통일합니다. |
| tensor parallelism | 텐서 병렬화(TP) | terms.kr | |
| pipeline parallelism | 파이프라인 병렬화(PP) | terms.kr | |
| context parallelism | 컨텍스트 병렬화(CP) | 제안 | |
| sequence parallelism | 시퀀스 병렬화(SP) | 제안 | |
| expert parallelism | 전문가 병렬화(EP) | 제안 | |
| sharding | 샤딩 | 제안 | |
| all-reduce, all-gather, reduce-scatter | 영어 그대로 | 제안 | 통신 연산 이름입니다. terms.kr는 all-reduce를 “올리듀스”로 옮깁니다. |
| microbatch | 마이크로배치 | 제안 | |
| pipeline bubble | 파이프라인 버블 | 제안 | |
| activation | 활성화 값(activation) | 제안 | 메모리 문맥에서 쓰는 말입니다. |
| activation recomputation, activation checkpointing | 활성화 재계산 | 제안 | |
| mixed precision | 혼합 정밀도 | terms.kr | |
| memory bandwidth | 메모리 대역폭 | terms.kr | |
| interconnect | 인터커넥트 | 제안 | |
| node | 노드 | terms.kr | |
| kernel | 커널 | terms.kr | GPU 커널 문맥입니다. |
| FLOPs | FLOPs | 제안 | 약어 그대로 둡니다. |
| MFU | 모델 FLOPs 활용률(MFU) | 제안 | |

## 정하지 않은 용어

리뷰에서 하나를 고르면 위 표로 옮깁니다.

| 영어 | 후보 | 비고 |
| --- | --- | --- |
| ablation | 어블레이션, 절제 실험, 제거 실험 | terms.kr에 없습니다. Smol 전체에 자주 나옵니다. |
| supervised fine-tuning (SFT) | 지도 파인튜닝(SFT), SFT | |
