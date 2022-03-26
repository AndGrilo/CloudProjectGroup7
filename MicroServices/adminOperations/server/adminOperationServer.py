import os

from flask import Flask, json, request
import grpc

from adminOperations_pb2 import Game,DeleteGameRequest,DeleteUserRequest
from adminOperations_pb2_grpc import AdminOperationsStub

api = Flask(__name__)

adminoperations_host = os.getenv("ADMINOPERATIONS_HOST", "localhost")

adminoperations_channel = grpc.insecure_channel(
    f"{adminoperations_host}:50052"
)

adminoperations_client = AdminOperationsStub(adminoperations_channel)


@api.route('/admin/games', methods=['POST'])
def addGame():
    data = json.loads(request.data)
    addGame_request = Game(
        url=data['url'],
        types=data['types'],
        name=data['name'],
        desc_snippet=data['desc_snippet'],
        recent_reviews=data['recent_reviews'],
        all_reviews=data['all_reviews'],
        release_date=data['release_date'],
        developer=data['developer'],
        publisher=data['publisher'],
        popular_tags=data['popular_tags'],
        game_details=data['game_details'],
        languages=data['languages'],
        achievements=data['achievements'],
        genre=data['genre'],
        game_description=data['game_description'],
        mature_content=data['mature_content'],
        minimum_requirements=data['minimum_requirements'],
        recommended_requirements=data['recommended_requirements'],
        original_price=data['original_price'],
        discount_price=data['discount_price']
    )
    addGame_response = adminoperations_client.AddGame(
        addGame_request
    )
    return json.dumps(addGame_response.message)


@api.route('/admin/games', methods=['PUT'])
def updateGame():
    data = json.loads(request.data)
    updateGame_request = Game(
        url=data['url'],
        types=data['types'],
        name=data['name'],
        desc_snippet=data['desc_snippet'],
        recent_reviews=data['recent_reviews'],
        all_reviews=data['all_reviews'],
        release_date=data['release_date'],
        developer=data['developer'],
        publisher=data['publisher'],
        popular_tags=data['popular_tags'],
        game_details=data['game_details'],
        languages=data['languages'],
        achievements=data['achievements'],
        genre=data['genre'],
        game_description=data['game_description'],
        mature_content=data['mature_content'],
        minimum_requirements=data['minimum_requirements'],
        recommended_requirements=data['recommended_requirements'],
        original_price=data['original_price'],
        discount_price=data['discount_price']
    )
    updateGame_response = adminoperations_client.UpdateGame(
        updateGame_request
    )
    return json.dumps(updateGame_response.message)


@api.route('/admin/games', methods=['DELETE'])
def deleteGame():
    url = request.args.get('url')
    deleteGame_request = DeleteGameRequest(
        url=url,
    )
    deleteGame_response = adminoperations_client.DeleteGame(
        deleteGame_request
    )
    return json.dumps(deleteGame_response.message)

@api.route('/admin/users', methods=['DELETE'])
def deleteGame():
    id = request.args.get('id')
    deleteUser_request = DeleteUserRequest(
        id=id,
    )
    deleteUser_response = adminoperations_client.DeleteUser(
        deleteUser_request
    )
    return json.dumps(deleteUser_response.message)