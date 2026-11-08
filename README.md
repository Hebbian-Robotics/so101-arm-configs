# SO-101 arm configurations

Arm profiles and calibrations keyed by USB controller serial number.

Clone the repository wherever convenient:

```sh
git clone https://github.com/Hebbian-Robotics/so101-arm-configs.git
```

Import an arm by specifying the serial, local port and profile output directory:

```sh
python3 so101-arm-configs/import_arm.py 5B90101575 \
  --port /dev/your-serial-port --output-dir /path/to/profiles
```

The importer creates `so101-<serial>.toml` in the chosen directory and installs
the matching LeRobot calibration JSON. It refuses to overwrite different files.
The profile extends `so101-manual`; use it with a compatible profile loader.
Support and disable the arm before switching controllers. If a controller board
is replaced, migrate the configuration to its new serial number.
