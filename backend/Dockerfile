FROM python:3.8-slim-buster

WORKDIR /app
COPY . .
RUN make build

CMD ["uvicorn", "sprites.main:app", "--reload"]
