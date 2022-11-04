from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from flask_apscheduler import APScheduler
import scheduleTest
import json
import itertools

app = Flask(__name__)
api = Api(app)
CORS(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=str, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=str, help="Likes of the video is required", required=True)

videos = {}


class SerializableGenerator(list):
    """Generator that is serializable by JSON"""

    def __init__(self, iterable):
        tmp_body = iter(iterable)
        try:
            self._head = iter([next(tmp_body)])
            self.append(tmp_body)
        except StopIteration:
            self._head = []

    def __iter__(self):
        return list


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def post(self, video_id):
        args = video_put_args.parse_args()
        return {video_id: args}

    def put(self, video_id):
        with open("my_number.txt") as f:
            for line in f:
                print(int(line))
                return(int(line))
#                yield json.dumps(SerializableGenerator(iter(int(line))))


class user(Resource):
    def get(self):
        name = "CJM"
        age = 32
        return {"name": name, "age": age}

    def post(self):
        name = "post CJM"
        age = 34
        return {"name": name, "age": age}


class HelloWorld(Resource):
    def get(self, name):
        print(request.form)
        return {"name": name}


api.add_resource(user, "/user")
api.add_resource(Video, "/video/<int:video_id>")
api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == '__main__':
    # scheduler = APScheduler()
    # scheduler.add_job(id= 'Description of cron job', func = scheduleTest.scheduledTask, trigger = 'interval', seconds = 5)
    # scheduler.add_job(id='id2', func=scheduleTest.scheduledTaskOneMore, trigger='interval', seconds=3)
    # scheduler.start()
    app.run()
