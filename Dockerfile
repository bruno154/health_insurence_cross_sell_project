FROM jupyter/base-notebook

USER jovyan

COPY requirements.txt /home/jovyan/work

WORKDIR /home/jovyan/work

RUN pip install -r requirements.txt

# RUN conda install --quiet --yes -c conda-forge --file \
#     requirements.txt