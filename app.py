from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    if request.method == "POST":
        try:
            num = int(request.form.get("number"))
            for i in range(1, 11):
                output += f"{num} x {i} = {num * i}<br>"
        except:
            output = "Please enter a valid number!"

    return f"""
    <html>
    <head>
        <title>Multiplication Table</title>
    </head>
    <body style="font-family: Arial; padding: 30px;">
        <h2>Enter a number to generate its table</h2>
        <form method="POST">
            <input type="number" name="number" placeholder="Enter number" required>
            <button type="submit">Generate</button>
        </form>
        <h3>{output}</h3>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
