"""
Enhanced Visualizations for Corrected SIR Pandemic Model
=======================================================
Professional visualizations with realistic results
Krishna Aryal - Georgia Tech MS Analytics
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import binom
import pandas as pd

# Set professional style
plt.style.use('default')  # More reliable than seaborn
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'

def create_sir_visualization(results, save_path='results/sir_curve_corrected.png'):
    """
    Create professional SIR curve visualization with CORRECT results
    """
    plt.figure(figsize=(12, 8))
    
    # Plot SIR curves with proper styling
    plt.plot(results['Day'], results['Susceptible'], 'b-', linewidth=3, label='Susceptible', alpha=0.8)
    plt.plot(results['Day'], results['Infected'], 'r-', linewidth=3, label='Infected', alpha=0.8)
    plt.plot(results['Day'], results['Recovered'], 'g-', linewidth=3, label='Recovered', alpha=0.8)
    
    # Professional styling
    plt.xlabel('Days', fontsize=14, fontweight='bold')
    plt.ylabel('Population', fontsize=14, fontweight='bold')
    plt.title('Corrected SIR Pandemic Model: Realistic Disease Progression\nGeorgia Tech ISYE 6644 - Proper Implementation (β=0.5, γ=0.1)', 
                fontsize=14, fontweight='bold', pad=20)
    
    # Add grid and legend
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12, loc='center right')
    
    # Find and annotate peak with CORRECT values
    peak_day = results.loc[results['Infected'].idxmax(), 'Day']
    peak_infections = results['Infected'].max()
    
    plt.annotate(f'Peak Infection\nDay {int(peak_day)}: {int(peak_infections)} cases\n({peak_infections/1000:.1%} of population)',
                xy=(peak_day, peak_infections), 
                xytext=(peak_day + 15, peak_infections + 50),
                arrowprops=dict(arrowstyle='->', color='red', alpha=0.7),
                fontsize=11, ha='center',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="white", alpha=0.9, edgecolor='red'))
    
    # Add R0 information
    R0 = 0.5 / 0.1  # β/γ
    plt.text(0.02, 0.98, f'Basic Reproduction Number (R₀): {R0:.1f}\nRealistic epidemic parameters', 
            transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7))
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"✅ SIR curve saved to {save_path}")

def create_binomial_analysis(n=20, p=0.02, save_path='results/binomial_analysis_corrected.png'):
    """
    Classroom infection probability analysis (unchanged - this was correct)
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
    print(f"✅ Binomial analysis saved to {save_path}")
    
    # Print key statistics
    print("Classroom Infection Analysis (Binomial Distribution)")
    print("=" * 50)
    print(f"Parameters: n={n} students, p={p:.3f} infection probability")
    print(f"Expected infections per day: {expected_value:.2f}")
    print(f"Most likely outcome: {k_values[max_prob_idx]} infections (P={probabilities[max_prob_idx]:.4f})")
    print(f"Probability of no infections: {probabilities[0]:.4f}")
    print(f"Probability of 1+ infections: {1-probabilities[0]:.4f}")

