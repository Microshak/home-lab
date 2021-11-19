docker run --rm -it -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v $(pwd)/notebooks:/home/jovyan/work jupyter/datascience-notebook

