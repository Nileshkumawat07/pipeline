from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DevOps Automation Journey</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Segoe UI", Arial, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            min-height: 100vh;
            color: #ffffff;
        }

        .container {
            width: 90%;
            max-width: 1100px;
            margin: 40px auto;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(12px);
            border-radius: 18px;
            padding: 40px;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.45);
        }

        h1 {
            text-align: center;
            font-size: 3rem;
            margin-bottom: 10px;
        }

        .subtitle {
            text-align: center;
            font-size: 1.1rem;
            opacity: 0.85;
            margin-bottom: 40px;
        }

        .steps {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 25px;
        }

        .card {
            background: rgba(255, 255, 255, 0.12);
            padding: 25px;
            border-radius: 16px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        }

        .step {
            font-size: 0.85rem;
            letter-spacing: 1px;
            color: #00e6ff;
            margin-bottom: 8px;
            font-weight: bold;
        }

        .card h2 {
            font-size: 1.5rem;
            margin-bottom: 12px;
        }

        .card p {
            font-size: 0.95rem;
            line-height: 1.6;
            opacity: 0.9;
        }

        .flow {
            margin-top: 45px;
            padding: 25px;
            border-radius: 14px;
            background: rgba(0, 0, 0, 0.25);
            text-align: center;
            font-size: 1rem;
        }

        .flow span {
            color: #00e6ff;
            font-weight: bold;
        }

        footer {
            margin-top: 40px;
            text-align: center;
            font-size: 0.85rem;
            opacity: 0.7;
        }
    </style>
</head>
<body>

<div class="container">
    <h1> CI/CD  Automation  by nilesh </h1>
    <p class="subtitle">From Code Commit to Cloud– Fully Automated</p>

    <div class="steps">

        <div class="card">
            <div class="step">STEP 1</div>
            <h2>Write Application Code</h2>
            <p>
                The journey starts by writing applicatio code (Python / Flask).
                This code is stored in a GitHub repository so that every change
                can be tracked and versioned.
            </p>
        </div>

        <div class="card">
            <div class="step">STEP 2</div>
            <h2>Push Code to GitHub</h2>
            <p>
                When the developer pushes code to GitHub, it becomes the
                single source of truth. This push event triggers the
                automation pipeline.
            </p>
        </div>

        <div class="card">
            <div class="step">STEP 3</div>
            <h2>Jenkins CI Trigger</h2>
            <p>
                GitHub Webhook automatically notifies Jenkins.
                Jenkins starts the pipeline without any manual intervention.
            </p>
        </div>

        <div class="card">
            <div class="step">STEP 4</div>
            <h2>Build Docker Image</h2>
            <p>
                Jenkins builds a Docker image using a Dockerfile.
                This ensures the application runs the same everywhere.
            </p>
        </div>

        <div class="card">
            <div class="step">STEP 5</div>
            <h2>Push Image to Docker Hub</h2>
            <p>
                Jenkins securely logs into Docker Hub using an access token
                and pushes the image to a remote container registry.
            </p>
        </div>

        <div class="card">
            <div class="step">STEP 6</div>
            <h2>Deploy on AWS EC2</h2>
            <p>
                The Docker image is pulled on an EC2 server and run as a
                container. The app runs 24×7 independent of the developer machine.
            </p>
        </div>

        <div class="card">
            <div class="step">STEP 7</div>
            <h2>Access via Browser</h2>
            <p>
                The application is exposed on a port and accessed using
                the EC2 public IP directly from a browser.
            </p>
        </div>

        <div class="card">
            <div class="step">STEP 8</div>
            <h2>Future Code Changes</h2>
            <p>
                For any new change, the developer only pushes code again.
                The entire pipeline runs automatically from start to end.
            </p>
        </div>

    </div>

    <div class="flow">
        <span>GitHub</span> → <span>Jenkins</span> → <span>Docker Build</span> →
        <span>Docker Hub</span> → <span>AWS EC2</span> → <span>Browser</span>
    </div>

    <footer>
        <p>Automated using Flask • Docker • Jenkins • Docker Hub • AWS EC2</p>
    </footer>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
