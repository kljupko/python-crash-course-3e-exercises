import os, time, requests

url = "https://api.github.com/search/repositories"
params = {
    "q": "language:python stars:>10000",
    "sort": "stars",
    "order": "desc",
    "per_page": 30,
}

headers = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "python-crash-course-script",  # any non-empty string
}

token = os.getenv("GITHUB_TOKEN")  # optional but recommended
if token:
    headers["Authorization"] = f"Bearer {token}"

r = requests.get(url, params=params, headers=headers)
print("URL:", r.url)
print("Status:", r.status_code)
print("X-RateLimit-Remaining:", r.headers.get("X-RateLimit-Remaining"))
print("X-RateLimit-Reset:", r.headers.get("X-RateLimit-Reset"))

try:
    data = r.json()
except Exception as e:
    print("JSON decode error:", e)
    print("Body:", r.text[:500])
    raise

# Helpful on 4xx
if r.status_code >= 400:
    print("Error message:", data.get("message"))
    print("Errors:", data.get("errors"))
    raise SystemExit()

items = data.get("items", [])
print("Total repositories:", data.get("total_count"))
print("Repositories returned:", len(items))
print("First repo:", items[0]["full_name"] if items else "—")

