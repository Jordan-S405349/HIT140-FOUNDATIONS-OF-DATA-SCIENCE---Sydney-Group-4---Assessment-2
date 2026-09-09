
from pathlib import Path
import math, pandas as pd, numpy as np
from scipy import stats

BASE=Path(__file__).resolve().parents[1]
df=pd.read_csv(BASE/"Datasets/task3_speed_goals.csv")
threshold=df["Average_Speed"].mean()
df["Group"]=np.where(df["Average_Speed"]>threshold,"Above-average speed","Below-average speed")
sample=pd.concat([df[df.Group=="Above-average speed"].sample(20,random_state=42),
                  df[df.Group=="Below-average speed"].sample(20,random_state=42)],ignore_index=True)
a=sample.loc[sample.Group=="Above-average speed","Goals"]; b=sample.loc[sample.Group=="Below-average speed","Goals"]
test=stats.ttest_ind(a,b,equal_var=False)
va,vb=a.var(ddof=1),b.var(ddof=1); na,nb=len(a),len(b)
diff=a.mean()-b.mean(); se=math.sqrt(va/na+vb/nb)
dfw=(va/na+vb/nb)**2/((va/na)**2/(na-1)+(vb/nb)**2/(nb-1))
crit=stats.t.ppf(.975,dfw); ci=(diff-crit*se,diff+crit*se)

print("Task 3 - Speed and Goals")
print("Mean speed threshold:",threshold)
print("Above mean goals:",a.mean(),"Below mean goals:",b.mean())
print("Welch t:",test.statistic,"df:",test.df,"p:",test.pvalue)
print("95% CI for mean difference:",ci)

