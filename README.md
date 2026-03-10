# SISMONET: Capturing the Seismic Heartbeat of the Cosmos - SALOS Algorith Suazabots
**NASA Space Apps Challenge 2024** **Team:** Suazabots  
**Challenge:** Seismic Detection Across the Solar System

## Project Summary
Planetary seismology faces significant challenges due to the difficulty of transmitting high-resolution data to Earth. **SISMONET** addresses this by implementing the **SALOS** algorithm, a refined STA/LTA (Short-Term Average / Long-Term Average) approach designed to distinguish between seismic signals and background noise with high precision.

Our solution optimizes data selection, ensuring that only scientifically relevant information is prioritized for transmission, thereby increasing reliability and energy efficiency for planetary landers.

## The SALOS Algorithm
The core of this project is the **SALOS** algorithm. It analyzes wave amplitude over consecutive periods to identify the onset of seismic events in data from the **Apollo** (Moon) and **InSight** (Mars) missions.

### Key Features:
* **Multi-Range Detection:** Categorizes data based on amplitude thresholds:
    * **Green:** High-amplitude data.
    * **Orange:** Intermediate-range data.
* **Density Analysis:** Identifies the onset of earthquakes by detecting the accumulation of intermediate and high-amplitude signals.
* **Dynamic Adaptability:** Unlike static triggers, SALOS allows for threshold adjustments based on the specific seismic environment (Mars vs. Moon).

## Performance and Results
Based on rigorous testing against NASA’s baseline algorithms:
* **Effectiveness:** **98.2%** (compared to the 92% baseline).
* **Accuracy:** Successfully identified the earthquake onset in **169 out of 172 plots**.
* **Optimization:** The 3 remaining plots were addressed through dynamic threshold adjustments, demonstrating the program's flexibility.

## Repository Structure
* **/MARS**: Implementation for Mars InSight Lander data.
* **/MOON**: Implementation for Apollo Passive Seismic Experiment data.
* **Scripts:** Python-based tools using ObsPy, NumPy, Pandas, and Matplotlib.

## Resources & Documentation
* **Demo Video:** [Watch on YouTube](https://www.youtube.com/watch?v=tNKmN-PjJuM)
* **Project Workspace:** [Google Drive Folder](https://drive.google.com/drive/folders/1JmIQ3F8qx46kxHheEy7D3yvwjakRjIHL?usp=sharing)
* **Official Profile:** [NASA Space Apps Project Page](https://www.spaceappschallenge.org/nasa-space-apps-2024/find-a-team/suazabots1/?tab=project)

## References
* NASA Space Apps 2024 Seismic Detection Data Packet.
* Apollo Passive Seismic Experiment Data Description.
* Mars InSight Seismic Data Information Sheet.
* *Bulletin of the Seismological Society of America (BSSA)*: STA/LTA parameter setting research.

---
*Developed by Team Suazabots for the 2024 NASA Space Apps Challenge.*
