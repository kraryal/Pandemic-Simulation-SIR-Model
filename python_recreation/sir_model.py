"""
SIR Pandemic Simulation - Correct Implementation
===============================================
Proper SIR model with realistic parameters and results
Krishna Aryal - Georgia Tech MS Analytics
"""

import numpy as np
import pandas as pd
from scipy.integrate import odeint

class SIRModel:
    """
    Correct SIR (Susceptible-Infected-Recovered) epidemic model
    
    Implements standard epidemiological SIR equations:
    dS/dt = -β*S*I/N
    dI/dt = β*S*I/N - γ*I  
    dR/dt = γ*I
    """
    
    def __init__(self, population=1000, initial_infected=1, beta=0.5, gamma=0.1):
        """
        Initialize SIR model with correct parameters
        
        Parameters:
        - population: Total population (N)
        - initial_infected: Initial infected individuals (I0)  
        - beta: Transmission rate (β) - realistic range 0.1-2.0
        - gamma: Recovery rate (γ) - typically 0.05-0.2
        """
        self.N = population
        self.I0 = initial_infected
        self.S0 = population - initial_infected
        self.R0 = 0
        self.beta = beta
        self.gamma = gamma
        
    def differential_equations(self, y, t):
        """
        SIR differential equations system
        """
        S, I, R = y
        
        dSdt = -self.beta * S * I / self.N
        dIdt = self.beta * S * I / self.N - self.gamma * I
        dRdt = self.gamma * I
        
        return dSdt, dIdt, dRdt
    
    def solve_model(self, t_max=75, t_points=1000):
        """
        Solve SIR model using continuous differential equations
        """
        t = np.linspace(0, t_max, t_points)
        y0 = [self.S0, self.I0, self.R0]
        solution = odeint(self.differential_equations, y0, t)
        
        results = pd.DataFrame({
            'Day': t,
            'Susceptible': solution[:, 0],
            'Infected': solution[:, 1], 
            'Recovered': solution[:, 2],
            'Total': solution.sum(axis=1)
        })
        
        return results
    
    def discrete_simulation(self, days=75):
        """
        Correct discrete time simulation with proper SIR equations
        """
        # Initialize arrays
        S = np.zeros(days + 1)
        I = np.zeros(days + 1)  
        R = np.zeros(days + 1)
        
        # Initial conditions
        S[0], I[0], R[0] = self.S0, self.I0, self.R0
        
        print(f"🦠 CORRECT SIR MODEL SIMULATION")
        print(f"Parameters: β={self.beta}, γ={self.gamma}, N={self.N}")
        print(f"Initial: S={S[0]}, I={I[0]}, R={R[0]}")
        print()
        
        # Discrete time evolution with CORRECT formulas
        for t in range(days):
            # Correct SIR equations
            new_infections = self.beta * S[t] * I[t] / self.N
            new_recoveries = self.gamma * I[t]
            
            # Update populations
            S[t+1] = S[t] - new_infections
            I[t+1] = I[t] + new_infections - new_recoveries
            R[t+1] = R[t] + new_recoveries
            
            # Show first 10 days for verification
            if t < 10:
                print(f"Day {t:2d}→{t+1:2d}: S={S[t+1]:7.2f}, I={I[t+1]:7.2f}, R={R[t+1]:7.2f}")
        
        # Create results DataFrame
        results = pd.DataFrame({
            'Day': range(days + 1),
            'Susceptible': S,
            'Infected': I,
            'Recovered': R,
            'Total': S + I + R
        })
        
        return results
    
    def get_peak_infection_day(self, results):
        """Find day with maximum infections"""
        peak_day = results.loc[results['Infected'].idxmax(), 'Day']
        peak_infections = results['Infected'].max()
        return int(peak_day), peak_infections
    
    def get_epidemic_summary(self, results):
        """
        Generate comprehensive summary statistics
        """
        peak_day, peak_infections = self.get_peak_infection_day(results)
        final_recovered = results['Recovered'].iloc[-1]
        recovery_rate = final_recovered / self.N
        
        # Basic reproduction number (R0)
        R0 = self.beta / self.gamma
        
        summary = {
            'Peak Infection Day': peak_day,
            'Peak Infections': int(peak_infections),
            'Peak Percentage': f"{peak_infections/self.N:.1%}",
            'Final Recovered': int(final_recovered),
            'Recovery Rate': f"{recovery_rate:.1%}",
            'Basic Reproduction Number (R0)': f"{R0:.2f}",
            'Total Population': self.N,
            'Transmission Rate (β)': self.beta,
            'Recovery Rate (γ)': self.gamma
        }
        
        return summary

    def classroom_model(self):
        """
        Classroom model for binomial analysis (20 students, p=0.02)
        """
        return {
            'students': 20,
            'probability': 0.02,
            'expected_daily_infections': 20 * 0.02
        }

# Example usage with correct parameters
if __name__ == "__main__":
    # Initialize model with realistic parameters
    model = SIRModel(population=1000, initial_infected=1, beta=0.5, gamma=0.1)
    
    # Run discrete simulation
    results = model.discrete_simulation(days=75)
    
    # Print comprehensive summary
    summary = model.get_epidemic_summary(results)
    print("\n" + "="*60)
    print("📊 CORRECT SIR MODEL RESULTS")
    print("="*60)
    for key, value in summary.items():
        print(f"{key:.<35} {value}")
    
    print(f"\n📈 This is what your Excel SHOULD show with β=0.5, γ=0.1")
    print(f"📈 Peak around day {summary['Peak Infection Day']} is realistic for flu-like epidemic")
    print(f"📈 R0 = {summary['Basic Reproduction Number (R0)']} means each person infects {float(summary['Basic Reproduction Number (R0)']):.1f} others")