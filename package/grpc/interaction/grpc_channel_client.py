from __future__ import print_function
import logging

import grpc
import pickle
from rpc_package.transfer_pb2 import Message, RequestMeta, Party
from rpc_package.transfer_pb2_grpc import TransferServerStub

from conf import MAX_MESSAGE_LENGTH, SERVER_CONF


class GrpcChannelClient(object):
    """A pseudo-duplex network client based on GRPC.
    """

    def __init__(self, party_id):
        self._channel = None
        self._stub = None
        self._party_id = party_id
        self.connect(addr_and_port=self._get_addr_and_port(party_id))

    @staticmethod
    def _get_addr_and_port(party_id):
        role_info = SERVER_CONF.get(party_id, {})
        grpc_port = role_info.get("grpc_port", None)
        if grpc_port is None:
            raise ValueError("grpc_port not set")
        addr_and_port = "[::]:{}".format(grpc_port)
        return addr_and_port

    def connect(self, addr_and_port):
        self._channel = grpc.insecure_channel(addr_and_port, options=[
            ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
            ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)])
        self._stub = TransferServerStub(self._channel)
        print("Created stub to %s" % addr_and_port)

    def disconnect(self):
        self._channel.close()

    @property
    def stub(self):
        return self._stub

    def remote(self, data_instance, dst_party_id, tag):
        msg = Message()
        msg.bytes.data = pickle.dumps(data_instance)
        join_tag = "{}_{}_{}".format(self._party_id, dst_party_id, tag)
        msg.request_meta.CopyFrom(
            RequestMeta(tag=join_tag,
                        src=Party(partyId=str(self._party_id)),
                        dst=Party(partyId=str(dst_party_id))))
        response = self._stub.send(msg)

        print("{} remote {}: {} success".format(self._party_id, dst_party_id, response))

    def get(self, src_party_id, tag):
        join_tag = "{}_{}_{}".format(src_party_id, self._party_id, tag)
        response = self._stub.get_local_server(RequestMeta(tag=join_tag,
                                                           src=Party(partyId=str(src_party_id)),
                                                           dst=Party(partyId=str(self._party_id))))

        print("{} get {}: {} success".format(src_party_id, self._party_id, response.request_meta))

        if response.request_meta.tag == "time_out":
            data_instance = None
        else:
            data_instance = pickle.loads(response.bytes.data)
        return data_instance
