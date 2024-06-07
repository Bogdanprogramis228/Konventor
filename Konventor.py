import yaml
import json
import argparse

def yaml_to_json(yaml_file, json_file):
    with open(yaml_file, 'r') as yf:
        data = yaml.safe_load(yf)
    
    with open(json_file, 'w') as jf:
        json.dump(data, jf, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Конвертер YAML у JSON")
    parser.add_argument("yaml_file", help="Вхідний YAML файл")
    parser.add_argument("json_file", help="Вихідний JSON файл")
    
    args = parser.parse_args()
    
    yaml_to_json(args.yaml_file, args.json_file)
    print(f"Конвертація завершена. JSON файл збережено як {args.json_file}")

#  python Konventor.py input.yaml output.json