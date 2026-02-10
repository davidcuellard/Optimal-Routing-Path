# Optimal Routing Path of Multi-Output Data Packets for Aeronautical Networks

**Author:** David Cuellar  
**Purpose:** Educational Research Project

## Abstract

The rise of the Internet and Industry 4.0 has resulted in numerous changes in how people live and work. The aeronautical industry is one of those that has been severely impacted. The use of commercial flights has grown in popularity, as has the need for effective communication systems. The Aeronautical Ad hoc NETwork (AANET) is a wireless communication system that allows aircraft to communicate with one another as well as with ground stations. The application of various optimization algorithms is critical in determining the best data packet routing path within the AANET.

This research project introduces and improves Dijkstra's Algorithm to provide multiple outputs as a solution to optimize network routing, taking into account important metrics such as **end-to-end transmission rate** and **end-to-end latency**. The algorithm is used to find the longest path, maximizing end-to-end transmission rate while minimizing end-to-end latency. The results are evaluated through comparison with the Breadth-First Search (BFS) Algorithm.

**Keywords:** AANET, Industry 4.0, Internet, Optimal Routing Path, Dijkstra's Algorithm, BFS

## Overview

Aeronautical networks present routing optimization problems for providing Internet access to onboard passengers. The Aeronautical Ad hoc NETwork (AANET) consists of involving each aircraft as a network node, capable of sending and receiving signals, with Ground Stations providing the main signal. Finding an optimal data packet routing path to a ground station requires considering metrics such as:
- End-to-end transmission rate
- End-to-end latency
- End-to-end spectral efficiency (SE)
- Path expiration time (PET)

## Key Features

### Multi-Output Dijkstra's Algorithm

The project implements an improved version of Dijkstra's Algorithm that addresses two main challenges:

1. **Multiple Equal Paths**: Nodes can have one or several equal paths (with the same Transmission Rate). The algorithm uses 2-dimensional arrays for E2E Transmission rate, previous node, and visited status, creating forks to deliver all possible solutions with maximum E2E Transmission rate.

2. **Multiple Outputs**: The algorithm provides multiple routing options, allowing selection of the best solution based on Pareto Optimal criteria (balancing transmission rate and latency).

### Algorithm Comparison

The project compares two optimization algorithms:

- **Dijkstra's Algorithm (Improved)**: Finds longest paths maximizing transmission rate
- **Breadth-First Search (BFS)**: Finds shortest paths in terms of hop count

## Methodology

### Data Processing

1. Import aircraft data (216 nodes) with polar coordinates (Altitude, Latitude, Longitude)
2. Add two Ground Stations: GS_LHR (London Heathrow) and GS_EWR (Newark)
3. Convert polar coordinates to Cartesian coordinates (Px, Py, Pz)
4. Calculate Euclidean distance matrix (218 × 218)
5. Create Transmission Rate matrix based on distances

### Dataset

- **Aircraft Nodes**: 216 commercial flights
- **Ground Stations**: 2 (LHR and EWR)
- **Total Nodes**: 218
- **Timestamp**: Single timestamp analysis (1530277200)

## Technologies Used

- **Python 3.9**
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **scipy** - Scientific computing (distance calculations)
- **matplotlib** - Data visualization
- **networkx** - Graph theory and network analysis
- **natsort** - Natural sorting

## Key Results

### End-to-End Transmission Rate

- **Dijkstra's Algorithm**: 
  - 65.7% of nodes achieve 43.505 Mbps
  - 19.4% achieve 31.895 Mbps
- **BFS Algorithm**: 
  - 84.3% have minimum of 31.895 Mbps

### End-to-End Latency

- **Dijkstra's Algorithm**: 
  - 19.4% achieve 50ms latency
  - Range: 50ms to 1350ms (some inefficiency)
- **BFS Algorithm**: 
  - 84.7% in range 50-200ms
  - Distribution: 23.6% at 200ms, 21.7% at 150ms, 19.9% at 100ms, 19.4% at 50ms
  - Maximum execution time: < 80ms

### Execution Time

- **Dijkstra's Algorithm**: 
  - Minimum: 0.1ms
  - Average: 5 seconds
  - Maximum: Up to 1 minute (for complex nodes with multiple paths)
- **BFS Algorithm**: 
  - Minimum/Average: ~10ms
  - Maximum: < 80ms

## Conclusions

- **Dijkstra's Algorithm** provides better end-to-end transmission rates and multiple output options, enabling Pareto Optimal selection, but suffers from higher latency and longer execution times for complex cases.

- **BFS Algorithm** demonstrates superior efficiency with consistent low latency and fast execution times, but is limited to single optimal solutions and doesn't account for node weights.

The improved Dijkstra's Algorithm successfully addresses the problem of finding optimal routing paths with multiple solutions, allowing for better decision-making through Pareto Optimal analysis.

## Usage

See the full detailed report, methodology, code implementation, and results analysis in:
- **`report.ipynb`** - Complete Jupyter notebook with all analysis

## Future Research

- Advanced search for cases with low latency but low transmission rate
- Investigation of trade-offs between latency and transmission rate
- Development of theoretical models predicting optimal balance
- Evaluation under different timestamp conditions
- Study of 5G latency and transmission rate constraints for IoT devices

## Model

![image](https://github.com/davidcuellard/blockchain-verify/blob/main/media/BN-Model.jpg?raw=true)

## License

[MIT](https://choosealicense.com/licenses/mit/)
