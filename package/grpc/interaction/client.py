from __future__ import print_function
import logging

import grpc
from rpc_package.transfer_pb2 import Message, RequestMeta, Party
from rpc_package.transfer_pb2_grpc import TransferServerStub

MAX_MESSAGE_LENGTH = 256 * 1024 * 1024


class GrpcChannelClient(object):
    """A pseudo-duplex network client based on GRPC.
    """

    def __init__(self, addr_and_port="localhost:50052"):
        self._channel = None
        self._stub = None
        self.connect(addr_and_port)

    def connect(self, addr_and_port):
        self._channel = grpc.insecure_channel(addr_and_port, options=[
            ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
            ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)])
        self._stub = TransferServerStub(self._channel)
        print("Created stub to %s" % addr_and_port)

    def disconnect(self):
        self._channel.close()

    def test_recv(self):
        m = Message()
        m.bytes.data = b'123'
        m.request_meta.CopyFrom(RequestMeta(tag="hello"))

        response = self._stub.recv(m)

        print("hello client received: {}".format(response))

    def test_get_local(self):
        response = self._stub.get_local_server(RequestMeta(tag="hello"))

        print("hello client received: {}".format(response))

        # response = self._stub.get_local_server(RequestMeta(tag="hello2"))
        #
        # print("hello client received: {}".format(response))

    def test_send(self):
        m = Message()
        m.bytes.data = b'123567'
        m.request_meta.CopyFrom(RequestMeta(tag="hello2", dst=Party(partyId="9999")))

        response = self._stub.send(m)

        print("hello2 client received: {}".format(response))


if __name__ == "__main__":

    client = GrpcChannelClient(addr_and_port="localhost:50050")
    client.test_recv()
    client.test_get_local()
    client.test_send()
    client.disconnect()
