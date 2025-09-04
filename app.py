# ACEest Fitness & Gym - Flask adaptation of the provided local app
# Provides simple workout tracking API (in-memory)
from flask import Flask, request, jsonify, abort

def create_app():
    app = Flask(__name__)

    # Simple in-memory store (cleared on restart)
    app.config.setdefault("WORKOUTS", [])

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), 200

    @app.route("/workouts", methods=["POST"])
    def add_workout():
        data = request.get_json(silent=True) or {}
        if "workout" not in data or "duration" not in data:
            return jsonify({"error": "workout and duration are required"}), 400
        # Validate duration
        try:
            duration = int(data["duration"])
        except (ValueError, TypeError):
            return jsonify({"error": "duration must be an integer"}), 400

        entry = {
            "id": len(app.config["WORKOUTS"]) + 1,
            "workout": data["workout"],
            "duration": duration
        }
        app.config["WORKOUTS"].append(entry)
        return jsonify(entry), 201

    @app.route("/workouts", methods=["GET"])
    def list_workouts():
        return jsonify(app.config["WORKOUTS"]), 200

    @app.route("/workouts/<int:w_id>", methods=["GET"])
    def get_workout(w_id):
        items = app.config["WORKOUTS"]
        for w in items:
            if w["id"] == w_id:
                return jsonify(w), 200
        abort(404)

    return app

app = create_app()

if __name__ == "__main__":
    # Development server
    app.run(host="0.0.0.0", port=5000)
