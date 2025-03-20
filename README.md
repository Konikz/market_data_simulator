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
