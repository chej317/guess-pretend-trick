> python -m src.train
Loading dataset 'roneneldan/TinyStories' from Hugging Face...
`trust_remote_code` is not supported anymore.
Please check that the Hugging Face dataset 'roneneldan/TinyStories' isn't based on a loading script and remove `trust_remote_code`.
If the dataset is based on a loading script, please ask the dataset author to remove it and convert it to a standard format like Parquet.
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Sampling 5000 examples...
> 

---

### 🚀 Training Summary
• Dataset: roneneldan/TinyStories (HuggingFace)
• Vocab Size: 90
• Batch Size: 64
• Block Size: 128
• Model Size: 2,725,338 parameters
• Device: cpu
• Max Iters: 5000

Step   100/5000 | Loss: 2.3896
✅ Step   100 | Train Loss: 2.3896 | Val Loss: 2.4053 | Time: 412.8s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_100.pt

Step   200/5000 | Loss: 2.2350
✅ Step   200 | Train Loss: 2.2350 | Val Loss: 2.2643 | Time: 648.3s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_200.pt

Step   300/5000 | Loss: 2.1493
✅ Step   300 | Train Loss: 2.1493 | Val Loss: 2.1478 | Time: 881.1s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_300.pt

Step   400/5000 | Loss: 1.9590
✅ Step   400 | Train Loss: 1.9590 | Val Loss: 1.9870 | Time: 1117.2s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_400.pt

Step   500/5000 | Loss: 1.8355
✅ Step   500 | Train Loss: 1.8355 | Val Loss: 1.8436 | Time: 1351.1s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_500.pt

Step   600/5000 | Loss: 1.6433
✅ Step   600 | Train Loss: 1.6433 | Val Loss: 1.7143 | Time: 1584.3s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_600.pt

Step   700/5000 | Loss: 1.5639
✅ Step   700 | Train Loss: 1.5639 | Val Loss: 1.6188 | Time: 1818.6s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_700.pt

Step   800/5000 | Loss: 1.4671
✅ Step   800 | Train Loss: 1.4671 | Val Loss: 1.5415 | Time: 2053.3s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_800.pt

Step   900/5000 | Loss: 1.4306
✅ Step   900 | Train Loss: 1.4306 | Val Loss: 1.4896 | Time: 2289.1s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_900.pt

Step  1000/5000 | Loss: 1.3950
✅ Step  1000 | Train Loss: 1.3950 | Val Loss: 1.4386 | Time: 2534.2s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_1000.pt

Step  1100/5000 | Loss: 1.3469
✅ Step  1100 | Train Loss: 1.3469 | Val Loss: 1.3958 | Time: 2788.4s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_1100.pt

Step  1200/5000 | Loss: 1.2859
✅ Step  1200 | Train Loss: 1.2859 | Val Loss: 1.3602 | Time: 3044.7s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_1200.pt

Step  1300/5000 | Loss: 1.2696
✅ Step  1300 | Train Loss: 1.2696 | Val Loss: 1.3276 | Time: 3287.6s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_1300.pt

Step  1400/5000 | Loss: 1.2455
✅ Step  1400 | Train Loss: 1.2455 | Val Loss: 1.3099 | Time: 3531.6s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_1400.pt

Step  1500/5000 | Loss: 1.2001
✅ Step  1500 | Train Loss: 1.2001 | Val Loss: 1.2704 | Time: 3768.9s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_1500.pt

Step  1600/5000 | Loss: 1.1825
✅ Step  1600 | Train Loss: 1.1825 | Val Loss: 1.2485 | Time: 4005.5s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_1600.pt

Step  1700/5000 | Loss: 1.1706
✅ Step  1700 | Train Loss: 1.1706 | Val Loss: 1.2406 | Time: 4249.3s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_1700.pt

Step  1800/5000 | Loss: 1.1806
✅ Step  1800 | Train Loss: 1.1806 | Val Loss: 1.2176 | Time: 4490.6s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_1800.pt

Step  1900/5000 | Loss: 1.1485
✅ Step  1900 | Train Loss: 1.1485 | Val Loss: 1.1978 | Time: 4726.6s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_1900.pt

Step  2000/5000 | Loss: 1.0427
✅ Step  2000 | Train Loss: 1.0427 | Val Loss: 1.1766 | Time: 4966.3s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_2000.pt

Step  2100/5000 | Loss: 1.1322
✅ Step  2100 | Train Loss: 1.1322 | Val Loss: 1.1610 | Time: 5205.5s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_2100.pt

Step  2200/5000 | Loss: 1.0943
✅ Step  2200 | Train Loss: 1.0943 | Val Loss: 1.1516 | Time: 5495.0s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_2200.pt

Step  2300/5000 | Loss: 1.0682
✅ Step  2300 | Train Loss: 1.0682 | Val Loss: 1.1352 | Time: 5795.7s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_2300.pt

