import pandas as pd
counts = pd.read_csv('counts.tsv', sep='\t', index_col=0)
counts.columns
counts_mean = counts.mean()
counts_std = counts.std()
counts_max = counts.max()
counts_min = counts.min()
counts_median = counts.median()
counts_25perc = counts.quantile(0.25)
counts_99perc_row = counts.quantile(0.99, axis=1)
counts.head(10)
counts.tail(10)
counts_describe = counts.describe() #including most stat shown before
counts_sort = counts.sort_values(by=list(counts.columns),axis=0) 
counts_sort.head()
counts_sort_onesample = counts.sort_values(by = ['M109Barcode_704-508'])
counts_sort_onesample.head()
counts_sort_onesample_R = counts.sort_values(by = ['M109Barcode_704-508'], ascending=False)
counts_sort_onesample_R.head()