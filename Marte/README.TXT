# SALOS: Seismic Analysis for Martian Data

## Overview

This project analyzes seismic data collected from MiniSEED files to detect earthquake events. 
It uses the ObsPy library for reading seismic data and visualizes the results using Matplotlib. 
The analysis focuses on distinguishing between noise and significant seismic activity based on predefined amplitude thresholds.

## Features

- Reads seismic data from MiniSEED files and CSV formats.
- Plots seismic signals with detected earthquake segments highlighted.
- Customizable thresholds for detecting significant seismic activity.
- Generates output plots saved in a specified directory.

## Requirements

- Python 3.x
- Libraries:
  - numpy
  - obspy
  - pandas
  - matplotlib

## Installation

To install the required libraries, run the following command:


Bash
    pip install numpy obspy pandas matplotlib


## Usage

1. Modify the paths for the input and output folders in the code:

   
   input_folder = r"D:\your folder to analyze"
   output_folder = r"D:\your folder for results"


3. Place your MiniSEED and corresponding CSV files in the specified input folder.
4. Run the script to analyze the seismic data and generate plots.

## Output

The script generates plots for each MiniSEED file, highlighting the detected earthquake segments. The output images are saved in the specified output folder.

## Example

After running the script, you will find output images similar to the following:

- example_plot.jpeg

Each plot includes:

- The seismic signal.
- Lines indicating points above predefined amplitude thresholds.
- Highlighted segments representing detected earthquakes.
- A watermark with the team name 'SUAZABOTS'.

## Acknowledgments

- [ObsPy](https://docs.obspy.org/) - for seismic data handling.
- [Matplotlib](https://matplotlib.org/) - for data visualization.
