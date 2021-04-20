import yaml


def reader(file):
    with open(file, "r") as f:
        try:
            return yaml.load(f)
        except yaml.YAMLError as exc:
            return exc
