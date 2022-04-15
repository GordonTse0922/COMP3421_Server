from flask_restful import Resource
from flask import request
from models.post import PostModel

class Post(Resource):
    def get(self, id ):
        post =PostModel.get_post(id)
        if not post:
            return {
                'message': 'post not exist!'
            }, 403
        return {
            'message': '',
            'post':'testing'
        }

    def post(self, name):
        return {'post': name}

    def put(self, name):
        return {'post': name}

    def delete(self, name):
        return {'post': name}


class Posts(Resource):
    def get(self, department_id ):
        posts =PostModel.get_all_department_post(department_id)
        if not posts:
            return {
                'message': 'This department do not have any post yet'
            }, 403
        return {
            'message': '',
            'post':'testing'
        }