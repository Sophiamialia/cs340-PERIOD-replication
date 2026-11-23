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

## 3. Final PDS Replay Results

Five independent replay attempts were performed for each selected schedule.

| Schedule | Successful Reproductions | Attempts | Observed Rate |
|---|---:|---:|---:|
| 47 | 5 | 5 | 100% |
| 80 | 5 | 5 | 100% |
| 222 | 0 | 5 | 0% |
| 349 | 0 | 5 | 0% |
| Total | 10 | 20 | 50% |

## 4. Interpretation

Schedules 47 and 80 consistently reproduced the assertion failure in all five attempts.

Schedules 222 and 349 entered the reproduction phase but did not reproduce the assertion failure in any of the five attempts.

These results demonstrate that scan-time error detection and independent PDS replay are distinct experimental outcomes.

The observed replay rates describe only the selected schedules in the current experimental environment and should not be interpreted as theoretical probabilities or the overall detection rate of PERIOD.

## 5. Archived Final Replay Logs

All 20 final replay logs are archived under:

- replay/final/schedule-47/
- replay/final/schedule-80/
- replay/final/schedule-222/
- replay/final/schedule-349/

Each directory contains five attempt logs (attempt-01.log through attempt-05.log).

The original schedule inputs are archived under:

- replay/inputs/schedule-47.input
- replay/inputs/schedule-80.input
- replay/inputs/schedule-222.input
- replay/inputs/schedule-349.input

SHA256 checks were performed on the archived logs. The five logs within each schedule group have matching hashes.

## 6. Experimental Limitations

The replay experiment covers four selected schedules only.

The results should be interpreted as observations from repeated executions under the current environment. They do not establish that schedules 222 and 349 can never reproduce the assertion failure.
