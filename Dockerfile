FROM python:3.10.6

ENV PYTHONUNBUFFERED=1

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

WORKDIR /app

RUN pip install --upgrade pip "poetry==1.5.1"
RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY mysite .

ENTRYPOINT [ "/docker-entrypoint.sh" ]
