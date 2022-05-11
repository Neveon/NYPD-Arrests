import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

historicDF = pd.read_csv("NYPD_Arrests_Data__Historic_.csv").dropna(subset = ["ARREST_DATE", "OFNS_DESC"])
recentDF = pd.read_csv("NYPD_Arrest_Data__Year_to_Date_.csv").dropna(subset = ["ARREST_DATE", "OFNS_DESC"])

# Create year column
historicDF["YEAR"] = historicDF["ARREST_DATE"].transform(lambda x: x[-4:])
recentDF["YEAR"] = recentDF["ARREST_DATE"].transform(lambda x: x[-4:])

# Concat both dataframes
totalArrests = pd.concat([historicDF, recentDF])
# print(totalArrests)

# Save new dataframe to hdf file for faster reading
totalArrests.to_hdf(r'./NYPD_Arrest_Data.h5', key='stage', mode='w')

# Count number of each crime

# totalArrestByYear = historicDF.groupby(["YEAR"])["OFNS_DESC"].count()
# totalArrest2021 = recentDF.groupby(["YEAR"])["OFNS_DESC"].count()

# totalArrestByYear = historicDF.groupby(["YEAR"])
# totalArrest2021 = recentDF.groupby(["YEAR"])

# totalArrests = pd.concat([totalArrestByYear, pd.DataFrame(totalArrest2021)])
# print(totalArrests.groupby(["YEAR"]))

# sb.lineplot(data=totalArrests)
# totalArrests.plot.bar()

# plt.xlabel("Year")
# plt.ylabel("Number of Arrests")
# plt.title("Number of Arrests Made in NYPD 2006-2021")
# plt.show()

# crimeByYear = historicDF.groupby(["YEAR", "OFNS_DESC"])["OFNS_DESC"].count()
#theftByYear = historicDF.groupby(["YEAR", "OFNS_DESC"])["OFNS_DESC"].count()
# print(crimeByYear.tail())
