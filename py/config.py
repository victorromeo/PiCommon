import json

class Config:
    def __init__(self, config_path:str = None):
        self.config_path = config_path
        self.config = {}
        if config_path is not None:
            self.ReadFromFile(self.config_path)

    def ReadFromFile(path:str):
        with open(path, 'r') as file:
            data = file.read()
            self.Read(data)

    def Read(self, data:str):
        self.config = json.load(data)

    def WriteToFile(self, path:str):
        with open(path, 'w') as file:
            file.write(self.Write())

    def Write():
        return json.dump(self, self.config)

    def Add(self, key:str, value):
        self.config[key.strip()] = value

    def Remove(self, key:str):
        self.config.pop(key)

    def Get():
        return json.dumps(self.config, sort_keys = self.sort_keys, indent = self.indent)
 
