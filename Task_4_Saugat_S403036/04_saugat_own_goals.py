from pathlib import Path
import math, pandas as pd
from scipy import stats
BASE=Path(__file__).resolve().parents[1]
df=pd.read_csv(BASE/"Datasets/task4_own_goals.csv")
sample=df.sample(40,random_state=42)
x=sample["Own_Goals"]; test=stats.ttest_1samp(x,0)
se=x.std(ddof=1)/(len(x)**0.5); crit=stats.t.ppf(.975,len(x)-1)
ci=(x.mean()-crit*se,x.mean()+crit*se)
print("Task 4 - Own Goals")
print("Mean:",x.mean(),"Median:",x.median(),"SD:",x.std(ddof=1))
print("One-sample t:",test.statistic,"df:",test.df,"p:",test.pvalue)
print("95% CI:",ci)
