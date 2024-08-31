# Tutorial for the Android Robust Malware Competition

Announcement: We are about to release a public challenge at one of the main conferences in ML and Security.
Stay tuned for future updates (registering to the [challenge platform](https://benchmarks.elsa-ai.eu/?ch=6&com=introduction) is enough to stay updated).

## Preparation

Before running the notebook, you need to complete the following steps.

1. Download the repository at: https://github.com/maurapintor/android_tutorial
2. Register to the ELSA benchmark platform: https://benchmarks.elsa-ai.eu/?ch=6&com=introduction
3. Go to Download and download these two items:
   1. APK hashes, timestamps, and labels
   2. DREBIN features
4. Put the files, unzipped in the "data" folder
5. (optional but recommended) Create a python environment `conda create -n android`
6. (optional but recommended) Activate the environment `conda activate android`
7. Install the requirements `pip install -r requirements.txt`

## Example

Run the example by starting the jupyter server.
Note that this is a tutorial where you have to write parts of the code to make it work. 

```bash
jupyter notebook android_challenge_tutorial.ipynb
```

You can also check the solution at https://github.com/maurapintor/android_tutorial/blob/main/android_challenge.ipynb
