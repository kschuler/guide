

# Making stimuli

These are the general guidelines I follow when making stimuli for one of my experiments. 

- [Sounds](#sounds)
  - [How to record sounds](#how-to-record-sounds)
  - [How to edit sounds](#how-to-edit-sounds)
  - [How to synthesize sounds](#how-to-synthesize-sounds)
- [Images](#images)
  - [How to find image stimuli](#how-to-find-image-stimuli)
  - [How to edit image stimuli](#how-to-edit-image-stimuli)
- [Videos](#videos) 
  - [How to find video stimuli](#how-to-find-video-stimuli)
  - [How to record video stimuli](#how-to-record-video-stimuli)
  - [How to edit video stimuli](#how-to-edit-video-stimuli)

## Sounds

I prefer to create sound stimuli by recording actual human voices.  Afterward, I edit them to control for specific features like noise and duration.  While speech synthesizers are great these days, I find it difficult to get them to pronounce nonsense words the way I want them to.  If my studies used natural language words or sentences, I would be fine with synthesizing sound stimuli.

### How to record sounds

In our lab we record sounds using a Marantz PMD671 located in BldgD 145-D.  Below are the instructions for typical use of the Marantz PMD671 in our lab. The full manual for the Marantz PMD671 is available [here](../static/marantz-pmd671.pdf).

##### To record sound files on the Marantz PMD671

First, slide the `POWER` switch to the right and release to turn on the Marantz.

![Turn on](../static/images/marantz-on.jpg)

The display will show you how much time is available on the CF card for recording.

![](../static/images/marantz-display.jpg)

Next, slide the `REC` button to the right and release to begin recording. The recording indicator light will be lit and steady while recording.  The display will show the recording time (`TRACK TIME`) of the current track (`TRACK`).

![](../static/images/marantz-record.jpg)

Push and release the `STOP` button to stop recording and end the track.  Press `STOP` a second time to close the audio file. The display will show you how much time is available on the CF card for recording.

![](../static/images/marantz-stop.jpg)

Repeat this process for each sound file you would like to record.  For example, let's say you want to record two sound files: "butterfly" and "doughnut".  You would have one sound file for "butterfly" and a separate one for "doughnut".  Typically, we like to record at least 3 examples of a stimulus in a given sound file to ensure we get a good one.  For example, you should say "butterfly" at least 3 times into the microphone when recording the "butterfly" sound file.  You will later [select the best sample](#select-the-best-sample) of "butterfly" within that sound file.

##### To access sound files recorded on the Marantz PMD671

To access your sound files, first slide the `POWER` switch to the right and release the power off. Plug the Marantz's USB cord into a computer. Then, press and hold the `USB MENU/STORE` button while you slide the `POWER` switch to the right and release.

![](../static/images/marantz-usb.jpg)

The  power is now on and the display will read `USB Online`.  The CF card appears as a removable device on your computer called `MARANTZ`.

![](../static/images/marantz-computer.png)

Navigate to `MARANTZ`.  You will see your recorded audio files in a folder named `MPGLANG1` as numbered `MP3` files.  Select your files and move or copy them to your desired destination.

![](../static/images/marantz-select.png)

**CAUTION - IMPORTANT
**

Be sure that you move ONLY the audio files (`TRACKS`) to other volumes.  **DO NOT modify or deleted the `EDL` file. ** The Marantz will be unable to recognize recorded tracks if the `EDL` file is missing or damaged.

At the close of your session, make sure that the `MPGLANG1` folder is empty of your recorded tracks. This ensures that the CF card will have enough space for other lab members to record.

### How to edit sounds

I use Audacity to edit sound files for my experiments.  There are four ways in which I typically edit my sound files.  I select the best sample of a given stimulus, remove background noise, add or remove silence if necessary, and export as a `.wav` file.

##### Select the best sample

First, select the file that you want to work on.  If you recorded files with the marantz, these files will be numbered `.mp3` files.

![Open sound file](../static/images/sound-file.png)

Right click to open the sound file you want to work on with Audacity.

![](../static/images/sound-open.png)

With the sound file open, listen to each of the recorded examples of the sound and select the one that sounds best to you.

![](../static/images/sound-select.png)

To select in Audacity you just click and drag around the sound that you want.  In this example, I've selected the first one.  Make sure that you get at least a little bit of the silence around the sound.  You will need it to [remove background noise](#remove-background-noise) later.

![](../static/images/sound-select-best.png)

With the best sound selected, hit `cmd + c` to copy it to the clipboard. Open a new audacity file by hitting `cmd + n`.  Then paste the selected sound file into the new audacity file with `cmd + v`.

![](../static/images/sound-paste.png)

##### Remove background noise

To remove background noise, we first need to zoom in to our sound stimulus.  Use `cmd + 1` to zoom in.  (Note that `cmd +3` zooms out and `cmd + 2` returns the sound stimulus to its original size.)

![](../static/images/sound-zoom.png)

Next we need to select a part of the silence to give Audacity a "noise profile".  Do this by clicking and dragging around the silence that you want to select.

![](../static/images/sound-select-silence.png)

Click `Effect > Noise Reduction` to open the "noise reduction" dialog box.

![](../static/images/sound-select-noise-reduction.png)

With your silence already selected and the "noise reduction" dialog box open, click the `Get Noise Profile` button.

![](../static/images/sound-noise-reduction.png)

Next, go back to the sound stimulus and select the entire audio sample.

![](../static/images/sound-select-all.png)

Select `Effect > Noise Reduction` again to return to the "noise reduction" dialog box.  This time select `OK`.

![](../static/images/sound-noise-reduction.png)

You can adjust the dB of noise reduction, the sensitivity, and the smoothing.  For my experiments, the default selections are appropriate.  For reference, those default selections are:

- Noise reduction (dB) : 12
- Sensitivity: 6.00
- Frequency smoothing(bands): 0

##### Add or remove silence

To remove silence (or any section of the stimulus), select the portion of want to remove and click `delete`.

![](../static/images/sound-select-silence.png)

To add silence, place the cursor where you want to add the silence.  Here I've chosen the end of the stimulus.

![](../static/images/sound-select-end.png)

Select `Generate > Silence...` from the Audacity menu.  

![](../static/images/sound-generate-silence.png)

In the "silence" dialog box, enter the amount of silence you want to generate.  Here I have entered 30 seconds of silence.

![](../static/images/sound-silence-dlg.png)

Click `OK` to finish generating silence.

##### Export final stimulus

To export the final stimulus, select `File > Export Audio...` or `File > Export Selected Audio...` if you have selected a smaller portion of a file to export.

![](../static/images/sound-export.png)

Enter a file name and select `WAV` format.

![](../static/images/sound-save.png)

Select `Save`.  You can enter meta-data if you wish to.  I often leave this part blank.

![](../static/images/sound-metadata.png)

Click `OK` to finish exporting your stimulus.

### How to synthesize sounds

##### Synthesize a short list of sounds

To synthesize sounds, you can use the `say` command in the terminal.  For example, to synthesize a single sound, you would type

```
say -v Alex -r 250 "say this please" -o ~/Desktop/say-this.wav --data-format=LEF32@32000
```
Each parameter in this command are:

- `say` is the command for Text-to-speech
- `-v Alex` use voice (`-v`) Alex 
- `-r 250` use a rate of 250 ms
- `"say this please"` is the text you want to synthesize
- `-o ~/Desktop/say-this.wav` is the path and name of the file you want to save
- `--data-format=LEF32@32000` is the format of the data (required for `WAV` files)

When I want so synthesize a short list of words or sentences with exactly the same parameters, I use my [synth-a-little.py](https://raw.githubusercontent.com/kschuler/helpers/master/synth-a-little.py) python script.

![](../static/images/script-synth-words.png)

The parameters in the script are:

- `path` is the name of a folder I want to create to save my sound files in
- `voice` is the voice I want to use
- `rate` is the speech rate
- `wordList` is a list of words or sentences that I want to synthesize

To download the script, navigate to the directory you want to save the script in.  For example, the Desktop.
```
cd ~/Desktop
```

then use `curl` to download the script.
```
curl -o synth-words.py https://raw.githubusercontent.com/kschuler/helpers/master/synth-a-little.py
```

To run the script, first edit [synth-a-little.py](https://raw.githubusercontent.com/kschuler/helpers/master/synth-a-little.py) with the parameters you want to use.  Then navigate to the script's directory.  For example, if you saved `synth-a-little.py` on your Desktop you would navigate to the Desktop

```
cd ~/Desktop
```

And then run the script using
```
python synth-a-little.py
```

##### Synthesize a long list of sounds

When I need to synthesize a long list of sounds, or a list of sounds with different parameters, I use my synth-a-lot.py script.  This script reads parameters from a `.csv` file for each individual sound file.

More coming soon...


## Images

### How to find image stimuli

When you are looking for images to use as stimuli, generally any open-source image search tool works well.  You can see some sources I recommend on my [favorite tools](../tools/favorites.md#images) page, including past stimuli used in the lab.

### How to edit image stimuli

There are two ways in which I typically edit image stimuli: removing background and re-sizing.  I like to edit images with [Inkscape](https://inkscape.org/en/), an open-source vector graphics editor.  To show how to remove background and re-size images in [Inkscape](https://inkscape.org/en/), we will edit this picture of doughnuts.

![](../static/images/doughnut.jpg)

##### Removing background from images

To remove background images, I like to outline the part of the image that I want and use the `clip` tool.  I created a short (silent) YouTube tutorial to show you how to do this. Click the image below to watch it.

[![](http://img.youtube.com/vi/7VmYqgosnp0/0.jpg)](https://www.youtube.com/watch?v=7VmYqgosnp0)

##### Re-sizing images

###### Using Inkscape

To re-size images with Inkscape, you can create a background of your desired size and export it with your image.  I created a (silent) YouTube tutorial for how to do this.  It is available by clicking the image below.

[![](http://img.youtube.com/vi/LYQxfBeBTf0/0.jpg)](https://www.youtube.com/watch?v=LYQxfBeBTf0)

###### Using Preview

It is also reasonably simple to edit images using `Preview` on a Mac.  To begin, open the file you want to edit with `Preview`.  Click and drag around the image to select the area you want.  

![](../static/images/preview-adjust-crop.png)

You can further adjust by clicking and dragging the blue circles.  Once you have the selection square the size you want, drag the square to adjust the position.  Then you can hit `cmd + k` to crop the image.  Once the image is cropped, hit `Tools > Adjust size...`.

![](../static/images/preview-tools.png)

In the `Adjust size` dialog box, close the lock icon by clicking on it.  This locks the aspect ratio to make sure the image does not get distorted. With the lock closed, adjust the size of the image.  When the lock is closed, you only need to adjust one dimension (height or width).  The other dimension will automatically adjust to preserve the aspect ratio.

![](../static/images/preview-adjust-size.png)


## Videos

Coming soon...

### How to find video stimuli

### How to record video stimuli

### How to edit video stimuli


