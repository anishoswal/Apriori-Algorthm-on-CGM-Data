#######I HAVE COMBINED ALL THE CSV FILES FOR ALL THE PATIENTS AND TO SHOW THE OUTPUT I HAVE CREATED A "FINALOUTPUT" FOLDER SIGNIFYING THE EXPECTED OUTPUTS IN FORM OF 3 CSV FILES#######
THE FINAL OUTPUT FOLDER CONTAINS:
A. 1MostFrequent
B. 2HighConfidence
C. 3AnamalousRules

# Apriori Algorithm on CGM Insulin Bolus Data
## Description
- The project encorporates finding the frequent itemsets in bins for which we use the InsulinBolus dataset and the CGMSeries dataset.
- I have combined both the datsets and all their parts for different patients into one ensembled datset. i.e. [BOLUSAll](BOLUSAll.csv) and [CGMAll](CGMAll.csv)
- Then I find the frequent itemsets in the form {Bin for CGM<sub>Max</sub>, Bin for CGM<sub>0</sub>} -> {InsulinBolus<sub>Max</sub>}
- Here CGM<sub>0</sub> stands for the time when the patient has a meal which is condsidered to to be the 6th Sample in the CGM data.