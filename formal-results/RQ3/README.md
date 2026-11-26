# RQ3 runtime overhead on two Figure 7 benchmarks

**Experiments by 1240023651 焦渝涵 (Jiao Yuhan).**

We measured Native and PERIOD on two synthetic benchmarks listed in Figure 7 of [Wen et al. (ICSE 2022)](https://wcventure.github.io/pdf/ICSE2022_PERIOD.pdf#page=10). Both modes ran in the same Docker container in an Ubuntu 22.04 VirtualBox guest.

For each benchmark, each of three batches recorded ten Native subprocess executions and ten timed subprocess executions in one PERIOD search. Batch 2 ran PERIOD first. Batches 1 and 3 ran Native first. The stopwatch measured wall-clock time from just before launching the subprocess through completion of `communicate()`. Both modes used `sudo` and captured stdout and stderr. The measured duration includes subprocess and `sudo` overhead. PERIOD's schedule generation and coverage processing outside the subprocess are outside the timing interval. The PERIOD run used `-y -d 3 -t 5 -f 10`.

| Benchmark | Native mean (ms) | PERIOD mean (ms) | PERIOD / Native |
| --- | ---: | ---: | ---: |
| `reorder_5_bad` | 6.648 | 17.957 | 2.701× |
| `reorder_10_bad` | 4.562 | 15.557 | 3.410× |

Each mean is based on 30 subprocess timings. All 120 recorded executions exited with code 0 and none timed out. The individual batch ratios were 2.808×, 3.000×, and 2.360× for `reorder_5_bad`, and 2.618×, 3.147×, and 4.662× for `reorder_10_bad`.

The summaries report per-mode statistics for [`reorder_5_bad`](summary.txt) and [`reorder_10_bad`](reorder_10_bad/summary.txt). Each batch has a per-execution CSV and the raw PERIOD search log.

| Batch | `reorder_5_bad` | `reorder_10_bad` |
| --- | --- | --- |
| 1 | [CSV](batch-1/timing.csv) · [Log](batch-1/period.log) | [CSV](reorder_10_bad/batch-1/timing.csv) · [Log](reorder_10_bad/batch-1/period.log) |
| 2 | [CSV](batch-2/timing.csv) · [Log](batch-2/period.log) | [CSV](reorder_10_bad/batch-2/timing.csv) · [Log](reorder_10_bad/batch-2/period.log) |
| 3 | [CSV](batch-3/timing.csv) · [Log](batch-3/period.log) | [CSV](reorder_10_bad/batch-3/timing.csv) · [Log](reorder_10_bad/batch-3/period.log) |

## PCT compatibility check

On kernel `6.8.0-149-generic`, the 64-bit executable from [SCTBench's bundled Pin 2.12](https://github.com/mc-imperial/sctbench/tree/d59ab26ddaedcd575ffb6a1f5e9711f7d6d2d9f2/pin) reported `6.8 is not a supported linux release` and exited with code 255 during a startup check. This attempt produced no PCT timing. The measurements above cover the PERIOD-to-Native comparison for the two listed benchmarks. [Terminal evidence](pin-2.12-linux-6.8.png)
