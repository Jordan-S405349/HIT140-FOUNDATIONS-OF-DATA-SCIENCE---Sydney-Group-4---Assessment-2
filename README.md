# FIFA World Cup 2026 - Group Analytics Project

This repository contains the Python code, datasets and generated outputs for the four selected analytic tasks used in the group presentation.

## Group members and task order

| Task | Student | Student ID | Analytic task | Statistical test |
|---|---|---|---|---|
| Task 1 | Syed Suleman Uddin Farhad | S403360 | Offers to Receive and Goals | Welch independent two-sample t-test |
| Task 2 | Jordan Then Ryan | S405349 | Clean Sheets | One-sample t-test against 1 |
| Task 3 | Ujjwol Neupane | S403295 | Speed and Goals | Welch independent two-sample t-test |
| Task 4 | Saugat Shrestha | S403036 | Own Goals | One-sample t-test against 0 |

## Analytic questions

### Task 1 - Offers to Receive and Goals
**Question:** Do teams with more offers to receive score significantly more goals than teams with fewer offers to receive?

- Focus: team movement and attacking positioning
- Variables: Offers to Receive, Goals
- Groups: High offers vs Low offers
- Threshold: median Offers to Receive = **1235.5**
- Sampling: 20 teams from each group, `random_state=42`
- Test: Welch independent two-sample t-test
- 95% CI: difference in mean goals between the two groups

### Task 2 - Clean Sheets
**Question:** Is the average number of clean sheets achieved by teams significantly different from 1 clean sheet?

- Focus: defensive performance
- Variable: Clean Sheets
- Comparison value: 1
- Sampling: simple random sample of 40 teams, `random_state=42`
- Test: two-sided one-sample t-test
- 95% CI: population mean clean sheets

### Task 3 - Speed and Goals
**Question:** Do teams with above-average movement speed score significantly more goals than teams with below-average movement speed?

- Focus: physical movement and attacking performance
- Variables: Average Speed, Goals
- Groups: Above-average speed vs Below-average speed
- Threshold: overall mean Average Speed = **5.977 km/h**
- Sampling: 20 teams from each group, `random_state=42`
- Test: Welch independent two-sample t-test
- 95% CI: difference in mean goals

### Task 4 - Own Goals
**Question:** Is the average number of own goals scored by teams significantly different from zero?

- Focus: errors and unusual scoring events
- Variable: Own Goals
- Comparison value: 0
- Sampling: simple random sample of 40 teams, `random_state=42`
- Test: two-sided one-sample t-test
- 95% CI: population mean own goals

## Assessment workflow

Each task includes:

1. Analytic question formulation
2. Data wrangling
3. Data preparation and sampling
4. Descriptive statistics
5. 95% confidence interval
6. One-sample or two-sample t-test
7. Interpretation and conclusion

## Folder structure

```text
FIFA_WC2026_Final_GitHub/
├── data/
│   ├── raw/
│   │   ├── task1_offers_to_receive_goals.csv
│   │   ├── task2_clean_sheets.csv
│   │   ├── task3_speed_goals.csv
│   │   └── task4_own_goals.csv
│   └── source_screenshots/
├── src/
│   ├── 01_syed_offers_goals.py
│   ├── 02_jordan_clean_sheets.py
│   ├── 03_ujjwol_speed_goals.py
│   ├── 04_saugat_own_goals.py
│   └── run_all_tasks.py
├── outputs/
│   ├── task1_offers_goals/
│   ├── task2_clean_sheets/
│   ├── task3_speed_goals/
│   ├── task4_own_goals/
│   └── group_results_summary.csv
├── README.md
├── requirements.txt
└── .gitignore
```

## How to run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run one task, for example:

```bash
python src/01_syed_offers_goals.py
```

Run all four tasks:

```bash
python src/run_all_tasks.py
```

## Data source

The raw values were transcribed from the FIFA World Cup 2026 team-statistics tables supplied in the assessment screenshots. The relevant categories are Goals, Offers to Receive, Average Speed, Clean Sheets and Own Goals.

The source screenshots are included in `data/source_screenshots/` to document the origin of the data.

## Important limitations

Several FIFA statistics are tournament totals. Teams that progressed further played more matches and therefore had more opportunity to accumulate totals such as Goals, Offers to Receive and Clean Sheets. These analyses should therefore be interpreted as statistical associations/comparisons rather than causal effects.

Own Goals and Clean Sheets are count variables with many low values, so distribution shape should be discussed when presenting the one-sample t-test results.

## Reproducibility

All sampling uses the fixed seed `random_state=42`.

## AI use

If AI assistance was used in planning, coding, slide preparation or documentation, it should be declared accurately in the required AI Usage Declaration for the unit. Every group member should understand the code and be able to explain their own statistical method.
