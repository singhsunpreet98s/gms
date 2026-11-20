import constants;
import json;
from pathlib import Path;
import os;
class JsonRepository:
    def __init__(self, collection):
        
        self.ids = [];
        db_path = Path(f"{Path.cwd()}/{constants.DEFAULT_SCHEMA_FOLDER}")

        db_path.mkdir(parents=True, exist_ok=True);
        self.path = f"{db_path}/{collection}.json";
        self.load_data();

    def load_data(self):
        path = Path(self.path);
        if path.exists():
            with open(self.path,'r') as file:
                        self.list = json.load(file);
        else:
             self.list = {"index":1, "data": []}
             self.save();
    def add(self, data):
        data.id = self.list['index'];
        self.ids.append(data.id);
        self.list['data'].append(data.__dict__);
        self.list['index'] += 1;
        return data;

    def get_all(self):
        return self.list['data'];

    def get_by_id(self,id):
         return next((item for item in self.list['data'] if item['id'] == id), None )

    def save(self):
        with open(self.path,'w') as dest:
            json.dump(self.list, dest, indent=4)
        return_data = self.ids;
        self.ids = [];
        return return_data;

    def remove(self,id):
        self.list['data'] = [data for data in self.list['data'] if data["id"] != id]

    def update(self,data):
        for entry in self.list['data']:
            if entry['id'] == data.id:
                entry.update(data.__dict__);





