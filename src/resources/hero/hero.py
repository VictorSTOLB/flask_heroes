from flask import request
from flask_restful import Resource

from src.models.lib import Hero



class HeroResource(Resource):
    @classmethod
    def get(cls, hero_id: int):
        hero = Hero.find_by_id(hero_id)
        print(hero)
        if not hero:
            return {"message": "Hero doesn't exist"}, 400
        return {'hero': hero.get()}

    @classmethod
    def post(cls):
        hero_req = request.json
        if Hero.find_by_id(hero_req["id"]):
            return {"message": "id exist"}, 400
        print(hero_req)
        hero = Hero(hero_req['id'], hero_req['name'])
        hero.add()
        return {'hero': hero.get()}

    @classmethod
    def put(cls, hero_id: int):
        hero_req = request.json
        # {
        #     "name": 12334423,
        #     "description": 123123
        # }
        hero = Hero.find_by_id(hero_id)
        if not hero:
            return {"message": "hero_id not exist"}, 400
        hero.update(hero_req)
        return {'hero': hero.get()}




    @classmethod
    def delete(cls, hero_id: int):
        hero = Hero.find_by_id(hero_id)
        if not hero:
            return {"message": "id not exist"}, 400
        hero.delete()
        return {"message": "Hero deleted"}


class HeroResourceList(Resource):
    @classmethod
    def get(cls):
        return {'heroes': Hero.get_list()}
