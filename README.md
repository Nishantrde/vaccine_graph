# COVID-19 Pandemic Simulation (Dec 2019 - 2025)

An interactive, real-time simulation of the COVID-19 pandemic using the SEIR epidemiological model with actual WHO/CDC data.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Features

- **Interactive Timeline**: Scrub through the entire COVID-19 pandemic (Dec 2019 - 2025)
- **Real-Time Visualization**: Watch disease spread, vaccination rollout, and variant waves
- **SEIR Model**: Scientifically accurate epidemiological modeling
- **Herd Immunity Tracking**: Live calculation based on R₀ values
- **Verified Sources**: Click any event to open WHO/CDC documentation
- **Multiple Variants**: Original, Alpha, Delta, Omicron, and subvariants

## 📊 Dashboard Components

### 🛡️ Herd Immunity Panel

**What is Herd Immunity?**

Herd immunity occurs when enough people become immune (through vaccination or recovery) that the virus can no longer spread effectively.

**Formula:**
```
Herd Immunity Threshold = 1 - (1/R₀)
```

| Variant | R₀ | Threshold |
|---------|-----|-----------|
| Original (Wuhan) | 2.5 | 60% |
| Alpha | 3.5 | 71% |
| Delta | 6.0 | 83% |
| Omicron | 10-18 | 90-94% |

### Population Status (SEIR Model)

| Compartment | Color | Description |
|-------------|-------|-------------|
| **Susceptible** | 🔵 Blue | Can get infected |
| **Exposed** | 🟡 Yellow | Infected, not yet contagious |
| **Infected** | 🔴 Red | Sick & contagious |
| **Recovered** | 🟢 Green | Natural immunity (temporary) |
| **Vaccinated** | 🟣 Purple | Vaccine-induced immunity |
| **Deceased** | ⚫ Gray | Died from disease |

### Key Metrics

| Metric | Description |
|--------|-------------|
| **R₀ (COVID)** | Reproduction number - >1 means spreading |
| **COVID Infected** | Currently active infections (%) |
| **COVID Deaths** | Cumulative mortality (%) |
| **Vaccinated** | Population with vaccine protection |
| **Recovered** | Population with natural immunity |
| **Awareness** | Public health awareness level |
| **Hesitancy** | Vaccine hesitancy rate |

### Timeline Events

Major COVID-19 milestones with verified WHO/CDC sources:
- First cases in Wuhan (Dec 2019)
- WHO Pandemic Declaration (Mar 2020)
- Variant emergences (Alpha, Delta, Omicron)
- Vaccine approvals and rollouts
- Policy changes and emergency endings

## 🎮 Controls

| Key | Action |
|-----|--------|
| `SPACE` | Play/Pause simulation |
| `←` `→` | Step backward/forward |
| `R` | Reset to beginning |
| `F11` | Toggle fullscreen |
| `ESC` | Exit fullscreen / Quit |
| `Mouse Drag` | Scrub through timeline |
| `Click Event` | Open WHO/CDC source link |

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/vaccine.git
cd vaccine

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Dependencies

```
pygame>=2.0.0
numpy>=1.20.0
```

## �� Usage

```bash
# Activate virtual environment
source venv/bin/activate

# Run the simulation
python interactive_simulation.py
```

## 📈 The SEIR Model

The simulation uses the **SEIR** (Susceptible-Exposed-Infected-Recovered) compartmental model:

```
S → E → I → R
↓       ↓
V       D
```

**Differential Equations:**
```
dS/dt = -βSI/N - vaccination_rate
dE/dt = βSI/N - σE
dI/dt = σE - γI
dR/dt = γI(1 - IFR)
dD/dt = γI × IFR
dV/dt = vaccination_rate × S
```

Where:
- **β** = transmission rate (R₀ × γ)
- **σ** = rate of progression from exposed to infected (1/latent period)
- **γ** = recovery rate (1/infectious period)
- **IFR** = Infection Fatality Rate

## 📚 Data Sources

All data is based on official WHO and CDC publications:

- [WHO COVID-19 Dashboard](https://covid19.who.int/)
- [WHO Variant Tracking](https://www.who.int/activities/tracking-SARS-CoV-2-variants)
- [CDC COVID Data Tracker](https://covid.cdc.gov/covid-data-tracker/)
- [Our World in Data - Vaccinations](https://ourworldindata.org/covid-vaccinations)

## 🔬 COVID-19 Parameters Used

| Parameter | Value | Source |
|-----------|-------|--------|
| Original R₀ | 2.5 | WHO |
| Delta R₀ | 5-6 | CDC |
| Omicron R₀ | 10-18 | WHO |
| Incubation Period | 5-6 days | CDC |
| Infectious Period | 10 days | WHO |
| Original IFR | 0.5-1% | WHO |
| Omicron IFR | 0.1-0.3% | WHO |

## 📁 Project Structure

```
vaccine/
├── interactive_simulation.py  # Main COVID-19 simulation
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── venv/                      # Virtual environment
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This simulation is for **educational purposes only**. While based on real WHO/CDC data, it is a simplified model and should not be used for medical decisions or policy-making. Always consult official health authorities for accurate COVID-19 information.

## 🙏 Acknowledgments

- World Health Organization (WHO)
- Centers for Disease Control and Prevention (CDC)
- Our World in Data
- The scientific community studying COVID-19

---

**Created**: December 2024  
**Last Updated**: December 2025  
**Author**: Nishant
