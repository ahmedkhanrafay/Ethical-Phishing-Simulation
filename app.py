from flask import Flask, render_template, request, redirect, url_for
from database import init_db, get_connection

app = Flask(__name__)

init_db()


@app.route("/")
def dashboard():
    conn = get_connection()

    campaigns = conn.execute(
        "SELECT COUNT(*) FROM campaigns"
    ).fetchone()[0]

    emails_sent = conn.execute(
        "SELECT COUNT(*) FROM events WHERE event_type = 'EMAIL_SENT'"
    ).fetchone()[0]

    clicks = conn.execute(
        "SELECT COUNT(*) FROM events WHERE event_type = 'LINK_CLICKED'"
    ).fetchone()[0]

    training = conn.execute(
        "SELECT COUNT(*) FROM events WHERE event_type = 'TRAINING_INTERACTION'"
    ).fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        campaigns=campaigns,
        emails_sent=emails_sent,
        clicks=clicks,
        training=training
    )


@app.route("/campaigns")
def campaigns():
    conn = get_connection()

    campaigns = conn.execute(
        "SELECT * FROM campaigns ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template(
        "campaigns.html",
        campaigns=campaigns
    )


@app.route("/create-campaign", methods=["GET", "POST"])
def create_campaign():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()

        if name:
            conn = get_connection()

            conn.execute(
                """
                INSERT INTO campaigns (name, description)
                VALUES (?, ?)
                """,
                (name, description)
            )

            conn.commit()
            conn.close()

        return redirect(url_for("campaigns"))

    return render_template("create_campaign.html")


@app.route("/recipients")
def recipients():
    return render_template("recipients.html")


@app.route("/education")
def education():
    return render_template("education.html")


@app.route("/analytics")
def analytics():
    conn = get_connection()

    sent = conn.execute(
        "SELECT COUNT(*) FROM events WHERE event_type = 'EMAIL_SENT'"
    ).fetchone()[0]

    opened = conn.execute(
        "SELECT COUNT(*) FROM events WHERE event_type = 'TRAINING_PAGE_VISITED'"
    ).fetchone()[0]

    clicked = conn.execute(
        "SELECT COUNT(*) FROM events WHERE event_type = 'LINK_CLICKED'"
    ).fetchone()[0]

    training = conn.execute(
        "SELECT COUNT(*) FROM events WHERE event_type = 'TRAINING_INTERACTION'"
    ).fetchone()[0]

    completed = conn.execute(
        "SELECT COUNT(*) FROM events WHERE event_type = 'CAMPAIGN_COMPLETED'"
    ).fetchone()[0]

    conn.close()

    open_rate = (opened / sent * 100) if sent else 0
    click_rate = (clicked / sent * 100) if sent else 0
    completion_rate = (completed / sent * 100) if sent else 0

    return render_template(
        "analytics.html",
        sent=sent,
        opened=opened,
        clicked=clicked,
        training=training,
        open_rate=round(open_rate, 1),
        click_rate=round(click_rate, 1),
        completion_rate=round(completion_rate, 1)
    )


@app.route("/send-simulation", methods=["GET", "POST"])
def send_simulation():
    if request.method == "POST":
        campaign_id = request.form.get("campaign_id")
        recipient_id = request.form.get("recipient_id")

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO events
            (campaign_id, recipient_id, event_type)
            VALUES (?, ?, ?)
            """,
            (
                campaign_id,
                recipient_id,
                "EMAIL_SENT"
            )
        )

        conn.commit()
        conn.close()

        return redirect(url_for("simulated_email"))

    return render_template("send_simulation.html")


@app.route("/simulated-email")
def simulated_email():
    return render_template("simulated_email.html")


@app.route("/simulation")
def simulation():
    conn = get_connection()

    campaign = conn.execute(
        "SELECT id FROM campaigns ORDER BY id DESC LIMIT 1"
    ).fetchone()

    recipient = conn.execute(
        "SELECT id FROM recipients ORDER BY id DESC LIMIT 1"
    ).fetchone()

    if campaign and recipient:

        already_visited = conn.execute(
            """
            SELECT 1 FROM events
            WHERE campaign_id = ?
            AND recipient_id = ?
            AND event_type = 'TRAINING_PAGE_VISITED'
            LIMIT 1
            """,
            (
                campaign[0],
                recipient[0]
            )
        ).fetchone()

        if not already_visited:
            conn.execute(
                """
                INSERT INTO events
                (campaign_id, recipient_id, event_type)
                VALUES (?, ?, ?)
                """,
                (
                    campaign[0],
                    recipient[0],
                    "TRAINING_PAGE_VISITED"
                )
            )

            conn.commit()

    conn.close()

    return render_template("simulation.html")


@app.route("/track/<event_type>")
def track_event(event_type):

    allowed_events = {
        "LINK_CLICKED",
        "TRAINING_INTERACTION",
        "CAMPAIGN_COMPLETED"
    }

    if event_type not in allowed_events:
        return "Invalid event", 400

    conn = get_connection()

    campaign = conn.execute(
        "SELECT id FROM campaigns ORDER BY id DESC LIMIT 1"
    ).fetchone()

    recipient = conn.execute(
        "SELECT id FROM recipients ORDER BY id DESC LIMIT 1"
    ).fetchone()

    if campaign and recipient:

        conn.execute(
            """
            INSERT INTO events
            (campaign_id, recipient_id, event_type)
            VALUES (?, ?, ?)
            """,
            (
                campaign[0],
                recipient[0],
                event_type
            )
        )

        conn.commit()

    conn.close()

    if event_type == "LINK_CLICKED":
        return redirect(url_for("simulation"))

    if event_type == "TRAINING_INTERACTION":
        return redirect(url_for("education"))

    return redirect(url_for("analytics"))


if __name__ == "__main__":
    app.run(debug=True)