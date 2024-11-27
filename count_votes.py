import sys
import requests


def fetch_github_comment(comment_url):
    # Extract the necessary parts from the comment URL
    parts = comment_url.split("/")
    owner, repo = parts[3], parts[4]

    comment_id = comment_url.split("#issuecomment-")[-1]

    # Construct the API URL
    api_url = (
        f"https://api.github.com/repos/{owner}/{repo}/issues/comments/{comment_id}"
    )

    # Make the request to the GitHub API
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()["body"]
    else:
        raise Exception(f"Failed to fetch comment: {response.status_code}")


def parse_votes(text):
    lines = text.split("\n")
    yes_votes = []
    no_votes = []
    abstain_votes = []
    not_voted = []
    invalid_votes = []
    current_voter = None
    vote_count = 0

    for line in lines:
        line = line.strip()

        if line.startswith("@"):
            # This line contains the voter's information
            if current_voter and vote_count == 0:
                not_voted.append(current_voter)
            current_voter = line
            vote_count = 0
        elif line.startswith("- [x]") or line.startswith("- [ ]"):
            # This line contains a vote
            if current_voter:
                if "[x]" in line:
                    vote_count += 1
                    if "yes" in line.lower():
                        yes_votes.append(current_voter)
                    elif "no" in line.lower():
                        no_votes.append(current_voter)
                    elif "abstain" in line.lower():
                        abstain_votes.append(current_voter)
        else:
            # If we encounter any other type of line, check if the previous voter's vote was valid
            if current_voter:
                if vote_count > 1:
                    invalid_votes.append(current_voter)
                elif vote_count == 0:
                    not_voted.append(current_voter)
            current_voter = None
            vote_count = 0

    # Check the last voter
    if current_voter:
        if vote_count > 1:
            invalid_votes.append(current_voter)
        elif vote_count == 0:
            not_voted.append(current_voter)

    return yes_votes, no_votes, abstain_votes, not_voted, invalid_votes


def print_results(yes_votes, no_votes, abstain_votes, not_voted, invalid_votes):
    total_voters = (
        len(yes_votes)
        + len(no_votes)
        + len(abstain_votes)
        + len(not_voted)
        + len(invalid_votes)
    )
    valid_voters = len(yes_votes) + len(no_votes) + len(abstain_votes)
    print(
        f"Total voters: {total_voters} (valid: {valid_voters} = {valid_voters / total_voters * 100:.2f}%)"
    )
    print(
        f"\nYes votes ({len(yes_votes)} / {len(yes_votes) / valid_voters * 100:.2f}%):"
    )
    for voter in yes_votes:
        print(f"- {voter}")

    print(f"\nNo votes ({len(no_votes)} / {len(no_votes) / valid_voters * 100:.2f}%)):")
    for voter in no_votes:
        print(f"- {voter}")

    print(
        f"\nAbstain votes ({len(abstain_votes)} / {len(abstain_votes) / valid_voters * 100:.2f}%):"
    )
    for voter in abstain_votes:
        print(f"- {voter}")

    print(f"\nNot voted ({len(not_voted)}):")
    for voter in not_voted:
        print(f"- {voter}")

    print(f"\nInvalid votes ({len(invalid_votes)}):")
    for voter in invalid_votes:
        print(f"- {voter}")

    # print("\nGitHub handles summary:")
    # print("Yes:", ", ".join([vote.split()[0] for vote in yes_votes]))
    # print("No:", ", ".join([vote.split()[0] for vote in no_votes]))
    # print("Abstain:", ", ".join([vote.split()[0] for vote in abstain_votes]))
    # print("Not voted:", ", ".join([vote.split()[0] for vote in not_voted]))
    # print("Invalid votes:", ", ".join([vote.split()[0] for vote in invalid_votes]))


# Example usage
comment_url = "https://github.com/conda/ceps/pull/75#issuecomment-2203197834"

try:
    if len(sys.argv) > 1:
        comment_url = sys.argv[1]

    comment_text = fetch_github_comment(comment_url)
    yes_votes, no_votes, abstain_votes, not_voted, invalid_votes = parse_votes(
        comment_text
    )
    print_results(yes_votes, no_votes, abstain_votes, not_voted, invalid_votes)
except Exception as e:
    print(f"An error occurred: {e}")
