#create a json file

import json

f = open("data.json","w")

content = [{"name":"arun","age":20},{"name":"alan","age":24}]

json.dump(content,f)
f.close()