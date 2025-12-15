import yaml, os

def read_config():
    config_file_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
    with open(config_file_path, "r") as config_data:
        return yaml.safe_load(config_data)