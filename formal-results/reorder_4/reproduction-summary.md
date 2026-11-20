# PERIOD Reproduction: reorder_4

## 1. SerialCompat Scan Results

| Trial | Error Interleavings | Timeouts |
|---|---:|---:|
| Trial 1 | 85 | 1 |
| Trial 2 | 87 | 0 |
| Trial 3 | 90 | 0 |

## 2. Baseline Comparison

| Metric | Original | New Baseline |
|---|---:|---:|
| Error schedules | 86 | 91 |
| Common error schedules | 85 | 85 |

Original-only: 1 (Schedule 349)
New-only: 6 (Schedules 80, 112, 113, 154, 184, 222)

## 3. PDS Replay Stability

| Schedule | Successful Replays | Attempts | Observed Rate |
|---|---:|---:|---:|
| 47 | 5 | 5 | 100% |
| 80 | 5 | 5 | 100% |
| 222 | 0 | 5 | 0% |
| 349 | 0 | 5 | 0% |

## 4. Interpretation

Schedules 47 and 80 consistently reproduced the assertion failure
during PDS replay.

Schedules 222 and 349 did not reproduce the assertion failure
in five repeated PDS replay attempts.

Scan-time error detection and successful independent replay
are distinct experimental outcomes.

The replay results are observations from five attempts per schedule
and should not be interpreted as theoretical probabilities.

## 5. Archived PDS Replay Logs

The original PDS replay logs have been archived under:

- replay/schedule-47.log
- replay/schedule-80.log
- replay/schedule-222.log
- replay/schedule-349.log

Replay observations:

| Schedule | Successful Replays | Attempts |
|---|---:|---:|
| 47 | 5 | 5 |
| 80 | 5 | 5 |
| 222 | 0 | 5 |
| 349 | 0 | 5 |

Schedules 47 and 80 consistently reproduced the assertion failure.
Schedules 222 and 349 did not reproduce the assertion failure
in the five observed attempts.

These observations are specific to the current experimental
environment and should not be interpreted as theoretical probabilities.
