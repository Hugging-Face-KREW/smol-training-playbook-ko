# Smol 주차별 번역 배정표

[발표·리뷰어 배정 시트](https://docs.google.com/spreadsheets/d/1nTZjClBRm8hwDR9pfx5JGZyhUf3Ajn0k76w8oPMudrk/edit#gid=709064888) · [주차별 범위·마감](https://docs.google.com/spreadsheets/d/1nTZjClBRm8hwDR9pfx5JGZyhUf3Ajn0k76w8oPMudrk/edit#gid=550580206) · [번역 작업 가이드](../TRANSLATION_GUIDE.md)

이 문서는 시트의 발표 범위를 Smol 원문 줄 번호와 인터랙티브 그림 파일에 대응시킨 배정표입니다. 담당자·리뷰어는 2026-11-01 확인 기준이며, 이후 배정과 마감 변경은 시트를 우선합니다. 범위가 바뀌면 이 문서의 줄 번호와 그림 목록도 함께 갱신합니다.

## 자료와 기준 파일

- [영문 원문 Space](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook): 그림과 문맥을 확인합니다.
- [고정 영문 원본](original/article.en.mdx): 아래 줄 번호의 기준입니다. 원문 Space의 최신 줄 번호와 혼동하지 마세요.
- [번역할 본문](../app/src/content/article.mdx): 담당 줄의 자연어 설명을 번역합니다.
- [한국어 Space](https://huggingface.co/spaces/huggingface-KREW/smol-training-playbook-ko): 머지 후 공개 상태를 확인합니다.

**시작·끝 줄을 모두 포함**합니다. 빈 줄과 문법만 있는 줄도 범위에 포함되지만 번역을 위해 바꾸지는 않습니다. 본문 한 줄과 원문 한 줄의 대응을 유지합니다.

## 주차별 본문 배정

| 주차 | 담당자 | 리뷰어 | Smol 범위 | 고정 원문 줄 |
| --- | --- | --- | --- | --- |
| 1 | 정우준 | 김주원 · 이은지 | 제목·저자 정보, Introduction, Training Compass, Small Ablation | [L1–693](original/article.en.mdx?plain=1#L1-L693) |
| 2 | 김주원 | 이은지 · 함지율 | Architecture 도입, Architecture Choices부터 Additional Considerations까지 | [L694–1401](original/article.en.mdx?plain=1#L694-L1401) |
| 3 | 이은지 | 함지율 · 김주원 | Going Sparse: MoE부터 Architecture의 Rules of Engagement까지 | [L1402–2054](original/article.en.mdx?plain=1#L1402-L2054) |
| 4 | 함지율 | 김주원 · 이은지 | Optimizer and Training Hyperparameters, Scaling Laws | [L2055–2484](original/article.en.mdx?plain=1#L2055-L2484) |
| 5 | 김주원 | 이은지 · 김신곤 | Data Curation, Training Marathon | [L2485–3025](original/article.en.mdx?plain=1#L2485-L3025) |
| 6 | 이은지 | 김신곤 · 박동우 | Post-Training 도입부터 SFT의 Targeting Specific Capabilities까지 | [L3026–3630](original/article.en.mdx?plain=1#L3026-L3630) |
| 7 | 김신곤 | 박동우 · 함지율 | SFT Hyperparameters부터 Wrapping Up Post-Training까지 | [L3631–4254](original/article.en.mdx?plain=1#L3631-L4254) |
| 8 | 박동우 | 함지율 · 이은지 | Infrastructure 도입 + Outside a GPU 전체 | [L4255–4270](original/article.en.mdx?plain=1#L4255-L4270) + [L4568–5416](original/article.en.mdx?plain=1#L4568-L5416) |
| 9 | 함지율 | 이은지 · 김주원 | Inside a GPU 전체 | [L4271–4567](original/article.en.mdx?plain=1#L4271-L4567) |
| 14 | 정우준 | 미정 | Building Resilient Training Systems부터 Conclusion·References까지 | [L5417–5807](original/article.en.mdx?plain=1#L5417-L5807) |

1주차의 저자 이름·소속·URL·import·설정 키는 유지하고, 제목·부제·설명 등 번역 가능한 자연어만 바꿉니다. 8주차는 두 구간으로 나뉘며, 사이의 Inside a GPU는 9주차 담당입니다.

14주차 References의 논문 제목·서지 정보는 원문을 유지하고, 분류 제목과 설명 문장을 번역합니다. Citation 안내는 본문 밖 [Footer.astro](../app/src/components/Footer.astro)에 있으므로, 14주차에는 이미 번역된 문구인지 확인하고 필요한 안내 문구만 번역합니다. 인용 데이터는 유지합니다.

9·14주차의 Ultra 부분과 10–13주차는 이 문서에서 다루지 않습니다. Ultra의 번역 파일과 줄 범위는 추후 정합니다.

## 본문과 함께 번역할 인터랙티브 그림

각 본문 담당자가 **각주·그림 캡션·표·사이드노트와 해당 구간의 인터랙티브 그림 문구까지** 같은 PR에서 번역합니다. 아래 HTML 파일은 모두 `app/src/content/embeds/` 아래에 있습니다. 참조 줄은 고정 영문 원본의 `<HtmlEmbed>` 시작 줄입니다.

그림의 텍스트는 두 곳에 있을 수 있습니다.

- **본문의 `<HtmlEmbed>`와 `config`**: 그림 제목, 캡션, 축 설명 등 자연어 값은 본인 담당 줄 안에서 번역합니다.
- **아래 HTML 파일**: 화면에 보이는 제목·라벨·범례·툴팁·버튼·설명 문구를 번역합니다. HTML/JavaScript 문법, 선택자, 데이터 키, `metric`, 파일 경로, 수치, 단위와 계산 로직은 유지합니다. 벤치마크·모델 이름 등 고유명사도 유지합니다.

### 여러 주차가 공유하는 파일

`d3-line-chart.html`은 2·4·5·8·9주차, `d3-six-line-charts.html`은 2·4·5주차가 공유합니다. 두 파일의 공용 UI 문구는 **처음 사용하는 2주차 담당자가 번역**합니다. 이후 담당자는 번역 여부를 확인하고 자기 본문의 `config` 문구를 번역합니다. 공용 파일에 추가 수정이 필요하면 기존 담당자와 조율하고 PR에 영향받는 주차를 적습니다.

예를 들어 본문 `config`의 `title: "Attention Loss"`는 설명 제목이므로 번역할 수 있지만, `metric: "hellaswag"`와 `dataUrl`은 동작에 필요한 값이므로 바꾸지 않습니다. 공용 HTML을 번역하면 그 파일을 사용하는 다른 주차의 공용 UI에도 반영됩니다.

본문 줄 번호 유지 규칙은 `article.mdx`에 적용합니다. HTML 파일도 불필요한 줄바꿈·전체 포맷팅을 피하고, 실제 수정 파일을 PR에 함께 적습니다. 번역 후 로컬 화면에서 그림이 표시되고 툴팁·버튼 등이 동작하는지 확인합니다.

### 1주차 · 정우준

| HTML 파일 | 본문 참조 줄 | 담당 메모 |
| --- | --- | --- |
| [training-compass.html](../app/src/content/embeds/training-compass.html) | L151 | 해당 그림 문구 번역 |
| [wrong-reasons.html](../app/src/content/embeds/wrong-reasons.html) | L181 | 해당 그림 문구 번역 |
| [train-model-decision-flowchart.html](../app/src/content/embeds/train-model-decision-flowchart.html) | L189 | 해당 그림 문구 번역 |
| [parameter-calculator.html](../app/src/content/embeds/parameter-calculator.html) | L568 | 해당 그림 문구 번역 |

### 2주차 · 김주원

| HTML 파일 | 본문 참조 줄 | 담당 메모 |
| --- | --- | --- |
| [attention-mechanisms.html](../app/src/content/embeds/attention-mechanisms.html) | L795 | 해당 그림 문구 번역 |
| [d3-line-chart.html](../app/src/content/embeds/d3-line-chart.html) | L837, L952, L1011, L1189, L1302, L1346 | 공용 파일 문구 번역 |
| [d3-six-line-charts.html](../app/src/content/embeds/d3-six-line-charts.html) | L850, L965, L1024, L1202, L1320, L1364 | 공용 파일 문구 번역 |
| [token-distribution.html](../app/src/content/embeds/token-distribution.html) | L906 | 해당 그림 문구 번역 |
| [doc-masking.html](../app/src/content/embeds/doc-masking.html) | L921 | 해당 그림 문구 번역 |
| [embedding-calculator.html](../app/src/content/embeds/embedding-calculator.html) | L995 | 해당 그림 문구 번역 |
| [parameter-comparison.html](../app/src/content/embeds/parameter-comparison.html) | L1001 | 해당 그림 문구 번역 |
| [rope-demo.html](../app/src/content/embeds/rope-demo.html) | L1142 | 해당 그림 문구 번역 |
| [position-masking.html](../app/src/content/embeds/position-masking.html) | L1255 | 해당 그림 문구 번역 |

### 3주차 · 이은지

| HTML 파일 | 본문 참조 줄 | 담당 메모 |
| --- | --- | --- |
| [efficiency-leverage.html](../app/src/content/embeds/efficiency-leverage.html) | L1428 | 해당 그림 문구 번역 |
| [benchmark-performance.html](../app/src/content/embeds/benchmark-performance.html) | L1685 | 해당 그림 문구 번역 |
| [model-architecture-decision-flowchart.html](../app/src/content/embeds/model-architecture-decision-flowchart.html) | L1780 | 해당 그림 문구 번역 |
| [tokenization-comparison.html](../app/src/content/embeds/tokenization-comparison.html) | L1832 | 해당 그림 문구 번역 |
| [tokenizer-comparison.html](../app/src/content/embeds/tokenizer-comparison.html) | L1982 | 해당 그림 문구 번역 |

### 4주차 · 함지율

| HTML 파일 | 본문 참조 줄 | 담당 메모 |
| --- | --- | --- |
| [d3-line-chart.html](../app/src/content/embeds/d3-line-chart.html) | L2165, L2196, L2228, L2282 | 공용 문구 확인, 본인 config 번역 |
| [d3-six-line-charts.html](../app/src/content/embeds/d3-six-line-charts.html) | L2241, L2295 | 공용 문구 확인, 본인 config 번역 |

### 5주차 · 김주원

| HTML 파일 | 본문 참조 줄 | 담당 메모 |
| --- | --- | --- |
| [ablation-study.html](../app/src/content/embeds/ablation-study.html) | L2532 | 해당 그림 문구 번역 |
| [d3-line-chart.html](../app/src/content/embeds/d3-line-chart.html) | L2657, L2710, L2746, L2838 | 공용 문구 확인, 본인 config 번역 |
| [d3-six-line-charts.html](../app/src/content/embeds/d3-six-line-charts.html) | L2855 | 공용 문구 확인, 본인 config 번역 |
| [data-mixture-stages.html](../app/src/content/embeds/data-mixture-stages.html) | L2952 | 해당 그림 문구 번역 |
| [base-model-performance.html](../app/src/content/embeds/base-model-performance.html) | L3017 | 해당 그림 문구 번역 |

### 6주차 · 이은지

| HTML 파일 | 본문 참조 줄 | 담당 메모 |
| --- | --- | --- |
| [post-training-adventure.html](../app/src/content/embeds/post-training-adventure.html) | L3033 | 해당 그림 문구 번역 |
| [d3-sft-baby-baseline.html](../app/src/content/embeds/d3-sft-baby-baseline.html) | L3444 | 해당 그림 문구 번역 |
| [d3-sft-think-follow-0.html](../app/src/content/embeds/d3-sft-think-follow-0.html) | L3564 | 해당 그림 문구 번역 |
| [d3-sft-think-follow-1.html](../app/src/content/embeds/d3-sft-think-follow-1.html) | L3625 | 해당 그림 문구 번역 |

### 7주차 · 김신곤

| HTML 파일 | 본문 참조 줄 | 담당 메모 |
| --- | --- | --- |
| [input-labels-training.html](../app/src/content/embeds/input-labels-training.html) | L3641 | 해당 그림 문구 번역 |
| [d3-sft-mask-turns.html](../app/src/content/embeds/d3-sft-mask-turns.html) | L3684 | 해당 그림 문구 번역 |
| [data-packing.html](../app/src/content/embeds/data-packing.html) | L3696 | 해당 그림 문구 번역 |
| [d3-sft-packing-runtime.html](../app/src/content/embeds/d3-sft-packing-runtime.html) | L3708 | 해당 그림 문구 번역 |
| [d3-sft-packing-tokens.html](../app/src/content/embeds/d3-sft-packing-tokens.html) | L3719 | 해당 그림 문구 번역 |
| [d3-sft-packing-vs-no-packing.html](../app/src/content/embeds/d3-sft-packing-vs-no-packing.html) | L3725 | 해당 그림 문구 번역 |
| [d3-sft-packing-vs-bs.html](../app/src/content/embeds/d3-sft-packing-vs-bs.html) | L3731 | 해당 그림 문구 번역 |
| [d3-sft-lr-scan.html](../app/src/content/embeds/d3-sft-lr-scan.html) | L3752 | 해당 그림 문구 번역 |
| [d3-sft-epoch-scan.html](../app/src/content/embeds/d3-sft-epoch-scan.html) | L3769 | 해당 그림 문구 번역 |
| [training-pipeline.html](../app/src/content/embeds/training-pipeline.html) | L3790 | 해당 그림 문구 번역 |
| [d3-sft-mid-train.html](../app/src/content/embeds/d3-sft-mid-train.html) | L3849 | 해당 그림 문구 번역 |
| [d3-sft-base-vs-mid.html](../app/src/content/embeds/d3-sft-base-vs-mid.html) | L3857 | 해당 그림 문구 번역 |
| [d3-po-loss-ablations.html](../app/src/content/embeds/d3-po-loss-ablations.html) | L3948 | 해당 그림 문구 번역 |
| [d3-po-lr-ablation.html](../app/src/content/embeds/d3-po-lr-ablation.html) | L3975 | 해당 그림 문구 번역 |
| [d3-po-beta-ablation.html](../app/src/content/embeds/d3-po-beta-ablation.html) | L3989 | 해당 그림 문구 번역 |
| [d3-po-size-ablation.html](../app/src/content/embeds/d3-po-size-ablation.html) | L3997 | 해당 그림 문구 번역 |
| [instruct-models-without-reasoning.html](../app/src/content/embeds/instruct-models-without-reasoning.html) | L4007 | 해당 그림 문구 번역 |
| [d3-rl-token-histogram.html](../app/src/content/embeds/d3-rl-token-histogram.html) | L4066 | 해당 그림 문구 번역 |
| [d3-rl-full-length.html](../app/src/content/embeds/d3-rl-full-length.html) | L4076 | 해당 그림 문구 번역 |
| [d3-rl-reward-curves.html](../app/src/content/embeds/d3-rl-reward-curves.html) | L4122 | 해당 그림 문구 번역 |
| [d3-rl-aime25.html](../app/src/content/embeds/d3-rl-aime25.html) | L4128 | 해당 그림 문구 번역 |
| [d3-rl-token-comparison.html](../app/src/content/embeds/d3-rl-token-comparison.html) | L4134 | 해당 그림 문구 번역 |
| [d3-rl-aime25-comparisons.html](../app/src/content/embeds/d3-rl-aime25-comparisons.html) | L4142 | 해당 그림 문구 번역 |
| [rl-training-sync.html](../app/src/content/embeds/rl-training-sync.html) | L4223 | 해당 그림 문구 번역 |

### 8주차 · 박동우

| HTML 파일 | 본문 참조 줄 | 담당 메모 |
| --- | --- | --- |
| [aws-bandwidth-bottleneck.html](../app/src/content/embeds/aws-bandwidth-bottleneck.html) | L4589, L4668, L4791, L4852, L4890, L5014, L5409 | 해당 그림 문구 번역 |
| [d3-line-chart.html](../app/src/content/embeds/d3-line-chart.html) | L4682, L4708, L4904 | 공용 문구 확인, 본인 config 번역 |
| [nccl-all-reduce-singlenode-bandwidth-plot.html](../app/src/content/embeds/nccl-all-reduce-singlenode-bandwidth-plot.html) | L4945 | 해당 그림 문구 번역 |
| [nccl-alltoall-singlenode-bandwidth-plot.html](../app/src/content/embeds/nccl-alltoall-singlenode-bandwidth-plot.html) | L4968 | 해당 그림 문구 번역 |
| [nccl-bandwidth-comparison.html](../app/src/content/embeds/nccl-bandwidth-comparison.html) | L5027 | 해당 그림 문구 번역 |
| [nccl-latency-comparison.html](../app/src/content/embeds/nccl-latency-comparison.html) | L5051 | 해당 그림 문구 번역 |
| [gds-interactive-heatmaps.html](../app/src/content/embeds/gds-interactive-heatmaps.html) | L5383 | 해당 그림 문구 번역 |

### 9주차 · 함지율

| HTML 파일 | 본문 참조 줄 | 담당 메모 |
| --- | --- | --- |
| [gpu-sm-architecture.html](../app/src/content/embeds/gpu-sm-architecture.html) | L4302 | 해당 그림 문구 번역 |
| [d3-line-chart.html](../app/src/content/embeds/d3-line-chart.html) | L4500 | 공용 문구 확인, 본인 config 번역 |

### 14주차 · 정우준

| HTML 파일 | 본문 참조 줄 | 담당 메모 |
| --- | --- | --- |
| [nccl-all-reduce-bandwidth-plot-throttling.html](../app/src/content/embeds/nccl-all-reduce-bandwidth-plot-throttling.html) | L5503 | 해당 그림 문구 번역 |
| [amdahl-law-gpu-scaling.html](../app/src/content/embeds/amdahl-law-gpu-scaling.html) | L5615 | 해당 그림 문구 번역 |
| [d3-memory-analysis.html](../app/src/content/embeds/d3-memory-analysis.html) | L5648 | 해당 그림 문구 번역 |

### 외부 iframe

아래는 다른 Space나 데이터셋의 화면을 가져오는 iframe입니다. 로컬 HTML 파일이 없으므로 이 저장소에서 내부 문구를 직접 번역할 수 없습니다. iframe의 URL과 동작은 유지하고, 주변 설명·캡션을 번역합니다. 외부 화면 자체의 한국어화는 별도 작업으로 논의합니다.

| 주차 | 본문 참조 줄 | 외부 화면 |
| --- | --- | --- |
| 1 | L157 | [모델 공개 현황](https://cfahlgren1-model-release-heatmap.hf.space/) |
| 1 | L626 | [사전학습 벤치마크 뷰어](https://huggingface.co/datasets/HuggingFaceTB/llm-benchmarks-viewer/embed/viewer/default/mmlu) |
| 5 | L2899 | [Loss 비교](https://tfrere-loss-experiment.hf.space?project=spike-loss-comparison&metrics=loss&sidebar=hidden&navbar=hidden&smoothing=0&) |
| 6 | L3159 | [후학습 벤치마크 뷰어](https://huggingface.co/datasets/HuggingFaceTB/post-training-benchmarks-viewer/embed/viewer/aime25/test) |
| 6 | L3402 | [Chat Template Playground](https://huggingfacejs-chat-template-playground.hf.space?modelId=HuggingFaceTB%2FSmolLM3-3B&example=hello-world) |
| 7 | L3899 | [Orca DPO 데이터셋 뷰어](https://huggingface.co/datasets/Intel/orca_dpo_pairs/embed/viewer/default/train) |
| 7 | L3915 | [Snorkel Preference 데이터셋 뷰어](https://huggingface.co/datasets/snorkelai/Snorkel-Mistral-PairRM-DPO-Dataset/embed/viewer/default/train_iteration_1) |

목록은 고정 원문의 `<HtmlEmbed>` 90곳과 외부 `<iframe>` 7곳을 기준으로 작성했습니다. 본문에서 참조하지 않는 그림 파일은 주차별 담당에 포함하지 않습니다. 상단 Hero에서 사용하는 `banner.html`은 공통 UI 영역이므로 별도 작업으로 다룹니다.
