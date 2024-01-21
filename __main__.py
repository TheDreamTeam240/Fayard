import argparse
import logging
import client
import json
import random

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    setup_logging()

    parser = argparse.ArgumentParser()

    parser.add_argument("server_host", help="Server host")
    parser.add_argument("server_tcp_port", help="Server TCP port", type=int)
    parser.add_argument("server_udp_port", help="Server UDP port", type=int)
    parser.add_argument("client_udp_port", help="Client UDP port", type=int)

    args = parser.parse_args()

    logging.info(f"Connecting to server {args.server_host}:{args.server_tcp_port} (TCP) and {args.server_udp_port} (UDP)")
    logging.info(f"Client UDP port: {args.client_udp_port}")


    network_client = client.Client(args.server_host,
                                   args.server_tcp_port,
                                   args.server_udp_port,
                                   args.client_udp_port)

    print("Client identifier: %s" % network_client.identifier)

    #  Create a room on server
    network_client.create_room("Test room")

    print("Client create room  %s" % network_client.room_id)

    #  Get rooms list

    rooms = network_client.get_rooms()

    selected_room = None
    if rooms is not None and len(rooms) != 0:
        for room in rooms:
            print("Room %s (%d/%d)" % (room["name"], int(room["nb_players"]), int(room["capacity"])))

        # Get first room for tests
        selected_room = rooms[0]['id']
    else:
        print("No rooms")
    
    #  Join client 1 room
    try:
        network_client.join_room(selected_room)
    except Exception as e:
        print("Error : %s" % str(e))
    
    print("Client join %s" % network_client.room_id)

    while True:
        #  Send message to room (any serializable data)
        network_client.send({"x": random.randint(0, 100), "y": random.randint(0, 100)})

        # get server data (only client 3)
        message = network_client.get_messages()
        if len(message) != 0:
            for message in message:
                message = json.loads(message)
                sender, value = message.popitem()
                print("Client %s received %s from %s" % (network_client.identifier, value, sender))

if __name__ == "__main__":
    main()
