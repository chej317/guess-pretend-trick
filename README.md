# 🚀 Tiny GPT: From Bigram to Generative Pre-trained Transformer

> **학기말 프로젝트: 인공지능과 금융공학 (ECO4126)**  
> **목표**: 기초적인 통계적 언어 모델부터 최신 LLM의 근간인 Transformer 아키텍처(GPT-2)까지의 학습 과정을 증명하고, 실제로 작동하는 '나만의 GPT' 구현.

본 리포지토리는 언어 모델의 발전 과정을 단계별 노트북으로 기록하고, 최종적으로 모듈화된 GPT 모델을 통해 텍스트를 생성하는 전체 파이프라인을 포함하고 있습니다.

---

## 📑 1. 학습 로드맵 (Evolutionary Path)

단순한 코드 복사-붙여넣기가 아닌, 모델의 복잡도를 점진적으로 높여가며 원리를 파악했습니다. `notebooks/` 폴더에서 각 단계를 확인할 수 있습니다.

1. **`notebook_01`**: Bigram Language Model (통계 기반의 기초 모델)
2. **`notebook_02`**: MLP Character Model (Embedding 공간 도입 및 신경망 학습)
3. **`notebook_03`**: MLP on Tiny Shakespeare (데이터셋 확장을 통한 일반화 시도)
4. **`notebook_04`**: Sequence Dataset & Minimal Model (시퀀스 데이터 처리 기초)
5. **`notebook_05`**: Single-Head Masked Self-Attention (Attention 메커니즘의 이해)
6. **`notebook_06`**: **Tiny GPT 완성** (Multi-head Attention, FeedForward, Residual, LayerNorm 통합)

---

## 🛠️ 2. 기술적 사양 (Technical Architecture)

본 프로젝트에서 구현된 `Tiny GPT`는 GPT-2 아키텍처를 기반으로 하며, 다음과 같은 현대적인 DL 기법들을 포함합니다.

- **Architecture**: Decoder-only Transformer
- **Key Components**:
  - **Multi-Head Self-Attention**: 문맥 내의 다양한 관계를 병렬적으로 학습
  - **Positional Embedding**: 시퀀스 내 단어의 위치 정보 학습
  - **Residual Connections**: 깊은 신경망에서의 그래디언트 소실 문제 해결
  - **Layer Normalization (Pre-norm)**: 학습 안정성 및 수렴 속도 향상
  - **Character-level Tokenization**: 유연한 어휘 대응이 가능한 문자 단위 인코딩

---

## 📂 3. 프로젝트 구조 (Project Structure)

모듈화된 설계를 통해 확장성과 유지보수성을 높였습니다.

```text
src/
├── config.py    # 하이퍼파라미터 관리 (Batch size, Block size, Model dimension 등)
├── dataset.py   # 데이터 로딩 및 인코딩 (Hugging Face Datasets 연동 지원)
├── model.py     # GPT 모델 아키텍처 (Head, Block, MultiHeadAttention 구현)
├── train.py     # 학습 파이프라인 및 가중치 저장 시스템
└── generate.py  # 학습된 모델을 이용한 텍스트 생성 추론 엔진
```

---

## 🤖 4. AI 협업 및 투명성 (AI Collaboration & Transparency)

본 프로젝트는 최신 소프트웨어 개발 패러다임에 맞춰 **AI(Gemini CLI)를 보조 개발 도구 및 프로젝트 오케스트레이터로 활용**했습니다. 

단순히 AI가 생성한 코드를 사용하는 것에 그치지 않고, 다음과 같은 원칙을 지키며 협업했습니다:
- **과정의 투명성**: AI와의 모든 기술적 논의, 버그 수정 과정, 아키텍처 결정 사항을 `conversation_history/` 폴더에 가감 없이 기록하여 공개합니다.
- **주도적 설계**: AI는 코드 구현의 효율성을 높이는 도구로 활용되었으며, 전체적인 프로젝트 방향성과 모듈화 구조는 학습 목표에 맞춰 주도적으로 설계되었습니다.
- **학습 도구화**: 복잡한 개념(Self-Attention, Residual Connection 등)을 코드로 구현하는 과정에서 AI와 질의응답을 주고받으며 학습의 깊이를 더했습니다.

이러한 기록은 본 프로젝트가 단순한 결과물이 아니라, **'인간과 AI의 협업을 통한 학습의 여정'**임을 증명합니다.

---

## 🚀 5. 시작하기 (Quick Start)

### 환경 설정
```bash
pip install -r requirements.txt
```

### 모델 학습
본 프로젝트는 기본적으로 `TinyStories` 데이터셋을 사용하여 영문 창작 능력을 학습합니다.
```bash
python -m src.train --max_iters 5000 --batch_size 64
```

### 텍스트 생성 (Inference)
학습된 체크포인트를 사용하여 문장을 생성합니다.
```bash
python -m src.generate --checkpoint checkpoints/gpt_checkpoint_5000.pt --start_text "Once upon a time,"
```

---

## 📈 6. 지능의 진화 (Evolution of Intelligence)

본 프로젝트의 가장 큰 특징은 학습 단계별로 모델의 '지능'이 어떻게 발달하는지 직접 관찰할 수 있다는 점입니다. 

### 학습 단계별 생성 결과 비교 (Sample Comparison)

| 학습 단계 (Step) | 생성 결과 (Prompt: "Once upon a time,") | 특징 |
| :--- | :--- | :--- |
| **Step 100** | `j#$! 1a*& ...` | 무작위 문자열 생성 (지능 없음) |
| **Step 1000** | `Once upon a time, the boy and the mom go ...` | 기본적인 단어 조합 및 문법 구조 습득 |
| **Step 2500** | `Once upon a time, there was a little girl who loved to play...` | 문장 간 연결이 자연스러워짐 |
| **Step 5000** | `Once upon a time, there was a little girl who loved to play in the park with her friends...` | 문맥이 풍부하고 자연스러운 스토리텔링 |

> **💡 Checkpoint 안내**: 리포지토리 용량 최적화를 위해 위 4개의 핵심 **마일스톤 체크포인트**만 기본으로 포함되어 있습니다. 직접 학습을 진행하면 `checkpoints/` 폴더에 100단위로 더 세밀한 체크포인트(예: 3000, 3100 등)가 생성되며, 이를 통해 지능이 변하는 미세한 과정을 직접 탐구해 볼 수 있습니다.

---

## 🛠️ 7. 유틸리티 활용법 (Utility Scripts)

### 체크포인트 비교 (Compare Checkpoints)
기본 제공되는 마일스톤이나 직접 학습한 체크포인트들을 동일한 프롬프트로 한눈에 비교합니다.
```bash
# 기본 마일스톤 비교
python -m src.compare --steps 100 1000 2500 5000 --prompt "Once upon a time,"

# 직접 학습한 특정 단계(예: 3000)를 포함하여 비교
python -m src.compare --steps 100 1000 3000 5000
```

