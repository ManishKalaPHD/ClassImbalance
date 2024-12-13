# ClassImbalance
This respository contains pseudo code and Python implementations of SMOTE (Synthetic Minority Oversampling Technique) and kMeansSMOTE techniques to mitigate class imbalance in avalanche related datasets.


## Repository Structure  


ClassImbalance/
├── Pseudocode/                 # Folder containing pseudo-code for SMOTE and KMeansSMOTE
│   ├── KMeansSMOTE.txt
│   └── SMOTE.txt
├── PythonCode/                 # Folder containing Python implementations
│   ├── KMeansSMOTE.py
│   └── SMOTE.py
├── README.md                   # Project documentation
└── LICENSE                     # License information




## Features  

- Pseudocode:  
  Step-by-step instructions to understand the algorithmic logic behind SMOTE and KMeansSMOTE.  

- Python Implementations: 
  Python scripts implementing both techniques with clear, modular code for easy integration into your projects.


## Installation  

Clone the repository to your local system:  

git clone https://github.com/ManishKalaPHD/ClassImbalance.git
cd ClassImbalance


Ensure you have Python 3.8+ and install the required dependencies:  

pip install numpy scikit-learn



Usage  

Pseudo-code  
The Pseudocode/ folder contains the algorithmic steps for SMOTE and KMeansSMOTE. You can refer to these files for a high-level understanding of the techniques:  
- KMeansSMOTE.txt
- SMOTE.txt  


Python Code  
The PythonCode/ folder contains Python scripts:  
1. KMeansSMOTE Implementation: 
   Run the KMeansSMOTE script for clustering-based oversampling.  
   
   python PythonCode/KMeansSMOTE.py
   

2. SMOTE Implementation: 
   Run the SMOTE script to generate synthetic samples for your imbalanced dataset.  
   
   python PythonCode/SMOTE.py
   

About the Techniques  

1.KMeansSMOTE:  
   A variation of SMOTE that applies kMeans clustering before generating synthetic samples, ensuring better distribution of synthetic samples and reducing overfitting.
   
2. SMOTE (Synthetic Minority Oversampling Technique): 
   SMOTE works by generating synthetic samples for the minority class using interpolation between nearest neighbors in feature space.  



License  

This project is licensed under the [MIT License](LICENSE).



Acknowledgments  

Special thanks to the developers and researchers who contributed to the original design of SMOTE and kMeans-SMOTE algorithms.

