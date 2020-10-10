import requests
from tqdm import tqdm

url = "http://www.greenteapress.com/thinkpython/thinkpython.pdf"

chunk_s = 512

r = requests.get(url, stream=False)
# stream allows us to download only the request headers till this time without downloading the complete request body
# r.content

print(r.headers)

iteration = int(r.headers['content-length'])/chunk_s
print(iteration)

# list(r.iter_content(chunk_size=chunk_s))
# tqdm(r.iter_content(chunk_size=chunk_s),total=iteration)

with open("python.pdf", "wb") as f:
    for chunk in tqdm(r.iter_content(chunk_size=chunk_s), total=iteration):
        f.write(chunk)
