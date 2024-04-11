FROM python:2 AS builder

RUN git clone https://github.com/satyammittal/PyTest-Tetris.git

WORKDIR ./PyTest-Tetris

RUN pip install pytest

RUN pip install pygame

FROM builder AS tester

COPY --from=builder /PyTest-Tetris /PyTest-Tetris

CMD ["bash"]
