from eventlet import wsgi

from ryu.lib import rpc
from ryu.tests.unit.sample import websocket_master as websocket

@websocket.WebSocketWSGI
def ws_handler(ws):
    for i in itertools.count():
        data = {
            'count': i,
        }
        ws.send(unicode(json.dumps(data)))
        eventlet.sleep(1)

wsgi.server(eventlet.listen(('', 8081)), ws_handler)

