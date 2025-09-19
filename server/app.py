# server/app.py
#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return jsonify({'message': 'Flask SQLAlchemy Lab 1'}), 200

# --- Views ---

# GET /earthquakes/<int:id> — single quake by ID (200 or 404)
@app.route('/earthquakes/<int:id>')
def get_earthquake(id):
    quake = Earthquake.query.get(id)
    if not quake:
        return jsonify({"message": f"Earthquake {id} not found."}), 404
    return jsonify({
        "id": quake.id,
        "magnitude": quake.magnitude,
        "location": quake.location,
        "year": quake.year
    }), 200

# GET /earthquakes/magnitude/<float:magnitude> — quakes with magnitude >= threshold
@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    quakes = (
        Earthquake.query
        .filter(Earthquake.magnitude >= magnitude)
        .order_by(Earthquake.magnitude.desc(), Earthquake.id.asc())
        .all()
    )

    return jsonify({
        "count": len(quakes),
        "quakes": [
            {
                "id": q.id,
                "magnitude": q.magnitude,
                "location": q.location,
                "year": q.year
            } for q in quakes
        ]
    }), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)

