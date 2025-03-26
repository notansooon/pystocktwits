
from pystocktwits import Streamer
import argparse
def main():
    
    parser = argparse.ArgumentParser(description='fetch data from stocktwits')
    parser.add_argument('--type', choices=["user", "symbol"])
    parser.add_argument('--id', type=str)
    args = parser.parse_args()
    
    
    
    stream = Streamer()
    
    try:
        
        if (args.type == "user"):
            
            user_json = stream.get_user_msgs(user_id=args.id)
           
            print(user_json)
        elif(args.type == "symbol"):
            symbol_json = stream.get_symbol_msgs(symbol_id=args.id)
            print(symbol_json)
        
    except Exception as e:
        print(f"Error: {e}")
        return
if __name__ == "__main__":
    main()