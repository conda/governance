import csv
import io
from pathlib import Path


def csv_to_markdown(csv_data):
    # Create a StringIO object to simulate a file
    csv_file = io.StringIO(csv_data)

    # Read the CSV data
    csv_reader = csv.DictReader(csv_file)

    # Start the Markdown output
    markdown_output = "# GitHub Users Selection List\n\n"

    # Process each row
    for row in csv_reader:
        github_username = row["github_username"]
        name = row["name"]

        # Build the Markdown line
        line = f"@{github_username} ({name})\n"
        line += "- [ ]  yes\n"
        line += "- [ ]  no\n"
        line += "- [ ]  abstain\n"

        markdown_output += line + "\n"

    return markdown_output


if __name__ == "__main__":
    # Read the CSV file
    csv_data = Path("steering.csv").read_text()

    # Convert the CSV data to Markdown
    markdown_output = csv_to_markdown(csv_data)

    print(markdown_output)
