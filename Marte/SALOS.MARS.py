import os
import numpy as np
import obspy
import pandas as pd
import matplotlib.pyplot as plt

# Define input and output folder paths
input_folder = r"D:\your folder to analyze"
output_folder = r"D:\your folder for results"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over all files in the input folder
for file in os.listdir(input_folder):
    if file.endswith(".mseed"):
        mseed_path = os.path.join(input_folder, file)
        csv_path = os.path.join(input_folder, file.replace('.mseed', '.csv'))

        # Try to load the MiniSEED file
        try:
            st = obspy.read(mseed_path)
            tr = st[0]  # Assuming there's only one trace
            data = tr.data
            sampling_rate = tr.stats.sampling_rate
        except Exception as e:
            print(f"Failed to load MiniSEED file: {e}")
            print("Attempting to load the CSV file...")
            # Load CSV file if MiniSEED fails
            df = pd.read_csv(csv_path)
            data = df['amplitude'].values  # Assuming there's a column 'amplitude' in the CSV
            sampling_rate = 1 / (df['time'][1] - df['time'][0])  # Calculate sampling rate from 'time' column

        # Thresholds for Mars
        yellow_threshold = 500  # Yellow threshold (only above 500)
        green_threshold = 750   # Green threshold

        # Create a figure for plotting with larger size
        fig, ax = plt.subplots(figsize=(12, 8))  # Increase figure size
        # Plot the seismic signal
        time = np.arange(0, len(data)) / sampling_rate
        ax.plot(time, data, color='black', label='Seismic Signal')
        ax.set_title(f"Earthquake Start Detection - {file}")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude (Velocity on Y-axis)")

        # Filter points where amplitude is greater than yellow threshold
        above_yellow_points = data > yellow_threshold
        above_green_points = data > green_threshold

        # Plot line for points above yellow threshold (yellow)
        if np.any(above_yellow_points):
            ax.plot(time[above_yellow_points], data[above_yellow_points], color='orange',
                    label=f'Amplitude > {yellow_threshold}', linewidth=2)

        # Plot line for points above green threshold (green)
        if np.any(above_green_points):
            ax.plot(time[above_green_points], data[above_green_points], color='green',
                    label=f'Amplitude > {green_threshold}', linewidth=2)

        # Identify continuous segments where data is above yellow and green thresholds (earthquakes)
        segments = []
        in_segment = False
        segment_start = 0
        has_yellow = False
        has_green = False

        for i in range(len(data)):
            if data[i] > yellow_threshold:
                if not in_segment:
                    in_segment = True
                    segment_start = i
                if data[i] > green_threshold:
                    has_green = True
            else:
                if in_segment:
                    if has_green:
                        segments.append((segment_start, i - 1))
                    in_segment = False
                    has_green = False

        # Add last segment if it ends at the end of the data
        if in_segment and has_green:
            segments.append((segment_start, len(data) - 1))

        # Plot segments identified as earthquakes in blue
        for start, end in segments:
            ax.plot(time[start:end + 1], data[start:end + 1], color='blue', linewidth=3)

        # Add single legend
        ax.legend(['Seismic Signal', f'Amplitude > {yellow_threshold}', f'Amplitude > {green_threshold}', 'Detected Earthquake'], loc='upper right')

        # Add watermark
        plt.text(0.5, 0.05, 'SUAZABOTS', fontsize=30, color='gray', alpha=0.5, ha='center', va='center', transform=ax.transAxes)

        # Adjust layout
        plt.tight_layout()

        # Save the figure in the output folder
        output_file_name = os.path.join(output_folder, file.replace('.mseed', '.png'))
        plt.savefig(output_file_name)
        plt.close()  # Close figure to free memory

        # Print results
        print(f"Plot saved for {file} in {output_file_name}.")
