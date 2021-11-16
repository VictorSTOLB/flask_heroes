import json


class Hero:
    hero_id: int = None
    name: str = None

    def __init__(self, hero_id: int, name: str):
        self.hero_id = hero_id
        self.name = name

    @classmethod
    def get_list(cls) -> list:
        with open('./hero.txt', 'r') as fr:
            lst = json.load(fr)
        return lst

    @classmethod
    def find_by_id(cls, hero_id: int):
        for h in cls.get_list():
            if int(h['id']) == hero_id:
                return cls(h["id"], h["name"])
        return None

    def get(self):
        return {'id': self.hero_id, 'name': self.name}

    def add(self):
        hl = self.get_list()
        hl.append(self.get())
        self.save(hl)

    def save(self, hl: list):
        with open('hero.txt', 'w') as fw:
            json.dump(hl, fw)

    def delete(self):
        hl = self.get_list()
        hl.remove(self.get())
        self.save(hl)

    def update(self, hero_upd: dict):
        hl = self.get_list()
        h_index = hl.index(self.get())
        hl[h_index]["name"] = hero_upd["name"]
        # hl[h_index]["description"] = hero_upd["description"]
        self.name = hero_upd["name"]
        self.save(hl)

    def __repr__(self):
        return "<Hero id:{}>".format(self.hero_id)
