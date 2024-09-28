import pandas as pd
import os

examples_path = os.path.join('..','esci-shopping-queries', 'data', 'shopping_queries_dataset_examples.parquet')
products_path = os.path.join('..','esci-shopping-queries', 'data', 'shopping_queries_dataset_products.parquet')
sources_path = os.path.join('..','esci-shopping-queries', 'data', 'shopping_queries_dataset_sources.csv')

examples = pd.read_parquet(examples_path)
products = pd.read_parquet(products_path)
sources = pd.read_csv(sources_path)

examples_products = pd.merge(
    examples,
    products,
    how='left',
    left_on=['product_locale','product_id'],
    right_on=['product_locale', 'product_id']
)

examples_products = examples_products[examples_products['product_locale'] == 'us']

task_3 = examples_products[examples_products['large_version'] == 1]
task_3['substitute_label'] = task_3['esci_label'].apply(lambda esci_label: 1 if esci_label == 'S' else 0)
task_3 = task_3.drop('esci_label', axis=1)
task_3_train = task_3[task_3['split'] == 'train']
task_3_test = task_3[task_3['split'] == 'test']