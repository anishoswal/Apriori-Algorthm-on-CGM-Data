"""I HAVE COMBINED ALL THE CSV FILES FOR ALL THE PATIENTS AND TO SHOW THE OUTPUT I HAVE CREATED A "FINAL OUTPUT" FOLDER SIGNIFYING THE EXPECTED OUTPUTS IN FORM OF 3 CSV FILES"""
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori as ap
from mlxtend.frequent_patterns import association_rules as ar
import math
import pandas as pd
import re
import glob
import warnings
warnings.filterwarnings("ignore")

"""
files = glob.glob("DataCGM\*.csv")
li = []
for filename in files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
frame = pd.concat(li, axis=0, ignore_index=True)
frame.to_csv("CGMAll.csv")

files = glob.glob("DataBOLUS\*.csv")
li = []
for filename in files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
frame = pd.concat(li, axis=0, ignore_index=True)
frame.to_csv("BOLUSAll.csv")"""

def CalculateBins(bin):
    return int((math.ceil(bin / 10.0)) - 4)*10


def maximum(x):
    return max(x)
#CSV Read
cgm, bol = pd.read_csv('CGMAll.csv'), pd.read_csv('BOLUSAll.csv')

#Preprocessing
nan_row = cgm.isna().sum(axis=1)
rowNaN_list = list()
columns = len(cgm.iloc[0])
for i in range(len(nan_row)):
    if nan_row.iloc[i] > 0.4 * columns:
        rowNaN_list.append(i)
cgm.drop(rowNaN_list, inplace=True)
cgm.reset_index(inplace=True, drop=True)
#cgm.interpolate(method='quadratic', order=2, inplace=True)
cgm.bfill(inplace=True)
cgm.ffill(inplace=True)

#Bin Creation and Assignment to the data
CGmax, CG0, BOLmax = [], [], []
apriDF = []
for i in range(len(cgm)):
    CGmax.append(maximum(cgm.loc[i]))
    BOLmax.append(maximum(bol.loc[i]))
    CG0.append(cgm.loc[i][5])
    apriDF.append([CalculateBins(max(cgm.loc[i])), CalculateBins(cgm.loc[i][5]), max(bol.loc[i])])

#Apriori Algorithm
#For Most Frequent Itemsets
transEnc = TransactionEncoder()
transactions = pd.DataFrame(transEnc.fit(apriDF).transform(apriDF), columns=transEnc.columns_)
rules = ar(ap(transactions, min_support=0.00000000001, use_colnames=True), min_threshold=0.0)
rules["antecedent_len"] = rules["antecedents"].apply(lambda x: len(x))
for column in ['antecedents','consequents']:
    rules[column] = rules[column].astype(str)
    rules[column] = rules[column].str.replace(re.escape('frozenset({'), '')
    rules[column] = rules[column].str.replace(re.escape('})'), '')
rules["SET"] = rules["antecedents"]+',' +rules['consequents']
rules['SET'] = rules['SET'].str.replace("'", "")
rules['SET'] = rules.SET.apply(lambda x: x.split(','))
#rules.to_csv("Rules.csv")
li = rules['SET'].tolist()
y = [[(float(j)) for j in i] for i in li]
for i in y:
    i.sort(reverse=True)
b = list()
for sublist in y:
    if sublist not in b:
        b.append(sublist)
df = pd.DataFrame(b,columns=['CGMax','CG0','Bolus'])
df['CG0'] = df['CG0']/10
df['CGMax'] = df['CGMax']/10
df.dropna(subset=['Bolus'], inplace=True)
df['Bolus'] = df['Bolus'].astype(str)
df['CG0'] = df['CG0'].astype(int)
df['CGMax'] = df['CGMax'].astype(int)
df['CG0'] = df['CG0'].astype(str)
df['CGMax'] = df['CGMax'].astype(str)
df['Rule'] = "("+df['CGMax'] + "," + df['CG0'] + ","+df['Bolus']+ ")"
df.drop(['CGMax','CG0','Bolus'], inplace=True, axis=1)
df.to_csv("FinalOutput"+r"/"+"1MostFrequent.csv", index=False, header=False)

#For Highest Confidence Datasets
confidence = rules[(rules['antecedent_len'] >= 2) & (rules['confidence'] ==1)]
confidence["antecedent_len"] = confidence["antecedents"].apply(lambda x: len(x))
for column in ['antecedents','consequents']:
    confidence[column] = confidence[column].astype(str)
    confidence[column] = confidence[column].str.replace(re.escape('frozenset({'), '')
    confidence[column] = confidence[column].str.replace(re.escape('})'), '')
confidence["SET"] = confidence["antecedents"]+',' +confidence['consequents']
confidence['SET'] = confidence['SET'].str.replace("'", "")
confidence['SET'] = confidence.SET.apply(lambda x: x.split(','))
li = confidence['SET'].tolist()
y = [[(float(j)) for j in i] for i in li]
for i in y:
    i.sort(reverse=True)
b = list()
for sublist in y:
    if sublist not in b:
        b.append(sublist)
df = pd.DataFrame(b,columns=['CGMax','CG0','Bolus'])
df['CG0'] = df['CG0']/10
df['CGMax'] = df['CGMax']/10
df.dropna(subset=['Bolus'], inplace=True)
df['Bolus'] = df['Bolus'].astype(str)
df['CG0'] = df['CG0'].astype(int)
df['CGMax'] = df['CGMax'].astype(int)
df['CG0'] = df['CG0'].astype(str)
df['CGMax'] = df['CGMax'].astype(str)
df['Rule'] = "{"+df['CGMax'] + "," + df['CG0'] + "->"+df['Bolus']+ "}"
df.drop(['CGMax','CG0','Bolus'], inplace=True, axis=1)
df.to_csv("FinalOutput"+r"/"+"2HighConfidence.csv", index=False, header=False)

#For Anomalous Rules
least = rules[(rules['antecedent_len'] >= 2) & (rules['confidence'] <=0.333)]
least["antecedent_len"] = least["antecedents"].apply(lambda x: len(x))
for column in ['antecedents','consequents']:
    least[column] = least[column].astype(str)
    least[column] = least[column].str.replace(re.escape('frozenset({'), '')
    least[column] = least[column].str.replace(re.escape('})'), '')
least["SET"] = least["antecedents"]+',' +least['consequents']
least['SET'] = least['SET'].str.replace("'", "")
least['SET'] = least.SET.apply(lambda x: x.split(','))
li = least['SET'].tolist()
y = [[(float(j)) for j in i] for i in li]
for i in y:
    i.sort(reverse=True)
b = list()
for sublist in y:
    if sublist not in b:
        b.append(sublist)
df = pd.DataFrame(b,columns=['CGMax','CG0','Bolus'])
df['CG0'] = df['CG0']/10
df['CGMax'] = df['CGMax']/10
df.dropna(subset=['Bolus'], inplace=True)
df['Bolus'] = df['Bolus'].astype(str)
df['CG0'] = df['CG0'].astype(int)
df['CGMax'] = df['CGMax'].astype(int)
df['CG0'] = df['CG0'].astype(str)
df['CGMax'] = df['CGMax'].astype(str)
df['Rule'] = "{"+df['CGMax'] + "," + df['CG0'] + "->"+df['Bolus']+ "}"
df.drop(['CGMax','CG0','Bolus'], inplace=True, axis=1)
df.to_csv("FinalOutput"+r"/"+"3AnamalousRules.csv", index=False, header=False)