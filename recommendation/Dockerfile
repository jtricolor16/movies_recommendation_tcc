FROM python:3.8
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY servico_recomendacao.py servico_recomendacao.py
CMD python servico_recomendacao.py