# PERIOD Baseline Comparison: reorder_4

## 1. Experimental Results

| Metric | Original Baseline | New Baseline |
|---|---:|---:|
| Error Interleavings | 86 | 91 |

## 2. Common Error Interleavings

| Metric | Result |
|---|---:|
| Common Schedule IDs | 85 |
| Identical Interleavings | 85 |

All 85 common schedule IDs contain identical
saved interleaving records.

## 3. Different Error Interleavings

Original-only:
- Schedule 349

New-only:
- Schedule 80
- Schedule 112
- Schedule 113
- Schedule 154
- Schedule 184
- Schedule 222

## 4. Interpretation

The new baseline detected 91 error interleavings,
compared with 86 in the original baseline.

The two experiments shared 85 error schedule IDs,
and all 85 common records contained identical
interleaving patterns.

One error schedule appeared only in the original
baseline, while six appeared only in the new baseline.

These results demonstrate differences in the observed
error sets between the two baseline experiments.

Scan-time detection and independent replay stability
are evaluated separately.
