## This script will extract frames from a video for the first and last X seconds. It can be used if only
## credits at the beginning  and/or end of the video must be extracted.

##To use this script, replace 'videos_folder' with the path to the folder containing
##the video files, add length of the start and end sequences in seconds,
##and run the script. The extracted images for each video will be saved
##in a separate folder inside the 'extracted_images' folder. The name of each video's
##output folder will be the same as the video file name, without the file extension.

import cv2
import os

# Set the folder path where the videos are stored
folder_path = '/videos_folder/'

# Set the folder path where the extracted images will be saved
output_folder = 'extracted_images'

# Set start length is seconds
startsec = 10
# Set end length in seconds
endsec = 10

# Set the frame rate to x frames per second
frame_rate = 1

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
        framecount = video.get(cv2.CAP_PROP_FRAME_COUNT)
        
        print(framecount)
        # calculate number of frames of start and end sequences
        start_sequence_endframe = int(interval * startsec)
        end_sequence_startframe = int(framecount - interval * endsec)
        # check if start- and endsequences don't overlap or extend ength of video
        if end_sequence_startframe + start_sequence_endframe > framecount:
            start_sequence_endframe = framecount
            end_sequence_startframe = 0
        print(start_sequence_endframe)
        print(end_sequence_startframe)

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
            if (count % interval == 0) and ((count < start_sequence_endframe) or (count > end_sequence_startframe)):
                # Save the image to the video's output folder
                cv2.imwrite(os.path.join(video_output_folder, f'image{count}.jpg'), frame)
                print(f'creating startsequence image {count}')

            # Increment the counter
            count += 1

        # Release the video file
        video.release()

# Close all windows
cv2.destroyAllWindows()
