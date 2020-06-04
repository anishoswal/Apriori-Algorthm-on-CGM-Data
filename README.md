#######I HAVE COMBINED ALL THE CSV FILES FOR ALL THE PATIENTS AND TO SHOW THE OUTPUT I HAVE CREATED A "FINALOUTPUT" FOLDER SIGNIFYING THE EXPECTED OUTPUTS IN FORM OF 3 CSV FILES#######
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
- Segregate all the found CGM<sub>0 and Max</sub> values in bins of size 10mg/dL starting from **~50 – 60**, 60 – 70, 70 – 80,/...350 into bins named **1**, 2, 3 .... respectively. Example: 53,56,59 all belong to the itemset 50 - 60 which is **Bin number: 1**.
- Apply the Apriori Algorithm to the binned data to find the frequent datasets for each of the patients in form **{Bin for CGM<sub>Max</sub>, Bin for CGM<sub>0</sub>} -> {InsulinBolus<sub>Max</sub>}**.
