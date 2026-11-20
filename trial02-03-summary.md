# CS.reorder_4_bad: Three-Trial Experimental Summary

Date: 2026-11-20

## 1. PERIOD

| Metric | Trial 01 | Trial 02 | Trial 03 |
|---|---:|---:|---:|
| Total schedules | 100 | 100 | 100 |
| First error schedule | 9 | 9 | 9 |
| Error interleavings | 12 | 12 | 12 |
| Timeouts | 0 | 0 | 0 |
| Elapsed time (s) | 5.52715 | 2.15610 | 4.16526 |

Mean elapsed time: 3.94950 s
Sample standard deviation: 1.69585 s

## 2. Serial Compatibility

| Metric | Trial 01 | Trial 02 | Trial 03 |
|---|---:|---:|---:|
| Total schedules | 384 | 384 | 384 |
| First error schedule | 47 | 47 | 47 |
| Error interleavings | 85 | 87 | 90 |
| Timeouts | 1 | 0 | 0 |
| Elapsed time (s) | 28.28271 | 10.12333 | 10.64638 |

Mean elapsed time: 16.35081 s
Sample standard deviation: 10.33664 s

## 3. Comparison

| Metric | PERIOD | Serial Compatibility |
|---|---:|---:|
| Mean elapsed time (s) | 3.94950 | 16.35081 |
| Sample standard deviation (s) | 1.69585 | 10.33664 |
| Total schedules | 100 | 384 |
| Mean error interleavings | 12.00 | 87.33 |
| Total timeouts | 0 | 1 |

The PERIOD pilot configuration consistently detected its first
error at schedule 9, while Serial Compatibility detected its
first error at schedule 47.

PERIOD had a shorter mean elapsed time in these three trials.
The Serial Compatibility implementation is adapted and is not
an unmodified original Serial implementation.

These results are limited to CS.reorder_4_bad and the
experimental configuration documented in README-trial.md.
