FROM python:3.8.1

EXPOSE 8000
WORKDIR /RickeyMorty

COPY requirements.txt ./

RUN pip3 install --no-cache-dir --upgrade -r ./requirements.txt

COPY . ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
