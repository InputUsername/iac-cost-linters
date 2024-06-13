# Master's Thesis

Code and data for my master's thesis on cost issues in cloud software (Terraform) artifacts.

<!--
## Scripts
- `collect_data.ipynb` is used to collect commit diffs and set up `diffs.json` and `errors.json` files; usage:
  1. create a file `TOKEN.txt` containing a GitHub access token
  2. place the set of commits/issues (e.g. the original `dataset.json`) in the same directory as the notebook, or edit the path in the script
  3. run the notebook
  
  If `diffs.json` already exists, it will skip any commit that already has diffs. The script will also dump its output after fetching a commit to prevent losing progress. Errors are written to `errors.json`, but are ignored when rerunning in order to retry in case of one-off issues.
- `analyse_data.ipynb` is used to compute some statistics on the diffs dataset and generated codes
- `processing.py` is a helper script that goes through all commits that have not been coded yet and opens them in the browser (for easier processing) one-by-one

## Data
- `diffs.json` is the main dataset containing, for each (still available) commit:
    - `url`
    - `files` (as returned by the GitHub API, including diffs)
    - `existing_codes`
    - `codes`
    - `notes`
- `errors.json` contains commits which caused errors; this is included for completeness but otherwise not used
-->
