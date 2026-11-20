import re
import csv
import statistics
from pathlib import Path

FILES = {
    "PERIOD": [
        "reorder4-period-trial01.log",
        "reorder4-period-trial02.log",
        "reorder4-period-trial03.log",
    ],
    "Serial Compatibility": [
        "reorder4-serial-compat-trial01.log",
        "reorder4-serial-compat-trial02.log",
        "reorder4-serial-compat-trial03.log",
    ],
}

ANSI_RE = re.compile(r'\x1b\[[0-9;]*[A-Za-z]')


def analyze(filename):
    text = Path(filename).read_text(errors="replace")

    # Remove terminal color codes
    text = ANSI_RE.sub("", text)

    lines = text.splitlines()

    def extract(pattern):
        values = re.findall(pattern, text, re.MULTILINE)
        if not values:
            raise ValueError(
                f"Cannot extract data from {filename}: {pattern}"
            )
        return values[-1]

    first_error = None

    for i, line in enumerate(lines):
        if "[Error Found]" in line:
            for previous in reversed(lines[:i]):
                match = re.search(r"test\s+(\d+):", previous)
                if match:
                    first_error = int(match.group(1))
                    break
            break

    elapsed = extract(
        r"Time\s+[\d:.]+\s+([\d:.]+)\s*$"
    )

    hours, minutes, seconds = elapsed.split(":")

    elapsed_seconds = (
        int(hours) * 3600
        + int(minutes) * 60
        + float(seconds)
    )

    return {
        "method": "",
        "file": filename,
        "total_schedules": int(
            extract(r"Round\s+0\s+(\d+)")
        ),
        "first_error": first_error,
        "errors": int(
            extract(r"Total Error Interleavings:\s*(\d+)")
        ),
        "timeouts": int(
            extract(r"Total Timeouts Interleavings:\s*(\d+)")
        ),
        "elapsed": elapsed_seconds,
    }


all_results = []
summary = {}

for method, files in FILES.items():

    trials = []

    for filename in files:
        result = analyze(filename)
        result["method"] = method
        trials.append(result)
        all_results.append(result)

    times = [r["elapsed"] for r in trials]
    errors = [r["errors"] for r in trials]

    summary[method] = {
        "mean_time": statistics.mean(times),
        "std_time": statistics.stdev(times),
        "mean_errors": statistics.mean(errors),
        "total_timeouts": sum(r["timeouts"] for r in trials),
    }

print("=" * 75)
print("CS.reorder_4_bad - Three-Trial Experimental Results")
print("=" * 75)

for method, trials in [
    (m, [r for r in all_results if r["method"] == m])
    for m in FILES
]:
    print("\nMethod:", method)

    for i, r in enumerate(trials, 1):
        print(
            f"Trial {i}: "
            f"Schedules={r['total_schedules']}, "
            f"First Error={r['first_error']}, "
            f"Errors={r['errors']}, "
            f"Timeouts={r['timeouts']}, "
            f"Time={r['elapsed']:.5f}s"
        )

    s = summary[method]

    print(f"Mean time: {s['mean_time']:.5f}s")
    print(f"Sample SD: {s['std_time']:.5f}s")
    print(f"Mean errors: {s['mean_errors']:.2f}")
    print(f"Total timeouts: {s['total_timeouts']}")

# Export raw trial-level data
with open("trial-results.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "method", "file", "total_schedules",
            "first_error", "errors", "timeouts", "elapsed"
        ]
    )
    writer.writeheader()
    writer.writerows(all_results)

# Export summary data
with open("trial-summary.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Method", "Mean elapsed time (s)",
        "Sample SD (s)", "Mean error interleavings",
        "Total timeouts"
    ])

    for method, s in summary.items():
        writer.writerow([
            method,
            f"{s['mean_time']:.5f}",
            f"{s['std_time']:.5f}",
            f"{s['mean_errors']:.2f}",
            s["total_timeouts"],
        ])

print("\nCSV files generated:")
print("1. trial-results.csv")
print("2. trial-summary.csv")
print("\nAnalysis completed successfully.")
