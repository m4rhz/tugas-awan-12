from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Hidup adalah perjuangan yang indah.",
    "Sukses adalah perjalanan, bukan tujuan.",
    "Tetap rendah hati dan terus belajar.",
    "Mimpi besar dimulai dari langkah kecil.",
    "Positif selalu lebih baik daripada negatif."
]

@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
