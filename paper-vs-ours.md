# CS.reorder_4_bad: Paper vs. Ours

Date: 2026-11-20

## 1. Benchmark

Benchmark: CS.reorder_4_bad

Paper: Controlled Concurrency Testing via Periodical Scheduling
Conference: ICSE 2022

Paper Table: Table 2

## 2. Experimental Configuration

PERIOD command:

python3 -u /workdir/PERIOD/tool/DBDS/run_PDS.py \
-y -d 3 -t 5 -f 10000 ./reorder_4_bad

Serial compatibility command:

python3 -u /workdir/PERIOD/tool/DBDS/run_SerialCompat.py \
-y -d 3 -t 5 -f 10000 ./reorder_4_bad

Parameters:
- Bug depth: 3
- Per-execution timeout: 5 seconds (our experimental configuration; not claimed to be the paper's timeout setting)
- Schedule budget: 10000
- Independent trials: 3 per method

Note: The Serial compatibility runner is an adapted
implementation, not the unmodified original Serial artifact.

## 3. Paper vs. Our Results

| Metric | PERIOD Paper | PERIOD Ours | Serial Paper | Serial Compatibility Ours |
|---|---:|---:|---:|---:|
| Schedules to first bug | 9 | 9 | 37 | 47 |
| Total schedules | 100 | 100 | 384 | 384 |
| Buggy schedules (paper) / Error interleavings (ours) | 12 | 12 | 90 | 87.33 (mean) |

The PERIOD results reproduce the reported first-error schedule
and total schedule count. The number of error interleavings is
numerically equal to the paper's reported number of buggy
schedules (12), although the exact equivalence of these counters
has not been independently established.

The Serial compatibility results reproduce the total schedule
count, but differ in the first-error position and the number
of error interleavings.

The paper reports buggy schedules, whereas our runner reports
error interleavings. These counters are shown side by side for
reference; their exact equivalence has not been established.

The paper reports 90 buggy schedules for Serial, whereas our
three adapted Serial trials report 85, 87, and 90 error
interleavings, respectively.

## 4. Repeated Experimental Results

### PERIOD

| Metric | Trial 1 | Trial 2 | Trial 3 |
|---|---:|---:|---:|
| Total schedules | 100 | 100 | 100 |
| First error | 9 | 9 | 9 |
| Error interleavings | 12 | 12 | 12 |
| Timeouts | 0 | 0 | 0 |
| Elapsed time (s) | 5.52715 | 2.15610 | 4.16526 |

Mean elapsed time: 3.94950 s
Sample standard deviation: 1.69585 s

### Serial Compatibility

| Metric | Trial 1 | Trial 2 | Trial 3 |
|---|---:|---:|---:|
| Total schedules | 384 | 384 | 384 |
| First error | 47 | 47 | 47 |
| Error interleavings | 85 | 87 | 90 |
| Timeouts | 1 | 0 | 0 |
| Elapsed time (s) | 28.28271 | 10.12333 | 10.64638 |

Mean elapsed time: 16.35081 s
Sample standard deviation: 10.33664 s

## 5. Interpretation and Limitations

1. PERIOD consistently detected its first error at schedule 9
   in all three trials, matching the paper.

2. PERIOD explored 100 schedules in each trial, matching the
   paper's reported total schedule count.

3. PERIOD reported 12 error interleavings in each trial. This is
   numerically equal to the paper's 12 buggy schedules, but exact
   equivalence of the two counters remains unverified.

4. Serial compatibility explored 384 schedules in each trial,
   matching the paper's total schedule count.

5. Serial compatibility detected its first error at schedule
   47, whereas the paper reports schedule 37.

6. The mean number of error interleavings for Serial
   compatibility was 87.33, compared with 90 in the paper.

7. One Serial compatibility trial recorded one timeout.
   The other two recorded none.

8. The adapted Serial runner contains compatibility
   modifications. Its results must not be presented as results
   from an unmodified original Serial implementation.

9. Equal command-line depth arguments do not necessarily
   represent identical period bounds between the two runners.

10. These experiments cover only CS.reorder_4_bad and do not
   establish reproduction of all results in Table 2.

11. The paper reports 10 invocations for each compared
    technique on each program, whereas our experiments
    currently contain three independent trials per method.
    Therefore, our repeated-trial results are not a complete
    reproduction of the paper's statistical evaluation.

## 6. Reproducibility Files

- analyze_results.py
- trial-results.csv
- trial-summary.csv
- reorder4-period-trial01.log
- reorder4-period-trial02.log
- reorder4-period-trial03.log
- reorder4-serial-compat-trial01.log
- reorder4-serial-compat-trial02.log
- reorder4-serial-compat-trial03.log
- serial-compat.patch
