# iac-cost-linters

This repository hosts supplementary scripts and data for my Master's Thesis titled *"Catching Cost Issues in Infrastructure as Code Artifacts using Linters"*.

The results of the thematic analysis phase have been further refined and extended in a separate repository, [search-rug/iac-cost-patterns](https://github.com/search-rug/iac-cost-patterns). In addition, the extensions to [Checkov](https://github.com/InputUsername/checkov/tree/cost-rules) and [TFLint](https://github.com/InputUsername/tflint-ruleset-cost) are also available in separate repositories.

This repository is organized as follows:

0. **Updating the original dataset with commits from 2022-2024**
    - `1 - <name>.json`, `2 - <name>.json`: initial 2 rounds of individual labeling
    - `3 - merged.json`: datasets merged after resolution by third rater
    - `4 - updated.json`: dataset updated with additional labels
    - `5 - filtered.json`: dataset without cost-unrelated commits
    - `agreement.py`: compute agreement (Krippendorff's alpha) between two or more raters
    - `conflicts.py`: highlight cases where raters disagree
1. **Fetching diffs and coding them**
    - `collect_data.ipynb`: script to retrieve commit diffs and set up the dataset for coding. Produces:
        - `diffs.json`: main dataset of coded diffs
        - `errors.json`: errors while fetching diffs
        - `codes.json`: list of codes and descriptions
    - `processing.py`: helper script to process commits to-be-coded
2. **Combining codes into themes and patterns**
    - `analyse_data.ipynb`: script to compute statistics and other useful information on the diffs dataset. Produces:
        - `codes.csv`: codes, descriptions and the number of occurrences
        - `codes_grouped.csv`: manually grouped codes to find patterns
        - (`clouds.csv`: distribution of cloud-specific codes)
    - `themes_and_patterns.ipynb`: combining codes into patterns and collecting their occurrences. Produces:
        - `pattern_occurrences.csv`: set of `<pattern>, <occurrence url>` pairs
        - `themes.json`: list of themes/patterns, occurrences per technology and relevant codes
        - `theme_occurrences.json`: list of occurrences with associated theme/pattern and codes
    - `cooccurrences.py`: helper script to compute co-occurrences of patterns within commits and repositories. Produces:
        - `cooccurrences_with_commits.csv`: set of `<pattern>, <repository>, <commit hash>` triples for further analysis
3. **Implementation helpers**
    - `old_gen.py`: helper script to process commits that contain the *Old generation* antipattern
    - `old-generation-analysis.csv`: analysis of the *Old generation* commits to find the most common fixes
4. **Evaluation of the implemented linter rules**
    - `before_after.ipynb`: grab repository states before and after commits. Produces:
        - `snapshots/<owner>-<repo>-<original commit hash>/`
            - `before-<commit hash of parent>/` (one per parent commit): repository state before the commit
            - `after/`: repository state after the commit
            - `latest/`: repository state after the latest commit
        - `errors.json`: errors while retrieving repository states
    - `benchmark.ipynb`: benchmarks Checkov and TFLint. Produces:
        - `results/checkov_<timestamp>.json`
        - `results/tflint_<timestamp>.json`
    - `evaluation.ipynb`: computes statistics (precision/recall, performance) based on benchmark results.
