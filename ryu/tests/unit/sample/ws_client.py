from websocket import create_connection

ws = create_connection('ws://127.0.0.1:8081')

while True:
    data = ws.recv()
    print(data)

