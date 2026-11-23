# CS340 PERIOD Replication

A four-member group project for CS340 Operating Systems, Academic Year 2026–2027.

## 1. Selected Paper

**Controlled Concurrency Testing via Periodical Scheduling**

Cheng Wen, Mengda He, Bohao Wu, Zhiwu Xu, and Shengchao Qin.
ICSE 2022.

- Paper: https://wcventure.github.io/pdf/ICSE2022_PERIOD.pdf
- Original repository: https://github.com/wcventure/PERIOD
- DOI: https://doi.org/10.1145/3510003.3510178

This repository documents our replication experiments. The original PERIOD tool and benchmarks are credited to their authors.

## 2. Team Members

| Full Name | Student ID | GitHub Username | Main Responsibility |
|---|---|---|---|
| Li Mengya | 1240035896 | Sophiamialia | TBD |
| Jiao Yuhan | 1240023651 | jiaoyuhan060208 | TBD |
| Lin Mengyao | 1240020457 | lynn060104 | TBD |
| TBD | TBD | TBD | TBD |

Team responsibilities and individual contributions will be updated as the project progresses.

## 3. Replication Objectives

The project aims to:

1. Reproduce selected concurrency bug detection results reported in the PERIOD paper.
2. Compare PERIOD with a Serial compatibility implementation on selected benchmarks.
3. Conduct a controlled extension experiment.
4. Document experimental configurations, results, limitations, and deviations from the original paper.

The current formal experiments focus on the `CS.reorder_4_bad` benchmark corresponding to Table 2 of the paper.

## 4. Experimental Environment

| Item | Configuration |
|---|---|
| Host OS | Windows 11 |
| Linux environment | WSL2 |
| Distribution | Ubuntu 22.04.1 LTS |
| Architecture | x86_64 |
| CPU | 12th Gen Intel Core i5-1230U |
| Logical CPUs | 12 |
| Available memory | Approximately 7.6 GiB |
| Docker version | 29.1.3 |
| Container OS | Ubuntu 18.04.5 LTS |
| Python version | 3.6.9 |
| Clang version | 10.0.0 |
| Container | eager_ramanujan |
| Docker image | period:latest |

Upstream source commit:

`b6f72a7b06d01ffa7114b640312873ec2578a5ea`

The container shares the WSL2 Linux kernel.

Detailed environment information is available in `environment-container.txt`.

## 5. Benchmark and Experimental Configuration

Benchmark: `CS.reorder_4_bad`

Working directory:

`/workdir/PERIOD/evaluation/CS/reorder_4`

### PERIOD

```bash
python3 -u /workdir/PERIOD/tool/DBDS/run_PDS.py \
-y -d 3 -t 5 -f 10000 ./reorder_4_bad
```

### Serial Compatibility

```bash
python3 -u /workdir/PERIOD/tool/DBDS/run_SerialCompat.py \
-y -d 3 -t 5 -f 10000 ./reorder_4_bad
```

Experimental parameters:

- Bug depth argument: 3
- Per-execution timeout: 5 seconds
- Schedule budget: 10000
- Independent trials: 3 per method

The Serial compatibility runner is an adapted implementation, not the unmodified original Serial artifact.

The two runners translate their depth arguments into period bounds differently. Equal command-line depth values do not necessarily represent identical search bounds.

## 6. Experimental Results

### 6.1 PERIOD

Three independent trials were conducted.

| Metric | Trial 01 | Trial 02 | Trial 03 |
|---|---:|---:|---:|
| Total schedules | 100 | 100 | 100 |
| First error schedule | 9 | 9 | 9 |
| Error interleavings | 12 | 12 | 12 |
| Timeouts | 0 | 0 | 0 |
| Elapsed time (s) | 5.52715 | 2.15610 | 4.16526 |

Mean elapsed time: 3.94950 seconds.

Sample standard deviation: 1.69585 seconds.

PERIOD consistently detected its first error at schedule 9 in all three trials.

### 6.2 Serial Compatibility

Three independent trials were conducted.

| Metric | Trial 01 | Trial 02 | Trial 03 |
|---|---:|---:|---:|
| Total schedules | 384 | 384 | 384 |
| First error schedule | 47 | 47 | 47 |
| Error interleavings | 85 | 87 | 90 |
| Timeouts | 1 | 0 | 0 |
| Elapsed time (s) | 28.28271 | 10.12333 | 10.64638 |

Mean elapsed time: 16.35081 seconds.

Sample standard deviation: 10.33664 seconds.

One timeout was observed in Trial 01. Its cause has not been independently established.

### 6.3 Comparison Between Methods

| Metric | PERIOD | Serial Compatibility |
|---|---:|---:|
| Mean elapsed time (s) | 3.94950 | 16.35081 |
| Total schedules per trial | 100 | 384 |
| Mean error interleavings | 12.00 | 87.33 |
| Total timeouts across trials | 0 | 1 |

