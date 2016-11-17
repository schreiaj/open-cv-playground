FROM continuumio/anaconda
EXPOSE 8888

RUN conda install opencv -y --quiet
RUN conda install jupyter -y --quiet

ADD . /code
WORKDIR /code

CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser"]
