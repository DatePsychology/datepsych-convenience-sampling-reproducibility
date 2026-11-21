# GitHub publication instructions

## Suggested repository

- **Repository name:** `datepsych-convenience-sampling-reproducibility`
- **GitHub description:** `Published-number reconstructions, source audit, and figure code for a methodological critique of DatePsychology's convenience-sampling essay.`
- **Visibility:** Public, if you want Substack readers to inspect it.

## Easiest upload: GitHub website

1. Download and **extract the ZIP file**; GitHub's normal file uploader expects the files inside, not the ZIP as a single blob.
2. In the DatePsychology GitHub account or organization, create a new repository using the suggested name. Do **not** initialize a second README (the package already has one).
3. Choose **Add file → Upload files**, then drag the **contents of the extracted repository folder**, including the `article_figures/`, `reproduced_figures/`, and `tests/` subfolders. Preserve folder structure.
4. Commit the upload. Verify the root README appears and clicking the two figure directories works.
5. Ideally run the commands in `README.md` locally and verify the 8 tests pass.
6. After your Substack article is live, replace the placeholder in `README.md` under “Companion article” with the actual article URL.

## Git command alternative

From the folder containing this README (change the remote to the actual empty GitHub repository URL you created):

```bash
git init
git add .
git commit -m "Add convenience-sampling source audit and figure reproduction"
git branch -M main
git remote add origin https://github.com/DatePsychology/datepsych-convenience-sampling-reproducibility.git
git push -u origin main
```

**The URL above is a suggested future destination, not a live link until you create and upload the repository.**

## Short paragraph for the article's notes/references

> **Reproducibility and source audit.** The publicly reported statistics used in Figure 1, the code to reproduce the visualization, and a source-by-source audit of the principal numerical claims are available in our [GitHub reproducibility repository](REPLACE_WITH_ACTUAL_GITHUB_URL). The package reconstructs results from published summary statistics; it does not contain participants' data or claim to reproduce the author's unpublished 90-paper sampling classifications.

Substitute the actual GitHub repository URL for `REPLACE_WITH_ACTUAL_GITHUB_URL` **after** you upload the files. When pasting into Substack, make the words “GitHub reproducibility repository” a direct external hyperlink, as with the article's footnotes.
