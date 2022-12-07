from flask import Blueprint, jsonify
from api.utils import load_posts, get_posts_by_pk
from main.posts_dao import PostsDAO


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts():
    return jsonify(load_posts())


@api_blueprint.route('/api/posts/<int:postid>', methods=['GET'])
def get_post_by_id(postid):
    return jsonify(get_posts_by_pk(postid))


get_post_by_id(1)




