import json
import os

class TestConfig:
    def __init__(self, path="testparams.json"):
        with open(path, "r") as f:
            self.params = json.load(f)

    def __getattr__(self, item):
        return self.params.get(item)


