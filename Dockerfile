# Базовый образ с Python
FROM python:3.8-slim-buster

# Устанавливаем необходимые пакеты
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    wget \
    curl \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libnss3

# Установка Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install


WORKDIR /app
COPY ./requirements.txt /app
COPY ./test1.py /app
COPY ./BaseApp.py /app
COPY ./api.py /app
COPY ./FrontPages.py /app
COPY ./conftest.py /app
COPY ./nkbihfbeogaeaoehlefnkodbefgpgknn /app/nkbihfbeogaeaoehlefnkodbefgpgknn
COPY ./profile /app/profile


RUN pip install --no-cache-dir -r requirements.txt

# Запускаем тесты
CMD pytest test1.py && tail -f /dev/null

