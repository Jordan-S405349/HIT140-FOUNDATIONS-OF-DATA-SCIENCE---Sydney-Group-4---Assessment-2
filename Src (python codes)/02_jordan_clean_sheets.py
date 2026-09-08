from pathlib import Path
import math, pandas as pd
from scipy import stats
BASE=Path(__file__).resolve().parents[1]
df=pd.read_csv(BASE/"data/raw/task2_clean_sheets.csv")
sample=df.sample(40,random_state=42)
x=sample["Clean_Sheets"]; test=stats.ttest_1samp(x,1)
se=x.std(ddof=1)/(len(x)**0.5); crit=stats.t.ppf(.975,len(x)-1)
ci=(x.mean()-crit*se,x.mean()+crit*se)
print("Task 2 - Clean Sheets")
print("Mean:",x.mean(),"Median:",x.median(),"SD:",x.std(ddof=1))
print("One-sample t:",test.statistic,"df:",test.df,"p:",test.pvalue)
print("95% CI:",ci)
