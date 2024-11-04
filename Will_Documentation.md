{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO6rKyrlQ3zYZvqyNt2FGCQ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sarahlawlis/esci-shopping-queries/blob/main/Will_Documentation.md\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Decription: not retain the bert model, but understand vocabulary in the dataset that are not pretrained in the bert models, no model trianing or classification, how do we add domain knowledge without model training."
      ],
      "metadata": {
        "id": "5XpkS4ATU1OI"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "To incorporate domain knowledge into the BERT embeddings without retraining the model, I followed these steps:\n",
        "\n",
        "Identify Domain-Specific Vocabulary:\n",
        "\n",
        "Extract unique words or phrases from your dataset that are not well-represented or understood by the pretrained BERT tokenizer.\n",
        "You can use the tokenizer to tokenize your text data and identify tokens that are split in unnatural ways, which suggests they are not in the tokenizer’s vocabulary.\n",
        "\n",
        "Create Embeddings for New Vocabulary:\n",
        "\n",
        "Use a method to create embeddings for the new vocabulary words. You can average the embeddings of subword tokens that BERT assigns to these words or use context-based embeddings from BERT to represent them.\n",
        "For example, pass sentences containing the domain-specific terms through the BERT model and average the output embeddings from the relevant layers.\n",
        "\n",
        "Enhance the Embeddings with Domain Knowledge:\n",
        "\n",
        "Use techniques like post-processing or fusion with external embeddings (e.g., using domain-specific word embeddings) to enrich the representation of these terms.\n",
        "You can combine BERT embeddings with domain-specific embeddings by concatenating or averaging them.\n",
        "\n",
        "Preprocessing:\n",
        "\n",
        "Ensure that your tokenizer is appropriately configured to handle domain-specific terms. If certain terms are critical, consider adding special tokens in the preprocessing pipeline.\n",
        "\n",
        "Evaluation and Use:\n",
        "\n",
        "Check if the enhanced embeddings improve performance on any downstream tasks or provide better semantic representation for analysis."
      ],
      "metadata": {
        "id": "7VIZLQlgUVOj"
      }
    }
  ]
}