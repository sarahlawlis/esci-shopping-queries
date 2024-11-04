# Task V1

The purpose of task V1 is to understand how and when different BERT like models yield high accuracy when classifying ESCI labels for products based on corresponding queries.

## Data Preparation
   **Data Loading**: Three datasets are loaded:
- Examples Dataset (`shopping_queries_dataset_examples.parquet`)
- Products Dataset (`shopping_queries_dataset_products.parquet`)
- Sources Dataset (`shopping_queries_dataset_sources.csv`)

**Data Merging and Filtering**: 
- The `examples` and `products` datasets are merged on product locale and ID, retaining U.S. locale data only

**Label Encoding**:
- ESCI labels ("Exact", "Substitute", "Complement", "Irrelevant") are mapped to integers for classification:
- **E**: 0, **S**: 1, **C**: 2, **I**: 3
**Data Splitting**: The data is split into training and test sets, with a 10,000-row sample taken for efficient processing

## Generating Embeddings
- DistilBERT Model: A pre-trained DistilBERT model (`distilbert-base-uncased`) generates embeddings for the product queries and titles.
- Embedding Generation:
    - The `generate_embeddings` function processes text in batches of 128, tokenizing and encoding with DistilBERT.
    - Query and product title embeddings are concatenated for each pair.
    - Embedding DataFrame: The combined embeddings are stored in a DataFrame with columns representing each dimension.

## Defining Multi-layer Perceptron Model
**Model Architecture**:

- A fully connected neural network class `FullyConnected` is defined with:
- An initial dense layer, dropout layer, and max pooling.
- A final dense layer for output.

**Model Parameters**:
- Input Size: 1536 (combined embedding size).
- Hidden Layer Size: 128.
- Output Layers: 4 (for each ESCI label).

**Model Initialization**:
- The model is instantiated, with Cross-Entropy Loss as the criterion and Adam optimizer configured with a learning rate of \(5 \times 10^{-5}\).

## Classification
**Subset Selection**:
- A subset of indices is matched from the training data to align embeddings with their corresponding ESCI labels.

**Training Setup**:
- The model will use the subset embeddings and labels to classify the ESCI label for each query-product pair, aiming to maximize accuracy on the validation set.