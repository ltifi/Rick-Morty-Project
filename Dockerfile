FROM python:3.8.1

EXPOSE 8000
WORKDIR /RickeyMorty

COPY requirements.txt ./

RUN pip3 install --no-cache-dir --upgrade -r ./requirements.txt
RUN apt-get update \
    && apt-get -y install gcc make \
    && rm -rf /var/lib/apt/lists/*s
# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install xvfb -y
RUN apt-get install -y google-chrome-stable
# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
RUN python3 --version
RUN pip3 --version
RUN pip install --no-cache-dir --upgrade pip
COPY . ./


CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]