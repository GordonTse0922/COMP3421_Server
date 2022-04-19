from flask_restful import Resource
from flask import request
from models.post import PostModel
from schema.post import PostSchema
from marshmallow import ValidationError

post_schema = PostSchema(many=False)
posts_schema = PostSchema(only=['id','user','title','content','created_at','comments'],many=True)
class Post(Resource):
    def get(self):
        post =PostModel.get_post()
        if not post:
            return {
                'message': 'post not exist!'
            }, 403
        return {
            'post': post_schema.dump(post)
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
    def get(self):
        posts =PostModel.get_all_department_post()
        if not posts:
            return {
                'message': 'This department do not have any post yet',
                'posts':[]
            },200
        return {
            'posts': posts_schema.dump(posts)
        }