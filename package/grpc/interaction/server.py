import time
from threading import Event, Thread
from concurrent import futures
import grpc
from cacheout import Cache

from rpc_package.transfer_pb2 import Message, Bytes, Empty, RequestMeta
from rpc_package.transfer_pb2_grpc import TransferServerServicer, \
    add_TransferServerServicer_to_server
from grpc_channel_client import GrpcChannelClient
from network.io import Channel
from conf import MAX_MESSAGE_LENGTH, TIMEOUT
from conf import SERVER_CONF


class GrpcChannelServicer(TransferServerServicer):
    """A pseudo-duplex network server based on GRPC.
    """

    cache_data = Cache(maxsize=256)

    def __init__(self, party_id):
        self.channel_dict = {}
        self._init_channel(party_id)

    def _init_channel(self, party_id):
        for _party_id, role_info in SERVER_CONF.items():
            if _party_id != party_id:
                self.channel_dict[_party_id] = GrpcChannelClient(party_id=_party_id)
                print("connect party id {} channel".format(_party_id))

    def recv(self, request: Message, context):
        """
        接收远程的请求数据
        """
        request_meta = request.request_meta
        GrpcChannelServicer.cache_data.set(request_meta.tag, request)
        print("set data {}".format(request_meta.tag))
        return Empty(content="recv success")

    def send(self, request: Message, context):
        """
        发送数据到本地服务,本地服务再调其他服务recv
        """
        request_meta: RequestMeta = request.request_meta
        dst_party_id = request_meta.dst.partyId
        if dst_party_id not in self.channel_dict:
            raise ValueError("dst_party_id not in channel_dict")
        response = self.channel_dict[dst_party_id].stub.recv(request)
        return Empty(content=response.content)

    def get_local_server(self, request: RequestMeta, context):
        """
        从本地服务获取数据
        """
        try:
            count = 0
            while count < TIMEOUT:
                tag_data = GrpcChannelServicer.cache_data.get(request.tag, None)
                if tag_data is None:
                    time.sleep(0.1)
                else:
                    GrpcChannelServicer.cache_data.delete(request.tag)
                    return tag_data
                count += 1
            return Message(request_meta=RequestMeta(tag="time_out"), empty=Empty(content="get method timeout"))
        except Exception as e:
            print(e)


class GrpcChannelServer(Channel):

    def __init__(self, party_id="9999"):
        self._init_serve(party_id)

    def _init_serve(self, party_id):
        role_info = SERVER_CONF.get(party_id, {})
        if len(role_info) == 0:
            raise ValueError("party_id not set")

        grpc_port = role_info.get("grpc_port", None)
        addr_and_port = "[::]:{}".format(grpc_port)
        self._servicer_thread = Thread(target=self.serve, args=(addr_and_port, party_id))
        self._servicer_thread.start()
        self._stop_event = Event()

    def serve(self, addr_and_port, party_id):
        """Start server to serve.
        Arguments:
            addr_and_port (str): The address and port, default: "[::]:50052"
        """
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[
            ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
            ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)], )
        servicer = GrpcChannelServicer(party_id)
        add_TransferServerServicer_to_server(servicer, server)
        server.add_insecure_port(addr_and_port)
        server.start()
        print("Server started at %s" % addr_and_port)
        self._stop_event.wait()
        if not GrpcChannelServicer.cache_data.size():
            time.sleep(3)
        server.stop(grace=10)
        # close channel
        [channel.disconnect() for channel in servicer.channel_dict.values()]
        # server.wait_for_termination()

    def stop(self):
        self._stop_event.set()

    def send(self, data):
        pass

    def recv(self):
        pass


if __name__ == "__main__":
    server = GrpcChannelServer(party_id="9999")
    # server.stop()
