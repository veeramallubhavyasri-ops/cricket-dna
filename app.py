<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CricketDNA | AI Cricket Analytics</title>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    background: #07111f;
    color: #f1f5f9;
    font-family: Arial, sans-serif;
}

header {
    padding: 22px 7%;
    background: #0b192b;
    border-bottom: 1px solid #23364d;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 15px;
}

.logo {
    color: #42e8a5;
    font-size: 25px;
    font-weight: bold;
}

.logo span {
    color: white;
}

header p {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 5px;
}

.badge {
    color: #42e8a5;
    border: 1px solid #42e8a5;
    padding: 8px 12px;
    border-radius: 20px;
    font-size: 12px;
}

.hero {
    padding: 42px 7% 30px;
    background: linear-gradient(130deg, #102a3d, #07111f 75%);
}

.hero small {
    color: #42e8a5;
    letter-spacing: 3px;
    font-weight: bold;
}

.hero h1 {
    font-size: clamp(32px, 6vw, 54px);
    margin: 15px 0;
}

.hero h1 span {
    color: #42e8a5;
}

.hero p {
    color: #a9b9ca;
    line-height: 1.7;
    max-width: 600px;
}

.container {
    padding: 25px 7% 50px;
}

.section-title {
    margin: 25px 0 17px;
    font-size: 21px;
}

.section-title span {
    color: #42e8a5;
}

select, button {
    border: 1px solid #30465d;
    background: #102238;
    color: white;
    padding: 13px;
    border-radius: 9px;
    font-size: 14px;
}

select {
    width: 100%;
    margin: 8px 0;
}

button {
    background: #42e8a5;
    color: #07111f;
    border: none;
    font-weight: bold;
    cursor: pointer;
    margin-top: 10px;
}

button:hover {
    opacity: 0.85;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(145px, 1fr));
    gap: 15px;
}

.card {
    background: #102035;
    border: 1px solid #243950;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
}

.stat-label {
    color: #9aafc3;
    font-size: 13px;
}

.stat-value {
    font-size: 28px;
    margin: 13px 0 5px;
    font-weight: bold;
}

.green {
    color: #42e8a5;
}

.muted {
    color: #91a5b9;
    font-size: 12px;
}

.two-col {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 18px;
}

.chart-box {
    height: 280px;
    position: relative;
}

