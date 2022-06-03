import pandas as pd

df = pd.read_csv("datasets/Salaries.csv")

print(
    "1.HEAD\n",
    df.head(),
    "\n"
)

print(
    "2.INFO"
)
df.info()
print()

print(
    "3.Max OvertimePay:\n",
    df["OvertimePay"].max(),
    "\n"
)

joseph = df.loc[df["EmployeeName"].str.contains("JOSEPH DRISCOLL", case = True)]

print(
    "4.Joseph's JobTitle:\n",
    joseph["JobTitle"].values[0],
    "\n"
)

print(
    "5. Joseph's TotalPayBenefits:\n",
    joseph["TotalPayBenefits"].values[0],
    "\n"
)

print(
    "6.Highest paid person (including benefits):\n",
    df["EmployeeName"][df["TotalPayBenefits"].idxmax()],
    "\n"
)

print(
    "7.Lowest paid person (including benefits):\n",
    df["EmployeeName"][df["TotalPayBenefits"].idxmin()],
    "\n"
)


print(
    "8.Average BasePay per year:",
)
years = df["Year"].unique()
for i in years:
    yearPay = df.loc[df["Year"] == i, "BasePay"]
    print(i, ":", yearPay.mean())
print()

jobTitles = df["JobTitle"]

print(
    "9.Unique JobTitles count:\n",
    jobTitles.nunique(),
    "\n"
)

print(
    "10.Top 5 most common jobs:"
)
topFive = jobTitles.value_counts()[:5].index.tolist()
for job in topFive:
    print(job)
print()

year2013 = df.loc[df["Year"] == 2013]
print(
    "11.JobTitles with single occurrence in 2013:\n",
    (year2013["JobTitle"].value_counts() == 1).value_counts().get(True),
    "\n"
)

print(
    "12.Count of people with the word Chief in their JobTitle:\n",
    (jobTitles.loc[jobTitles.str.contains("Chief")]).count()
)