def create_corrected_dashboard(results, save_path='results/corrected_dashboard.png'):
    """
    Comprehensive dashboard with CORRECTED model results
    """
    from sir_model import SIRModel
    
    # Create comparison plots with better spacing
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Main title with better positioning
    fig.suptitle('SIR Model: Corrected Analysis Dashboard', 
                fontsize=18, fontweight='bold', y=0.95)
    fig.text(0.5, 0.91, 'Georgia Tech ISYE 6644 - Realistic Epidemiological Parameters', 
             ha='center', fontsize=14, style='italic', color='darkblue')
    
    # SIR Curves (First 60 days)
    days_subset = results['Day'][:60]
    ax1.plot(days_subset, results['Susceptible'][:60], 'b-', label='Susceptible', linewidth=3, alpha=0.8)
    ax1.plot(days_subset, results['Infected'][:60], 'r-', label='Infected', linewidth=3, alpha=0.8) 
    ax1.plot(days_subset, results['Recovered'][:60], 'g-', label='Recovered', linewidth=3, alpha=0.8)
    ax1.set_title('Corrected SIR Model: Realistic Epidemic Progression', fontweight='bold', fontsize=12)
    ax1.set_xlabel('Days', fontweight='bold')
    ax1.set_ylabel('Population', fontweight='bold')
    ax1.legend(frameon=True, fancybox=True, shadow=True)
    ax1.grid(True, alpha=0.3)
    
    # Phase Portrait
    ax2.plot(results['Susceptible'], results['Infected'], 'purple', linewidth=3, alpha=0.8)
    ax2.scatter(results['Susceptible'].iloc[0], results['Infected'].iloc[0], 
               color='green', s=100, label='Start', zorder=5)
    peak_idx = results['Infected'].idxmax()
    ax2.scatter(results['Susceptible'].iloc[peak_idx], results['Infected'].iloc[peak_idx], 
               color='red', s=100, label=f'Peak (Day {peak_idx})', zorder=5)
    ax2.set_title('SIR Phase Portrait (S vs I)', fontweight='bold', fontsize=12)
    ax2.set_xlabel('Susceptible Population', fontweight='bold')
    ax2.set_ylabel('Infected Population', fontweight='bold')
    ax2.legend(frameon=True, fancybox=True, shadow=True)
    ax2.grid(True, alpha=0.3)
    
    # Parameter Sensitivity - Transmission Rate
    colors = ['#2ecc71', '#f39c12', '#e74c3c']  # Green, Orange, Red
    betas = [0.3, 0.5, 0.7]
    for i, beta in enumerate(betas):
        model_sens = SIRModel(beta=beta)
        results_sens = model_sens.discrete_simulation(days=60)
        ax3.plot(results_sens['Day'], results_sens['Infected'], 
                color=colors[i], label=f'β={beta}', linewidth=3, alpha=0.8)
    ax3.set_title('Sensitivity Analysis: Transmission Rate (β)', fontweight='bold', fontsize=12)
    ax3.set_xlabel('Days', fontweight='bold') 
    ax3.set_ylabel('Infected Population', fontweight='bold')
    ax3.legend(frameon=True, fancybox=True, shadow=True)
    ax3.grid(True, alpha=0.3)
    
    # Parameter Sensitivity - Recovery Rate
    colors = ['#e67e22', '#3498db', '#9b59b6']  # Orange, Blue, Purple
    gammas = [0.05, 0.1, 0.15]
    for i, gamma in enumerate(gammas):
        model_rec = SIRModel(gamma=gamma)
        results_rec = model_rec.discrete_simulation(days=60)
        ax4.plot(results_rec['Day'], results_rec['Infected'], 
                color=colors[i], label=f'γ={gamma}', linewidth=3, alpha=0.8)
    ax4.set_title('Sensitivity Analysis: Recovery Rate (γ)', fontweight='bold', fontsize=12)
    ax4.set_xlabel('Days', fontweight='bold')
    ax4.set_ylabel('Infected Population', fontweight='bold') 
    ax4.legend(frameon=True, fancybox=True, shadow=True)
    ax4.grid(True, alpha=0.3)
    
    # Adjust layout
    plt.subplots_adjust(top=0.88, hspace=0.3, wspace=0.25)
    
    # Save with high quality
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
    print(f"✅ Dashboard saved to {save_path}")

if __name__ == "__main__":
    # Import and run SIR model
    from sir_model import SIRModel
    
    print("🎨 Creating corrected visualizations...")
    print("=" * 40)
    
    # Run corrected model
    model = SIRModel(population=1000, initial_infected=1, beta=0.5, gamma=0.1)
    results = model.discrete_simulation(days=75)
    
    # Get summary for verification
    summary = model.get_epidemic_summary(results)
    print(f"📈 Peak: Day {summary['Peak Infection Day']}, {summary['Peak Infections']} cases")
    print(f"📊 R₀: {summary['Basic Reproduction Number (R0)']}")
    print()
    
    # Generate all visualizations
    create_sir_visualization(results)
    create_binomial_analysis()  
    create_corrected_dashboard(results)
    
    print("\n🎉 All corrected visualizations created successfully!")
    print("📁 Files saved to results/ directory")
    print("✅ Models now show realistic epidemiological behavior")