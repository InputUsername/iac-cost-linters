# Master's Thesis

Code and data for my master's thesis on cost issues in cloud software (Terraform) artifacts.

The repository is organized as follows:

0. **Updating the original dataset with commits from 2022-2024**
    - `1 - <name>.json`, `2 - <name>.json`: initial 2 rounds of individual labeling
    - `3 - merged.json`: datasets merged after resolution by third rater
    - `4 - updated.json`: dataset updated with additional labels
    - `5 - filtered.json`: dataset without cost-unrelated commits
    - `agreement.py`: compute agreement (Krippendorf's alpha) between two or more raters
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
3. **Implementation helpers**
    - `old_gen.py`: helper script to process commits that contain the *Old generation* antipattern
    - `old-generation-analysis.csv`: analysis of the *Old generation* commits to find the most common fixes
4. **Evaluation of the implemented linter rules**
    - `before_after.ipynb`: grab repository states before and after commits. Produces:
        - `snapshots/<owner>-<repo>-<original commit hash>/`
            - `before-<commit hash of parent>` (one per parent commit): repository state before the commit
            - `after`: repository state after the commit
        - `errors.json`: errors while retrieving repository states
    - `evaluation2.ipynb`: evaluation of Checkov and TFLint rules in terms of precision/recall and performance. Produces:
        - `results_checkov_2.json`
        - `results_tflint_2.json`
