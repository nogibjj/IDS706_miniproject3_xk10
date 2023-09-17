"""
Main code
"""

import polars as pl
import matplotlib.pyplot as plt
import seaborn as sns


def readfile(file_path):
    data = pl.read_csv(file_path)
    return data


# Function to generate summary statistics and create a data visualization
def generate_summary_and_visualization(
    data, output_summary_report, histogram_image_path
):
    # Generate summary statistics for numeric columns
    summary_stats = data.describe()

    # Create a histogram visualization for the 'Age' column
    plt.figure(figsize=(8, 6))
    sns.histplot(data["Age"], kde=True, color="skyblue")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.savefig(histogram_image_path, bbox_inches="tight")
    plt.close()

    # Save the summary report in Markdown format
    with open(output_summary_report, "w", encoding="utf-8") as markdown_file:
        markdown_file.write(summary_stats.to_pandas().to_markdown())
        markdown_file.write(f"\n![Histogram]({histogram_image_path})\n")
    print(f"Summary report saved to {output_summary_report}")


if __name__ == "__main__":
    # Specify the input CSV file and output file paths
    input_file_path = "bmi.csv"  # Update with your dataset file path
    summary_report = "summary_report.md"
    histogram_image = "age_histogram.png"

    # Read the dataset
    df = readfile(input_file_path)

    # Generate summary statistics and create a histogram
    generate_summary_and_visualization(df, summary_report, histogram_image)
