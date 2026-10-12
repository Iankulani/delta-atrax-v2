#!/bin/bash
# DELTA-ATRAX-V2 Health Check

set -e

echo "🦀 DELTA-ATRAX-V2 Health Check"
echo "=============================="

# Check Python
if command -v python3 &> /dev/null; then
    echo "✅ Python: $(python3 --version)"
else
    echo "❌ Python not found"
    exit 1
fi

# Check Docker
if command -v docker &> /dev/null; then
    echo "✅ Docker: $(docker --version)"
else
    echo "⚠️ Docker not found"
fi

# Check web dashboard
if curl -s http://localhost:5000 > /dev/null 2>&1; then
    echo "✅ Web Dashboard: Running"
else
    echo "⚠️ Web Dashboard: Not running"
fi

# Check database
if [ -f ".delta_atrax_v2/delta_atrax_v2.db" ]; then
    echo "✅ Database: Found"
else
    echo "⚠️ Database: Not initialized"
fi

echo ""
echo "Health check complete!"
