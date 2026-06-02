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

## 🚀 4. 시작하기 (Quick Start)

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

## 📊 5. 결과 예시 (Sample Output)

`Tiny GPT (approx. 13M params)` 모델이 생성한 결과입니다:

**Prompt:** `"Once upon a time,"`  
**Output:**  
> *"Once upon a time, there was a boy named Tim. Timmy and his friend said "Mom, I am the other day!", "Mom, kiss it or d..."* (학습 단계에 따라 지속적으로 품질이 향상됨)

