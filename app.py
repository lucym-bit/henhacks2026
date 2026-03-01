import imports as I
import os
from main import risk_factor as risk

app = I.Flask(__name__)
PLOT_DIR = os.path.join("static", "plots")
os.makedirs(PLOT_DIR, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    state_risk = None
    national_risk = None
    plot_path = None

    if I.request.method == "POST":
        state = I.request.form["state"]
        try:
            state_risk, national_risk = risk(state)

            # Generate plot
            I.plt.figure(figsize=(6, 4))
            I.plt.bar(["State", "National Avg"], [state_risk, national_risk], color=["blue", "orange"])
            I.plt.ylabel("Cancer Risk per 100,000")
            I.plt.title(f"Cancer Risk for {state.upper()} vs National Avg")
            I.plt.tight_layout()

            plot_path = os.path.join(PLOT_DIR, f"{state.upper()}_risk.png")
            I.plt.savefig(plot_path)
            I.plt.close()
        except Exception as e:
            state_risk = str(e)

    return I.render_template(
        "index.html",
        state_risk=state_risk,
        national_risk=national_risk,
        plot_path=plot_path
    )


if __name__ == "__main__":
    app.run(debug=True)
