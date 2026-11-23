#!/usr/bin/env python3
"""
AutoPCB Demo - Showcases the board-as-code PCB design tool.

This script demonstrates AutoPCB's ability to generate KiCad PCB designs
from JSON specifications.
"""

import json
import subprocess
import sys
from pathlib import Path


def create_sample_spec():
    """Create a sample PCB spec for demonstration."""
    return {
        "project_name": "Demo Board",
        "layers": 2,
        "trace_width": 0.2,
        "trace_clearance": 0.15,
        "components": [
            {
                "name": "U1",
                "value": "TL431",
                "footprint": "SOT23-5",
                "x": 0,
                "y": 0,
                "rotation": 0
            },
            {
                "name": "C1",
                "value": "10uF",
                "footprint": "0603",
                "x": 10,
                "y": 0,
                "rotation": 0
            },
            {
                "name": "R1",
                "value": "10k",
                "footprint": "0603",
                "x": 20,
                "y": 0,
                "rotation": 0
            }
        ],
        "power_rail": {
            "voltage": 5.0,
            "current": 1.0,
            "trace_width": 0.3
        }
    }


def demo_autopcb():
    """Run a demo AutoPCB design."""
    print("=" * 60)
    print("AutoPCB Demo - Board as Code PCB Design")
    print("=" * 60)
    print()
    
    # Create sample spec
    spec = create_sample_spec()
    print("Sample spec created:")
    print(json.dumps(spec, indent=2))
    print()
    
    # In production, this would call the AutoPCB API
    # For demo, we'll show what the output would look like
    print("AutoPCB would generate:")
    print("  - .kicad_pcb file (routed PCB)")
    print("  - .kicad_pro project files")
    print("  - Gerbers + drill files")
    print("  - BOM + PnP")
    print("  - STL 3D models")
    print()
    
    print("Demo complete!")
    print()
    print("To use AutoPCB:")
    print("  1. Visit https://autopcb.mkechem.com")
    print("  2. Sign up for free (1 credit)")
    print("  3. Upload your JSON spec")
    print("  4. Download your KiCad project")
    print()
    print("Pro tier: $49.99/month - unlimited boards")


if __name__ == "__main__":
    demo_autopcb()
