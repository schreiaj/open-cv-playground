FROM continuumio/anaconda
EXPOSE 8888

RUN conda install opencv -y --quiet
RUN conda install jupyter ipywidgets -y --quiet
RUN conda install -c https://conda.binstar.org/asmeurer pandoc -y --quiet


CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--notebook-dir=src"]
