from flask_restful import Resource
from flask import request
from models.comment import CommentModel

class Comment(Resource):
    def get(self, post_id ):
        post =CommentModel.get_comments(post_id)
        if not post:
            return {
                'message': 'no comment for this post!'
            }, 403
        return {
            'message': '',
            'post':'testing'
        },200

    def post(self, post_id):
        result = comment_schema.load(request.json)

        if len(result.errors) > 0:
            return result.errors, 433

        comment = CommentModel(result.data['user_id'],result.data['post_id'],result.data['content'])
        comment.add_comment()
        return {
            'message': 'Insert user success',
            'comment': 'testing'
        }

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