"""No network or individual participant-level data needed."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import reproduce_convenience_sampling as repl


class ReproductionTests(unittest.TestCase):
    def setUp(self):
        self.data=repl.read_rohr()

    def test_row_counts_and_coverage(self):
        self.assertEqual(len(self.data),15)
        self.assertEqual(len([r for r in self.data if r['benchmark']=='Microcensus']),8)
        self.assertEqual(len([r for r in self.data if r['benchmark']=='GGSS']),7)

    def test_transcribed_published_points(self):
        vals={(r['benchmark'],r['survey']):r['no_diff_percent'] for r in self.data}
        self.assertAlmostEqual(vals['Microcensus','GGSS'],87.6)
        self.assertAlmostEqual(vals['Microcensus','NP1'],34.5)
        self.assertAlmostEqual(vals['Microcensus','NP4'],85.5)
        self.assertAlmostEqual(vals['GGSS','NP2'],91.3)
        self.assertAlmostEqual(vals['GGSS','NP1'],56.6)

    def test_benchmark_absence(self):
        self.assertNotIn(('GGSS','GGSS'),{(r['benchmark'],r['survey']) for r in self.data})

    def test_nonprobability_overlaps_probability(self):
        for benchmark in repl.SURVEYS:
            a=[r['no_diff_percent'] for r in self.data if r['benchmark']==benchmark and r['survey_type']=='Probability']
            b=[r['no_diff_percent'] for r in self.data if r['benchmark']==benchmark and r['survey_type']=='Nonprobability']
            self.assertGreater(max(b),min(a))
            self.assertLess(min(b),max(a))

    def test_large_difference_figures(self):
        x={(r['benchmark'],r['survey_type']):r for r in repl.read_large_diff()}
        self.assertAlmostEqual(x['Microcensus','Probability']['large_diff_percent'],8.7)
        self.assertAlmostEqual(x['Microcensus','Probability']['magnitude_diff_percent'],8.1)
        self.assertAlmostEqual(x['Microcensus','Nonprobability']['large_diff_percent'],15.4)
        self.assertAlmostEqual(x['Microcensus','Nonprobability']['magnitude_diff_percent'],14.3)
        self.assertAlmostEqual(x['GGSS','Probability']['large_diff_percent'],3.9)
        self.assertAlmostEqual(x['GGSS','Nonprobability']['magnitude_diff_percent'],6.6)

    def test_alexander_arithmetic_not_silent_deduplication(self):
        a=repl.read_alex()
        self.assertEqual(a['online_first'],36)
        self.assertEqual(a['online_later'],39)
        self.assertEqual(sum(a[k] for k in ('online_social','online_unspecified','online_mturk','online_other')),40)
        self.assertEqual(a['student']+a['online_first']+a['remaining'],98)
        self.assertEqual(a['paper_total'],90)

    def test_citation_source_coverage(self):
        with (ROOT/'source_reference_map.csv').open(newline='',encoding='utf-8') as f:
            rows=list(csv.DictReader(f))
        self.assertEqual([r['footnote_number'] for r in rows],[str(i) for i in range(1,12)])
        self.assertTrue(all(r['source_url'].startswith('https://') for r in rows))

    def test_full_run_generates_expected_artifacts(self):
        with tempfile.TemporaryDirectory() as temp:
            out=Path(temp)
            text=repl.run(out,verbose=False)
            self.assertIn('No Diff',text)
            self.assertIn('Category sums',text)
            for name in ['figure_01_rohr_per_survey_no_diff.png','rohr_per_survey_summaries.csv',
                         'alexander_arithmetic_checks.csv','reconstruction_results.txt']:
                self.assertTrue((out/name).is_file(),name)
                self.assertGreater((out/name).stat().st_size,10)

if __name__=='__main__':
    unittest.main()