.insight {
    background: linear-gradient(120deg, #123a36, #102035);
    border: 1px solid #287e65;
    padding: 22px;
    border-radius: 15px;
    line-height: 1.8;
}

footer {
    text-align: center;
    padding: 25px;
    color: #91a5b9;
    border-top: 1px solid #243950;
    font-size: 12px;
}

.note {
    color: #f5cf79;
    font-size: 12px;
    line-height: 1.7;
    margin-top: 12px;
}

@media(max-width: 480px) {
    .hero {
        padding-top: 30px;
    }

    .container {
        padding-left: 5%;
        padding-right: 5%;
    }

    .stat-value {
        font-size: 24px;
    }
}
</style>
</head>

<body>

<header>
    <div>
        <div class="logo">🏏 Cricket<span>DNA</span></div>
        <p>INTELLIGENCE BEHIND EVERY INNING</p>
    </div>
    <div class="badge">● ANALYTICS STUDIO</div>
</header>

<section class="hero">
    <small>CRICKET × DATA × AI</small>
    <h1>Discover the <span>DNA</span><br>of Performance.</h1>
    <p>
        Explore cricket statistics, compare players and discover
        performance patterns through an interactive analytics dashboard.
    </p>
</section>

<main class="container">

    <h2 class="section-title">01 / <span>Player Explorer</span></h2>

    <div class="card">
        <label for="player">Select a player</label>
        <select id="player" onchange="updateDashboard()">
            <option value="virat">Virat Kohli</option>
            <option value="rohit">Rohit Sharma</option>
            <option value="dhoni">MS Dhoni</option>
            <option value="bumrah">Jasprit Bumrah</option>
            <option value="hardik">Hardik Pandya</option>
        </select>

        <p class="muted" id="role">Top-order batter</p>
    </div>

    <div class="grid">

        <div class="card">
            <div class="stat-label">Career Runs*</div>
            <div class="stat-value green" id="runs">850</div>
            <div class="muted">Sample dataset</div>
        </div>

        <div class="card">
            <div class="stat-label">Batting Average*</div>
            <div class="stat-value" id="average">42.5</div>
            <div class="muted">Illustrative value</div>
        </div>

        <div class="card">
            <div class="stat-label">Strike Rate*</div>
            <div class="stat-value" id="strike">138.2</div>
            <div class="muted">Illustrative value</div>
        </div>

        <div class="card">
            <div class="stat-label">Performance Index</div>
            <div class="stat-value green" id="score">82/100</div>
            <div class="muted">Demo calculation</div>
        </div>

    </div>

    <h2 class="section-title">02 / <span>Performance DNA</span></h2>

    <div class="two-col">

        <div class="card">
            <h3>Performance Profile</h3>
            <br>
            <div class="chart-box">
                <canvas id="radarChart"></canvas>
            </div>
        </div>

        <div class="card">
            <h3>Recent Match Trends</h3>
            <br>
            <div class="chart-box">
                <canvas id="lineChart"></canvas>
            </div>
        </div>

    </div>

    <h2 class="section-title">03 / <span>Player Comparison</span></h2>

    <div class="card">

        <label for="playerA">Player A</label>
        <select id="playerA">
            <option value="virat">Virat Kohli</option>
            <option value="rohit">Rohit Sharma</option>
            <option value="dhoni">MS Dhoni</option>
            <option value="bumrah">Jasprit Bumrah</option>
            <option value="hardik">Hardik Pandya</option>
        </select>

        <label for="playerB">Player B</label>
        <select id="playerB">
            <option value="rohit">Rohit Sharma</option>
            <option value="virat">Virat Kohli</option>
            <option value="dhoni">MS Dhoni</option>
            <option value="bumrah">Jasprit Bumrah</option>
            <option value="hardik">Hardik Pandya</option>
        </select>

        <button onclick="comparePlayers()">Compare Players ⚔️</button>

        <div id="comparison" style="margin-top:20px;line-height:2"></div>

    </div>

    <h2 class="section-title">04 / <span>CricketDNA Insights</span></h2>

    <div class="insight">
        <h3>🧬 Performance Lab</h3>
        <p id="insight" style="margin-top:10px">
            Select a player to explore the demonstration insights.
        </p>
        <p class="note">
            Demo only: insights are based on illustrative data.
            They are not verified player assessments or real AI predictions.
        </p>
    </div>

    <h2 class="section-title">05 / <span>Project Roadmap</span></h2>

    <div class="grid">

        <div class="card">
            <h3>📊 Data Analytics</h3>
            <p class="muted" style="margin-top:10px">
                Analyze real ball-by-ball data and player statistics.
            </p>
        </div>

        <div class="card">
            <h3>🤖 Machine Learning</h3>
            <p class="muted" style="margin-top:10px">
                Train and evaluate models using historical match data.
            </p>
        </div>

        <div class="card">
            <h3>💡 Explainable AI</h3>
            <p class="muted" style="margin-top:10px">
                Explain which input features influence a prediction.
            </p>
        </div>

    </div>

</main>

<footer>
    🏏 CricketDNA — AI Cricket Analytics Project<br><br>
    Built for learning, sports analytics and experimentation.
</footer>

<script>
const players = {
    virat: {
        name: "Virat Kohli",
        role: "Top-order batter",
        runs: 850,
        average: 42.5,
        strike: 138.2,
        score: 82,
        profile: [90, 85, 82, 78, 88],
        trend: [35, 62, 28, 75, 54, 82],
        insight: "This demonstration profile shows balanced batting metrics. With verified ball-by-ball data, the app could examine performance by venue, opponent and match situation."
    },

    rohit: {
        name: "Rohit Sharma",
        role: "Opening batter",
        runs: 790,
        average: 39.5,
        strike: 145.4,
        score: 80,
        profile: [88, 80, 92, 76, 82],
        trend: [64, 18, 79, 42, 91, 55],
        insight: "This illustrative profile emphasizes attacking batting. Real data could help measure scoring rates in different phases of an innings."
    },

    dhoni: {
        name: "MS Dhoni",
        role: "Wicketkeeper-batter",
        runs: 620,
        average: 38.7,
        strike: 135.0,
        score: 78,
        profile: [75, 89, 85, 92, 90],
        trend: [20, 47, 36, 68, 42, 76],
        insight: "This illustrative profile emphasizes finishing and pressure situations. Verified match data would be needed to evaluate those abilities."
    },

    bumrah: {
        name: "Jasprit Bumrah",
        role: "Fast bowler",
        runs: 45,
        average: 9.0,
        strike: 80.0,
        score: 88,
        profile: [92, 85, 88, 90, 82],
        trend: [2, 3, 1, 4, 2, 3],
        insight: "This demonstration profile is intended to represent bowling analysis. Bowling-specific metrics such as wickets, economy and bowling average should be used for a meaningful evaluation."
    },

    hardik: {
        name: "Hardik Pandya",
        role: "All-rounder",
        runs: 510,
        average: 30.0,
        strike: 150.0,
        score: 79,
        profile: [80, 78, 90, 75, 84],
        trend: [32, 48, 12, 65, 40, 71],
        insight: "This illustrative all-rounder profile could be extended to analyze both batting and bowling contributions using real match records."
    }
};

let radarChart;
let lineChart;

function updateDashboard() {
    const key = document.getElementById("player").value;
    const p = players[key];

    document.getElementById("role").textContent = p.role;
    document.getElementById("runs").textContent = p.runs;
    document.getElementById("average").textContent = p.average;
    document.getElementById("strike").textContent = p.strike;
    document.getElementById("score").textContent = p.score + "/100";
    document.getElementById("insight").textContent = p.insight;

    if (radarChart) radarChart.destroy();
    if (lineChart) lineChart.destroy();

    radarChart = new Chart(document.getElementById("radarChart"), {
        type: "radar",
        data: {
            labels: [
                "Consistency",
                "Adaptability",
                "Scoring",
                "Pressure",
                "Recent Form"
            ],
            datasets: [{
                label: p.name,
                data: p.profile,
                backgroundColor: "rgba(66,232,165,0.15)",
                borderColor: "#42e8a5",
                pointBackgroundColor: "#42e8a5",
                borderWidth: 2
            }]
        },
        options: {
            maintainAspectRatio: false,
            scales: {
                r: {
                    min: 0,
                    max: 100,
                    ticks: {
                        display: false,
                        stepSize: 20
                    },
                    pointLabels: {
                        color: "#cbd5e1",
                        font: { size: 10 }
                    },
                    grid: {
                        color: "#30465d"
                    },
                    angleLines: {
                        color: "#30465d"
                    }
                }
            },
            plugins: {
                legend: {
                    labels: { color: "#f1f5f9" }
                }
            }
        }
    });

    lineChart = new Chart(document.getElementById("lineChart"), {
        type: "line",
        data: {
            labels: ["Match 1", "Match 2", "Match 3", "Match 4", "Match 5", "Match 6"],
            datasets: [{
                label: "Illustrative runs / wickets",
                data: p.trend,
                borderColor: "#42e8a5",
                backgroundColor: "rgba(66,232,165,0.12)",
                fill: true,
                tension: 0.35
            }]
        },
        options: {
            maintainAspectRatio: false,
            scales: {
                x: {
                    ticks: { color: "#a9b9ca" },
                    grid: { color: "#243950" }
                },
                y: {
                    beginAtZero: true,
                    ticks: { color: "#a9b9ca" },
                    grid: { color: "#243950" }
                }
            },
            plugins: {
                legend: {
                    labels: { color: "#f1f5f9" }
                }
            }
        }
    });
}

function comparePlayers() {
    const a = players[document.getElementById("playerA").value];
    const b = players[document.getElementById("playerB").value];

    let result = "";

    if (a.name === b.name) {
        result = "Please select two different players.";
    } else {
        result = `
            <h3>${a.name} 🆚 ${b.name}</h3>
            <p>Illustrative runs: ${a.runs} vs ${b.runs}</p>
            <p>Illustrative average: ${a.average} vs ${b.average}</p>
            <p>Illustrative strike rate: ${a.strike} vs ${b.strike}</p>
            <p>Demonstration index: ${a.score} vs ${b.score}</p>
            <p class="note">
                These sample values are for demonstrating the interface,
                not verified career statistics. The metrics are not necessarily
                comparable across different player roles or formats.
            </p>
        `;
    }

    document.getElementById("comparison").innerHTML = result;
}

updateDashboard();
</script>

</body>
</html>