# SO-101 arm configurations

SO-101 profiles and calibrations, keyed by USB controller serial number.

From the station checkout, clone this repository into the ignored local directory:

```sh
mkdir -p profiles/local
git clone https://github.com/Hebbian-Robotics/so101-arm-configs.git profiles/local/arm-configs
```

Import an arm using its board serial and the local serial port:

```sh
python3 profiles/local/arm-configs/import_arm.py 5B90101575 --port /dev/your-serial-port
```

The importer creates `profiles/local/so101-<serial>.toml` and installs the
matching LeRobot calibration JSON. It refuses to overwrite different files.
Use `--profile local/so101-<serial>` when starting the station. Support and
disable the arm before switching controllers. USB ports are machine-specific.
If a board is replaced, migrate the configuration to its new serial number.
Run the station's SO-101 gain setup after calibration as documented there.
