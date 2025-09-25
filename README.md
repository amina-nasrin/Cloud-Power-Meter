# 🌍 Cloud Power Meter (CPM)

**Bridging the Gap in Power Measurement for Heterogeneous Cloud**

[![IEEE Transactions on Sustainable Computing](https://img.shields.io/badge/IEEE-Transactions%20on%20Sustainable%20Computing-blue)](https://doi.org/10.1109/TSUSC.2025.3607207)

## 📌 Overview
Cloud Power Meter (CPM) is a **machine learning–based framework**. It provides **accurate, real-time power estimation** across **heterogeneous cloud environments** (AWS, Azure, GCP, and Chameleon Cloud)—**without requiring administrative privileges**.

This work has been **accepted in IEEE Transactions on Sustainable Computing (2025)** and addresses one of the most pressing challenges in modern computing: **energy inefficiency in cloud infrastructures**.  

By combining a **decision tree** for cross-platform adaptability with a **multi-variable polynomial regression model**, CPM matches the precision of Intel’s RAPL power model while being deployable on commercial cloud VMs.

---

## 🔬 How It Works

<p align="center">
<img width="722" height="751" alt="ce2" src="https://github.com/user-attachments/assets/8ed9f4a6-d748-4ca0-81cb-6e21e1dab0b7" alt="CPM"/>

</p>

1. **Deploy CPM** on a cloud VM.  
2. **Collect host specs** (CPU model, frequency, cores, memory, instance type, etc.).  
3. **Decision Tree** locates the closest-matching “CPM Instance” from training data based on collected host specs. 
4. Collect CPU Utilization for deployed workload. **CPU utilization is normalized** based on allocated vs. physical cores.  
5. **Polynomial Regression Model** estimates real-time power consumption.
   
---

## 🚀 Key Contributions
- **Novel ML Integration of Decision Tree + Multi-variable Polynomial Regression model for real-time power estimation mitigating Cloud Heterogeneity**

<p align="center">
<img width="522" height="309" alt="Decision Tree (1)" src="https://github.com/user-attachments/assets/f4bd3194-b0bf-42ea-9dd3-cc0b44b66782" />

</p>

  - **Decision Tree classifier** maps unseen VM specifications to the closest known instance (aka "CPM Instance") from the dataset.
  
  - **polynomial regression** provides accurate predictions across diverse workloads with Decision Tree output and normalized CPU utilizations.
    
- **Accurate ML-based Power Estimation**  
  After extensive analysis and experimentation, we adopted a **third-degree multi-variable polynomial regression model** for the power prediction task. Polynomial regression was selected because it effectively captures the **non-linear relationships** among power-affecting parameters. Building on prior research in this field and supported by SPEC benchmark data, it is evident that the relationship between workload parameters and power consumption is inherently non-linear.  

  - Outperforms **14 existing power models**.  
  - Significantly more accurate than **TDP-based measurements**.  
  - Achieves **RAPL-level accuracy** without requiring privileged (root/sudo) access.  


- **Cross-Cloud Adaptability**
  - Validated CPM across multiple commercial and academic platforms with heterogeneous hardware configurations.  
  - Works across AWS, Microsoft Azure, Google Cloud, and academic testbeds.  

- **Massive Real-World Validation**  
  - Analyzed **~2.6 million VMs from Microsoft Azure**.  
  - Discovered **>80,000 kWh of potential monthly energy savings**, where 17% of VMs wasted energy due to underutilization.  

- **Sustainability Impact**  
  - Helps providers and enterprises reduce costs and carbon footprint.  
  - Demonstrated practical applications for reducing costs, conserving energy
  - Provides actionable insights for **green cloud computing** and compliance with emerging **GHG emission disclosure laws**.

---

## 📊 Case Studies & Results
- **SPEC Benchmarks:** Demonstrated CPM’s superior accuracy across 11 workloads.  
- **Chameleon Cloud:** Validated adaptability on unseen hardware.  
- **Commercial Clouds (AWS, Azure):** Proved CPM’s effectiveness under strict privilege limitations.
 <p align="center">
<img width="2625" height="662" alt="1plot_cham" src="https://github.com/user-attachments/assets/75d662d3-de52-4c91-8279-009b8f932cec" />

</p> 
- **Microsoft Azure Dataset:**  
  - Nearly **40% of VMs never exceeded 5% CPU utilization**.  
  - Identified **366 idle VMs wasting ~15,000 kWh in a month**.  
  - Energy optimization through core downgrading achieved up to **59.12% savings**.  
---

## 🛠️ Repository Structure
This work was executed at the Green Computing Lab at Texas State University, supervised of Dr. Ziliang Zong [ziliang@txstate.edu](mailto:ziliang@txstate.edu).

**Contributors**
[aminanasrin@txstate.edu](mailto:aminanasrin@txstate.edu)
[dayuan@txstate.edu](mailto:dayuan@txstate.edu)
