from flask_restful import Resource
import json


class Hero(Resource):
    @classmethod
    def get(cls, hero_id: int):
        return {'hello': 'get', 'id': hero_id}

    @classmethod
    def post(cls):
        return {'hello': 'post'}

    @classmethod
    def put(cls, hero_id: int):
        return {'hello': 'put'}

    @classmethod
    def delete(cls, hero_id: int):
        return {'hello': 'delete'}


class HeroList(Resource):
    @classmethod
    def get(cls):
        # открываем файл в режиме чтения
        with open('src/resources/hero/hero.txt', 'r') as fr:
            # читаем из файла
            lst = json.load(fr)
        return {'heroes': lst}
