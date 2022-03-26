# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import library_pb2 as library__pb2


class LibraryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListGames = channel.unary_unary(
                '/Library/ListGames',
                request_serializer=library__pb2.ListGamesLibRequest.SerializeToString,
                response_deserializer=library__pb2.ListGamesLibResponse.FromString,
                )
        self.AddGame = channel.unary_unary(
                '/Library/AddGame',
                request_serializer=library__pb2.AddGameLibRequest.SerializeToString,
                response_deserializer=library__pb2.Game.FromString,
                )
        self.DeleteGame = channel.unary_unary(
                '/Library/DeleteGame',
                request_serializer=library__pb2.DeleteGameLibRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class LibraryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListGames(self, request, context):
        """Returns a list of games in the library
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddGame(self, request, context):
        """Add a new game to the library
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteGame(self, request, context):
        """Deletes a game from the library
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LibraryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListGames': grpc.unary_unary_rpc_method_handler(
                    servicer.ListGames,
                    request_deserializer=library__pb2.ListGamesLibRequest.FromString,
                    response_serializer=library__pb2.ListGamesLibResponse.SerializeToString,
            ),
            'AddGame': grpc.unary_unary_rpc_method_handler(
                    servicer.AddGame,
                    request_deserializer=library__pb2.AddGameLibRequest.FromString,
                    response_serializer=library__pb2.Game.SerializeToString,
            ),
            'DeleteGame': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteGame,
                    request_deserializer=library__pb2.DeleteGameLibRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Library', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Library(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListGames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/ListGames',
            library__pb2.ListGamesLibRequest.SerializeToString,
            library__pb2.ListGamesLibResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/AddGame',
            library__pb2.AddGameLibRequest.SerializeToString,
            library__pb2.Game.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/DeleteGame',
            library__pb2.DeleteGameLibRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
