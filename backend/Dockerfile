FROM python:3.6 AS compile-image
RUN apt-get -y update
RUN apt-get install -y  --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" 

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.6-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
CMD ["uvicorn", "sprites.main:app", "--reload"]
