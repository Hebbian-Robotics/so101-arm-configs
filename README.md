# SO-101 arm configurations

Profiles and calibrations keyed by USB controller serial number.

To set up an arm:

1. Copy `arms/<serial>/profile.toml` to your profiles directory and replace
   `__LOCAL_PORT__` with the USB serial port on your computer.
2. Copy `arms/<serial>/calibration.json` to LeRobot's calibration directory,
   naming it `so101_<serial>.json`. The default directory is
   `~/.cache/huggingface/lerobot/calibration/robots/so_follower/`.
3. Select the copied profile when starting your controller. The profile extends
   `so101-manual` and requires a compatible profile loader.

Use a separate profile and calibration for each arm. Check existing files before
copying, and support and disable the arm before switching controllers. If a
controller board is replaced, migrate its configuration to the new serial.
