import os
import numpy as np
import obspy
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Define the folder paths
input_folder = r"D:\your folder to analyze"
output_folder = r"D:\your folder for results"

# Create output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over all files in the input folder
for file in os.listdir(input_folder):
    if file.endswith(".mseed"):
        mseed_path = os.path.join(input_folder, file)
        csv_path = os.path.join(input_folder, file.replace('.mseed', '.csv'))

        # Attempt to load the MiniSEED file
        try:
            st = obspy.read(mseed_path)
            tr = st[0]  # Assuming it has a single trace
            data = tr.data
            sampling_rate = tr.stats.sampling_rate
        except Exception as e:
            print(f"Could not load MiniSEED file: {e}")
            print("Attempting to load CSV file...")
            # Load the CSV file if MiniSEED fails
            df = pd.read_csv(csv_path)
            data = df['amplitude'].values  # Assuming there's a column 'amplitude' in the CSV
            sampling_rate = 1 / (df['time'][1] - df['time'][0])  # Calculate sampling rate from 'time' column

        # Find peaks in the data
        peaks, _ = find_peaks(data)

        # Find the highest and second-highest peaks
        if len(peaks) > 0:
            # Filter peaks above the threshold
            threshold_1 = 1e-9  # Yellow threshold
            threshold_2 = 2e-9  # Green threshold
            filtered_peaks = peaks[data[peaks] > threshold_1]

            if len(filtered_peaks) > 0:
                # Select the two highest peaks
                highest_peaks_indices = np.argsort(data[filtered_peaks])[-2:]  # Get indices of the 2 highest peaks
                highest_peaks = filtered_peaks[highest_peaks_indices]
            else:
                print(f"No peaks found above the threshold in {file}.")
                highest_peaks = []
        else:
            print(f"No peaks found in {file}.")
            highest_peaks = []

        # Initialize variables for earthquake start and end
        earthquake_start = None
        earthquake_end = None
        accumulation_start = None  # Variable to mark the start of accumulation

        if len(highest_peaks) > 0:
            # Get the highest peak
            highest_peak = highest_peaks[0]
            # Check the next 30 points
            for i in range(highest_peak + 1, min(highest_peak + 31, len(data))):
                if data[i] > 0:
                    if earthquake_start is None:
                        earthquake_start = i  # Mark the start of the earthquake
                    # Check if data is decreasing
                    if data[i] >= data[i - 1]:  # If not decreasing
                        break

            # Look for stabilization (regulation)
            if earthquake_start is not None:
                for j in range(earthquake_start, len(data)):
                    if data[j] < np.mean(data[earthquake_start:j]) * 1.05:  # Stabilization within +/- 5%
                        earthquake_end = j
                        break
                else:
                    earthquake_end = len(data)  # No stabilization found, use till the end

        # Create a larger figure for plotting
        fig, ax = plt.subplots(figsize=(12, 8))  # Increase figure size
        # Plot the seismic signal
        time = np.arange(0, len(data)) / sampling_rate
        ax.plot(time, data, color='black', label='Seismic Signal')
        ax.set_title(f"Earthquake Start Detection - {file}")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude (Velocity on Y-axis)")

        # Filter points where amplitude is between threshold_1 and threshold_2
        points_between_thresholds = (data > threshold_1) & (data <= threshold_2)
        points_above_threshold_2 = data > threshold_2

        if np.any(points_between_thresholds):
            # Plot line for points between thresholds (yellow)
            ax.plot(time[points_between_thresholds], data[points_between_thresholds], color='orange',
                    label=f'Amplitude between {threshold_1} and {threshold_2}', linewidth=2)

        if np.any(points_above_threshold_2):
            # Plot line for points above threshold_2 (green)
            ax.plot(time[points_above_threshold_2], data[points_above_threshold_2], color='green',
                    label=f'Amplitude > {threshold_2}', linewidth=2)

            # Analyze data accumulation in the green region
            accumulation = np.zeros_like(data)
            count = 0

            for i in range(len(data)):
                if points_above_threshold_2[i]:
                    count += 1
                    if accumulation_start is None:  # Mark the start of accumulation
                        accumulation_start = i
                else:
                    if count > 0:
                        # Mark accumulation at the previous position
                        accumulation[i - count] = count
                    count = 0

            # Mark the last segment if ended with accumulated data
            if count > 0:
                accumulation[len(data) - count] = count

            # Plot the accumulation as "Earthquake"
            ax.fill_between(time, 0, accumulation * 1e-7, color='purple', alpha=0.3, label='Earthquake')

        # Add legend and adjust layout
        ax.legend()
        plt.tight_layout()

        # Add watermark
        fig.text(0.5, 0.5, 'SUAZABOTS', fontsize=40, color='gray', ha='center', va='center', alpha=0.3, rotation=30)

        # Save the figure in the output folder
        output_file_name = os.path.join(output_folder, file.replace('.mseed', '.png'))
        plt.savefig(output_file_name)
        plt.close()  # Close the figure to free memory

        # Print results
        print(f"Plot saved for {file} in {output_file_name}.")
