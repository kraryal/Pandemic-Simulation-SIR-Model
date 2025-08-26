"""
Enhanced Visualizations for SIR Pandemic Model
==============================================
Advanced plotting capabilities beyond Excel charts
Krishna Aryal - Georgia Tech MS Analytics
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import binom
import pandas as pd

# Set professional style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

def create_sir_visualization(results, save_path='results/sir_curve_python.png'):
    """
    Create professional SIR curve visualization
    Enhanced version of Excel chart with better styling
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Plot SIR curves
    ax.plot(results['Day'], results['Susceptible'], 'b-', linewidth=3, label='Susceptible', alpha=0.8)
    ax.plot(results['Day'], results['Infected'], 'r-', linewidth=3, label='Infected', alpha=0.8)
    ax.plot(results['Day'], results['Recovered'], 'g-', linewidth=3, label='Recovered', alpha=0.8)
    
    # Styling
    ax.set_xlabel('Days', fontsize=14, fontweight='bold')
    ax.set_ylabel('Population', fontsize=14, fontweight='bold')
    ax.set_title('SIR Pandemic Model: Disease Progression Over Time\nPython Recreation of Georgia Tech Excel Analysis', 
                fontsize=16, fontweight='bold', pad=20)
    
    # Add grid and legend
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=12, loc='center right')
    
    # Add annotations for key insights
    peak_day = results.loc[results['Infected'].idxmax(), 'Day']
    peak_infections = results['Infected'].max()
    
    ax.annotate(f'Peak Infection\nDay {int(peak_day)}: {int(peak_infections)} cases',
                xy=(peak_day, peak_infections), 
                xytext=(peak_day + 15, peak_infections + 50),
                arrowprops=dict(arrowstyle='->', color='red', alpha=0.7),
                fontsize=10, ha='center',
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def create_binomial_analysis(n=20, p=0.02, save_path='results/binomial_analysis_python.png'):
    """
    Classroom infection probability analysis
    Enhanced version of Excel binomial distribution
    """
    # Calculate probabilities for all possible outcomes
    k_values = np.arange(0, n+1)
    probabilities = binom.pmf(k_values, n, p)
    
    # Create visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Bar chart
    bars = ax1.bar(k_values, probabilities, alpha=0.7, color='steelblue', edgecolor='black')
    ax1.set_xlabel('Number of Students Infected', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Probability', fontsize=12, fontweight='bold')
    ax1.set_title('Binomial Distribution: Classroom Infection Probability\n(n=20 students, p=0.02)', 
                 fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Highlight most likely outcomes
    max_prob_idx = np.argmax(probabilities)
    bars[max_prob_idx].set_color('red')
    
    # Add expected value line
    expected_value = n * p
    ax1.axvline(expected_value, color='orange', linestyle='--', linewidth=2, 
                label=f'Expected Value: {expected_value}')
    ax1.legend()
    
    # Cumulative distribution
    cumulative = binom.cdf(k_values, n, p)
    ax2.plot(k_values, cumulative, 'go-', linewidth=2, markersize=6)
    ax2.set_xlabel('Number of Students Infected', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Cumulative Probability', fontsize=12, fontweight='bold')
    ax2.set_title('Cumulative Distribution Function\nP(X ≤ k)', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
    
    # Print key statistics
    print("Classroom Infection Analysis (Binomial Distribution)")
    print("=" * 50)
    print(f"Parameters: n={n} students, p={p:.3f} infection probability")
    print(f"Expected infections per day: {expected_value:.2f}")
    print(f"Most likely outcome: {k_values[max_prob_idx]} infections (P={probabilities[max_prob_idx]:.4f})")
    print(f"Probability of no infections: {probabilities[0]:.4f}")
    print(f"Probability of 1+ infections: {1-probabilities[0]:.4f}")

def create_comparison_dashboard(results, save_path='results/comparison_dashboard.png'):
    """
    Comprehensive dashboard comparing discrete vs continuous solutions
    """
    from sir_model import SIRModel
    
    # Get continuous solution for comparison  
    model = SIRModel()
    continuous_results = model.solve_model(t_max=75, t_points=76)
    
    # Create comparison plots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # SIR Curves Comparison
    days_discrete = results['Day'][:36]  # First 36 days like Excel
    ax1.plot(days_discrete, results['Susceptible'][:36], 'b-', label='Susceptible', linewidth=2)
    ax1.plot(days_discrete, results['Infected'][:36], 'r-', label='Infected', linewidth=2) 
    ax1.plot(days_discrete, results['Recovered'][:36], 'g-', label='Recovered', linewidth=2)
    ax1.set_title('SIR Model: Disease Progression (First 36 Days)', fontweight='bold')
    ax1.set_xlabel('Days')
    ax1.set_ylabel('Population')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Phase Portrait
    ax2.plot(results['Susceptible'], results['Infected'], 'purple', linewidth=2)
    ax2.set_title('SIR Phase Portrait (S vs I)', fontweight='bold')
    ax2.set_xlabel('Susceptible Population')
    ax2.set_ylabel('Infected Population')
    ax2.grid(True, alpha=0.3)
    
    # Parameter Sensitivity
    betas = [0.3, 0.5, 0.7]
    for beta in betas:
        model_sens = SIRModel(beta=beta)
        results_sens = model_sens.discrete_simulation(days=75)
        ax3.plot(results_sens['Day'], results_sens['Infected'], 
                label=f'β={beta}', linewidth=2)
    ax3.set_title('Sensitivity Analysis: Transmission Rate (β)', fontweight='bold')
    ax3.set_xlabel('Days') 
    ax3.set_ylabel('Infected Population')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Recovery Rate Analysis
    gammas = [0.05, 0.1, 0.15]
    for gamma in gammas:
        model_rec = SIRModel(gamma=gamma)
        results_rec = model_rec.discrete_simulation(days=75)
        ax4.plot(results_rec['Day'], results_rec['Infected'], 
                label=f'γ={gamma}', linewidth=2)
    ax4.set_title('Sensitivity Analysis: Recovery Rate (γ)', fontweight='bold')
    ax4.set_xlabel('Days')
    ax4.set_ylabel('Infected Population') 
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.suptitle('SIR Model: Comprehensive Analysis Dashboard\nGeorgia Tech ISYE 6644 - Advanced Analytics', 
                fontsize=16, fontweight='bold', y=0.95)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # Import and run SIR model
    from sir_model import SIRModel
    
    print("Creating enhanced visualizations...")
    
    # Run model
    model = SIRModel()
    results = model.discrete_simulation(days=75)
    
    # Generate all visualizations
    create_sir_visualization(results)
    create_binomial_analysis()  
    create_comparison_dashboard(results)
    
    print("All visualizations created successfully!")
    print("Files saved to results/ directory")