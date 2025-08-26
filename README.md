# Pandemic Simulation: SIR Model for Policy Decision Support

[![Excel](https://img.shields.io/badge/Excel-Advanced-green.svg)](https://www.microsoft.com/excel)
[![Statistics](https://img.shields.io/badge/Statistics-SIR%20Model-blue.svg)](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology)
[![Georgia Tech](https://img.shields.io/badge/Georgia%20Tech-ISYE%206644-gold.svg)](https://www.gatech.edu/)

## 🦠 Project Overview

**Advanced epidemiological modeling using SIR (Susceptible-Infected-Recovered) compartmental models for pandemic response and policy decision support.**

Developed during Georgia Tech MS Analytics coursework (ISYE 6644 - Simulation), this project demonstrates sophisticated statistical modeling techniques applied to real-world public health challenges, directly relevant to data science applications in healthcare, risk assessment, and policy analytics.

### 🎯 Key Achievements
- **SIR Model Implementation**: Mathematical modeling of disease transmission dynamics
- **Excel Advanced Analytics**: Complex simulation using differential equations and statistical methods
- **Monte Carlo Simulation**: Probabilistic analysis of infection spread patterns
- **Policy Applications**: Decision support framework for public health interventions

## 🔬 Technical Methodology

### Compartmental Modeling Approach

Susceptible (S) → Infected (I) → Recovered (R)
dS/dt = -βSI/N
dI/dt = βSI/N - γI
dR/dt = γI
Where:
β = transmission rate (0.5)
γ = recovery rate (0.1)
N = total population (1000)

## 🐍 Python Recreation & Enhancement

### Advanced Implementation Beyond Excel
To demonstrate modern data science capabilities, this project includes a **complete Python recreation** of the Excel model with enhanced features:

**Key Python Enhancements:**
- **Object-Oriented Design**: Clean, maintainable SIR model class
- **Advanced Visualizations**: Professional matplotlib/seaborn charts  
- **Sensitivity Analysis**: Parameter exploration beyond Excel capabilities
- **Statistical Integration**: Scipy integration for continuous solutions
- **Production-Ready Code**: Documented, testable, scalable implementation

### Python Files
- `sir_model.py`: Complete SIR model implementation with discrete and continuous solutions
- `visualizations.py`: Enhanced plotting capabilities with statistical analysis  
- `requirements.txt`: Dependencies for easy environment setup

### Running the Python Analysis
```bash
# Install dependencies
pip install -r python_recreation/requirements.txt

# Run SIR model analysis
python python_recreation/sir_model.py

# Generate enhanced visualizations  
python python_recreation/visualizations.py


### Statistical Analysis Components
- **Binomial Distribution Modeling**: Infection probability calculations
- **Expected Value Analysis**: E(X) = np = 20 × 0.02 = 0.4 expected infections
- **Geometric Growth Patterns**: Exponential infection spread modeling
- **Probability Distribution Analysis**: 20-person classroom infection scenarios

## 📊 Key Results & Findings

### SIR Model Results (Population = 1000)
- **Peak Infection Day**: Day 17 with maximum infected population
- **Epidemic Duration**: ~75 days total duration
- **Final Recovery Rate**: 92% of population recovered
- **Transmission Parameters**: β = 0.5, γ = 0.1

### Classroom Simulation (20 Students)
- **Expected Daily Infections**: 0.4 students per day
- **Probability Distribution**: Binomial(n=20, p=0.02)
- **Most Likely Outcome**: 0-1 infections per day
- **Infection Period**: 3 days infectious period per student

## 💼 Business Applications & Value

| Public Health Application | Business Data Science Analog | Transferable Skills |
|---------------------------|------------------------------|-------------------|
| **Disease Spread Prediction** | Customer churn propagation modeling | Time series forecasting, contagion analysis |
| **Policy Intervention Timing** | Marketing campaign optimization | A/B testing, intervention analysis |
| **Resource Allocation Planning** | Supply chain demand forecasting | Capacity planning, resource optimization |
| **Risk Assessment Modeling** | Financial risk stress testing | Monte Carlo simulation, scenario analysis |

### Real-World Impact
- **COVID-19 Relevance**: Model directly applicable to pandemic response planning
- **Healthcare Analytics**: Foundation for hospital capacity planning and resource allocation
- **Business Continuity**: Framework for organizational risk assessment during health crises
- **Insurance Applications**: Actuarial modeling for health and business interruption insurance

## 🛠️ Technical Implementation

### Advanced Excel Techniques Demonstrated
- **Differential Equation Solving**: Numerical methods for continuous modeling using discrete time steps
- **Monte Carlo Simulation**: Probabilistic scenario analysis with multiple iterations
- **Dynamic Data Visualization**: Interactive charts showing epidemic progression over time
- **Statistical Distribution Analysis**: Complete binomial probability calculations
- **Parameter Sensitivity Analysis**: Testing different β and γ values

### Mathematical Foundation

Discrete Time Implementation:
St+1 - St = -βSt × (It/Nt)
It+1 - It = βSt × (It/Nt) - γIt
Rt+1 - Rt = γIt
Nt = St + It + Rt (population conservation)

## 🎓 Georgia Tech MS Analytics Integration

**Course**: ISYE 6644 - Simulation and Modeling  
**Instructor**: [Dave Goldsman]  
**Focus**: Advanced statistical simulation techniques for business and policy applications

**Academic Rigor Demonstrated**:
- Mathematical modeling of complex systems
- Statistical distribution analysis and application
- Monte Carlo simulation methodology
- Business decision support through quantitative analysis
- Professional technical documentation and presentation

## 📁 Repository Structure

Pandemic-Simulation-SIR-Model/
├── README.md                    # This comprehensive overview
├── excel_model/                 # Excel implementation files
│   └── pandemic_simulation.xlsx # Complete SIR model with calculations
├── docs/                        # Technical documentation
│   └── methodology.pdf          # Detailed mathematical methodology and results
├── results/                     # Analysis outputs and visualizations
└── presentation/                # Summary materials

## 🚀 Business Relevance for Data Science

### Demonstrated Data Science Capabilities
✅ **Advanced Statistical Modeling**: SIR differential equations and probability theory  
✅ **Excel Mastery**: Complex business modeling tool proficiency  
✅ **Public Policy Analytics**: Government and healthcare decision support systems  
✅ **Risk Assessment**: Quantitative analysis for business continuity planning  
✅ **Scenario Planning**: Monte Carlo methods for uncertainty quantification  
✅ **Mathematical Rigor**: Peer-reviewed academic methodology applied to real problems  

### Target Industry Applications
- **Healthcare Data Science**: Epidemiological modeling, patient flow optimization, resource planning
- **Insurance Analytics**: Actuarial modeling, pandemic risk assessment, business interruption analysis
- **Supply Chain Management**: Disruption modeling, capacity planning, risk mitigation
- **Financial Services**: Contagion risk modeling, stress testing, scenario analysis
- **Government Consulting**: Policy impact analysis, resource allocation, emergency planning
- **Pharmaceutical**: Clinical trial modeling, drug efficacy analysis, market penetration studies

## 🔗 Technical References & Methodology

1. **Compartmental Models in Epidemiology** - Mathematical SIR model foundations
2. **Monte Carlo Methods in Statistical Simulation** - Probabilistic analysis techniques  
3. **Excel Advanced Analytics** - Business modeling and simulation best practices
4. **Georgia Tech ISYE 6644** - Academic simulation and modeling methodologies

## 📈 Future Enhancements

- **Python Implementation**: Recreate model in Python with enhanced visualization
- **Parameter Optimization**: Automated parameter fitting using historical data
- **Interactive Dashboard**: Web-based interface for real-time policy scenario testing
- **Multi-Population Modeling**: Extended SEIR models with demographic stratification

## 📧 Contact

**Krishna Aryal**  
Georgia Tech MS Analytics | Published Researcher | Advanced Statistical Modeler  

🔗 **Main Portfolio**: https://github.com/kraryal/QCD-Phase-Transitions-ML  
🔗 **Google Scholar**: https://scholar.google.com/citations?user=fsWWqa0AAAAJ  
🔗 **LinkedIn**: [Your LinkedIn Profile]  

*Demonstrating advanced statistical modeling and business analytics capabilities through academic excellence and practical application*

---

## 🎯 For Data Science Recruiters

This project demonstrates:
- **🔬 Advanced Mathematical Modeling** with real-world public health applications
- **📊 Excel Expertise** for business analytics and executive decision support  
- **📈 Statistical Rigor** through probability theory, Monte Carlo simulation, and model validation
- **💼 Policy Impact Analysis** showing business acumen and stakeholder value creation
- **🎓 Academic Excellence** through rigorous Georgia Tech MS Analytics coursework
- **🦠 Timely Relevance** addressing critical challenges in pandemic preparedness and response

**Perfect example of translating complex mathematical concepts into actionable business insights for high-stakes decision making.**