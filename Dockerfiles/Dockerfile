FROM python:2

RUN git clone https://github.com/satyammittal/PyTest-Tetris.git

WORKDIR ./PyTest-Tetris

RUN pip install pytest

RUN pip install pygame

RUN pip install wheel

CMD ["bash"]

CMD ["python setup.py sdist bdist_wheel"]
