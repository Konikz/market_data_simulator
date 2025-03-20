import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import grpc
import time
import random
import json
from concurrent import futures

import market_data_pb2
import market_data_pb2_grpc

# Load instrument configurations from the JSON file
def load_instruments(config_path="config/instruments.json"):
    with open(config_path, "r") as f:
        instruments = json.load(f)
    return {inst["instrument_id"]: inst for inst in instruments}

# Load instruments once when server starts
INSTRUMENTS = load_instruments()

class MarketDataService(market_data_pb2_grpc.MarketDataServiceServicer):
    def Subscribe(self, request, context):
        instrument_id = request.instrument_id
        # Check if instrument exists in configuration
        if instrument_id not in INSTRUMENTS:
            context.set_details("Instrument not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return
        # Simulate streaming market data updates
        while True:
            update = market_data_pb2.OrderBookUpdate(
                instrument_id=instrument_id,
                bid_prices=[round(random.uniform(100, 110), 2) for _ in range(5)],
                ask_prices=[round(random.uniform(110, 120), 2) for _ in range(5)]
            )
            yield update
            time.sleep(1)  # Delay between updates

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    market_data_pb2_grpc.add_MarketDataServiceServicer_to_server(MarketDataService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
