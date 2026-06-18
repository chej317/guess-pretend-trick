# Conversation History - 06181821

**Date:** 2026-06-18
**Topic:** Showcasing training progression via checkpoints on GitHub.

## User Question
> 지금 프로젝트의 장점 중 하나는, 프롬프트에 '특정 gpt checkpoint'를 포함함으로써, 훈련 정도에 따라 결과물이 달라지는 걸 볼 수 있다는 거야. 이걸 보여주기 위해서 깃허브를 어떻게 꾸미는 게 좋을까?

## Implemented Changes
1. **`src/train.py` Update**: Added real-time loss logging to `checkpoints/loss_history.json`.
2. **`src/compare.py` Created**: A new utility to generate side-by-side text comparisons from different checkpoints.
3. **`src/plot_loss.py` Created**: A visualization tool to generate a `loss_plot.png` from training logs.
4. **`README.md` Enhancement**: Added a structured "Evolution of Intelligence" section with a comparison table and usage instructions for the new tools.

## Recommendations for the User
- **Run the comparison**: Use `python -m src.compare --steps 100 1000 5000` to get real samples for your README.
- **Generate the plot**: Run `python -m src.plot_loss` after training to update the visualization.
- **Git LFS**: If you plan to upload many 13MB checkpoints, consider setting up Git LFS or only uploading 3-4 key milestones to avoid repository bloat.
