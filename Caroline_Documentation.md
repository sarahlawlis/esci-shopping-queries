# V1 Documentation - Caroline Cordes

## Data

1. Loading the data
Examples Dataset (shopping_queries_dataset_examples.parquet)
Products Dataset (shopping_queries_dataset_products.parquet)
Sources Dataset (shopping_queries_dataset_sources.csv)
2. Merging the data
The examples and products datasets are merged on product locale and ID, retaining U.S. locale data only
3. Encoding labels
To perform multi-classification, we map the the Exact, Substitute, Classification, and Irrelevant to corresponding numbers
- E -> 0
- S -> 1
- C -> 2
- I -> 3

## Embeddings 
Used the distilroberta-base, a distilled version of the RoBERTa-base model. The model has 6 layers, 768 dimensions and 12 heads , totalizing 82M parameters. 


Used the generate_embeddings function created by sarah to with a batch size of 128 to process the embeddings. Passed the query and product title through the function and concatenate them to get create a dataframe with the concatenated embeddings and has a size of (n, 1536)


## Modeling 
Created a Multi-Layer Perceptron model with a 
linear, activation, dropout, and maxpool layer with a final classification layer which we passed our test and train loaders through. 


## Data Loader 
The data loader works to by using the index values from the embeddings data set and finding the corresponding label that is associated with the index to create a different dataset 


