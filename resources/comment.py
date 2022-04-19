from flask_restful import Resource
from flask import request
from models.comment import CommentModel
from schema.comment import CommentOutputSchema, CommentSchema
from marshmallow import ValidationError

comment_schema = CommentSchema(many=False)
comments_schema = CommentSchema(many=True)
comments_output_schema = CommentOutputSchema(many=True)
class Comment(Resource):
    def get(self  ):
        comments =CommentModel.get_comments()
        if not comments:
            return {
                'message': 'This post do not have any  comment yet'
            }, 403
        return {
            'comments': comments_schema.dump(comments)
        }

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, 400
        try:
            data = comment_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        comment = CommentModel(
            data['user_id'],
            data['post_id'],
            data['content']
            )
        comment.add()
        return {
            'message': 'Insert comment success',
        }

    def put(self, name):
        return {'post': name}

    def delete(self, name):
        return {'post': name}


class Comments(Resource):
    def get(self):
        comments =CommentModel.get_comments()
        if not comments:
            return {
                'message': 'This post do not have any comment yet',
                'comments':[]
            }, 200
        return {
            'comments': comments_output_schema.dump(comments)
        }