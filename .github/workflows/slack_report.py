import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_file_to_slack(token, channel, file_path, filename=None):
    # Initialize Slack WebClient
    client = WebClient(token=token)

    # Set filename if not provided
    if not filename:
        filename = os.path.basename(file_path)

    # Upload file to Slack
    try:
        response = client.files_upload(
            channels=channel,
            file=file_path,
            filename=filename
        )
        print("File uploaded successfully:", response)
    except SlackApiError as e:
        print(f"Error uploading file: {e.response['error']}")

if __name__ == "__main__":
    slack_token = 'your_slack_token'  # Replace with your Slack Bot/User OAuth Access Token
    slack_channel = 'https://app.slack.com/client/T072VPU7371/C0736F0U878'  # Replace with your Slack channel name or ID
    file_path = 'performance_data.png'  # Path to the file you want to send
    file_name = 'performance_data.png'  # Optional: specify a custom filename for the file

    send_file_to_slack(slack_token, slack_channel, file_path, file_name)
