# Key Features:
    # Nearest Neighbors Search: Uses sklearn.neighbors.NearestNeighbors to efficiently compute m nearest neighbors.
    # Synthetic Sample Generation: Interpolates between a sample and a randomly chosen neighbor using a random gap (random_gap).
    # Dynamic Iteration: The while True loop allows for further checks if required, such as achieving a specific imbalance ratio.

# Imbalance Ratio Calculation:

    #A helper function calculate_ratio computes the ratio of minority class size to majority class size.
    # The algorithm checks if the current ratio is less than the desired_ratio.

#Stopping Condition:

    #The while loop continues until the imbalance ratio (minority/majority) meets or exceeds the desired_ratio.

#Dynamic Minority Size Update:

    #Each time synthetic samples are generated, the current minority class size is updated by adding the count of generated synthetic samples.

# Output:

    # The matrix_smoted array contains the generated synthetic samples.
   # You can append these synthetic samples to your original dataset to balance the class distribution.


import numpy as np
from sklearn.neighbors import NearestNeighbors

def SMOTE(matrix_avalanche, N, m, desired_ratio, majority_class_size):
    """
    SMOTE algorithm to generate synthetic samples with imbalance ratio check.
    
    Parameters:
        matrix_avalanche (numpy array): Matrix of original minority class samples.
        N (int): Number of synthetic samples to generate per minority class sample.
        m (int): Number of nearest neighbors to consider for interpolation.
        desired_ratio (float): Target ratio of minority to majority class size.
        majority_class_size (int): Number of samples in the majority class.
        
    Returns:
        numpy array: Matrix of synthetic samples.
    """
    # Number of samples and parameters
    A, num_param = matrix_avalanche.shape
    
    # Initialize storage for synthetic samples
    matrix_smoted = []
    
    # Fit Nearest Neighbors model to the data
    nbrs = NearestNeighbors(n_neighbors=m).fit(matrix_avalanche)
    
    # Current minority class size
    current_minority_size = A
    
    # Calculate the current imbalance ratio
    def calculate_ratio(minority_size, majority_size):
        return minority_size / majority_size

    while calculate_ratio(current_minority_size, majority_class_size) < desired_ratio:
        for i in range(A):
            # Find `m` nearest neighbors for the i-th sample
            _, nn_indices = nbrs.kneighbors([matrix_avalanche[i]])
            nn_indices = nn_indices.flatten()
            
            for _ in range(N):
                # Randomly select a neighbor from the nearest neighbors
                random_idx = np.random.choice(nn_indices)
                
                # Generate a synthetic sample
                synthetic_sample = []
                for j in range(num_param):
                    random_gap = np.random.rand()  # Random number in [0,1]
                    euc_dist = matrix_avalanche[random_idx, j] - matrix_avalanche[i, j]
                    synthetic_value = matrix_avalanche[i, j] + random_gap * euc_dist
                    synthetic_sample.append(synthetic_value)
                
                # Append the generated sample to the synthetic samples matrix
                matrix_smoted.append(synthetic_sample)
        
        # Update the minority class size
        current_minority_size = A + len(matrix_smoted)
    
    return np.array(matrix_smoted)


# Example usage
if __name__ == "__main__":
    # Example input data (5 samples, 3 features)
    matrix_avalanche = np.array([
        [1.0, 2.0, 3.0],
        [1.5, 2.5, 3.5],
        [1.2, 2.2, 3.2],
        [1.8, 2.8, 3.8],
        [1.4, 2.4, 3.4]
    ])
    
    N = 2  # Generate 2 synthetic samples per original sample
    m = 10  # Use 10 nearest neighbors
    desired_ratio = 0.5  # Target ratio of minority to majority class
    majority_class_size = 20  # Number of samples in the majority class
    
    synthetic_samples = SMOTE(matrix_avalanche, N, m, desired_ratio, majority_class_size)
    print("Original Samples:")
    print(matrix_avalanche)
    print("\nSynthetic Samples:")
    print(synthetic_samples)

