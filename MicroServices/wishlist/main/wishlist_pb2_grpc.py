# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import wishlist_pb2 as wishlist__pb2


class WishlistStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListGames = channel.unary_unary(
                '/Wishlist/ListGames',
                request_serializer=wishlist__pb2.ListGamesWishRequest.SerializeToString,
                response_deserializer=wishlist__pb2.ListGamesWishResponse.FromString,
                )
        self.AddGame = channel.unary_unary(
                '/Wishlist/AddGame',
                request_serializer=wishlist__pb2.Game.SerializeToString,
                response_deserializer=wishlist__pb2.AddGameWishResponse.FromString,
                )
        self.DeleteGame = channel.unary_unary(
                '/Wishlist/DeleteGame',
                request_serializer=wishlist__pb2.DeleteGameWishRequest.SerializeToString,
                response_deserializer=wishlist__pb2.DeleteGameWishResponse.FromString,
                )


class WishlistServicer(object):
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


def add_WishlistServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListGames': grpc.unary_unary_rpc_method_handler(
                    servicer.ListGames,
                    request_deserializer=wishlist__pb2.ListGamesWishRequest.FromString,
                    response_serializer=wishlist__pb2.ListGamesWishResponse.SerializeToString,
            ),
            'AddGame': grpc.unary_unary_rpc_method_handler(
                    servicer.AddGame,
                    request_deserializer=wishlist__pb2.Game.FromString,
                    response_serializer=wishlist__pb2.AddGameWishResponse.SerializeToString,
            ),
            'DeleteGame': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteGame,
                    request_deserializer=wishlist__pb2.DeleteGameWishRequest.FromString,
                    response_serializer=wishlist__pb2.DeleteGameWishResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Wishlist', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Wishlist(object):
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
        return grpc.experimental.unary_unary(request, target, '/Wishlist/ListGames',
            wishlist__pb2.ListGamesWishRequest.SerializeToString,
            wishlist__pb2.ListGamesWishResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/Wishlist/AddGame',
            wishlist__pb2.Game.SerializeToString,
            wishlist__pb2.AddGameWishResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/Wishlist/DeleteGame',
            wishlist__pb2.DeleteGameWishRequest.SerializeToString,
            wishlist__pb2.DeleteGameWishResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)