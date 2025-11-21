"""
Generate markdown documents for each team
"""
import sys

from jinja2 import Environment
from ruamel.yaml import YAML

yaml = YAML()

TEMPLATE = """
# {{ name }}

{{ description }}

## Requirements

This team is defined as a {{ charter }} team.

{{ requirements or "No requirements specified." }}

## Members
{% for member in members %}
* [@{{ member }}](https://github.com/{{ member }})
{%- endfor %}
{%- if emeritus %}
* Emeritus:
{%- for member in emeritus %}
  * [@{{ member }}](https://github.com/{{ member }})
{%- endfor %}
{%- endif %}

## Resources

This team has write access to these repositories:
{% for repo in scopes["codeowners"] %}
* [`{{ repo }}`](https://github.com/{{ repo }})
{%- endfor %}
{% if scopes["other"] %}
Additionally, it controls these other resources:
{% for other in scopes["other"] %}
* {{ other }}
{%- endfor %}
{%- endif %}
{%- if links %}

## Links
{% for link in links %}
* {{ link }}
{%- endfor %}
{%- endif %}
"""

yml_path = sys.argv[1]
with open(yml_path) as f:
    data = yaml.load(f)
env = Environment()
tpl = env.from_string(TEMPLATE)
print(tpl.render(data))
