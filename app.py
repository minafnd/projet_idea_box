from flask import Flask, request, render_template, redirect, flash, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    event_date = db.Column(db.Date, nullable = False)
    event_type = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable = False)
    location = db.Column(db.String(100), nullable = False)
    created_at = db.Column(db.Date, default=db.func.current_date())

    def __repr__(self):
        return f"Event('{self.title}', '{self.event_date}', '{self.event_type}', '{self.description}', '{self.location}', '{self.created_at}')"

with app.app_context(): 
    db.create_all()

@app.route("/")
def accueil():
    return render_template("accueil.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method== "POST": 
        title = request.form.get("title", "")
        event_date_str = request.form.get("event_date", "")
        event_type = request.form.get("event_type", "")
        description = request.form.get("description", "")
        location = request.form.get("location", "")

        errors = []

        if not title:
            errors.append("Merci de renseigner le titre de l'évent.")
        if not event_date_str: 
            errors.append("Merci de renseigner la date de l'évent")
        if not event_type:
            errors.append("Merci de renseigner le type de l'évent.")
        if not description:
            errors.append("Merci de donner une description à votre évent.")
        if not location:
            errors.append("Merci de préciser le lieu de l'évent.")

        if errors:
            for error in errors:
                flash(error, "error")
            return redirect("/form")
        
        event_date = datetime.strptime(event_date_str, '%Y-%m-%d').date() #j'ai du transformer le format de la date pour qu'elle puisse être sauvegardée en format date dans ma BDD
        
        entry = Event(title=title, event_date=event_date, event_type=event_type, description=description, location=location)
        db.session.add(entry)
        db.session.commit()

        flash("L'évènement a bien été créé ! 📅 ", "success")
        return render_template('form.html', title=title, event_date=event_date, event_type=event_type, description=description, location=location)
    
    return render_template("form.html")

@app.route("/events")
def events():
    entries = Event.query.all()
    return render_template("events.html", entries = entries)

@app.route("/delete-event/<int:event_id>")
def delete_event(event_id):
    entry = Event.query.get(event_id)
    if not entry:
        flash("Entrée d'historique non trouvée", "error")
        return redirect(url_for("events"))
    db.session.delete(entry)
    db.session.commit()
    flash("Evenement supprimée avec succès", "success")
    return redirect(url_for("events"))

@app.route("/events/<date>", methods = ["GET"])
def list_events(date):
    chosen_date = datetime.strptime(date, '%Y-%m-%d').date()
    events = (
        db.session.query(Event)
        .filter(Event.event_date >= chosen_date)
        .order_by(Event.event_date.asc())
        .limit(5)
        .all()
    ) 
    clean_event = []

    for event in events:
        clean_event.append({
        "id": event.id,
        "title": event.title,
        "type": event.event_type,
        "date": event.event_date,
        "description": event.description,
        "event": event.location,
        })

    return jsonify({
        "event":clean_event
    })

if __name__ == "__main__":
    app.run(debug=True)
