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

## Wrist cameras

`camera-defaults.toml` gives registered soft-gripper arms a shared wrist-camera
selector. RUA matches the USB vendor, product and serial to a connected capture
device. An arm with a replacement camera can override the selector in
`arms/<USB-controller-serial>/cameras.toml`. Both selectors use
`VID:PID:USB_SERIAL`, with hexadecimal VID and PID.

Set `wrist = "none"` in an arm’s camera file to opt out of the shared default.
At the station, `--camera wrist=DEVICE` selects an explicit device.
See the [RUA camera guide](https://github.com/Hebbian-Robotics/rua/blob/main/docs/cameras.md)
for camera discovery and troubleshooting.

## Board labels

| Label | USB controller serial |
| --- | --- |
| 1 | [`5B90101575`](arms/5B90101575/) |
| 2 | [`5B90101549`](arms/5B90101549/) |
| 3 | [`5B90101464`](arms/5B90101464/) |
| 4 | [`5CBC430692`](arms/5CBC430692/) |
| 5 | [`5B7B009457`](arms/5B7B009457/) |
| 6 | [`5B79081103`](arms/5B79081103/) |
| 7 | [`5B79080492`](arms/5B79080492/) |
| 8 | [`5CBC431221`](arms/5CBC431221/) |
| 9 | [`5B7B014478`](arms/5B7B014478/) |
| 10 | [`5B90101711`](arms/5B90101711/) |
| 11 | [`5CBC431070`](arms/5CBC431070/) |
| 12 | [`5CBC431217`](arms/5CBC431217/) |
| 13 | [`5CBC453054`](arms/5CBC453054/) |
| 14 | [`5CBC432354`](arms/5CBC432354/) |
| 15 | [`5CBC453097`](arms/5CBC453097/) |
| 16 | [`5CBC430694`](arms/5CBC430694/) |
| 17 | [`5B7B015191`](arms/5B7B015191/) |
| 19 | [`5B7B009458`](arms/5B7B009458/) |

Board labels can be any unique name. We currently use sequential numbers.
Calibration directories are keyed by USB serial.
