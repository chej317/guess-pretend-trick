# 인공지능과 금융공학: Tiny GPT 프로젝트 컨텍스트 (Gemini CLI용)

## 1. 프로젝트 개요
* **목표**: '인공지능과 금융공학' 학기말 과제를 위한 나만의 'GPT-2 (Tiny GPT)' 깃허브 리포지토리 구축.
* **요구 수준**: 학부생 수준에서 이해 및 구현 가능한 코드. 상용 서비스급의 완벽한 엔지니어링보다는 **'학습 과정의 증명'**과 **'실행 가능한 모듈화된 GPT (Working GPT)'**를 보여주는 것이 핵심.
* **현재 보유 자산**: 기초적인 통계적 언어 모델(Bigram)부터 시작해 Self-Attention을 거쳐 Tiny GPT로 빌드업하는 과정을 담은 6개의 주피터 노트북 파일.

## 2. 소스 데이터 (수업 노트북 흐름)
* `notebook_01`: Bigram Language Model (`names.txt` 기반 통계적 모델)
* `notebook_02`: MLP Character Model (Embedding 및 MLP 도입)
* `notebook_03`: MLP on Tiny Shakespeare (데이터셋 변경)
* `notebook_04`: Sequence Dataset & Minimal Sequence Model
* `notebook_05`: Single-Head Masked Self-Attention
* `notebook_06`: Tiny GPT (Multi-head attention, FeedForward, Residual, LayerNorm 적용 완성본)

## 3. 목표 깃허브 리포지토리 구조
노트북 환경을 벗어나, 터미널에서 독립적으로 실행 가능한 파이썬 패키지 형태로 모듈화하는 것이 최종 목표.

```text
my-tiny-gpt2/
├── README.md                  # 프로젝트 개요 및 실행 방법
├── requirements.txt           # 필요 라이브러리 (torch 등)
├── data/                      # 텍스트 데이터 (names.txt, tinyshakespeare.txt)
├── notebooks/                 # 학습 과정 증명용 (notebook_01 ~ 06)
└── src/                       # 🚀 Working GPT 구현을 위한 핵심 모듈 (notebook_06 기반 분리)
    ├── config.py              # 하이퍼파라미터 (batch_size, block_size, n_embd, lr 등)
    ├── dataset.py             # 텍스트 인코딩(stoi, itos) 및 DataLoader (get_batch)
    ├── model.py               # PyTorch 모델 (Head, MultiHeadAttention, FeedForward, Block, GPTLanguageModel)
    ├── train.py               # 모델 학습 루프 및 체크포인트 저장
    └── generate.py            # 학습된 가중치 로드 및 텍스트 생성 추론 스크립트

## 4. 필수 워크플로우 (Mandatory Workflows)
* **대화 기록 자동화**: 매 세션 시작 시 또는 대화 중에 `conversation_history/` 폴더에 대화 내용을 기록한다.
* **파일명 규칙**: `conversation_history_MMDDHHmm.md` (월일시분) 형식으로 저장한다.
* **자동 실행**: 사용자가 요청하지 않아도 새로운 세션이나 주요 작업 단계에서 해당 파일을 생성/업데이트하여 기록을 보존한다.