"""
SIR Model - Exact Match with Excel Implementation
================================================
Fixed to match Excel results from Georgia Tech ISYE 6644 project
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class SIRModelExcelMatch:
    """
    SIR model that exactly matches Excel implementation
    """
    
    def __init__(self, population=1000, initial_infected=1, beta=0.5, gamma=0.1):
        self.N = population
        self.I0 = initial_infected
        self.S0 = population - initial_infected  
        self.R0 = 0
        self.beta = beta
        self.gamma = gamma
        
    def discrete_simulation_excel_style(self, days=30):
        """
        Excel-style discrete simulation matching your document
        Using the exact approach from your Excel file
        """
        # Initialize with exact Excel starting values
        S = [self.S0]  # Start with 999
        I = [self.I0]  # Start with 1
        R = [self.R0]  # Start with 0
        
        print(f"Starting values: S0={S[0]}, I0={I[0]}, R0={R[0]}")
        print(f"Parameters: β={self.beta}, γ={self.gamma}, N={self.N}")
        print()
        
        for t in range(days):
            # Excel formulas (matching your document):
            # New infections = β * S(t) * I(t) / N  
            # New recoveries = γ * I(t)
            
            current_S = S[t]
            current_I = I[t] 
            current_R = R[t]
            
            # Calculate transitions
            new_infections = self.beta * current_S * current_I / self.N
            new_recoveries = self.gamma * current_I
            
            # Update populations (Excel-style)
            next_S = current_S - new_infections
            next_I = current_I + new_infections - new_recoveries  
            next_R = current_R + new_recoveries
            
            S.append(next_S)
            I.append(next_I)
            R.append(next_R)
            
            # Debug first few days
            if t < 5:
                print(f"Day {t}→{t+1}:")
                print(f"  New infections: {self.beta} × {current_S:.2f} × {current_I:.2f} / {self.N} = {new_infections:.4f}")
                print(f"  New recoveries: {self.gamma} × {current_I:.2f} = {new_recoveries:.4f}")
                print(f"  Next day: S={next_S:.2f}, I={next_I:.2f}, R={next_R:.2f}")
                print()
        
        # Create DataFrame
        results = pd.DataFrame({
            'Day': range(len(S)),
            'Susceptible': S,
            'Infected': I,
            'Recovered': R,
            'Total': [s+i+r for s,i,r in zip(S,I,R)]
        })
        
        return results
    
    def classroom_model(self):
        """
        Classroom model from your document (20 students)
        """
        # Parameters from your document
        n_students = 20
        infection_prob = 0.02
        
        # Expected infections per day
        expected = n_students * infection_prob
        
        return {
            'students': n_students,
            'probability': infection_prob,
            'expected_daily_infections': expected
        }

# Test with your exact parameters
if __name__ == "__main__":
    print("🦠 SIR MODEL - EXCEL MATCH TEST")
    print("=" * 40)
    
    # Large population model (1000 people)
    print("1️⃣ LARGE POPULATION MODEL (N=1000)")
    model_large = SIRModelExcelMatch(population=1000, initial_infected=1, beta=0.5, gamma=0.1)
    results_large = model_large.discrete_simulation_excel_style(days=10)
    
    print("First 10 days results:")
    print(results_large.round(2))
    print()
    
    # Find peak
    peak_day = results_large.loc[results_large['Infected'].idxmax(), 'Day']
    peak_infections = results_large['Infected'].max()
    print(f"Peak infection: Day {int(peak_day)}, {int(peak_infections)} cases")
    print()
    
    # Classroom model  
    print("2️⃣ CLASSROOM MODEL (N=20)")
    classroom = model_large.classroom_model()
    print(f"Students: {classroom['students']}")
    print(f"Daily infection probability: {classroom['probability']}")
    print(f"Expected daily infections: {classroom['expected_daily_infections']}")