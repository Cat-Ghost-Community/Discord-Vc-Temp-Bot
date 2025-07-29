# Butterfly VC

Butterfly VC is a full-featured Discord bot that automatically creates temporary voice channels for users when they join a specific parent VC (called "𝗕𝘂𝘁𝘁𝗲𝗿𝗳𝗹𝘆 VC") and provides them with full control through an embed message containing action buttons.

## Features

*   **Automatic Voice Channel Creation:** When a user joins the specified parent voice channel (Butterfly VC), the bot automatically creates a new private voice channel under the same category.
*   **VC Control Panel:** Once the personal VC is created, the bot sends a control panel as an embed message with interactive buttons in the linked text channel (same category).
    *   **Ban:** Prompt to mention a user to ban from the VC.
    *   **Bitrate:** Prompt for new bitrate (between 8000–96000).
    *   **Hide:** Toggle visibility of the VC for others.
    *   **Invite:** Prompt to mention a user and allow them to join the VC.
    *   **Limit:** Prompt to set user limit (0 = unlimited).
    *   **Lock:** Toggle lock/unlock for joining the VC.
    *   **Name:** Prompt to rename the VC.
    *   **Transfer:** Prompt to transfer ownership of the VC to another user.

## Requirements

*   Python 3.8+
*   discord.py

## Installation

1.  Clone the repository:
    ```
    git clone https://github.com/Cat-Ghost-Community/Discord-Vc-Temp-Bot.git
    ```
2.  Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
3.  Create a `requirements.txt` file and add the following line:
    ```
    discord.py
    ```

## Usage

1.  Run the bot:
    ```
    python main.py
    ```
2.  Use the `/setup` command to create the "𝗕𝘂𝘁𝘁𝗲𝗿𝗳𝗹𝘆 VC" category and voice channel.
3.  Join the "𝗕𝘂𝘁𝘁𝗲𝗿𝗳𝗹𝘆 VC" channel to create your own temporary voice channel.

## Configuration

1.  Open `main.py` and replace `"YOUR_BOT_TOKEN"` with your bot's token.
2.  (Optional) Change the `command_prefix` to your desired prefix.
3.  Enable the "Message Content Intent" in your bot's settings on the Discord Developer Portal.
