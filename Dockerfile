FROM python:3.11-slim

ENV PYTHONPATH="/usr/src/app/adapters/inbound/grpc:/usr/src/app"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p adapters/inbound/grpc

RUN python -m grpc_tools.protoc \
    -I . \
    -I /usr/local/lib/python*/site-packages/grpc_tools/_proto \
    --python_out=adapters/inbound/grpc \
    --grpc_python_out=adapters/inbound/grpc \
    ./auth.proto

CMD [ "python", "./main.py" ]

