from pathlib import Path
import math, pandas as pd, numpy as np
from scipy import stats
BASE=Path(__file__).resolve().parents[1]
df=pd.read_csv(BASE/"data/raw/task1_offers_to_receive_goals.csv")
threshold=df["Offers_to_Receive"].median()
df["Group"]=np.where(df["Offers_to_Receive"]>threshold,"High offers","Low offers")
sample=pd.concat([df[df.Group=="High offers"].sample(20,random_state=42),
                  df[df.Group=="Low offers"].sample(20,random_state=42)],ignore_index=True)
high=sample.loc[sample.Group=="High offers","Goals"]; low=sample.loc[sample.Group=="Low offers","Goals"]
test=stats.ttest_ind(high,low,equal_var=False)
va,vb=high.var(ddof=1),low.var(ddof=1); na,nb=len(high),len(low)
diff=high.mean()-low.mean(); se=math.sqrt(va/na+vb/nb)
dfw=(va/na+vb/nb)**2/((va/na)**2/(na-1)+(vb/nb)**2/(nb-1))
crit=stats.t.ppf(.975,dfw); ci=(diff-crit*se,diff+crit*se)
print("Task 1 - Offers to Receive and Goals")
print("Median threshold:",threshold)
print("High mean:",high.mean(),"Low mean:",low.mean())
print("Welch t:",test.statistic,"df:",test.df,"p:",test.pvalue)
print("95% CI for mean difference:",ci)
