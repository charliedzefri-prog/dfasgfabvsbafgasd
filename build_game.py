import json, os

with open('/home/user/assets_data.json', 'r') as f:
    assets_json_str = f.read()

with open('/home/user/game_template.html', 'r') as f:
    template = f.read()

html_out = template.replace('__ASSETS_JSON__', assets_json_str)

with open('/home/user/index.html', 'w') as f:
    f.write(html_out)

print("Updated index.html written successfully! Size:", len(html_out))
