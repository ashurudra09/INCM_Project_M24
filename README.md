# Izhikevich Neuron Model for Pattern Recognition

## Overview

This repository demonstrates the use of the Izhikevich neuron model for pattern recognition/classification tasks. The project simulates biologically-inspired spiking neuron dynamics and applies them to real-world datasets (Iris and Penguins), showcasing both the neural simulation and its application as a classifier compared to traditional machine learning models.

---

## Features

- **Biologically-Inspired Neuron Simulation:**  
  Implements the Izhikevich neuron model, simulating spiking behavior and membrane dynamics for different neuron types (e.g., regular spiking, intrinsic bursting).

- **Data Preprocessing & Encoding:**  
  Converts standard datasets (Iris, Penguins) into current input signals suitable for neuron-based simulation.

- **Pattern Recognition:**  
  Trains single neurons to classify input patterns using biologically plausible mechanisms.

- **Comparative Analysis:**  
  Benchmarks the Izhikevich neuron-based classifier against traditional classifiers (e.g., SVM, Logistic Regression) and visualizes results.

- **Data Visualization:**  
  Provides Jupyter notebooks and scripts for exploring and visualizing input datasets.

---

## Tech Stack

- **Languages:** Python 3.x
- **Core Libraries:**  
  - NumPy (numerical computation)  
  - pandas (data manipulation)  
  - Matplotlib (visualization)  
  - Jupyter Notebook (experiment documentation)  
- **Custom Modules:**  
  - `izhikevich_neuron_model.ipynb` (neuron simulation)  
  - `data_viz.py` (data visualization)  
  - `neuron_model_classification.py` (classification with neuron model)  

---

## How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ashurudra09/INCM_Project_M24.git
   cd INCM_Project_M24
   ```

2. **Install Dependencies**
   ```bash
   pip install numpy pandas matplotlib jupyter
   ```

3. **Datasets**
   - Make sure `iris.csv` and `penguins.csv` are available in the `datasets/` directory.
   - [Iris dataset](https://gist.github.com/curran/a08a1080b88344b0c8a7)
   - [Penguins dataset](https://github.com/mwaskom/seaborn-data/blob/master/penguins.csv)

4. **Explore Notebooks**
   - **Neuron Simulation:**  
     Open [`Code/izhikevich_neuron_model.ipynb`](Code/izhikevich_neuron_model.ipynb) to understand and run the neuron model simulations.
   - **Data Visualization:**  
     Explore [`Code/data_viz.ipynb`](Code/data_viz.ipynb) (or `data_viz.py`) for dataset visualizations.
   - **Classification and Results:**  
     See [`Code/classification.ipynb`](Code/classification.ipynb) for training/testing the neuron model and comparing it with other models.

   Run Jupyter Lab/Notebook:
   ```bash
   jupyter notebook
   ```

---

## Project Structure

```
INCM_Project_M24/
│
├── Code/
│   ├── izhikevich_neuron_model.ipynb   # Neuron model simulation and explanation
│   ├── data_viz.py                     # Data analysis & visualization script
│   ├── neuron_model_classification.py   # (WIP) Neuron-based classifier
│   ├── classification.ipynb            # Training/testing neuron and traditional models
│   └── data_viz.ipynb                  # (Optional) Jupyter version of data_viz.py
├── datasets/
│   ├── iris.csv                        # Iris dataset
│   └── penguins.csv                    # Penguins dataset
└── README.md
```

---

## Ideas Used

- **Izhikevich Neuron Model:**  
  A computationally efficient spiking neuron model that can reproduce a wide variety of firing patterns observed in real biological neurons.

- **Pattern Encoding:**  
  Real-world tabular data is encoded into current input signals, which are then processed by the simulated neuron.

- **Single Neuron Classification:**  
  Demonstrates that even a single spiking neuron (with appropriate input encoding and training) can perform basic pattern recognition.

- **Comparison with Conventional ML:**  
  Provides a side-by-side evaluation of biologically-inspired and traditional classification approaches on standard datasets.

---

## Future Scope

- **Extend to Multi-Neuron Networks:**  
  Implement networks of Izhikevich neurons for more complex classification and time-series tasks.

- **Broader Dataset Support:**  
  Test with more challenging or larger datasets.

- **Advanced Training Algorithms:**  
  Explore STDP (Spike-Timing Dependent Plasticity) and other biologically realistic learning rules.

- **Optimization & Performance:**  
  Parallelize simulation, leverage GPUs, or use optimized libraries for larger-scale experiments.

- **Visualization Improvements:**  
  Enhance visualization of spike trains, membrane potentials, and decision boundaries.

---

## Suggested Alternate Repository Name

**spiking-neuron-pattern-classifier**

*Rationale:* This name is more descriptive, highlighting the use of spiking neuron models for pattern recognition and classification. It is concise, unambiguous, and more suitable for discoverability.

---

## References

- Izhikevich, E. M. (2003). Simple model of spiking neurons. IEEE Transactions on Neural Networks.
- [Izhikevich Model Wiki](https://en.wikipedia.org/wiki/Izhikevich_model)
- [Iris Dataset](https://gist.github.com/curran/a08a1080b88344b0c8a7)
- [Penguins Dataset](https://github.com/mwaskom/seaborn-data/blob/master/penguins.csv)

---
