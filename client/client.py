import grpc
import market_data_pb2
import market_data_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = market_data_pb2_grpc.MarketDataServiceStub(channel)
    # Change instrument_id here to test error handling (e.g., "MSFT" for a non-existent instrument)
    request = market_data_pb2.SubscriptionRequest(instrument_id="AAPL")
    
    try:
        for update in stub.Subscribe(request):
            print(f"Received update for {update.instrument_id}")
            print("Bids:", update.bid_prices)
            print("Asks:", update.ask_prices)
            print("-" * 40)
    except grpc.RpcError as e:
        # Handle the error gracefully
        print("Error received from server:", e.details())

if __name__ == "__main__":
    run()
