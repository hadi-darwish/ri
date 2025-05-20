from flask import Flask, request, jsonify, render_template
import numpy as np
from scipy.optimize import fsolve
import os

app = Flask(__name__)

def solve_for_ri(m_val, f_val, ro):
    """
    Solves the given equation for the inner radius ri given m_val, f_val, and ro.
    
    Parameters:
    m_val (float): Input variable M
    f_val (float): Input variable F
    ro (float): Outer radius ro
    
    Returns:
    float: The solution for inner radius ri
    """
    def equation(ri):
        try:
            term1 = f_val / (np.pi * (ro**2 - ri**2) - 0.002)
            term2 = (4 * m_val * ro) / (np.pi * (ro**4 - ri**4))
            
            inside_sqrt = 5.7595 * term1**2 - 4.8642 * term1 * term2 + 4.1089 * term2**2
            if inside_sqrt < 0:
                return np.inf  # Return infinity if square root would be imaginary
            return np.sqrt(inside_sqrt) - (0.820652 * 10**6)
        except Exception:
            return np.inf
    
    # Initial guess for ri (must be less than ro)
    initial_guess = ro * 0.5
      # Solve the equation numerically with bounds
    try:
        ri_solution = fsolve(equation, initial_guess, full_output=True)
        if ri_solution[2] != 1:  # Check if solution converged
            raise ValueError("Solution did not converge")
            
        ri = ri_solution[0][0]
        
        # Ensure the solution is physically meaningful (0 < ri < ro)
        if ri <= 0 or ri >= ro:
            raise ValueError("Solution out of bounds")
            
        return ri
    except Exception:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    try:
        M = float(data.get('M', 0))
        F = float(data.get('F', 0))
        ro = float(data.get('ro', 0))
        
        if ro <= 0:
            return jsonify({"error": "ro must be positive"}), 400
            
        ri = solve_for_ri(M, F, ro)
        
        if ri is None:
            return jsonify({"error": "Could not find a valid solution for ri"}), 400
        else:
            return jsonify({"ri": ri})
            
    except ValueError:
        return jsonify({"error": "Please enter valid numbers for all fields"}), 400

# For local development
if __name__ == "__main__":
    app.run(debug=True)
