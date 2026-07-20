#!/bin/env sh

set -e

DEVICE_PATH="/dev/video5"
TITLE="Phone Webcam Setup"

check_install() {
    BODY="Found: "
    for tool in "$@"; do
        if RESULT=$(pacman -Q "$tool" 2>/dev/null); then
          BODY+="\n$RESULT"
        else
          BODY+="\nerror: $tool not installed"
        fi
    done
    if [ -e "$DEVICE_PATH" ]; then
      BODY+="\n$DEVICE_PATH found"
    else
      BODY+="\nerror: $DEVICE_PATH not found.Please setup a loopback device"
    fi

    ERRORS=$(printf "$BODY" | grep -c "error:"|| printf "No errors found!")

    # BODY=""
    printf "$BODY"

    if [ "$ERRORS" -ne 0 ]; then
      printf "\n\nErrors found, exiting.\n"
      return 1;
    else
      notify-send -a "$TITLE" "Setting up webcam" "\n$BODY"
      return 0;
    fi
}    

detect_device(){
  if ! adb devices | grep -wc "device"; then
    MSG="Android device not detected!"
    printf "$MSG"
    notify-send -a "$TITLE" "$MSG" || printf "notify-send failed"
    exit 1;
  else
    notify-send -a "$TITLE" "Android device detected.Setting up webcam."
  fi
}

init_webcam(){
 if timeout 6  notify-send -a "$TITLE" \
    "Default orientation: Horizontal, change to Vertical?"\
     -A "Yes"; then
     
   printf "INIT VERTICAL  MODE"
   scrcpy --video-source=camera --camera-size=1920x1080 --camera-facing=front --v4l2-sink=$DEVICE_PATH  --no-playback --display-orientation=flip90
 else
   printf "INIT HORIZONTAL MODE"
   scrcpy --video-source=camera --camera-size=1920x1080 --camera-facing=front --v4l2-sink=$DEVICE_PATH  --no-playback --display-orientation=flip0

 fi
}

VALUE=$(notify-send -t 10000 -a "$TITLE" "Setup phone as webcam?" -A "Yes" -A "No")

if [ $VALUE -eq 0 ]; then
  check_install libnotify android-tools v4l2loopback-dkms scrcpy

  if detect_device ; then
  #  scrcpy --video-source=camera --camera-size=1920x1080 --camera-facing=front --v4l2-sink=$DEVICE_PATH  --no-audio-playback --display-orientation=flip90
  # scrcpy --video-source=camera --camera-size=1920x1080 --camera-facing=front --v4l2-sink=$DEVICE_PATH  --no-playback
    init_webcam
  fi
else
  notify-send -a "$TITLE" "Setup Declined, exiting."
  exit 0
fi

