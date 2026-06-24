# A2RL Drone Racing Simulation

**Team:** Simulation Team  
**Competition:** Abu Dhabi Autonomous Racing League (A2RL)  
**Simulator:** Crazyflow (JAX-based drone physics simulator)  

---

## System Requirements

| Requirement | Details |
|---|---|
| Operating System | Windows 10/11 (64-bit) or Ubuntu Linux 20.04+ |
| Python Version | 3.11 exactly |
| RAM | Minimum 8GB recommended |
| GPU | Not required for simulation (CPU is sufficient) |
| Internet | Required for initial installation |

---

## Installation — Windows

### Step 1 Enable Long Path Support
1. Press Win + R, type regedit, right-click → Run as administrator
2. Navigate to: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
3. Double-click LongPathsEnabled, change value from 0 to 1
4. Restart your computer

### Step 2  Install Python 3.11
Download from: https://www.python.org/downloads/release/python-3113/
- Choose Windows installer (64-bit)
- Check "Add Python to PATH" during installation

### Step 3 Create Virtual Environment
```bash
py -3.11 -m venv crazyflow-env
"C:\Users\YourName\crazyflow-env\Scripts\activate"
```

### Step 4  Install Crazyflow
```bash
pip install crazyflow
```

### Step 5  Clone and Install
```bash
git clone https://github.com/singularit-drone-wing/A2RL_Simulation.git
cd A2RL_Simulation
pip install -e .
```

---

## Installation  Linux (Ubuntu)

```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-pip git -y
python3.11 -m venv crazyflow-env
source crazyflow-env/bin/activate
pip install crazyflow
git clone https://github.com/singularit-drone-wing/A2RL_Simulation.git
cd A2RL_Simulation
pip install -e .
```

---

## Running the Simulation

```bash
python scripts/sim.py --config level0.toml
```

## Running IMU Simulation

```bash
python imu_simulation.py
```

---

## Difficulty Levels

| Level | Config File | Description |
|---|---|---|
| 0 | level0.toml | Fixed gates, easiest |
| 1 | level1.toml | Slightly randomized |
| 2 | level2.toml | Randomized gate positions |
| 3 | level3.toml | Full randomization, hardest |

---

## Official A2RL Track Specifications(to be confirmed)

| Specification | Details |
|---|---|
| Arena size | 100m x 30m |
| Number of gates | 11 |
| Gate outer size | 2.13m x 2.13m |
| Gate inner opening | 1.52m x 1.52m |
| Gate design | High contrast color coded |
| Drag race format | 83m straight with 4 sequential gates |

---

## Team Task Breakdown

| Task | Assignee | Status |
|---|---|---|
| Simulation Environment Setup | Ivana Anto |  Done |
| IMU Simulation | Ivana Anto | Done |
| Camera Simulation | Ivana Anto |  In Progress |
| A2RL Race Track 3D Environment | Anjela Joseph |  In progress |

---

## Known Issues

| Issue | Fix |
|---|---|
| SSL Certificate Error | Use mobile hotspot or trusted host flags |
| Long Path error on Windows | Enable LongPathsEnabled in registry |
| Warp import warnings | Safe to ignore |
| Level 2/3 drone crashes | Expected  default controller limitation |
