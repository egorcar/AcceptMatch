import os
import tempfile
import time
import pyautogui
from pushbullet import Pushbullet

# -------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------Data---------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

image_path = "acceptButton.png"
pick1 = "select2.png"
pick2 = "select1more.png"

click_x = 960
click_y = 513

pushbullet_api_key = "o.4HxAzwfcr5P3pf5i8LtCHdOeEm05pfIA"

pb = Pushbullet(pushbullet_api_key)


# -------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------Functions-------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
def is_image_on_screen(image):
    try:
        return pyautogui.locateOnScreen(image) is not None
    except pyautogui.ImageNotFoundException:
        return False


def take_screenshot_and_send():
    pyautogui.press("printscreen")
    time.sleep(1)
    screenshot = pyautogui.screenshot()
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
        screenshot.save(temp_file.name)

        # Send the screenshot file via Pushbullet
        with open(temp_file.name, "rb") as f:
            file_data = pb.upload_file(f, "Screenshot.png")
            pb.push_file(**file_data)

    # Delete the temporary file
    if os.path.exists(temp_file.name):
        os.unlink(temp_file.name)

    print("Screenshot sent successfully!")


def pick():
    got = False
    message_body = ""
    while True:
        pushes = pb.get_pushes()
        if pushes:
            latest_push = pushes[0]  # Get the latest push notification
            message_body = latest_push.get('body', '').strip()  # Extract the message body
            if message_body == 'Pa' or message_body == 'Dr' or message_body == 'Riki':
                got = True
        if got:
            if message_body == 'Pa':
                pyautogui.click(1055, 332)
                time.sleep(1)
                pyautogui.click(1483, 841)
                time.sleep(1)
                pb.push_note("Phantom Asassin picked", "")
                break
            if message_body == 'Dr':
                pyautogui.click(1002, 252)
                time.sleep(1)
                pyautogui.click(1483, 841)
                time.sleep(1)
                pb.push_note("Drow Ranger picked", "")
                break
            if message_body == 'Riki':
                pyautogui.click(1210, 328)
                time.sleep(1)
                pyautogui.click(1483, 841)
                time.sleep(1)
                pb.push_note("Riki picked", "")
                break
        time.sleep(1)


# -------------------------------------------------------------------------------------------------------------------
# ------------------------------------------Start of the script------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


# Calculate the end time (20 minutes from the current time)
end_time = time.time() + 20 * 60  # 20 minutes

match_found = False

while time.time() < end_time:  # Continue until the end time is reached
    print("Searching for the image...")
    if is_image_on_screen(image_path):
        pyautogui.click(click_x, click_y)  # Click on specified coordinates
        print("Image found.")
        pb.push_note("Match Found", "")
        match_found = True
        break
    time.sleep(1)  # Wait for 1 second before searching again
else:
    print("Image not found.")

if match_found:
    while True:
        if is_image_on_screen(pick1) or is_image_on_screen(pick2):
            take_screenshot_and_send()
            print("Waiting for user input...")
            pb.push_note("Pick: Pa/Dr/Riki", "")
            break
        time.sleep(0.5)

    pick()
    take_screenshot_and_send()

# print("Waiting for next input...")
# pb.push_note("Start buy?", "")
# pushes = pb.get_pushes()
#     if pushes:
#         latest_push = pushes[0]  # Get the latest push notification
#         message_body = latest_push.get('body', '').strip()  # Extract the message body
#         if message_body == 'No':
#
