import aiohttp
import asyncio
from flask import Flask,jsonify
import json

class datas():
    def __init__(self,id,name) -> None:
        self.id = id
        self.name = name
    
    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': f'{self.name}'
        }

urls = ['http://localhost:5555/url1',
        'http://localhost:5555/url2',
        'http://localhost:5555/url3']

app = Flask(__name__)

async def fetch_url(session, url):
    try:
        response = await session.get(url,timeout=4)
        text =await response.text()
        return text
    except Exception as e:
        return 'error'


def generate_json(fr,to):
    list = []
    for i in range(fr,to,1):
        list.append(datas(i, f'Test {i}') )
    return list    

def dump_list_to_json(items):
    return json.dumps(items, default = lambda x: x.__dict__)

@app.route('/url1')
def url1():
    item1 = generate_json(1,10)
    item2 = generate_json(31,40)

    return jsonify([e.serialize() for e in item1+item2])

@app.route('/url2')
def url2():
    item1 = generate_json(11,20)
    item2 = generate_json(41,50)
    return jsonify([e.serialize() for e in item1+item2])

@app.route('/url3')
def url3():
    item1 = generate_json(21,30)
    item2 = generate_json(51,60)
    return jsonify([e.serialize() for e in item1+item2])

@app.route('/')
async def async_get_urls_v2():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch_url(session, url))
            tasks.append(task)
        sites = await asyncio.gather(*tasks)

    list =[]
    for site in sites:
        if not 'error' in site:
            items = json.loads(site.strip())
            for item in items:
                list.append(datas(item['id'],item['name']) )

    list_sorted  = sorted(list)
    return jsonify([e.serialize() for e in list_sorted])

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False, host='localhost', port=5555)