import os

from flask import Flask, json, request
import grpc

from userManagement_pb2 import User,LoginRequest,LogoutRequest,AddUserRequest,EditUserRequest
from userManagement_pb2_grpc import UserManagementStub

api = Flask(__name__)


usermanagement_host = os.getenv("USERMANAGEMENT_HOST", "localhost")

usermanagement_channel = grpc.insecure_channel(
    f"{usermanagement_host}:50054"
)

usermanagement_client = UserManagementStub(usermanagement_channel)


@api.route('/addUser', methods=['POST'])
def addUser():
    data = json.loads(request.data)
    addUser_request = AddUserRequest(
        id=data['id'],
        nickname=data['nickname'],
        email=data['email'],
        password=data['password']
    )
    addUser_response = usermanagement_client.AddUser(
        addUser_request
    )
    return json.dumps(addUser_response.message)

@api.route('/editUser', methods=['PUT'])
def editUser():
    data = json.loads(request.data)
    updateUser_request = EditUserRequest(
        password=data['password'],
        new_password=data['new_password'],
        nickname=data['nickname'],
        email=data['email'],
        new_email=data['new_email']
    )
    updateUser_response = usermanagement_client.EditUser(
        updateUser_request
    )
    return json.dumps(updateUser_response.message)

@api.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    login_request = LoginRequest(
        email=data['email'],
        password=data['password']
    )
    login_response = usermanagement_client.LoginUser(
        login_request
    )
    return json.dumps(login_response.message)

@api.route('/logout', methods=['GET'])
def logout():
    data = json.loads(request.data)
    logout_request = LogoutRequest(
        email=data['email'],
    )
    logout_response = usermanagement_client.Logout(
        logout_request
    )
    return json.dumps(logout_response.message)