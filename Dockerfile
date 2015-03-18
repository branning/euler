from elyase/conda:2.7

RUN conda install -c auto bcrypt
WORKDIR /euler

