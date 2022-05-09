# RIDOH Survey Textual Analysis Project

Textual Analyses of COVID-19 RIDOH survey response data. Methods and results include:
- Text cleaning(lemmatization, tokenization, stop word removal)
- [term frequency - inverse document frequency](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) generation
- Word cloud generation
- Document-level word embedding dimensionality reduction via [t-distributed stochastic neighbor embedding](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding). 

The relevant code can be found in [survey-analysis-ipynb](https://github.com/thepolicylab/RIDOHcoding/blob/hwan-work/survey-text-analysis.ipynb). While some code cells are designated for the particular [survey text csv data](https://github.com/thepolicylab/RIDOHcoding/tree/hwan-work/data), the rest can potentally be applied in other textual analysis context. 


## Running the Code

To run the Jupyter notebook, please install [poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) and follow the folling steps:

1. Clone the repo on terminal
    - `git clone git@github.com:thepolicylab/RIDOHcoding.git`
2. Switch to the branch hwan-work
    - `git checkout hwan-work`
3. Navigate to the project directory and install dependencies
    - `poetry install`
4. Execute the code cells in the Jupyter Notebook

## Resources

[Spacy documentation](https://spacy.io/)

[term frequency - inverse document frequency walkthrough](https://towardsdatascience.com/lovecraft-with-natural-language-processing-part-3-tf-idf-vectors-8c2d4df98621)
- [sklearn.TfidfTransformer vs. sklearn.TfidfVectorizer](https://kavita-ganesan.com/tfidftransformer-tfidfvectorizer-usage-differences/#.Ynlu5RPMJQI)

[Python Word Cloud library](https://peekaboo-vision.blogspot.com/2012/11/a-wordcloud-in-python.html)

[Spacy.Vectors](https://spacy.io/api/vectors)

[t-SNE walkthrough](https://danielmuellerkomorowska.com/2021/01/05/introduction-to-t-sne-in-python-with-scikit-learn/)



