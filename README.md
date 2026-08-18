# 🚀 PlacementReady - Engineering Placement Preparation & Diagnostic Platform

A web platform built specifically for engineering students to evaluate, benchmark, and accelerate their placement readiness across:
1. **📄 ATS Resume & JD Matcher**: Scores ATS compatibility, identifies missing role keywords, and turns weak bullet points into high-impact STAR-format achievements.
2. **🎯 Skill Gap Matrix**: Interactive Spider/Radar chart comparing student skills against industry benchmarks for SDE-1, Full Stack, Data Analyst, ML Engineer, and DevOps roles.
3. **🚀 Project Portfolio Auditor**: Evaluates architectural complexity (caching, Docker, authentication, automated testing, cloud deployment) and suggests high-impact upgrades.
4. **💻 Coding & DSA Playground**: Topic-wise coding challenges with an in-browser code editor, Python sandbox execution, test cases, and time/space complexity analysis.
5. **🎙️ AI Mock Interview Studio**: Interactive HR (STAR method) and Technical rounds with Text-to-Speech questions, voice recording, instant AI scoring, and benchmark model answers.
6. **📊 Placement Readiness Index (PRI) Dashboard**: Holistic 0–100 score + 60-day personalized sprint roadmap and one-click exportable summary report.

---

## 🏃 How to Run the Platform

### Option 1: Python Local Server (Recommended)
Open your terminal in the project directory and run:
```bash
python backend/server.py
```
Then navigate to: **`http://localhost:8000`** in your browser.

### Option 2: Direct In-Browser (Zero Dependencies)
You can directly open `frontend/index.html` in any modern web browser (Chrome, Edge, Firefox, Safari). All features include automatic client-side fallback engines for analysis, chart rendering, and interview scoring.

---

## 📁 Project Architecture

```
placement-ready-platform/
├── backend/
│   ├── server.py              # REST API server & sandbox execution handler
│   └── data.json              # Benchmark databases (Roles, DSA, Interviews, Blueprints)
├── frontend/
│   ├── index.html             # Complete single-page application
│   ├── css/
│   │   └── style.css          # Glassmorphism, animations, print/PDF styles
│   └── js/
│       └── app.js             # State management, Chart.js radar, voice AI & ATS engine
└── README.md
```
