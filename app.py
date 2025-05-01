from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/reservation", methods=["POST"])
def reservation():
    data = request.json
    return jsonify({
        "message": "Réservation enregistrée",
        "données": data
    })

if __name__ == "__main__":
    app.run(debug=True)
