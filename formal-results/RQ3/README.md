# RQ3 runtime overhead on `reorder_5_bad`

We measured Native and PERIOD on the synthetic `reorder_5_bad` benchmark listed in Figure 7 of [Wen et al. (ICSE 2022)](https://wcventure.github.io/pdf/ICSE2022_PERIOD.pdf#page=10). Both modes ran in the same Docker container in an Ubuntu 22.04 VirtualBox guest.

Each of three batches recorded ten Native subprocess executions and ten timed subprocess executions in one PERIOD search. Batch 2 ran PERIOD first. Batches 1 and 3 ran Native first. The stopwatch measured wall-clock time from just before launching the subprocess through completion of `communicate()`. Both modes used `sudo` and captured stdout and stderr. The measured duration includes subprocess and `sudo` overhead. PERIOD's schedule generation and coverage processing outside the subprocess are outside the timing interval. The PERIOD run used `-y -d 3 -t 5 -f 10`.

| Mode | Timed executions | Mean (ms) | Median (ms) | Sample SD (ms) |
| --- | ---: | ---: | ---: | ---: |
| Native | 30 | 6.648 | 6.313 | 1.314 |
| PERIOD | 30 | 17.957 | 18.004 | 4.596 |

The ratio of the pooled means was **2.701×**. The three batch ratios were 2.808×, 3.000×, and 2.360×. Every recorded execution in the three batches exited with code 0, and none timed out. The result covers one benchmark and the PERIOD-to-Native comparison under our measurement protocol.

The [summary](summary.txt) reports the same statistics. Each batch has a per-execution CSV and the raw PERIOD search log.

| Batch | Timings | Runner output |
| --- | --- | --- |
| 1 | [CSV](batch-1/timing.csv) | [Log](batch-1/period.log) |
| 2 | [CSV](batch-2/timing.csv) | [Log](batch-2/period.log) |
| 3 | [CSV](batch-3/timing.csv) | [Log](batch-3/period.log) |
