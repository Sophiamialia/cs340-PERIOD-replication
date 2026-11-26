# RQ1: Reproduction Results

## 1. Experimental Objective

This experiment evaluates PERIOD (PDS) and SerialCompat
on two concurrent benchmarks: reorder_3_bad and
reorder_4_bad.

Three independent trials were conducted for each method
and benchmark under the corresponding experimental
configuration.

## 2. Experimental Environment

- Environment: WSL2 + Docker
- Benchmark 1: reorder_3_bad (3 threads)
- Benchmark 2: reorder_4_bad (4 threads)
- Bug depth: 3
- Subprocess timeout: 5 seconds
- Runs limit: 10000
- Number of trials: 3 per method and benchmark

## 3. Results on reorder_3_bad (3 Threads)

### 3.1 PERIOD (PDS)

| Trial | Tested | Errors | Timeouts |
|---|---:|---:|---:|
| 1 | 27 | 6 | 0 |
| 2 | 27 | 6 | 0 |
| 3 | 27 | 6 | 0 |
| Average | 27 | 6 | 0 |

### 3.2 SerialCompat

| Trial | Tested | Errors | Timeouts |
|---|---:|---:|---:|
| 1 | 30 | 10 | 0 |
| 2 | 30 | 8 | 0 |
| 3 | 30 | 10 | 0 |
| Average | 30 | 9.33 | 0 |

## 4. Results on reorder_4_bad (4 Threads)

### 4.1 PERIOD (PDS)

| Trial | Tested | Errors | Timeouts |
|---|---:|---:|---:|
| 1 | 100 | 11 | 1 |
| 2 | 100 | 12 | 0 |
| 3 | 100 | 12 | 0 |
| Average | 100 | 11.67 | 0.33 |

Average runtime: 7783.33

Average elapsed time: 16.83212 seconds.

### 4.2 SerialCompat

| Trial | Tested | Errors | Timeouts |
|---|---:|---:|---:|
| 1 | 384 | 90 | 0 |
| 2 | 384 | 90 | 0 |
| 3 | 384 | 88 | 0 |
| Average | 384 | 89.33 | 0 |

Average runtime: 742.

## 5. Preliminary Comparison

On reorder_3_bad, SerialCompat explored 30 interleavings,
while PDS explored 27 interleavings per trial.

On reorder_4_bad, SerialCompat explored 384 interleavings,
while PDS explored 100 interleavings per trial.

SerialCompat detected more error interleavings in both
benchmark experiments.

However, the number of explored interleavings differs
between the methods. Therefore, raw error counts should
not be interpreted as a direct measure of overall
effectiveness.

## 6. Repeated-Trial Analysis

PDS consistently detected 6 errors in all three
reorder_3_bad trials.

For reorder_4_bad, PDS detected 11, 12, and 12 errors.

SerialCompat detected 10, 8, and 10 errors on
reorder_3_bad, and 90, 90, and 88 errors on
reorder_4_bad.

No timeouts occurred in the SerialCompat trials.

One timeout occurred in the first PDS trial on
reorder_4_bad.

## 7. Data Organization

All experimental records are stored under:

formal-results/WSL2/

The directories contain:
- Raw execution logs (run.log)
- Experimental summaries (summary.txt)
- Error interleaving records
- Timeout records, where applicable
- Aggregate CSV files

## 8. Current Status

- reorder_3_bad: 3 PDS trials and 3 SerialCompat trials.
- reorder_4_bad: 3 PDS trials and 3 SerialCompat trials.
- All 12 trials completed.
- Error interleaving files collected.
- Timeout records collected where applicable.
- Aggregate experimental statistics prepared.
