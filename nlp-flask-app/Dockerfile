FROM python:3.8-slim-buster

RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install transformers Flask gunicorn

COPY . /app
WORKDIR /app
RUN python -c "from model import download_model; download_model()"

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]