# Source audit — numerical reproduction and limits

**Audit date:** 2026-11-21. This is a *published-results reconstruction*, not new empirical sampling research. The article's discussion of convenience sampling is a literature synthesis. The numerical files here do not make that discussion itself experimentally reproducible.

## 1. Original essay: what it says and what it does not provide

Source: [Alexander (2024), *How Samples Are Collected in Evolutionary and Personality Psychology*](https://datepsychology.com/how-samples-are-collected-in-evolutionary-and-personality-psychology/), May 10, 2024.

The essay says the author's surveys recruit mainly via YouTube, Twitter/X, and the DatePsychology website. Those venues do **not** establish the breakdown by follower status, the sampling frame, or who ultimately participated. Its 90-paper review is described in the text, but no complete 90-row selection and sampling classification table is provided. Consequently, neither exact inclusion decisions nor original paper-level percentages can be reproduced here.

The printed count strings transcribed in `published_alexander_sampling_counts.csv` are:

| Publicly stated quantity | Value | What is actually established |
|---|---:|---|
| Papers/samples reviewed | 90 | Author's stated denominator; no full coding table |
| Student samples | 49 | Author's tally; may overlap online |
| Online survey samples | 36 | Author's first count |
| Later online denominator | 39 | Author's phrase “18 of the 39” |
| Social-media recruitment specified | 18 | A putative online subgroup |
| Unspecified online recruitment | 9 | A putative online subgroup |
| MTurk | 8 | A putative online subgroup |
| Other platforms | 5 | A putative online subgroup |
| Remaining categories | 13 | 4+2+2+2+2+1 reported under remaining papers |

**Reproducible arithmetic:** 18+9+8+5=40 *category assignments*, not necessarily 40 unique papers; 49+36+13=98 *category assignments*, not necessarily 98 unique papers. The 36/39 discrepancy is unexplained by the accessible prose. It is therefore incorrect to infer a specific number of erroneous classifications from those sums.

The repository deliberately omits the inherited provisional 102-reference bibliography: its correspondence to Alexander's unpublished 90-paper selections was not demonstrated, and including the incomplete audit could mislead readers.

## 2. Rohr et al. figure: exact number provenance

Source: [Rohr, Silber & Felderer (2025), *Comparing the Accuracy of Univariate, Bivariate, and Multivariate Estimates across Probability and Nonprobability Surveys with Population Benchmarks*](https://journals.sagepub.com/doi/10.1177/00811750241280963), *Sociological Methodology* 55(1), DOI [10.1177/00811750241280963](https://doi.org/10.1177/00811750241280963). Online publication: 2024-09-28.

All values in `published_rohr_correlations.csv` were transcribed from the **text immediately following published Figures 3 and 4**. They are not values read from pixel positions, simulated, extracted from unseen data, or recomputed from microdata.

### Figure 3 — German microcensus benchmark

| Probability surveys | No Diff | Nonprobability surveys | No Diff |
|---|---:|---|---:|
| GGSS | 87.6% | NP1 | 34.5% |
| GESIS Panel | 72.5% | NP2 | 83.8% |
| German Internet Panel | 60.8% | NP3 | 65.4% |
| | | NP4 | 85.5% |
| | | NP5 | 61.5% |

Paper's stated maximum correlation-pair count: 18 choose 2 = **153**, assuming all 18 variables are present. Variable omissions mean that actual comparisons can be fewer. Variables are demographic and occupational. Original figure: **weighted** and **Bonferroni-adjusted**; statistical testing used 2,000 bootstrap iterations and an adjustment based on **18 parameters**, not literally one Bonferroni factor for each of all 153 pairs.

### Figure 4 — GGSS benchmark

| Probability surveys | No Diff | Nonprobability surveys | No Diff |
|---|---:|---|---:|
| GESIS Panel | 83.6% | NP1 | 56.6% |
| German Internet Panel | 79.0% | NP2 | 91.3% |
| | | NP3 | 76.1% |
| | | NP4 | 89.4% |
| | | NP5 | 65.4% |

Paper's stated maximum correlation-pair count: 38 choose 2 = **703**, assuming 38 variables; actual variable coverage varies. Variables include demographic, political, and religious affiliation items. **GGSS is the benchmark**, so it is not simultaneously a compared row. Original figure: weighted, 2,000 bootstrap iterations, Bonferroni adjustment based on **37 parameters**.

### “No Diff” is not an accuracy guarantee

The source defines **No Diff** using its significance-based comparison procedure. A high share can reflect estimates close to the benchmark or inadequate precision. It does **not** demonstrate equivalence or identify the true causal contribution of recruitment differences. The authors' comparisons differ in field periods, modes, sample construction, and variables; most nonprobability samples come from commercial online panels, not social-media creator audiences. The two benchmark panels should not be pooled as if they were the same set of variables.

The regenerated visualization intentionally plots **all 15 published survey values**, rather than averaging away NP1's poor performance or the overlap between NP and probability-panel findings. It is a replot of published results, not a reproduction of the original paper's Figure 3/4 stacked categories.

## 3. Large-difference classifications

The authors' *separate* “Large Diff” comparison requires statistical criteria plus a sufficiently large difference in magnitude or direction. The percentages below are author-reported **averages across survey types**, not observed participant proportions:

| Benchmark | Survey type | Large Diff | Magnitude component | Provenance |
|---|---|---:|---:|---|
| Microcensus | Probability | 8.7% | 8.1% | Figure 3 narrative; online supplement C.12 |
| Microcensus | Nonprobability | 15.4% | 14.3% | Figure 3 narrative; supplement C.12 |
| GGSS | Probability | 3.9% | 3.9% | Figure 4 narrative; supplement C.13 |
| GGSS | Nonprobability | 7.5% | 6.6% | Figure 4 narrative; supplement C.13 |

The figure in the essay **does not** plot these group-average categories. They are reported in the prose. The difference between total “Large Diff” and magnitude components should not be interpreted as an exact rate of sign reversals: category definitions and rounding matter. Nor should these four group averages be confused with our script's **arithmetic means of rounded “No Diff” survey values**—those describe a different statistic.

## 4. Other major article sources, what each supports

See `source_reference_map.csv` (11 entries) and `claim_source_audit.csv` (17 claims) for the linked source trail. Key inferential boundaries:

- **Jager et al. (2017)** explicitly discuss how sample composition affects association and subgroup estimates, using a **hypothetical illustration**. Their 92.5% convenience-sampling figure applies to classifiable studies from **five developmental-science journals in 2007–2011**, not all sciences or psychological research. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC5606225/).
- **Gosling et al. (2004)** offer meaningful supporting evidence for web-based personality research. [DOI](https://doi.org/10.1037/0003-066X.59.2.93).
- **Mullinix et al. (2015)** and **Coppock et al. (2018)** study experimental effects across samples; their consistency results are relevant but not universal guarantees about observational personality correlations. [Mullinix DOI](https://doi.org/10.1017/XPS.2015.19); [Coppock DOI](https://doi.org/10.1073/pnas.1808083115).
- **Lehdonvirta et al. (2021)** examine topical self-selection and other differences in nonprobability recruiting; strongest benchmarks concern sample composition/descriptive estimates. [DOI](https://doi.org/10.1002/poi3.238).
- **Donzowa, Kühne & Zindel (2025)** and **Donzowa, Perrotta & Zagheni (2025)** examine Facebook recruitment design. The latter reports **20 out of 32** models without a statistically significant image effect; nonsignificance is not equivalence. [First DOI](https://doi.org/10.12758/mda.2025.05); [second full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12237053/).
- **Herbenick et al. (2026)** describe new journal-adopted reporting requirements for online sexuality research, including fraud and automated-response concerns. They **postdate** Alexander's May 2024 essay. [Publisher](https://link.springer.com/article/10.1007/s10508-026-03657-1).
- **Schmitt (2005)** provides independent cross-cultural evidence about the *direction* of the average sociosexuality sex difference across 48 nations; it does **not** furnish 48 nationally representative samples or a direct measurement of selection bias in the DatePsychology audience. [DOI](https://doi.org/10.1017/S0140525X05000051).

## 5. What was not done

- No original DatePsychology survey microdata, questionnaire codebooks, or recruitment logs were analyzed.
- No 90-paper original audit sheet was recovered; no verified line-by-line reclassification of all 90 was done.
- No original Rohr respondent data, weights, bootstrap resamples, exact model specifications, or per-comparison test outcomes were reanalyzed.
- No attempt to derive a quantitative selection-bias correction for sociosexuality outcomes.
- No source's copyright-protected full article or PDF is redistributed.

Thus the repo makes **the chart, the transcribed statistics, the arithmetic, and the source trail** reproducible—not every empirical claim in the published research literature.
