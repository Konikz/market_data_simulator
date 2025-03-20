# Market Data Simulator

A simple market data dissemination simulator built with Python and gRPC. This project is designed to help aspiring quantitative developers and software engineers understand client-server communication, middleware, and scalable API design in a microservice architecture.

## Overview

The Market Data Simulator consists of two main components:

- **Server Application:**  
  Reads instrument configurations from a JSON file and simulates order book updates. The server streams snapshots and incremental updates to connected clients via a gRPC service.

- **Client Application:**  
  A simple console client that subscribes to the market data service, receives streaming updates, and prints the order book data. It also gracefully handles errors if an invalid instrument is requested.

## Features

- **gRPC-based Communication:**  
  Utilizes Protocol Buffers to define a service for real-time market data updates.
  
- **Configuration-Driven:**  
  Instrument details (e.g., ID, symbol, contract specs) are loaded from a JSON configuration file.
  
- **Error Handling:**  
  The client detects and handles errors gracefully when subscribing to non-existent instruments.

## Project Structure

```plaintext
market_data_simulator/
├── client/                 # Client-side code
│   └── client.py
├── config/                 # Configuration files
│   └── instruments.json
├── proto/                  # Protocol Buffer definitions
│   └── market_data.proto
├── server/                 # Server-side code
│   └── server.py
├── market_data_pb2.py      # Generated from .proto
├── market_data_pb2_grpc.py # Generated from .proto
└── README.md               # This file
```

## Prerequisites

- Python 3.6+
- `grpcio`, `grpcio-tools`, and `protobuf` packages

## Setup Instructions

### Create and Activate a Virtual Environment:
```sh
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Install Dependencies:
```sh
pip install grpcio grpcio-tools protobuf
```

### Generate gRPC Code:
From the project root, run:
```sh
python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/market_data.proto
```

## Running the Project

### Starting the Server
1. Open a terminal.
2. Navigate to the project root and activate the virtual environment.
3. Run the server using:
   ```sh
   python -m server.server
   ```
   The server listens on port 50051 and logs a message when started.

### Running the Client
1. Open a new terminal (keeping the server running).
2. Navigate to the project root and activate the virtual environment.
3. Run the client using:
   ```sh
   python -m client.client
   ```
   The client subscribes to the market data stream (default instrument is "AAPL"). You can modify the instrument ID in the client code to test different scenarios.

## Configuration

The `config/instruments.json` file holds the instrument configurations. For example:

```json
[
  {
    "instrument_id": "AAPL",
    "symbol": "Apple Inc.",
    "contract_specs": "Some contract details..."
  },
  {
    "instrument_id": "GOOG",
    "symbol": "Alphabet Inc.",
    "contract_specs": "Some contract details..."
  }
]
