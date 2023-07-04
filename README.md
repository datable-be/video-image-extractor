# video-image-extractor
extracts images from a video file and removes duplicates

## video-image-extract.py
**extract images from video**
This script extracts images from a video every x seconds. The number of seconds is defined by the frame_rate parameter.
To use this script, replace 'videos_folder' with the path to the folder containing the video files, and run the script. The extracted images for each video will be saved in a separate folder inside the 'extracted_images' folder. The name of each video's output folder will be the same as the video file name, without the file extension.

## video-image-extract_credits.py
**extract images from the beginning  and/or nd of a video**
To use this script, replace 'videos_folder' with the actual path to the folder containing your video files. Specify the desired lengths of the start and end sequences in seconds by modifying the startsec and endsec variables. You can also adjust the frame rate (frame_rate) if needed.
The extracted images for each video will be saved in a separate folder inside the 'extracted_images' folder, with the name of each video's output folder being the same as the video file name (without the extension). Make sure the 'extracted_images' folder exists or provide a different output folder path.

## remove-similar-images.py
**remove (quasi) duplicate images**
This script will search for similar images (e.g. images extracted from a video file). All quasi duplicate images will be moved to a subfolder in the output_folder.
To use the script, replace the 'extracted_images/video-1' folder with the path to the folder with images that have to deduplicated.
The threshold parameter represents the maximum hamming distance allowed for two image hashes to be considered similar. A lower threshold value will result in stricter similarity criteria, considering only images with very similar hashes as duplicates. Conversely, a higher threshold value will allow for more variation in the hashes and consider a broader range of images as similar.
