from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from generate import generate_content
import uvicorn


app = FastAPI()


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>marketing content</title>
    </head>
    <body>
        <h1>Get your Marketing Content!!</h1>
        <form id="urlForm" onsubmit="generateContent(event)">
            <input type="text" id="format" placeholder="Enter the format" autocomplete="off"/>
            <input type="text" id="topic" placeholder="Enter the topic" autocomplete="off"/>
            <button type="submit">submit</button>
        </form><br><br>
        <div id="content">
        </div>
        <script>
            
            function generateContent(event) {
                event.preventDefault();
                alert("Please wait few seconds...")
                var format = document.getElementById("format").value;
                var topic = document.getElementById("topic").value;
                var data = { "format": format, "topic":topic };
                fetch("/generateContent", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(data)
                })
                .then(response => {
                    if (!response.ok) {
                    throw new Error('Network response was not ok');
                    }
                    // Parse the response body as JSON
                    return response.json(); 
                })
                .then(data => {
                console.log(data)
                console.log(typeof data)
                        var contentDiv = document.getElementById("content");
                        var paragraph = document.createElement("p");
                        paragraph.textContent = data;
                        contentDiv.innerHTML = "";
                        contentDiv.appendChild(paragraph);
                })
                .catch(error => console.error("Error:", error));
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.post("/generateContent")
async def set_url(request: Request):
    data = await request.json()
    format = data["format"]
    topic = data["topic"]

    result = generate_content(topic=topic, format=format)
    print(result)
    return JSONResponse(content=result)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8016)
