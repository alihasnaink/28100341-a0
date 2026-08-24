# ATML PA0 - Advanced Topics in Machine Learning
28100341 - Ali Hasnain

This repository contains a collection of Jupyter Notebooks demonstrating various advanced concepts in machine learning, deep learning, and computer vision. Each notebook is independently reproducible and explores specific architectures, training paradigms, and analytical techniques.

## Notebooks Overview

### 1. [CLIP.ipynb](notebooks/CLIP.ipynb)
Explores multimodal image and text embeddings using OpenAI's **CLIP** model. 
- Performs zero-shot image classification on the STL-10 dataset.
- Evaluates the impact of different prompt engineering strategies.
- Visualizes the "modality gap" between image and text embeddings using UMAP dimensionality reduction.
- Aligns text and image embeddings using Orthogonal Procrustes analysis.

### 2. [CNNs.ipynb](notebooks/CNNs.ipynb)
Investigates the behavior and architecture of Convolutional Neural Networks (CNNs).
- Implements and trains a ResNet-152 model.
- Evaluates the structural importance of skip (residual) connections.
- Compares the training dynamics and performance of a baseline ResNet against a modified version with disabled skip connections.

### 3. [FeatureHierarchies.ipynb](notebooks/FeatureHierarchies.ipynb)
Analyzes feature representations extracted across different layers of deep neural networks.
- Extracts intermediate representations from ResNet-152 layers.
- Uses t-SNE and UMAP to visualize the feature hierarchy and class separability at different depths.
- Contrasts feature clustering in standard networks versus networks without skip connections.

### 4. [TransferLearning.ipynb](notebooks/TransferLearning.ipynb)
Compares different transfer learning methodologies on the Food-101 dataset.
- Evaluates linear probing (training only the final classification layer).
- Explores full model fine-tuning of a pre-trained ResNet-152.
- Benchmarks against a model trained entirely from scratch.
- Visualizes and compares the convergence and accuracy of all three strategies.

### 5. [VAEs.ipynb](notebooks/VAEs.ipynb)
Focuses on generative modeling using Variational Autoencoders (VAEs).
- Implements a VAE architecture from scratch using PyTorch.
- Trains the model on the MNIST dataset using a combined reconstruction and KL divergence loss.
- Generates new synthetic images by sampling from the learned latent space.
- Visualizes the structured continuous latent space using PCA.

### 6. [ViT.ipynb](notebooks/ViT.ipynb)
Introduces Vision Transformers (ViT) and explores their internal mechanisms.
- Performs image classification using a pre-trained Hugging Face ViT model.
- Extracts and visualizes internal self-attention maps to understand patch focus.
- Explores interpretability of transformers compared to standard CNN attribution methods.
- Trains a linear probe using extracted CLS token representations.

## Setup and Installation

To run the notebooks locally, ensure you have Python installed, then install the required dependencies:

```bash
pip install -r requirements.txt
```

Each notebook is designed to be executed sequentially and independently. Ensure you have Jupyter Notebook or JupyterLab installed to open and run the `.ipynb` files.