Step  2400/5000 | Loss: 1.0610
✅ Step  2400 | Train Loss: 1.0610 | Val Loss: 1.1198 | Time: 6073.3s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_2400.pt

Step  2500/5000 | Loss: 1.0727
✅ Step  2500 | Train Loss: 1.0727 | Val Loss: 1.1217 | Time: 6316.6s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_2500.pt

Step  2600/5000 | Loss: 1.0213
✅ Step  2600 | Train Loss: 1.0213 | Val Loss: 1.1074 | Time: 6564.2s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_2600.pt

Step  2700/5000 | Loss: 0.9896
✅ Step  2700 | Train Loss: 0.9896 | Val Loss: 1.1031 | Time: 6862.7s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_2700.pt

Step  2800/5000 | Loss: 0.9985
✅ Step  2800 | Train Loss: 0.9985 | Val Loss: 1.0825 | Time: 7105.5s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_2800.pt

Step  2900/5000 | Loss: 1.0004
✅ Step  2900 | Train Loss: 1.0004 | Val Loss: 1.0718 | Time: 7348.2s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_2900.pt

Step  3000/5000 | Loss: 1.0040
✅ Step  3000 | Train Loss: 1.0040 | Val Loss: 1.0716 | Time: 7587.6s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_3000.pt

Step  3100/5000 | Loss: 1.0328
✅ Step  3100 | Train Loss: 1.0328 | Val Loss: 1.0650 | Time: 7887.7s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_3100.pt

Step  3200/5000 | Loss: 1.0035
✅ Step  3200 | Train Loss: 1.0035 | Val Loss: 1.0619 | Time: 8137.6s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_3200.pt

Step  3300/5000 | Loss: 0.9745
✅ Step  3300 | Train Loss: 0.9745 | Val Loss: 1.0458 | Time: 8370.2s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_3300.pt

Step  3400/5000 | Loss: 1.0118
✅ Step  3400 | Train Loss: 1.0118 | Val Loss: 1.0391 | Time: 8587.4s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_3400.pt

Step  3500/5000 | Loss: 1.0203
✅ Step  3500 | Train Loss: 1.0203 | Val Loss: 1.0304 | Time: 8813.1s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_3500.pt

Step  3600/5000 | Loss: 0.9686
✅ Step  3600 | Train Loss: 0.9686 | Val Loss: 1.0361 | Time: 9033.1s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_3600.pt

Step  3700/5000 | Loss: 0.9664
✅ Step  3700 | Train Loss: 0.9664 | Val Loss: 1.0187 | Time: 9254.3s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_3700.pt

Step  3800/5000 | Loss: 0.9728
✅ Step  3800 | Train Loss: 0.9728 | Val Loss: 1.0157 | Time: 9484.0s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_3800.pt

Step  3900/5000 | Loss: 0.9523
✅ Step  3900 | Train Loss: 0.9523 | Val Loss: 1.0077 | Time: 9699.3s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_3900.pt

Step  4000/5000 | Loss: 0.9431
✅ Step  4000 | Train Loss: 0.9431 | Val Loss: 1.0103 | Time: 9922.9s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_4000.pt

Step  4100/5000 | Loss: 0.9525
✅ Step  4100 | Train Loss: 0.9525 | Val Loss: 0.9963 | Time: 10147.2s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_4100.pt

Step  4200/5000 | Loss: 0.9052
✅ Step  4200 | Train Loss: 0.9052 | Val Loss: 0.9969 | Time: 10373.6s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_4200.pt

Step  4300/5000 | Loss: 0.9657
✅ Step  4300 | Train Loss: 0.9657 | Val Loss: 0.9938 | Time: 10596.6s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_4300.pt

Step  4400/5000 | Loss: 0.9576
✅ Step  4400 | Train Loss: 0.9576 | Val Loss: 1.0024 | Time: 10820.6s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_4400.pt

Step  4500/5000 | Loss: 0.9733
✅ Step  4500 | Train Loss: 0.9733 | Val Loss: 0.9902 | Time: 11049.9s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_4500.pt

Step  4600/5000 | Loss: 0.9451
✅ Step  4600 | Train Loss: 0.9451 | Val Loss: 0.9851 | Time: 11277.3s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_4600.pt

Step  4700/5000 | Loss: 0.9494
✅ Step  4700 | Train Loss: 0.9494 | Val Loss: 0.9858 | Time: 11500.7s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_4700.pt

Step  4800/5000 | Loss: 0.9210
✅ Step  4800 | Train Loss: 0.9210 | Val Loss: 0.9716 | Time: 11723.2s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_4800.pt

Step  4900/5000 | Loss: 0.8978
✅ Step  4900 | Train Loss: 0.8978 | Val Loss: 0.9704 | Time: 11947.2s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_4900.pt

Step  5000/5000 | Loss: 0.9380
✅ Step  5000 | Train Loss: 0.9380 | Val Loss: 0.9622 | Time: 12191.6s
💾 Saved checkpoint: checkpoints\gpt_checkpoint_5000.pt

Training complete.