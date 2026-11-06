# `doubleFree` smoke test

The first check was run earlier on the Ubuntu VM, inside the `period-lab` Docker container. I documented that check from screenshots because I did not save a full log at the time. I reran the search on November 6, 2026 and saved its [raw output](period-smoke-20261106.log).

- Built `/workdir/PERIOD/test/doubleFree` with `./cleanDIR.sh && ./build.sh`. It completed with two non-fatal return-type warnings.
- Ran `/workdir/PERIOD/tool/DBDS/run_PDS.py -y -d 3 ./df`.
- On the November 6 rerun, PERIOD tested 6 schedules, reported 4 error interleavings and 0 timeouts. The output directory was `out_df_2`; the reported test time was `00:00:01.54778`.
- On the earlier check, I replayed `out_df_1/Errors/000001_0000003_double-free` with `run_PDS.py -r`. AddressSanitizer ended with `SUMMARY: AddressSanitizer: double-free`. That replay was not part of the saved November 6 log.

The saved log begins with a `sudo: unable to resolve host` warning, but the search completed and produced the counts above. These checks show that the installation works; they are not a repeated benchmark experiment and do not yet show whether we can reproduce the paper's results. For formal experiments, we still need to save the command and raw output for every run.
