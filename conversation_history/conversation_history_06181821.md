# Conversation History - 06181821

**Date:** 2026-06-18
**Topic:** Showcasing training progression via checkpoints on GitHub.

## User Question
> 지금 프로젝트의 장점 중 하나는, 프롬프트에 '특정 gpt checkpoint'를 포함함으로써, 훈련 정도에 따라 결과물이 달라지는 걸 볼 수 있다는 거야. 이걸 보여주기 위해서 깃허브를 어떻게 꾸미는 게 좋을까?

## Implemented Changes
1. **Milestone Strategy**: Cleaned up `checkpoints/` to keep only 4 key milestones (100, 1000, 2500, 5000) for repository efficiency.
2. **`.gitignore` Update**: Configured to track only the milestone files while ignoring other potential checkpoints, preventing repository bloat.
3. **`src/compare.py` Created**: A new utility to generate side-by-side text comparisons from any available checkpoint.
4. **`README.md` Enhancement**: Added a detailed "Evolution of Intelligence" section explaining the milestone logic and providing usage examples for both default and custom checkpoints.

## Final Result for GitHub
- The repository now shows a clear "Evolution of Intelligence" through specific, committed milestones.
- Viewers are informed that intermediate checkpoints (like 3000) are conceptually available and can be generated/used by running the training script themselves.
- The repo remains under ~60MB while providing a fully functional, interactive demonstration of GPT training progression.
