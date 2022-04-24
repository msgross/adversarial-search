FROM ubuntu:latest

LABEL maintainer="mark@grossremarks.com"

USER root
SHELL ["/bin/bash", "-c"]
RUN mkdir py_bin \
  && cd py_bin
RUN apt-get update \
  && apt-get install -y \
  git \
  python3 \
  python3-pip \
  curl
# Install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - \
  && source ~/.poetry/env
RUN git clone https://github.com/msgross/adversarial-search.git
RUN cd adversarial-search \
  && source ~/.poetry/env \
  && poetry build \
  && pip install dist/*.whl
CMD ["python3"]
  