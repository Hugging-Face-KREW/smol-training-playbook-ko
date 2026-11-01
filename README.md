---
title: The Smol Training Playbook
short_description: The secrets to building world-class LLMs
emoji: 📚
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
header: mini
app_port: 8080
tags:
- research-article-template
- research paper
- scientific paper
- data visualization
thumbnail: >-
  https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook/public/thumb.png
---

## Smol Training Playbook 한국어 번역

Hugging Face KREW의 한국어 번역 저장소입니다.

**참여하기: [번역 작업 가이드](TRANSLATION_GUIDE.md)** · [영문 원본](docs/original/article.en.mdx)

- [한국어 Space](https://huggingface.co/spaces/huggingface-KREW/smol-training-playbook-ko)
- [원문 Space](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook)
- 번역은 브랜치에서 작업하고 GitHub PR로 리뷰합니다.
- `main`에 머지하면 GitHub Actions가 한국어 Space에 파일을 동기화하고 Space가 다시 빌드됩니다.
- Space 인증은 Trusted Publisher(OIDC)를 사용합니다. 저장소, `main` 브랜치, `sync-to-huggingface.yml` workflow로 제한합니다.
- Space에서 직접 수정하면 다음 동기화에서 덮어써질 수 있습니다. 파일 삭제도 동기화됩니다.

초기 파일은 한국어 Space의 `179c71bb4a1c10c8be98768dea04fbc2cfc8e9f9` 커밋에서 가져왔습니다. 아래는 원본 템플릿 문서입니다.

<div align="center">

# Research Article Template

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen.svg)](https://nodejs.org/)
[![Astro](https://img.shields.io/badge/Astro-4.10.0-orange.svg)](https://astro.build/)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/tfrere/research-article-template)


**A modern, interactive template for scientific writing** that brings papers to life with web-native features. The web offers what static PDFs can't: **interactive diagrams**, **progressive notation**, and **exploratory views** that show how ideas behave. This template treats interactive artifacts—figures, math, code, and inspectable experiments—as **first-class** alongside prose, helping readers **build intuition** instead of skimming results—all with **minimal setup** and no web knowledge required.
 
**[Try the live demo & documentation →](https://huggingface.co/spaces/tfrere/research-article-template)**

</div>

## 🚀 Quick Start

### Option 1: Duplicate on Hugging Face (Recommended)

1. Visit **[🤗 Research Article Template](https://huggingface.co/spaces/tfrere/research-article-template)**
2. Click **"Duplicate this Space"**
3. Clone your new repository:
   ```bash
   git clone git@hf.co:spaces/<your-username>/<your-space>
   cd <your-space>
   ```

### Option 2: Clone Directly

```bash
git clone https://github.com/tfrere/research-article-template.git
cd research-article-template
```

### Installation

```bash
# Install Node.js 20+ (use nvm for version management)
nvm install 20
nvm use 20

# Install Git LFS and pull assets
git lfs install
git lfs pull

# Install dependencies
cd app
npm install

# Start development server
npm run dev
```

Visit `http://localhost:4321` to see your site!

## 🎯 Who This Is For

- **Scientists** writing modern, web-native research papers
- **Educators** creating interactive, explorable lessons
- **Researchers** who want to focus on ideas, not infrastructure
- **Anyone** who values clear, engaging technical communication

## 🌟 Inspired by Distill

This template carries forward the spirit of [Distill](https://distill.pub/) (2016–2021), pushing interactive scientific writing even further with:
- Accessible, high-quality explanations
- Reproducible, production-ready demos
- Modern web technologies and best practices

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Ways to Contribute

- **Report bugs** - Open an issue with detailed information
- **Suggest features** - Share ideas for improvements
- **Improve documentation** - Help others get started
- **Submit code** - Fix bugs or add features
- **Join discussions** - Share feedback and ideas

## 📄 License

This project is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

- **Diagrams and text**: CC-BY 4.0
- **Source code**: Available on [Hugging Face](https://huggingface.co/spaces/tfrere/research-article-template)
- **Third-party figures**: Excluded and marked in captions

## 🙏 Acknowledgments

- Inspired by [Distill](https://distill.pub/) and the interactive scientific writing movement
- Built with [Astro](https://astro.build/), [MDX](https://mdxjs.com/), and modern web technologies
- Community feedback and contributions from researchers worldwide

## 📞 Support

- **[Community Discussions](https://huggingface.co/spaces/tfrere/research-article-template/discussions)** - Ask questions and share ideas
- **[Report Issues](https://huggingface.co/spaces/tfrere/research-article-template/discussions?status=open&type=issue)** - Bug reports and feature requests
- **Contact**: [@tfrere](https://huggingface.co/tfrere) on Hugging Face

---

**Made with ❤️ for the scientific community**