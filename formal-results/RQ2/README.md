# RQ2 — PERIOD vs. Native on `CS.reorder_4_bad`

We compared PERIOD with Native execution on one SCTBench benchmark in the same VirtualBox and Docker environment. Each method had three trials, with a budget of 100 test executions per trial and a five-second timeout per execution. PERIOD's initialization dry run was excluded from the test budget.

| Method | Trials that detected the target assertion failure | First detection in each trial | Timeouts by trial |
|---|---:|---|---|
| PERIOD | 3/3 | 9, 9, 9 | 1, 0, 0 |
| Native | 0/3 | Not observed in any trial | 0, 0, 0 |

Native completed all 300 attempts with normal exits. Under this benchmark and test budget, PERIOD detected the target assertion failure in all three trials, while Native did not observe it.

The raw PERIOD logs, Native per-attempt logs, and result tables are in [the RQ2 archive](rq2-results.XT5SKx.tar.gz).

## `CS.reorder_3_bad`

We ran three trials per method in the same VirtualBox and Docker environment, with a limit of 100 test executions per trial and a five-second timeout per execution.

| Method | Executions per trial | Trials detecting the target assertion failure | First detection by trial | Timeouts |
|---|---:|---:|---|---:|
| PERIOD | 27 | 3/3 | 6, 6, 6 | 0 |
| Native | 100 | 0/3 | Not observed | 0 |

Native also did not observe the target assertion failure in the first 27 attempts of any trial. The [three-thread experiment archive](rq2-reorder3-results.GlycQJ.tar.gz) contains the build log, PERIOD logs, and per-attempt Native records.
