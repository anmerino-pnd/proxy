import httpx
from clients import API_LOCAL
from fastapi import FastAPI, Request

app = FastAPI()


@app.api_route("/proxy/{path:path}", methods=["GET", "POST", "DELETE"])
async def proxy(path: str, request: Request):
    method = request.method
    url = f"{API_LOCAL}/{path}"
    headers = dict(request.headers)
    body = await request.body()

    async with httpx.AsyncClient() as client:
        response = await client.request(method, url, headers=headers, content=body)

    return response.text  # o response.json() si sabes que es JSON
