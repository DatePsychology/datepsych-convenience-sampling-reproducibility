#!/usr/bin/env python3
"""Reproduce published-number checks and the figure used in the companion essay.

Scope: transcribed aggregate values from Alexander (2024) and Rohr et al. (2025).
This script DOES NOT obtain participants, redo survey statistics, or impute missing
underlying papers or methods.
"""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ROHR = ROOT / 'published_rohr_correlations.csv'
LARGE = ROOT / 'published_rohr_large_differences.csv'
ALEX = ROOT / 'published_alexander_sampling_counts.csv'

SURVEYS = {
    'Microcensus': ['GGSS', 'GESIS Panel', 'German Internet Panel', 'NP1', 'NP2', 'NP3', 'NP4', 'NP5'],
    'GGSS': ['GESIS Panel', 'German Internet Panel', 'NP1', 'NP2', 'NP3', 'NP4', 'NP5'],
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open('r', encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def read_rohr(path: Path = ROHR) -> list[dict]:
    raw = read_rows(path)
    if len(raw) != 15:
        raise ValueError(f'Expected 15 rows (8 microcensus + 7 GGSS), got {len(raw)}')
    data = []
    for r in raw:
        row = dict(r)
        row['no_diff_percent'] = float(r['no_diff_percent'])
        if not (0 <= row['no_diff_percent'] <= 100):
            raise ValueError(f'No Diff outside 0-100: {r}')
        if row['survey_type'] not in {'Probability', 'Nonprobability'}:
            raise ValueError(f'Invalid survey type: {r}')
        if row['survey'].startswith('NP') != (row['survey_type'] == 'Nonprobability'):
            raise ValueError(f'Survey/type mismatch: {r}')
        data.append(row)
    for benchmark, survey_names in SURVEYS.items():
        found = [r['survey'] for r in data if r['benchmark'] == benchmark]
        if len(found) != len(survey_names) or set(found) != set(survey_names):
            raise ValueError(f'{benchmark}: expected {survey_names}, got {found}')
    return data


def read_large_diff(path: Path = LARGE) -> list[dict]:
    raw = read_rows(path)
    if len(raw) != 4:
        raise ValueError('Expected four magnitude/difference category summary rows')
    data=[]
    for r in raw:
        row = dict(r)
        row['large_diff_percent'] = float(r['large_diff_percent'])
        row['magnitude_diff_percent'] = float(r['magnitude_diff_percent'])
        if not 0 <= row['magnitude_diff_percent'] <= row['large_diff_percent'] <= 100:
            raise ValueError(f'Invalid share pair: {r}')
        data.append(row)
    return data


def read_alex(path: Path = ALEX) -> dict[str, int]:
    result = {}
    for r in read_rows(path):
        if r['claim_id'] in result:
            raise ValueError(f'Duplicate claim id: {r["claim_id"]}')
        result[r['claim_id']] = int(r['count'])
    needed = {'paper_total','student','online_first','online_later','online_social',
              'online_unspecified','online_mturk','online_other','remaining'}
    if set(result) != needed:
        raise ValueError(f'Unexpected Alexander count IDs: {set(result) ^ needed}')
    return result


def write_csv(path: Path, header: list[str], rows: list[list]):
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def summaries(no_diff: list[dict]) -> list[dict]:
    rows=[]
    for benchmark in SURVEYS:
        for kind in ('Probability','Nonprobability'):
            xs=[r['no_diff_percent'] for r in no_diff if r['benchmark']==benchmark and r['survey_type']==kind]
            rows.append({'benchmark':benchmark,'survey_type':kind,'n_surveys':len(xs),
                         'min_pct':min(xs),'max_pct':max(xs),'mean_pct':sum(xs)/len(xs)})
    return rows


def draw_figure(data: list[dict], output_file: Path) -> None:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    fig = plt.figure(figsize=(16, 9.5), facecolor='white')
    # The published article chart is a separate visual artifact; this figure
    # reproduces the same plotted 15 data points, not pixel-identical styling.
    axes = [fig.add_axes([.16, .16, .34, .61]), fig.add_axes([.66, .16, .30, .61])]
    prob_color = '#33445b'
    nonprob_color = '#7c8d9e'
    track_color = '#e4e8ec'
    text_color = '#25313d'
    for i,(bench,ax) in enumerate(zip(SURVEYS,axes)):
        names = SURVEYS[bench]
        ys = list(range(len(names)))[::-1]
        row_map = {(r['benchmark'],r['survey']):r for r in data}
        for name,y in zip(names,ys):
            r=row_map[(bench,name)]
            val=r['no_diff_percent']
            typ=r['survey_type']
            ax.hlines(y, 0, val, color=track_color, lw=2.4, zorder=1)
            ax.scatter([val],[y],marker='D' if typ=='Probability' else 'o',
                       color=prob_color if typ=='Probability' else nonprob_color,
                       s=87 if typ=='Probability' else 58,zorder=3)
            # Keep label within the figure when values approach the right edge.
            ha='right' if val>97 else 'left'
            dx=-2.4 if ha=='right' else 2.5
            ax.text(val+dx,y,f'{val:.1f}%',ha=ha,va='center',fontsize=12,color=text_color)
        ax.set_xlim(0, 108)
        ax.set_ylim(-0.5,len(names)-0.5)
        ax.set_yticks(ys)
        ax.set_yticklabels(names,fontsize=11.8)
        ax.set_xticks([0,25,50,75,100])
        ax.set_xticklabels([f'{x}%' for x in [0,25,50,75,100]],fontsize=10.5,color='#526171')
        ax.tick_params(axis='both',length=0,pad=8)
        ax.grid(axis='x',color='#e7ebef',linewidth=0.8)
        ax.set_axisbelow(True)
        for s in ax.spines.values(): s.set_visible(False)
        a,b = ('Microcensus benchmark','Demographic / occupational correlations') if i==0 else ('GGSS benchmark','Demographic / political / religious correlations')
        ax.text(0,1.075,f'{"A" if i==0 else "B"}  •  {a}',transform=ax.transAxes,fontweight='bold',fontsize=15.5,ha='left',color=text_color)
        ax.text(0,1.025,b,transform=ax.transAxes,fontsize=11.2,ha='left',color='#5e6d7a')
        if i==0:
            # Group divider below three probability surveys.
            ax.axhline(len(names)-3-0.5,color='#cfd7de',lw=.9)
        else:
            ax.axhline(len(names)-2-0.5,color='#cfd7de',lw=.9)
    fig.text(.045,.96,'Correlation comparisons differ across surveys',fontsize=23.5,
             fontweight='bold',ha='left',color=text_color)
    fig.text(.045,.925,'Share without a statistically detected difference from each benchmark; higher is not evidence of equivalence',
             fontsize=13.2,ha='left',color='#566776')
    legend = [
        Line2D([],[],marker='D',ls='none',markerfacecolor=prob_color,markeredgecolor=prob_color,markersize=9,label='Probability survey'),
        Line2D([],[],marker='o',ls='none',markerfacecolor=nonprob_color,markeredgecolor=nonprob_color,markersize=9,label='Nonprobability panel')
    ]
    fig.legend(handles=legend,loc='lower center',bbox_to_anchor=(.50,.085),ncol=2,frameon=False,fontsize=12)
    fig.text(.045,.038,'Source: Rohr, Silber & Felderer (2025), Figures 3–4. Weighted, multiple-testing-adjusted comparisons; benchmark sets differ.',
             fontsize=10.8,color='#667584',ha='left')
    output_file.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output_file,dpi=135,facecolor='white')
    plt.close(fig)


def run(out: Path, verbose: bool = True) -> str:
    out.mkdir(parents=True,exist_ok=True)
    rohr=read_rohr()
    large=read_large_diff()
    alex=read_alex()
    summary=summaries(rohr)
    write_csv(out/'rohr_per_survey_summaries.csv',
              ['benchmark','survey_type','n_surveys','min_no_diff_pct','max_no_diff_pct','mean_no_diff_pct'],
              [[r['benchmark'],r['survey_type'],r['n_surveys'],f"{r['min_pct']:.1f}",f"{r['max_pct']:.1f}",f"{r['mean_pct']:.2f}"] for r in summary])
    sub_total=sum(alex[k] for k in ('online_social','online_unspecified','online_mturk','online_other'))
    all_assignments=alex['student']+alex['online_first']+alex['remaining']
    write_csv(out/'alexander_arithmetic_checks.csv',
              ['comparison','value','interpretation'],[
                  ['online_count_difference',alex['online_later']-alex['online_first'],'39 vs 36: distinct printed denominators, underlying author definitions unknown'],
                  ['online_subcategory_sum',sub_total,'18 + 9 + 8 + 5 = 40 assignments; categories may overlap'],
                  ['student_online_other_sum',all_assignments,'49 + 36 + 13 = 98 assignments; categories may overlap'],
                  ['claimed_number_of_papers',alex['paper_total'],'90 papers claimed; exact selected bibliography/codebook unavailable'],
              ])
    draw_figure(rohr,out/'figure_01_rohr_per_survey_no_diff.png')
    lines=[
        'CONVENIENCE-SAMPLING ARTICLE — REPRODUCTION FROM PRINTED AGGREGATES',
        'Sources: Rohr, Silber & Felderer (2025), DOI 10.1177/00811750241280963;',
        '         Alexander (2024), original DatePsychology essay.',
        '',
        'FIGURE 1: PUBLISHED "NO DIFF" CORRELATION CLASSIFICATION',
        'This is NOT equivalence, a bias estimate, or an independent analysis of respondent data.',
    ]
    for r in summary:
        lines.append(f"  {r['benchmark']:11s} | {r['survey_type']:14s} | n={r['n_surveys']} surveys | min={r['min_pct']:.1f}% max={r['max_pct']:.1f}% (arithmetic mean={r['mean_pct']:.2f}%)")
    lines.extend(['','LARGE-DIFFERENCE SUMMARY (PUBLISHED GROUP AVERAGES)',
                  'Large Diff required statistical criteria and a sufficiently large magnitude or sign difference.'])
    for r in large:
        lines.append(f"  {r['benchmark']:11s} | {r['survey_type']:14s} | large={r['large_diff_percent']:.1f}%; magnitude={r['magnitude_diff_percent']:.1f}%")
    lines.extend(['','ALEXANDER PAPER COUNT — ARITHMETIC ONLY',
                  f"  Online totals printed: {alex['online_first']} and {alex['online_later']} (difference {alex['online_later']-alex['online_first']}).",
                  f"  Online subcategory assignments: {alex['online_social']}+{alex['online_unspecified']}+{alex['online_mturk']}+{alex['online_other']}={sub_total}.",
                  f"  Student + online + other category assignments: {alex['student']}+{alex['online_first']}+{alex['remaining']}={all_assignments}; paper denominator={alex['paper_total']}.",
                  '  NOTE: Category sums above are NOT counts of unique papers. Overlap is possible.',
                  '  We do not know which exact 90 papers or original category-coding decisions were used.',
                  '',
                  'LIMITATIONS',
                  '  * No individual respondent-level data or original statistical test outcomes included.',
                  '  * Counts of pairs per survey can be below the maximum because variable coverage varies.',
                  '  * Significance-based No Diff percentages depend on precision, weighting and adjustment.',
                  '  * Panel surveys are not the same as creator-recruited sexuality surveys.',
                  '  * This exercise does not test bias in DatePsychology survey estimates.',
                  ''])
    result='\n'.join(lines)
    (out/'reconstruction_results.txt').write_text(result,encoding='utf-8')
    if verbose: print(result)
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,default=ROOT/'reproduced_figures',help='Output folder (default: reproduced_figures)')
    args=p.parse_args()
    run(args.out)

if __name__=='__main__':
    main()
