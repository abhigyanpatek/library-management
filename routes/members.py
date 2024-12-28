from flask import Blueprint, jsonify, request
from auth import token_required
from db import members, get_next_id
from models import Member

members_bp = Blueprint('members', __name__)

@members_bp.route('/', methods=['GET'])
def get_members():
    return jsonify([member.__dict__ for member in members])

@members_bp.route('/', methods=['POST'])
@token_required
def add_member():
    data = request.json
    new_member = Member(get_next_id(members), data['name'], data['email'])
    members.append(new_member)
    return jsonify(new_member.__dict__), 201

@members_bp.route('/<int:member_id>', methods=['PUT'])
@token_required
def update_member(member_id):
    data = request.json
    for member in members:
        if member.id == member_id:
            member.name = data.get('name', member.name)
            member.email = data.get('email', member.email)
            return jsonify(member.__dict__)
    return jsonify({"message": "Member not found"}), 404

@members_bp.route('/<int:member_id>', methods=['DELETE'])
@token_required
def delete_member(member_id):
    global members
    members = [member for member in members if member.id != member_id]
    return jsonify({"message": "Member deleted"})