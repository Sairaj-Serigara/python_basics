import multiprocessing
import requests

def donlfile(url, name):
    print("started downloading")
    response = requests.get(url)
    open(f"sile/file{name}", "wb").write(response.content)
    print("finished downloading")

if __name__ == "__main__":   # 👈 required on Windows
    url = "https://picsum.photos/300/200"
    pros = []

    for i in range(5):
        p = multiprocessing.Process(target=donlfile, args=(url, i))
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
