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

task_2 = examples_products[examples_products['large_version'] == 1]
task_2_train = task_2[task_2['split'] == 'train']
task_2_test = task_2[task_2['split'] == 'test']