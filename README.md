# CS340 PERIOD Replication

A four-member group project for CS340 Operating Systems,
Academic Year 2026–2027.

## 1. Selected Paper

**Controlled Concurrency Testing via Periodical Scheduling**

Cheng Wen, Mengda He, Bohao Wu, Zhiwu Xu, and Shengchao Qin.
ICSE 2022.

- Paper: https://wcventure.github.io/pdf/ICSE2022_PERIOD.pdf
- Original repository: https://github.com/wcventure/PERIOD
- DOI: https://doi.org/10.1145/3510003.3510178

This repository documents our course replication work.
The original PERIOD tool and benchmarks are credited to their authors.

## 2. Team Members

| Full Name | Student ID | GitHub Username | Main Responsibility |
|-----------|------------|-----------------|---------------------|
| Li Mengya | 1240035896 | Sophiamialia | TBD |
| Jiao Yuhan| 1240023651 | jiaoyuhan060208 | TBD |
| Lin Mengyao|1240020457 | TBD | TBD|
|TBD|TBD|TBD|TBD|

Responsibilities and individual contributions will be updated
as the project progresses.

## 3. Replication Objectives

Our planned objectives are:

1. Reproduce detection results for a selected subset of the
   benchmarks in Table 2.
2. Compare PERIOD and Serial on selected benchmarks, subject
   to successful setup of both configurations.
3. Conduct one controlled extension experiment.

The final benchmark list, claims, configurations, and extension
question have not yet been finalized.

We will document all deviations from the original experiments.

## 4. Current Progress

Completed:

- Installed Ubuntu in VirtualBox on a Windows host.
- Installed Docker and verified image download and execution.
- Downloaded the authors' PERIOD Docker image.
- Built and tested the doubleFree demonstration.
- Successfully replayed a saved double-free execution.

Formal paper benchmark experiments have not started.

## 5. Initial Environment

| Item | Current Setup |
|------|---------------|
| Host operating system | Windows; exact version to be recorded |
| Virtualization software | VirtualBox; version to be recorded |
| Guest operating system | Ubuntu 24.04.4 LTS |
| Guest memory | 8192 MB |
| Virtual CPUs | 4 |
| Virtual disk capacity | 80 GB |
| Guest kernel | To be recorded |
| Docker image | wcventure/period:stable |
| Image digest | To be recorded |
| Starting code commit | To be recorded |
| Compiler and tool versions | To be recorded |

The container shares the guest Ubuntu kernel.
Both container and host environment details will be recorded.

## 6. Verified Demonstration

The doubleFree example was tested with:

```bash
cd "$ROOT_DIR/test/doubleFree"
./cleanDIR.sh
./build.sh
"$ROOT_DIR/tool/DBDS/run_PDS.py" -y -d 3 ./df
```

Observed results from the initial demonstration:

| Metric | Observed Value |
|--------|----------------|
| Total schedules explored | 6 |
| Schedules explored up to the first error | 3 |
| Schedules triggering double-free | 4 |

These are demonstration results, not formal paper replication results.
Four failing schedules do not imply four distinct vulnerabilities.

A saved failing schedule was replayed with:

```bash
"$ROOT_DIR/tool/DBDS/run_PDS.py" \
  -r out_df_1/Errors/000001_0000003_double-free ./df
```

AddressSanitizer reported an attempted double-free during replay.

## 7. Experiment and Data Policy

For formal experiments, we will:

- Define benchmark selection criteria before collecting results.
- Record commands, inputs, versions, bounds, and timeouts.
- Repeat each configuration at least three times.
- Report mean and standard deviation where applicable.
- Preserve logs supporting reported numerical results.
- Distinguish failures, timeouts, budget exhaustion,
  and completed runs without a detected error.
- Compare our results with the corresponding paper entries.

## 8. Planned Repository Structure

Directories will be added as work progresses.

```text
docs/       Reading notes, environment records, experiment plans
scripts/    Build, execution, and analysis scripts
results/    Processed experimental data
logs/       Selected raw logs supporting reported results
figures/    Generated charts
report/     Report and presentation materials
```

## 9. Collaboration

- Each member must use their own GitHub account.
- Commit messages must include the contributor's student ID,
  full name, and a description of the change.
- Meaningful progress must be committed and pushed each week.
- Do not commit credentials, VM or container images, build
  artifacts, or files larger than 50 MB.
- The final submission will be tagged v1.0.

Commit message format:

```text
<Student ID> <Full Name>: <description of change>
```

## 10. Contributions and AI Usage

The final report will include an individual contribution statement
and an AI usage statement.

AI assistance has been used for initial environment setup guidance
and drafting this README. Team members are responsible for checking
commands, understanding the tool, and validating all reported results.

## 11. Attribution and Licensing

Original code, benchmarks, and documentation remain subject to
their respective licenses.

When upstream materials are included, their license notices,
source information, and starting versions will be preserved.
