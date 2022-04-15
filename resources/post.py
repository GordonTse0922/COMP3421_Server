from flask_restful import Resource
from flask import request
from models.post import PostModel
from schema.post import PostSchema
from marshmallow import ValidationError

post_schema = PostSchema(many=False)
posts_schema = PostSchema(many=True)
class Post(Resource):
    def get(self):
        post =PostModel.get_post(id)
        if not post:
            return {
                'message': 'post not exist!'
            }, 403
        return {
            'message': '',
            'post':'testing'
        }

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, 400
        try:
            data = post_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        post = PostModel(
            data['title'],
            data['content'],
            data['user_id'],
            data['department_id'])
        post.add_post()
        return {
            'message': 'Insert post success',
        }

    def put(self):
        return {'post': 'test'}

    def delete(self):
        return {'post': 'test'}


class Posts(Resource):
    def get(self, department_id ):
        posts =PostModel.get_all_department_post(department_id)
        if not posts:
            return {
                'message': 'This department do not have any post yet'
            }, 403
        return {
            'posts': posts_schema.dump(posts)
        }