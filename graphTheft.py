import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

# Open h5 file
df = pd.read_hdf(r'./NYPD_Arrest_Data.h5')

sub_df = df.loc[df['OFNS_DESC'].str.contains("THEFT", case=False)]
# print(sub_df.loc[:, "OFNS_DESC"])

# print(sub_df[["YEAR", "OFNS_DESC"]])
theftByYear = sub_df[["YEAR", "OFNS_DESC"]].groupby(["YEAR", "OFNS_DESC"]).size().reset_index(name="Number of Offenses")
print(theftByYear)

# for line plots
# sb.lineplot(data=theftByYear.iloc[0:25:2], x="YEAR", y="counts")

# for bar plot
theftByYear.iloc[1::2].plot.bar(x="YEAR", y="Number of Offenses")

plt.title("Number of Arrests for Theft-Fraud in NYPD 2006-2021")
plt.show()
