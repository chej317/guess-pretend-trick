# Tiny GPT Working Repository

이 리포지토리는 `notebook_06.ipynb` 기반으로 구성한 작은 GPT 학습/추론 파이썬 프로젝트입니다.

## 구조

- `README.md` - 프로젝트 설명 및 실행 방법
- `requirements.txt` - 필요한 라이브러리
- `data/` - 텍스트 데이터를 저장할 위치
- `src/` - GPT 모델, 데이터셋, 학습 및 생성 코드
  - `config.py`
  - `dataset.py`
  - `model.py`
  - `train.py`
  - `generate.py`

## 설치

```bash
pip install -r requirements.txt
```

## 데이터 준비

`data/input.txt`에 학습할 텍스트를 넣습니다.

예시:
```bash
cd "c:\Users\witpo\OneDrive\바탕 화면\YONSEI\26-1\ECO4126 인공지능과금융공학\guess-pretend-trick"
python -c "from pathlib import Path; import urllib.request; Path('data').mkdir(exist_ok=True); urllib.request.urlretrieve('https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt', 'data/input.txt')"
```

## 학습

```bash
python -m src.train --data_path data/input.txt --output_dir checkpoints
```

## 생성

```bash
python -m src.generate --checkpoint checkpoints/gpt_checkpoint.pt --start_text "ROMEO:" --max_new_tokens 300
```

## 참고

이 구조는 다음 노트북 흐름을 따릅니다:
1. `notebook_01` - bigram
2. `notebook_02` - MLP char model
3. `notebook_03` - Shakespeare MLP
4. `notebook_04` - GPT-style sequence dataset
5. `notebook_05` - masked self-attention
6. `notebook_06` - Tiny GPT
