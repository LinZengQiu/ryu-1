import json
import itertools

from eventlet import wsgi
#import websocket80633ab22486228a64184bb9d8d6fd0ea7977677 as websocket
#import websocket849d45682fba7a2a1f16c39f26ad4f2dab80cffc as websocket
import websocket_master as websocket
import eventlet

@websocket.WebSocketWSGI
def ws_handler(ws):
    for i in itertools.count():
        data = {
            'count': i,
        }
        ws.send(json.dumps(data))
        eventlet.sleep(1)

wsgi.server(eventlet.listen(('', 8081)), ws_handler)

