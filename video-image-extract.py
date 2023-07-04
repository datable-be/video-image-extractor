##To use this modified script, replace 'videos_folder' with the path to the folder containing
##the video files, and run the script. The extracted images for each video will be saved
##in a separate folder inside the 'extracted_images' folder. The name of each video's
##output folder will be the same as the video file name, without the file extension.

import cv2
import os

# Set the folder path where the videos are stored
folder_path = '/videos_folder/'

# Set the folder path where the extracted images will be saved
output_folder = 'extracted_images'

# Create the output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Set the frame rate to x frames per second
frame_rate = 0.5

# Loop through all the files in the folder
for file_name in os.listdir(folder_path):
    # Check if the file is a video file
    print(f'Processing video {file_name}')
    if file_name.endswith('.mp4') or file_name.endswith('.avi'):
        # Open the video file
        video = cv2.VideoCapture(os.path.join(folder_path, file_name))

        # Create a directory to save the extracted images
        video_output_folder = os.path.join(output_folder, os.path.splitext(file_name)[0])
        if not os.path.exists(video_output_folder):
            os.makedirs(video_output_folder)

        # Set the interval to extract frames
        interval = int(video.get(cv2.CAP_PROP_FPS) / frame_rate)

        # Initialize a counter
        count = 0

        # Loop through the video frames
        while True:
            # Read a frame from the video
            ret, frame = video.read()

            # Check if the frame was successfully read
            if not ret:
                break

            # Extract an image every 2 seconds
            if count % interval == 0:
                # Save the image to the video's output folder
                cv2.imwrite(os.path.join(video_output_folder, f'image{count}.jpg'), frame)
                print(f'creating image {count}')

            # Increment the counter
            count += 1

        # Release the video file
        video.release()

# Close all windows
cv2.destroyAllWindows()
