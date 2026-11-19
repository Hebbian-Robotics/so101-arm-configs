# SO-101 arm configurations

Each `arms/<USB-controller-serial>/` directory contains the SO-101 setup in
`setup.toml` and its LeRobot-compatible `calibration.json`. Keep this repository
private and use a separate entry for each arm.

To calibrate, stop the controller, support and disable the arm, then run the
[SO-101 calibration tool](https://github.com/Hebbian-Robotics/so101/tree/main/setup)
with `--setup-directory /absolute/path/to/this/checkout`. For a new arm with the
soft gripper and wrist camera, also pass `--model-variant soft-gripper-camera`.
Review the model, save, and review and commit the resulting setup and calibration
files. Push the changes for the team. Existing settings are loaded when recalibrating.

RUA can select a registered arm automatically using this checkout; see its
[manual-control guide](https://github.com/Hebbian-Robotics/rua-preview/blob/main/docs/so101-manual-control.md).
For LeRobot, copy `calibration.json` to
`~/.cache/huggingface/lerobot/calibration/robots/so_follower/so101_<serial>.json`.
Check existing files before copying. A replacement controller requires checking
its association with the physical arm before reusing calibration.

## Board labels

| Label | USB controller serial |
| --- | --- |
| 1 | [`5B90101575`](arms/5B90101575/) |
| 2 | [`5B90101549`](arms/5B90101549/) |
| 3 | [`5B90101464`](arms/5B90101464/) |
| 4 | [`5CBC430692`](arms/5CBC430692/) |
| 5 | [`5B7B009457`](arms/5B7B009457/) |

Board labels can be any unique name. We currently use sequential numbers.
Calibration directories are keyed by USB serial.
