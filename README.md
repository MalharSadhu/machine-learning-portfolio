# 🔬 Machine Learning & Statistical Inference: An End-to-End Technical Portfolio

This repository houses an end-to-end data science laboratory and technical blog series spanning classical statistical inference, supervised learning, dimensionality reduction, unsupervised clustering, ensemble learning, neural representations, and time-series dynamics.

Every module follows a consistent 6-stage lifecycle:
1. **Clinical / Business Domain Framing**
2. **Exploratory Data Analysis (EDA) & Distribution Screening**
3. **Statistical Hypothesis Testing** (Parametric & Non-Parametric)
4. **Mathematical Derivations & Objective Formulations**
5. **Multi-Panel Diagnostic Visualizations**
6. **Automated Live Performance Reporting & Real-World Synthesis**

---

## 📊 Executive Portfolio Dashboard

| # | Module / Notebook | Target & Dataset | Primary Algorithm(s) | Statistical Validation | Key Performance / Focus |
| :-: | :--- | :--- | :--- | :--- | :--- |
| **01** | [**Linear Regression**](./01_linear_regression.ipynb) | Diabetes Progression ($n=442$) | Ordinary Least Squares (OLS) | Pearson $r$ / Spearman $\rho$ | $R^2 \approx 0.45$, Residual Homoscedasticity |
| **02** | [**Logistic Regression**](./02_logistic_regression.ipynb) | Breast Cancer Biopsy ($n=569$) | Binary Log-Odds & Sigmoid | Two-Sample Welch's $t$-test | $\text{AUC} > 0.99$, Type II Error Tuning |
| **03** | [**Decision Trees & Forests**](./03_decision_trees_random_forest.ipynb) | Italian Wine Terroir ($n=178$) | CART vs. Bagged Random Forest | One-Way ANOVA $F$-test | Variance Reduction, Impurity Splitting |
| **04** | [**Support Vector Machines**](./04_support_vector_machines.ipynb) | Iris Morphometrics ($n=150$) | Linear vs. RBF Kernel SVM | Kolmogorov-Smirnov ($D$) | Margin Geometry, Support Vector Sparsity |
| **05** | [**Classifier Benchmarking**](./05_classification_benchmarking.ipynb) | Wine Cultivar Benchmark ($n=178$) | LogReg vs. Naive Bayes vs. $k$-NN vs. Trees | Kruskal-Wallis $H$-test | Inductive Bias, Independence Violation |
| **06** | [**Dimensionality Reduction**](./06_dimensionality_reduction_pca_lda.ipynb) | 13D Wine Chemometrics ($n=178$) | Unsupervised PCA vs. Supervised LDA | Bartlett's Test of Sphericity | 80% Variance Retention vs. Fisher Scatter |
| **07** | [**Unsupervised Clustering**](./07_unsupervised_clustering.ipynb) | Unlabeled Iris Manifold ($n=150$) | $K$-Means vs. Ward's Hierarchical HAC | Hopkins Statistic ($H > 0.75$) | Silhouette Profile, Elbow Point, Dendrogram |
| **08** | [**Gradient Boosting**](./08_gradient_boosting.ipynb) | Breast Cancer Oncology ($n=569$) | Sequential Pseudo-Residuals (GBM) | Mann-Whitney $U$ Test | Staged Loss Decay, Learning Rate Shrinkage |
| **09** | [**Model Regularization**](./09_regularization_techniques.ipynb) | Augmented Collinear Diabetes ($n=442$) | Ridge ($L_2$) vs. Lasso ($L_1$) vs. ElasticNet | Global Regression $F$-test | Multicollinearity Damping, Sparsity Paths |
| **10** | [**Neural Networks (MLP)**](./10_neural_networks_mlp.ipynb) | Handwritten Digits ($n=1797$) | Multi-Layer Perceptron (Adam) | $\chi^2$ Test of Independence | ReLU vs. Sigmoid Vanishing Gradients |
| **11** | [**Time Series Forecasting**](./11_time_series_forecasting.ipynb) | Environmental Sensor Feed ($N=730$) | Ridge Autoregression vs. Lag Ensemble | Dickey-Fuller Unit Root Test | Out-of-Sample Chronological Holdout |

---

## 🛠️ Environment & Reproducibility

```bash
# Clone the repository
git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
cd <your-repo-name>

# Install required dependencies
pip install numpy pandas matplotlib seaborn scipy scikit-learn tabulate