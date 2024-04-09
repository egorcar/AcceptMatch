# Automated Dota 2 Draft Helper

This script automates certain actions in Dota 2 game, specifically assisting in the draft phase by detecting certain visual cues and executing corresponding actions.

## Features
- Detects a specified image on the screen and performs a click action.
- Monitors push notifications via Pushbullet for specific messages to initiate hero picking.
- Takes screenshots, sends them via Pushbullet, and prompts for user input.
- Selects heroes based on received notifications and performs actions accordingly.

## Prerequisites
- Python 3.x
- Required Python packages (`pip install pyautogui pushbullet.py`)

## Configuration
- `image_path`: Path to the image to be detected and clicked on.
- `pick1` and `pick2`: Paths to images indicating hero pick notifications.
- `click_x` and `click_y`: Coordinates for the click action after image detection.
- `pushbullet_api_key`: API key for Pushbullet integration.

## Usage
1. Run the script.
2. It will continuously search for the specified image on the screen.
3. Once the image is found, it clicks on the specified coordinates and sends a notification.
4. After a match is found, it waits for hero pick notifications.
5. Upon receiving a pick notification, it selects the corresponding hero and sends a confirmation.
6. Repeat steps 4-5 until the draft phase is complete.

## Notes
- This script assumes a specific game setup and screen resolution.
- Adjust coordinates and image paths according to your setup.
- Ensure Pushbullet API key is valid and accessible.

## Disclaimer
- Use this script responsibly and considerate of others in the gaming community.
- It's recommended to test the script in non-competitive environments before actual use.
