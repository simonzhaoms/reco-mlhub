import papermill as pm
import argparse

# NOTEBOOK parameters
notebook_parameters = {
    'TOP_K': 10,
    'MOVIELENS_DATA_SIZE': '100k'
}


def run_notebook(args):
    '''Run notebook
    '''
    pm.execute_notebook(
        args.input_notebook, 
        args.output_notebook, 
        cwd='recommenders',
        parameters=notebook_parameters,
    )
    results = pm.read_notebook(args.output_notebook).dataframe.set_index("name")["value"]

    for key, value in results.items():
        space = ' ' * (10 - len(key))
        print("{0}:{1} {2}".format(key, space, value))


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_notebook_path', type=str, dest='input_notebook', default='recommenders/notebooks/00_quick_start/sar_movielens.ipynb')
    parser.add_argument('--output_notebook_path', type=str, dest='output_notebook', default='output.ipynb')
    args = parser.parse_args()
    
    run_notebook(args)


if __name__ == "__main__":
    main()
