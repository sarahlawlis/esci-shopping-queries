# Documentation for Pre-trained Distilled Roberta model

## Core goal of this step is to pre-train a Distilled Roberta model on domain data to be used in further iterations of fine-tuning models. 

BERT models show that Masked Language Model (MLM) is a powerful pre-training approach. We plan to run MLM on a large, domain specific dataset (on-line retail shopping in this case) separate from the training dataset (Amazon shopping) we are using to replicate the results of the research paper, to prepare model future fine-tuning iterations.

Link to Shopping Queries Dataset: A Large-Scale ESCI Benchmark for Improving Product Search: https://arxiv.org/pdf/2206.06588

The dataset we used for pre-training this model was found via the Hugging Face hub and contains Google shopping data following a similar format to the Amazon shopping dataset, which is what we will be training our models on later. The Google dataset contains 983K entries and includes the following fields: 
    image
    item_ID
    query
    title
    position

The Google dataset can be found here: 
https://huggingface.co/datasets/Marqo/google-shopping-general-eval

For pre-training, we will only be considering the query and title fields as they directly relate the fields of interest in the Amazon dataset. 

### Step 1: Data pre-processing

We begin by cleaning the data for use in model training. First, we remove the columns that are not of interest to us for model training (image, item_ID, position). We then cleaned the remaining columns to strip any special characters and to change all letters to lowercase. 

From there, we wanted to determine if there were any misspellings in the query field that could impact the model. We tokenized values in the query field and created a word frequency to determine how often each word in appears in the query field. By looking at the least frequent words in the query field, we believe that we can see if there is a significant problem with customers misspelling search terms as misspellings are less likely to occur than common spellings. 

Using the SpellChecker function, which uses a Levenshtein Distance algorithm to find permutations within an edit distance of 2 from the original word. It then compares all permutations (insertions, deletions, replacements, and transpositions) to known words in a word frequency list. Those words that are found more often in the frequency list are more likely the correct results. So, we sorted our spell checked list of queries to find the tokens that appear with less frequency. 

What we found was even amongst the least frequent words, there doesn't appear to be very many, if any, common misspellings. Most of what appeared in this list are either acronyms for types or brands of products (dns, oled, dna, qled) or simply items that don't get searched for often (lifejackets, pashminas, paracord). At this point, we consider this to be adequate for model training without removal of specific list items. 

### Step 2: Model Building
