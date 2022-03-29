# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import suggestions_pb2 as suggestions__pb2


class SuggestionsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getSuggGames = channel.unary_unary(
                '/Suggestions/getSuggGames',
                request_serializer=suggestions__pb2.gameRequest.SerializeToString,
                response_deserializer=suggestions__pb2.GameResponse.FromString,
                )
        self.getSuggReviews = channel.unary_unary(
                '/Suggestions/getSuggReviews',
                request_serializer=suggestions__pb2.reviewRequest.SerializeToString,
                response_deserializer=suggestions__pb2.ReviewResponse.FromString,
                )


class SuggestionsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getSuggGames(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getSuggReviews(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SuggestionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getSuggGames': grpc.unary_unary_rpc_method_handler(
                    servicer.getSuggGames,
                    request_deserializer=suggestions__pb2.gameRequest.FromString,
                    response_serializer=suggestions__pb2.GameResponse.SerializeToString,
            ),
            'getSuggReviews': grpc.unary_unary_rpc_method_handler(
                    servicer.getSuggReviews,
                    request_deserializer=suggestions__pb2.reviewRequest.FromString,
                    response_serializer=suggestions__pb2.ReviewResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Suggestions', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Suggestions(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getSuggGames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Suggestions/getSuggGames',
            suggestions__pb2.gameRequest.SerializeToString,
            suggestions__pb2.GameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getSuggReviews(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Suggestions/getSuggReviews',
            suggestions__pb2.reviewRequest.SerializeToString,
            suggestions__pb2.ReviewResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
