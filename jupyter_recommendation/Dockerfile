FROM jupyter/datascience-notebook
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY modelo_recomendacao.ipynb modelo_recomendacao.ipynb
COPY movies.csv movies.csv
COPY tags.csv tags.csv
