"""
SIR Pandemic Simulation - Python Implementation
==============================================
Recreation of Excel model from Georgia Tech ISYE 6644 coursework
Krishna Aryal - MS Analytics

Original Excel model parameters:
- Population: 1000
- Initial Infected: 1  
- Transmission rate (β): 0.5
- Recovery rate (γ): 0.1
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import odeint

class SIRModel:
    """
    SIR (Susceptible-Infected-Recovered) epidemic model
    
    Based on compartmental modeling approach from Georgia Tech coursework
    Recreates Excel analysis with enhanced Python capabilities
    """
    
    def __init__(self, population=1000, initial_infected=1, beta=0.5, gamma=0.1):
        """
        Initialize SIR model parameters
        
        Parameters match Excel implementation:
        - population: Total population (N)
        - initial_infected: Initial infected individuals (I0)  
        - beta: Transmission rate (β)
        - gamma: Recovery rate (γ)
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
        
        dS/dt = -β*S*I/N
        dI/dt = β*S*I/N - γ*I  
        dR/dt = γ*I
        """
        S, I, R = y
        
        dSdt = -self.beta * S * I / self.N
        dIdt = self.beta * S * I / self.N - self.gamma * I
        dRdt = self.gamma * I
        
        return dSdt, dIdt, dRdt
    
    def solve_model(self, t_max=75, t_points=1000):
        """
        Solve SIR model over time period
        
        Returns pandas DataFrame with results matching Excel output
        """
        # Time points (matching Excel daily analysis)
        t = np.linspace(0, t_max, t_points)
        
        # Initial conditions
        y0 = [self.S0, self.I0, self.R0]
        
        # Solve differential equations
        solution = odeint(self.differential_equations, y0, t)
        
        # Create results DataFrame
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
        Discrete time simulation matching Excel approach
        
        Uses difference equations:
        S(t+1) - S(t) = -β*S(t)*I(t)/N
        I(t+1) - I(t) = β*S(t)*I(t)/N - γ*I(t)  
        R(t+1) - R(t) = γ*I(t)
        """
        # Initialize arrays
        S = np.zeros(days + 1)
        I = np.zeros(days + 1)  
        R = np.zeros(days + 1)
        
        # Initial conditions
        S[0], I[0], R[0] = self.S0, self.I0, self.R0
        
        # Discrete time evolution
        for t in range(days):
            # Calculate changes (matching Excel formulas)
            dS = -self.beta * S[t] * I[t] / self.N
            dI = self.beta * S[t] * I[t] / self.N - self.gamma * I[t]
            dR = self.gamma * I[t]
            
            # Update populations
            S[t+1] = S[t] + dS
            I[t+1] = I[t] + dI  
            R[t+1] = R[t] + dR
        
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
        """Find day with maximum infections (matching Excel analysis)"""
        peak_day = results.loc[results['Infected'].idxmax(), 'Day']
        peak_infections = results['Infected'].max()
        return int(peak_day), peak_infections
    
    def get_epidemic_summary(self, results):
        """
        Generate summary statistics matching Excel analysis
        """
        peak_day, peak_infections = self.get_peak_infection_day(results)
        final_recovered = results['Recovered'].iloc[-1]
        recovery_rate = final_recovered / self.N
        
        summary = {
            'Peak Infection Day': peak_day,
            'Peak Infections': int(peak_infections),
            'Final Recovered': int(final_recovered),
            'Recovery Rate': f"{recovery_rate:.1%}",
            'Total Population': self.N,
            'Transmission Rate (β)': self.beta,
            'Recovery Rate (γ)': self.gamma
        }
        
        return summary

# Example usage matching Excel parameters
if __name__ == "__main__":
    # Initialize model with Excel parameters
    model = SIRModel(population=1000, initial_infected=1, beta=0.5, gamma=0.1)
    
    # Run discrete simulation (matches Excel approach)
    results = model.discrete_simulation(days=75)
    
    # Print summary statistics
    summary = model.get_epidemic_summary(results)
    print("SIR Model Results - Python Recreation of Excel Analysis")
    print("=" * 55)
    for key, value in summary.items():
        print(f"{key}: {value}")
    
    # Show first 10 days (matching Excel table)
    print("\nFirst 10 Days of Simulation:")
    print(results.head(10).round(2))