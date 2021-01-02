# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto.opencv_proto.opencv_pb2 as opencv__pb2


class OpenCVStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RunOpenCV = channel.unary_unary(
                '/OpenCV/RunOpenCV',
                request_serializer=opencv__pb2.OpenCVRequest.SerializeToString,
                response_deserializer=opencv__pb2.OpenCVResponse.FromString,
                )


class OpenCVServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RunOpenCV(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OpenCVServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RunOpenCV': grpc.unary_unary_rpc_method_handler(
                    servicer.RunOpenCV,
                    request_deserializer=opencv__pb2.OpenCVRequest.FromString,
                    response_serializer=opencv__pb2.OpenCVResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'OpenCV', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OpenCV(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RunOpenCV(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OpenCV/RunOpenCV',
            opencv__pb2.OpenCVRequest.SerializeToString,
            opencv__pb2.OpenCVResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
