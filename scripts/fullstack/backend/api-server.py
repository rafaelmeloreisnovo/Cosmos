#!/usr/bin/env python3
"""
COSMOS Backend API Server
FastAPI-based REST API for COSMOS calculations and analysis
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import math

app = FastAPI(
    title="COSMOS API",
    description="REST API for COSMOS framework calculations and analysis",
    version="1.0.0"
)

# Enable CORS
# Note: For production, replace ["*"] with specific allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],  # Specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Models
class FibonacciResponse(BaseModel):
    sequence: List[float]
    terms: int
    modifier: float
    golden_ratio: float = 1.618033988749895


class GalaxyInfo(BaseModel):
    name: str
    type: str
    distance_ly: float
    spiral_arms: int
    fibonacci_correlation: str
    description: str


class EnergySimulationRequest(BaseModel):
    mass_kg: float
    wavelength_nm: float = 550
    duration_seconds: float = 1


class EnergySimulationResponse(BaseModel):
    input_mass_kg: float
    total_energy_j: float
    usable_energy_j: float
    power_watts: float
    efficiency: float = 0.15


# Routes
@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "COSMOS API",
        "version": "1.0.0",
        "author": "Rafael Melo Reis",
        "description": "REST API for COSMOS framework",
        "endpoints": [
            "/api/fibonacci",
            "/api/galaxy/{name}",
            "/api/energy/simulate",
            "/api/health"
        ]
    }


@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "COSMOS API"}


@app.get("/api/fibonacci", response_model=FibonacciResponse)
async def calculate_fibonacci(
    n: int = Query(10, ge=1, le=100, description="Number of terms"),
    modifier: float = Query(1.618033988749895, ge=1.0, le=2.0, description="Golden ratio modifier")
):
    """
    Calculate modified Fibonacci sequence.
    
    Args:
        n: Number of terms to generate (1-100)
        modifier: Golden ratio modifier (1.0-2.0)
    
    Returns:
        Modified Fibonacci sequence
    """
    sequence = [0, 1] if n >= 2 else [0] if n == 1 else []
    
    for i in range(2, n):
        next_val = sequence[i-1] + sequence[i-2] * modifier
        sequence.append(next_val)
    
    return FibonacciResponse(
        sequence=sequence,
        terms=n,
        modifier=modifier
    )


@app.get("/api/galaxy/{galaxy_name}", response_model=GalaxyInfo)
async def get_galaxy_info(galaxy_name: str):
    """
    Get galaxy information and analysis.
    
    Args:
        galaxy_name: Name of galaxy (M81, IC342, NGC628)
    
    Returns:
        Galaxy information and Fibonacci correlation analysis
    """
    galaxies = {
        "M81": GalaxyInfo(
            name="M81 (Bode's Galaxy)",
            type="Spiral Galaxy",
            distance_ly=11.8e6,
            spiral_arms=2,
            fibonacci_correlation="High",
            description="Prominent spiral arms following modified Fibonacci patterns with golden ratio proportions"
        ),
        "IC342": GalaxyInfo(
            name="IC 342 (Caldwell 5)",
            type="Intermediate Spiral",
            distance_ly=10.7e6,
            spiral_arms=2,
            fibonacci_correlation="Very High",
            description="Face-on spiral with clear Fibonacci-like structure, void spaces align with modified sequence"
        ),
        "NGC628": GalaxyInfo(
            name="NGC 628 (Messier 74)",
            type="Grand Design Spiral",
            distance_ly=32e6,
            spiral_arms=2,
            fibonacci_correlation="Excellent",
            description="Grand design spiral visible in James Webb imagery, fractal patterns in 33-layer matrix"
        )
    }
    
    galaxy_name_upper = galaxy_name.upper()
    if galaxy_name_upper not in galaxies:
        raise HTTPException(
            status_code=404,
            detail=f"Galaxy {galaxy_name} not found. Available: M81, IC342, NGC628"
        )
    
    return galaxies[galaxy_name_upper]


@app.post("/api/energy/simulate", response_model=EnergySimulationResponse)
async def simulate_energy_conversion(request: EnergySimulationRequest):
    """
    Simulate ATOMIC_EX_LIGHT energy conversion.
    
    Args:
        request: Simulation parameters
    
    Returns:
        Energy conversion simulation results
    """
    # Constants
    SPEED_OF_LIGHT = 299792458  # m/s
    CONVERSION_EFFICIENCY = 0.15
    
    # Calculate E=mc²
    total_energy = request.mass_kg * (SPEED_OF_LIGHT ** 2)
    
    # Apply conversion efficiency
    usable_energy = total_energy * CONVERSION_EFFICIENCY
    
    # Calculate power
    power = usable_energy / request.duration_seconds
    
    return EnergySimulationResponse(
        input_mass_kg=request.mass_kg,
        total_energy_j=total_energy,
        usable_energy_j=usable_energy,
        power_watts=power
    )


@app.get("/api/patterns/detect")
async def detect_patterns(
    data: str = Query(..., description="Comma-separated values", max_length=1000),
    pattern_type: str = Query("auto", description="Pattern type: fibonacci, spiral, auto")
):
    """
    Detect patterns in data.
    
    Args:
        data: Comma-separated numerical values (max 1000 chars)
        pattern_type: Type of pattern to detect
    
    Returns:
        Pattern detection results
    """
    # Validate input length
    parts = data.split(',')
    if len(parts) > 100:
        raise HTTPException(status_code=400, detail="Too many values. Maximum 100 values allowed.")
    
    try:
        values = [float(x.strip()) for x in parts]
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid data format. Use comma-separated numbers.")
    
    if len(values) < 3:
        raise HTTPException(status_code=400, detail="At least 3 values required")
    
    # Check for Fibonacci pattern
    golden_ratio = 1.618033988749895
    ratios = []
    for i in range(1, len(values)):
        if values[i-1] != 0:
            ratios.append(values[i] / values[i-1])
    
    avg_ratio = sum(ratios) / len(ratios) if ratios else 0
    fibonacci_detected = abs(avg_ratio - golden_ratio) < 0.1
    
    return {
        "data_points": len(values),
        "fibonacci_detected": fibonacci_detected,
        "average_ratio": avg_ratio,
        "golden_ratio_deviation": abs(avg_ratio - golden_ratio),
        "pattern_type": "fibonacci_sequence" if fibonacci_detected else "unknown"
    }


if __name__ == "__main__":
    import uvicorn
    print("\n🌌 COSMOS API Server")
    print("   Starting on http://localhost:8000")
    print("   API docs: http://localhost:8000/docs")
    print("   Rafael Melo Reis - RAFAELIA Project\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
