import bonobo
import pickle
import hashlib
from diskcache import Cache
from time import sleep
from tqdm import tqdm 

def hash(data):
    m = hashlib.sha256()
    m.update(pickle.dumps(data))
    return m.hexdigest()

cache = Cache("pipeline")
def cached(func):
    def wrapper_cached(*args, **kwargs):
        key = hash(hash(func.__name__) +hash(args) + hash(kwargs) )
        if key in cache:
            return cache[key]
        else:
            value = func(*args, **kwargs)
            cache[key]=value
        return value 
    return wrapper_cached


def generate_data():
    for x in range(10000):
        yield 'foo'
    
@cached
def uppercase(x: str):
    sleep(1)
    return x.upper()

def output(x: str):
    pass
    #print(x)
    
graph = bonobo.Graph(
    generate_data,
    uppercase,
    output,
)

if __name__ == '__main__':
    bonobo.run(graph)