# Tiny GPT Working Repository (English - TinyStories)

이 리포지토리는 `notebook_06.ipynb` 기반으로 구성한 작은 GPT 학습/추론 파이썬 프로젝트입니다.
현재는 Hugging Face의 `TinyStories` 데이터셋을 사용하여 영어를 구사하는 Tiny GPT를 만드는 데 최적화되어 있습니다.

## 구조

- `README.md` - 프로젝트 설명 및 실행 방법
- `requirements.txt` - 필요한 라이브러리 (torch, datasets 등)
- `data/` - 텍스트 데이터를 저장할 위치
- `src/` - GPT 모델, 데이터셋, 학습 및 생성 코드
  - `config.py` - 모델 및 학습 설정 (TinyStories 기본값 설정됨)
  - `dataset.py` - 문자 단위 토크나이징 및 데이터 로딩 (HF datasets 지원)
  - `model.py` - Multi-head Attention 기반 GPT 아키텍처
  - `train.py` - 학습 루프 및 체크포인트 저장
  - `generate.py` - 학습된 모델로 텍스트 생성

## 설치

```bash
pip install -r requirements.txt
```

## 학습 (TinyStories 영어 데이터셋)

기본적으로 `roneneldan/TinyStories` 데이터셋의 일부(5000개 샘플)를 사용하여 학습하도록 설정되어 있습니다.

```bash
# 기본 설정으로 학습 시작 (Hugging Face 데이터셋 자동 다운로드)
python -m src.train
```

만약 로컬 파일(`data/input.txt`)로 학습하고 싶다면:
```bash
python -m src.train --data_path data/input.txt --no_hf
```

## 생성

학습된 체크포인트를 사용하여 영어 이야기를 생성합니다.

```bash
python -m src.generate --checkpoint checkpoints/gpt_checkpoint_5000.pt --start_text "Once upon a time," --max_new_tokens 300
```
