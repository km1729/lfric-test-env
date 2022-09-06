FROM docker.io/jupyter/scipy-notebook:latest
COPY ./environment.yml /home/jovyan/requirements.yaml
RUN conda env update --file requirements.yaml --prune

CMD ["start-notebook.sh"]