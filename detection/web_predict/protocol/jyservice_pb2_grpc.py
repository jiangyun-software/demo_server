# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protocol import jyservice_pb2 as protocol_dot_jyservice__pb2


class JYServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TrainParameter = channel.unary_unary(
                '/JYService.JYService/TrainParameter',
                request_serializer=protocol_dot_jyservice__pb2.TrainParameterRequest.SerializeToString,
                response_deserializer=protocol_dot_jyservice__pb2.TrainParameterResponse.FromString,
                )
        self.TrainData = channel.stream_unary(
                '/JYService.JYService/TrainData',
                request_serializer=protocol_dot_jyservice__pb2.TrainDataRequest.SerializeToString,
                response_deserializer=protocol_dot_jyservice__pb2.TrainDataResponse.FromString,
                )
        self.Train = channel.unary_unary(
                '/JYService.JYService/Train',
                request_serializer=protocol_dot_jyservice__pb2.TrainRequest.SerializeToString,
                response_deserializer=protocol_dot_jyservice__pb2.TrainResponse.FromString,
                )
        self.TrainResult = channel.unary_stream(
                '/JYService.JYService/TrainResult',
                request_serializer=protocol_dot_jyservice__pb2.TrainResultRequest.SerializeToString,
                response_deserializer=protocol_dot_jyservice__pb2.TrainResultResponse.FromString,
                )


class JYServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def TrainParameter(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TrainData(self, request_iterator, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Train(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TrainResult(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JYServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TrainParameter': grpc.unary_unary_rpc_method_handler(
                    servicer.TrainParameter,
                    request_deserializer=protocol_dot_jyservice__pb2.TrainParameterRequest.FromString,
                    response_serializer=protocol_dot_jyservice__pb2.TrainParameterResponse.SerializeToString,
            ),
            'TrainData': grpc.stream_unary_rpc_method_handler(
                    servicer.TrainData,
                    request_deserializer=protocol_dot_jyservice__pb2.TrainDataRequest.FromString,
                    response_serializer=protocol_dot_jyservice__pb2.TrainDataResponse.SerializeToString,
            ),
            'Train': grpc.unary_unary_rpc_method_handler(
                    servicer.Train,
                    request_deserializer=protocol_dot_jyservice__pb2.TrainRequest.FromString,
                    response_serializer=protocol_dot_jyservice__pb2.TrainResponse.SerializeToString,
            ),
            'TrainResult': grpc.unary_stream_rpc_method_handler(
                    servicer.TrainResult,
                    request_deserializer=protocol_dot_jyservice__pb2.TrainResultRequest.FromString,
                    response_serializer=protocol_dot_jyservice__pb2.TrainResultResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'JYService.JYService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JYService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def TrainParameter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/JYService.JYService/TrainParameter',
            protocol_dot_jyservice__pb2.TrainParameterRequest.SerializeToString,
            protocol_dot_jyservice__pb2.TrainParameterResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TrainData(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/JYService.JYService/TrainData',
            protocol_dot_jyservice__pb2.TrainDataRequest.SerializeToString,
            protocol_dot_jyservice__pb2.TrainDataResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Train(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/JYService.JYService/Train',
            protocol_dot_jyservice__pb2.TrainRequest.SerializeToString,
            protocol_dot_jyservice__pb2.TrainResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TrainResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/JYService.JYService/TrainResult',
            protocol_dot_jyservice__pb2.TrainResultRequest.SerializeToString,
            protocol_dot_jyservice__pb2.TrainResultResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
