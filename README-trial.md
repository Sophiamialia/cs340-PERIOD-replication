# CS340 PERIOD: reorder_4 Pilot Experiments

Contributor: Li Mengya (李梦雅)
Experiment date: 2026-11-13
Status: One pilot run per method; not a completed replication.

## Benchmark and source

Benchmark: CS.reorder_4_bad, corresponding to Table 2.
Paper: https://wcventure.github.io/pdf/ICSE2022_PERIOD.pdf
Upstream: https://github.com/wcventure/PERIOD
The upstream commit and container environment are recorded in
environment-container.txt.

## Build

Working directory:
/workdir/PERIOD/evaluation/CS/reorder_4

Command:
bash ./build.sh

Build output: reorder4-build.log

## Runs

Both commands were executed from the benchmark directory.

PERIOD:
python3 -u /workdir/PERIOD/tool/DBDS/run_PDS.py -y -d 3 -t 5 -f 10000 ./reorder_4_bad

Serial compatibility runner:
python3 -u /workdir/PERIOD/tool/DBDS/run_SerialCompat.py -y -d 3 -t 5 -f 10000 ./reorder_4_bad

The initial PERIOD run invoked run_PDS.py directly rather than
through python3 -u. Exact invocation should also be checked
against the experiment records.

Parameters: depth argument 3, per-execution timeout 5 seconds,
schedule budget 10000. The runners translate depth into period
bounds differently; equal depth arguments do not mean identical
period counts.

## Pilot results

| Metric | PERIOD | Serial compatibility runner |
|---|---:|---:|
| Schedule number of first detected error | 9 | 47 |
| Total schedules | 100 | 384 |
| Error interleavings | 12 | 85 |
| Timeouts | 0 | 1 |
| Tool-reported total seconds | 5.52715 | 28.28271 |

PERIOD log: reorder4-period-trial01.log
PERIOD detailed output: out_reorder_4_bad_1/
Serial log: reorder4-serial-compat-trial01.log
Serial detailed output: out_reorder_4_bad_2/

Serial schedule 209 exceeded the 5-second timeout.
Its cause remains unverified; it is not classified as a deadlock.
Error interleavings are not counts of distinct vulnerabilities.

## Paper comparison

For CS.reorder_4_bad, Table 2 reports:
- PERIOD: first error 9; total schedules 100; buggy schedules 12.
- Serial: first error 37; total schedules 384; buggy schedules 90.

The PERIOD pilot matches these three reported counts.
The adapted serial pilot differs in first-error position and
error-interleaving count. No causal explanation is established yet.

## Compatibility modification

The old serial runner crashed during shared-memory access.
Its requested size was 24300 bytes; the existing segment was
24008 bytes. The old and current runners also use different
array element widths and offsets.

run_SerialCompat.py preserves the old runner's scheduling logic,
while copying three shared-memory helper functions from
run_PDS.py and changing four array declarations to c_uint16.
The original runner was not overwritten.
Changes are preserved in serial-compat.patch.

This is an adapted serial implementation, not an unmodified
execution of the paper's original Serial artifact.
Full equivalence with the paper setup remains to be validated.

## Excluded and pending work

Files named reorder4-serial-trial01.log, similarly misspelled
logs, and empty logs are failed launch attempts, not results.

Still pending:
- Independent repetitions and mean/standard deviation.
- Further validation of the serial adaptation.
- Investigation of the timeout and result discrepancies.
- VM OS, Docker, image identity, and host hardware records.
- A controlled extension experiment.

AI assisted troubleshooting and generation of the compatibility
adaptation. The team must review and validate these changes.
