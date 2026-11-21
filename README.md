# Convenience Samples, Generalizability, and Date Psychology — Reproducibility Materials

Code, published-number transcriptions, source checks, and the figure accompanying the [methodological review](https://datepsych.substack.com/p/convenience-samples-are-legitimate) **“Convenience Samples Are Legitimate. That Doesn't Make Them Interchangeable.”**

**Scope.** This is an independent **reconstruction from published aggregate statistics**, not a reanalysis of participant-level data, an independent replication of Rohr et al.'s survey calculations, or a replication of Alexander's 90-paper audit. This repository does **not** estimate bias in Date Psychology's own samples. It supplies the inputs and code behind the essay's chart, checks a few publicly printed numbers, and documents the limits of the cited evidence.


## What is included

| File or folder | Purpose |
|---|---|
| `reproduce_convenience_sampling.py` | Reads the transcribed source statistics, validates them, creates a new Figure 1, and writes a reproducible audit report and calculated summaries. |
| `published_rohr_correlations.csv` | **All 15 published survey-level “No Diff” percentages** from Rohr et al. (2025): 8 microcensus comparisons and 7 GGSS comparisons. |
| `published_rohr_large_differences.csv` | The paper's four published group-average large-difference and magnitude-difference percentages. |
| `published_alexander_sampling_counts.csv` | Alexander's printed 90-paper, student-sample and online-category numbers. **Not** a recovered 90-row coding sheet. |
| `source_reference_map.csv` | The essay's 11 numbered reference entries, source URLs, and applicability limits. |
| `claim_source_audit.csv` | Claim-by-claim guide to the original supporting source and interpretive limitation. |
| `SOURCE_AUDIT.md` | Original-source locations, calculations, methodological boundaries, and known uncertainties. |
| `article_figures/figure_01_rohr_per_survey_no_diff.png` | Unmodified copy of the **figure embedded in the final Substack article**. |
| `reproduced_figures/figure_01_rohr_per_survey_no_diff.png` | Replotted using the standalone script and the same 15 published percentages (not intended to be pixel-identical). |
| `reproduced_figures/*.csv` | Recomputed descriptive ranges and transparent arithmetic of Alexander's printed counts. |
| `reconstruction_results.txt` | Checked text output from the reproduction script (also in `reproduced_figures/`). |
| `tests/test_reconstruction.py` | Unit tests for transcribed values, panel coverage, numeric consistency, and end-to-end reproducibility. |
| `requirements.txt` | Python plotting dependency. |
| `GITHUB_UPLOAD_INSTRUCTIONS.md` | How to publish the package and link it from Substack. |

## Reproduce the chart and numeric checks

Requires **Python 3.10+**. In the repository directory:

```bash
python -m pip install -r requirements.txt
python reproduce_convenience_sampling.py
python -m unittest discover -s tests -v
```

The script writes the regenerated figure, `rohr_per_survey_summaries.csv`, `alexander_arithmetic_checks.csv`, and `reconstruction_results.txt` to `reproduced_figures/`. It does not overwrite `article_figures/`.

To use another output directory:

```bash
python reproduce_convenience_sampling.py --out another_folder
```

All numerical inputs are ordinary CSV files and can be inspected without installing Python. **No internet access is needed** to run the code. Figure fonts or layout may vary slightly between systems.

## What is being reconstructed?

### Figure 1 — Rohr et al.'s correlation comparisons

Rohr, Silber, and Felderer (2025) compared **three German probability surveys and five German nonprobability surveys** against benchmark data. The essay's figure plots their printed per-survey percentages of **“No Diff” correlation comparisons**, taken from the textual discussions accompanying **Figures 3 and 4**.

- **Microcensus benchmark:** eight compared surveys; up to 153 demographic/occupational variable pairs where all 18 variables were present.
- **GGSS benchmark:** seven compared surveys; up to 703 demographic/political/religious variable pairs where all 38 variables were present. GGSS itself is the benchmark and is not plotted as a comparison against itself.
- The original study used weighted analyses, bootstrap procedures and multiple-testing adjustments. **We did not rerun those procedures.** We replot the percentages that the authors published.
- **“No Diff” means the paper did not detect a statistically significant difference by its procedure. It does not mean equivalence, zero bias, or matching correlation estimates.** Power, measurement, sample composition, and variable coverage matter.

The descriptive ranges/means printed by our script are simple summaries of the **published rounded survey percentages**, not independent estimates of the original sampling uncertainty. The script does not calculate a probability of bias or infer the performance of DatePsychology's audience.

### Alexander's reported sampling categories

Alexander's May 2024 article reports a 90-paper count, including **49 student samples** and **36 online samples**, and subsequently uses the phrase **“18 of the 39”**. It lists four online subcategory counts of **18, 9, 8, and 5**.

The script shows that the subcategories total **40 assignments** and the student/online/other category tallies sum to **98 assignments**. **These sums are *not* unique-paper counts.** If a study used both student and online recruitment, category counts could overlap. Without the author's actual 90-paper inclusion list and codebook, the discrepancy is unresolved—not proof of an error or systematic misclassification.

The article deliberately gives this peripheral audit only limited emphasis. The repo contains **no unfinished 102-reference reconstruction** and does not pretend to reproduce an unavailable coding sheet.

## Principal findings and important limits

1. **Convenience sampling is legitimate:** the methodological literature documents many sound uses of both university and online convenience samples.
2. **Population proportions and associations are different estimands:** observational relationships often prove more stable than descriptive proportions, but stability varies with variables and recruitment.
3. **The Rohr benchmark is informative but not a direct analogy:** it involves German panel surveys and demographic/political variables, not a creator-recruited sociosexuality study.
4. **Replication across cultures is meaningful:** the essay credits Alexander's sociosexuality example rather than treating it as evidence-free. This repository does not estimate a pooled SOI-R sex difference.
5. **Reporting requirements introduced in November 2026 postdate the 2024 essay:** they are discussed as a subsequent development, not a retroactive standard.
6. **No original participant data** or unpublished 90-paper table were accessed or are redistributed here.

## Primary sources

- [Alexander (2024), original sampling essay](https://datepsychology.com/how-samples-are-collected-in-evolutionary-and-personality-psychology/).
- [Rohr, Silber & Felderer (2025), *Sociological Methodology*](https://doi.org/10.1177/00811750241280963), Figures 3–4 and the “Bivariate Comparison” discussion.
- [Jager, Putnick & Bornstein (2017), full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC5606225/).
- [Herbenick et al. (2026), journal reporting requirements](https://link.springer.com/article/10.1007/s10508-026-03657-1).

The complete 11-source list and links appear in [`source_reference_map.csv`](source_reference_map.csv); precise sourcing for the numerical files appears in [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md).

## Companion article

**Rights and data:** This repository includes only independently written code, a newly generated figure, one copy of the article's original figure, and short transcriptions of publicly reported summary numbers. It does not redistribute original research PDFs, copyrighted source texts, or respondent records. Citations and methodological interpretations do not confer rights over the source publications.
