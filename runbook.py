import papermill as pm
import time

INPUT_NOTEBOOK = 'recommenders/notebooks/00_quick_start/sar_movielens.ipynb'
OUTPUT_NOTEBOOK = 'sar_movielens_output.ipynb'

pm.execute_notebook(INPUT_NOTEBOOK, OUTPUT_NOTEBOOK, kernel_name=KERNEL_NAME)
results = pm.read_notebook(OUTPUT_NOTEBOOK).dataframe.set_index("name")["value"]

print("The run results:")
for key, value in results.items():
    print("{}: {}".format(key, value))