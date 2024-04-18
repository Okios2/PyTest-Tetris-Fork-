FROM python:2

RUN git clone https://github.com/Okios2/PyTest-Tetris-Fork-.git

WORKDIR ./PyTest-Tetris-Fork-

RUN python -m pip install --upgrade pip

RUN pip install pytest

RUN pip install pygame

RUN pip install wheel

RUN pip install setuptools

CMD ["bash"]

RUN "ls"

CMD ["python setup.py bdist_wheel"]
 
