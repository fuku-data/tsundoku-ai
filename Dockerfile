FROM python:3.12-slim

COPY ./requirements.txt .

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid 1000 streamlit \
    && useradd --uid 1000 --gid streamlit --shell /bin/bash --create-home streamlit \
    && mkdir /app \
    && chown -R streamlit:streamlit /app

EXPOSE 8501

WORKDIR /app

USER streamlit

COPY --chown=streamlit:streamlit ./tsundoku-ai/src .
COPY --chown=streamlit:streamlit ./book ./book

CMD ["streamlit", "run", "00_🏠_Home.py"]