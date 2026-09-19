# Experiment: JSON

import json

user = {
    "name": "Jahid",
    "skills": ["Python", "Go", "C++", "GenAI"],
    "learning": True,
}

json_data = json.dumps(user, indent=2)
print(json_data)

parsed_data = json.loads(json_data)
print(parsed_data["skills"])
