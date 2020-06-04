THE FINAL OUTPUT FOLDER CONTAINS:
A. 1MostFrequent
B. 2HighConfidence
C. 3AnamalousRules

# Apriori Algorithm on CGM Insulin Bolus Data
## Description
- The project encorporates finding the frequent itemsets in bins for which we use the InsulinBolus dataset and the CGMSeries dataset.
- I have combined both the datsets and all their parts for different patients into one ensembled datset. i.e. [BOLUSAll](BOLUSAll.csv) and [CGMAll](CGMAll.csv)
- Then I find the frequent itemsets in the form **{Bin for CGM<sub>Max</sub>, Bin for CGM<sub>0</sub>} -> {InsulinBolus<sub>Max</sub>}**.
- Here CGM<sub>0</sub> stands for the time when the patient has a meal which is condsidered to to be the 6th Sample in the CGM data.

## Plan
- Extracted the maxiumm Insulin Bolus Value from [BOLUSAll.csv](BOLUSAll.csv).
- Extracted the maximum CGM value from [CGMAll.csv](CGMAll.csv).
- Extracted the 6th sample from the [CGMAll.csv](CGMAll.csv) which is assumed to be the time when a meal was taken by the patient under observation.
- Segregate all the found CGM<sub>0 and Max</sub> values in bins of size 10mg/dL starting from **~50 – 60**, 60 – 70, 70 – 80,/...350 into bins named **1**, 2, 3 .... respectively. Example: 53,56,59 all belong to the itemset 50 - 60 which is **Bin - 1**.
- Apply the Apriori Algorithm to the binned data to find the frequent datasets for each of the patients in form **{Bin for CGM<sub>Max</sub>, Bin for CGM<sub>0</sub>} -> {InsulinBolus<sub>Max</sub>}**.
- Find the most frequent sets, largest confidence rules and anomalous rules with the least confidence.

## Input:
- [CGM Data](DataCGM).
- [Insulin Bolus Data](DataBOLUS).
- Combined Insulin Bolus and CGM Data into one .csv file. [BOLUSAll](BOLUSAll.csv) and [CGMAll](CGMAll.csv).

## Output
1.	CSV File with the **Most Frequent Sets**.
2.	CSV file with **Largest Confidence Rules**. 
3.	CSV file with **Anomalous Rules**. i.e. Rules with the Least Confidence.

## How to Run
```
python main.py
```

## Tested Environment
- **OS:** Windows 10
- **Python:** 3.7