PERIOD detected the first error earlier and completed the configured search in less time in these experiments.

However, the two implementations explored different numbers of schedules and use different period-bound translations. Therefore, these measurements should not be interpreted as a fully controlled performance comparison.

## 7. Comparison with the Original Paper

The paper reports the following results for `CS.reorder_4_bad` in Table 2.

| Metric | PERIOD Paper | PERIOD Ours | Serial Paper | Serial Compatibility Ours |
|---|---:|---:|---:|---:|
| Schedules to first bug | 9 | 9 | 37 | 47 |
| Total schedules | 100 | 100 | 384 | 384 |
| Buggy schedules / Error interleavings | 12 | 12 | 90 | 87.33 (mean) |

Observations:

1. PERIOD reproduced the reported first-error schedule and total schedule count.
2. PERIOD detected 12 error interleavings in every trial, numerically matching the paper's 12 buggy schedules.
3. The exact equivalence between error interleavings and buggy schedules has not been independently established.
4. Serial compatibility reproduced the total schedule count but detected its first error at schedule 47 rather than schedule 37.
5. Serial compatibility produced 85, 87, and 90 error interleavings, compared with 90 buggy schedules reported in the paper.

The paper reports 10 invocations for each compared technique on each program, whereas our current experiments contain three independent trials per method.

Therefore, this work is a partial reproduction of the selected benchmark, not a complete reproduction of all results in Table 2.

## 8. Baseline Comparison and PDS Replay

### 8.1 Baseline Comparison

Two saved baseline error sets were compared.

| Metric | Original Baseline | New Baseline |
|---|---:|---:|
| Error schedules | 86 | 91 |

The comparison identified:

- Common schedule IDs: 85
- Identical interleaving records among common IDs: 85
- Original-only schedule: 349
- New-only schedules: 80, 112, 113, 154, 184, 222

All 85 common schedule IDs contained identical saved interleaving records.

### 8.2 PDS Replay Results

Selected schedules were independently tested using PDS replay.

| Schedule | Assertion-Failure Reproductions | Attempts | Observed Rate |
|---|---:|---:|---:|
| 47 | 5 | 5 | 100% |
| 80 | 5 | 5 | 100% |
| 222 | 0 | 5 | 0% |
| 349 | 0 | 5 | 0% |

Schedules 47 and 80 consistently reproduced the assertion failure.

Schedules 222 and 349 did not reproduce the assertion failure in the five observed attempts.

These observations describe the current experimental environment and should not be interpreted as theoretical probabilities.

Scan-time error detection and successful independent replay are distinct experimental outcomes.

## 9. Reproducibility and Data Organization

Formal experiment logs are archived under:

```text
formal-results/
├── PERIOD/
│   ├── trial01/run.log
│   ├── trial02/run.log
│   └── trial03/run.log
│
├── SerialCompat/
│   ├── trial01/run.log
│   ├── trial02/run.log
│   └── trial03/run.log
│
└── reorder_4/
    ├── baselines/
    │   ├── original/Errors/
    │   └── new-baseline/Errors/
    │
    ├── replay/
    │   ├── schedule-47.log
    │   ├── schedule-80.log
    │   ├── schedule-222.log
    │   └── schedule-349.log
    │
    ├── baseline-comparison.md
    └── reproduction-summary.md
```

Additional experiment records include:

- `trial02-03-summary.md`
- `paper-vs-ours.md`
- `trial-results.csv`
- `trial-summary.csv`
- `analyze_results.py`
- `serial-compat.patch`
- `environment-container.txt`

The raw logs and saved error schedules are retained to support result verification.

## 10. Limitations and Future Work

The current experiments have several limitations:

1. Only one benchmark, `CS.reorder_4_bad`, has been formally evaluated.
2. The Serial implementation is an adapted compatibility version rather than the original unmodified artifact.
3. The two runners do not necessarily use equivalent period bounds.
4. The current repeated experiments contain three trials per method rather than the 10 invocations reported in the paper.
5. The equivalence between error interleavings and buggy schedules remains unverified.
6. Some saved schedules did not reproduce consistently during independent PDS replay.
7. Further experiments are required to investigate the differences between our results and the paper.

Future work will focus on additional benchmark validation, further investigation of replay stability, and the controlled extension experiment.

## 11. Contributions and AI Usage

Individual responsibilities and contributions will be documented by the project team.

AI assistance was used for environment troubleshooting, experimental workflow guidance, compatibility adaptation support, and documentation drafting.

Team members remain responsible for understanding, reviewing, and validating the experimental commands, code modifications, and reported results.

## 12. Attribution and Licensing

The original PERIOD tool, benchmarks, and documentation are credited to their respective authors.

Original source code and upstream materials remain subject to their respective licenses. Relevant license notices and source information are preserved in this repository.
