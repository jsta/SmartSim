
from os import path, mkdir

class Target:

    def __init__(self, name, params, experiment_name, target_dir_path):
        self.name = name
        self.params = params
        self._experiment = experiment_name
        self._path = target_dir_path
        self._models = {}


    def get_target_params(self):
        return self.params

    def get_target_dir(self):
        return self._path

    def get_models(self):
        return self._models

    def get_model(self, model_name):
        return self._models[model_name]

    def get_control_settings(self):
        return self._ctrl_settings

    def add_model(self, model):
        self._models[model.name] = model

    def set_control_settings(self, settings):
        self._ctrl_settings = settings

        
    def __str__(self):
        return self.name
    
