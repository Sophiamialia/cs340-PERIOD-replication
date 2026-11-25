# Extension: Worker Count and Schedule Exploration

This experiment measured how worker count affects PERIOD's schedule
exploration on a small shared-counter program. Each worker increments
the same counter twice under a mutex. We tested 2, 4, and 8 workers,
with three runs per setting.

All nine runs used the same VirtualBox VM and PERIOD container.
The VM ran Ubuntu 22.04.5 LTS with kernel 6.8.0-149-generic, four
visible CPUs, and 7.8 GiB of RAM. We kept the program, instrumentation,
depth argument (3), per-execution timeout (5 s), and schedule limit
(10,000) fixed across runs. See [environment.txt](environment.txt).

| Workers | Schedules per run | Elapsed time, mean ± sample SD (s) | Total timeouts |
|---:|---:|---:|---:|
| 2 | 26 | 1.43 ± 0.47 | 0 |
| 4 | 364 | 18.22 ± 4.01 | 0 |
| 8 | 3256 | 245.15 ± 160.91 | 2 |

Every run ended below the schedule limit. PERIOD reported zero error
interleavings in all nine runs. Both timeouts occurred in the second
8-worker run. Schedule counts were stable across repeats at each
worker count, but elapsed time varied considerably at 8 workers.

Increasing the worker count also increases the total number of counter
updates, since each worker performs two updates. These results describe
this program and configuration. The row-level measurements and links
to the raw logs are in [results.csv](results.csv).


